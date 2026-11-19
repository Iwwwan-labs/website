#!/usr/bin/env python3
"""Dependency-free checks for the Iwwwan-labs static website."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE_BASE = "/website"
# Published files, mirrored by the staging step in .github/workflows/pages.yml.
PUBLIC_FILES = ("index.html", "styles.css", "sitemap.xml", "robots.txt", "404.html")
HTML_PAGES = ("index.html", "404.html")
WORKFLOW = ROOT / ".github/workflows/pages.yml"


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.missing_alt, self.inline_styles = [], [], [], []
        self.has_main = self.has_title = self.has_description = False
        self.robots = ""
        self.classes = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs: self.ids.append(attrs["id"])
        self.classes.update(attrs.get("class", "").split())
        if tag == "a" and "href" in attrs: self.links.append(attrs["href"])
        if tag == "img" and "alt" not in attrs: self.missing_alt.append(self.getpos())
        if tag == "main": self.has_main = True
        if tag == "title": self.has_title = True
        if tag == "meta" and attrs.get("name", "").lower() == "description" and attrs.get("content", "").strip(): self.has_description = True
        if tag == "meta" and attrs.get("name", "").lower() == "robots": self.robots = attrs.get("content", "").lower()
        if "style" in attrs: self.inline_styles.append(self.getpos())


def resolve_local(href):
    """Map a local href to a repository path, or None when it is external."""
    parsed = urlparse(href)
    if parsed.scheme in ("http", "https") or href.startswith("//"):
        return None
    path = parsed.path
    if not path:
        return None
    if path.startswith("/"):
        if not (path == SITE_BASE or path.startswith(SITE_BASE + "/")):
            return ("outside-base", path)
        path = path[len(SITE_BASE):]
    target = (ROOT / path.lstrip("/")).resolve()
    return ("path", target)


def check_page(name, errors):
    page = ROOT / name
    if not page.exists():
        errors.append("Missing HTML page: " + name)
        return
    parser = SiteParser()
    parser.feed(page.read_text(encoding="utf-8"))
    parser.close()
    duplicates = [key for key, count in Counter(parser.ids).items() if count > 1]
    if duplicates: errors.append(name + ": duplicate IDs: " + ", ".join(duplicates))
    if not parser.has_main: errors.append(name + ": missing <main> landmark")
    if not parser.has_title: errors.append(name + ": missing <title>")
    if not parser.has_description: errors.append(name + ": missing meta description")
    if parser.missing_alt: errors.append(name + ": images missing alt attributes: " + str(parser.missing_alt))
    if parser.inline_styles: errors.append(name + ": inline style attributes found: " + str(parser.inline_styles))
    if name == "404.html" and "noindex" not in parser.robots:
        errors.append(name + ": error page must set robots noindex")
    # styles.css hides the primary nav links below 680px unless a mobile menu exists.
    if "site-nav" in parser.classes and "mobile-menu" not in parser.classes:
        errors.append(name + ": navigation needs a mobile menu; nav links are hidden on small screens")
    for href in parser.links:
        if not href or href.startswith(("#", "mailto:", "tel:")): continue
        resolved = resolve_local(href)
        if resolved is None: continue
        kind, value = resolved
        if kind == "outside-base":
            errors.append(name + ": root-absolute link outside " + SITE_BASE + ": " + href)
            continue
        if not value.is_relative_to(ROOT):
            errors.append(name + ": local link escapes repository: " + href)
        elif value.is_dir():
            if not (value / "index.html").exists(): errors.append(name + ": directory link without index.html: " + href)
        elif not value.exists():
            errors.append(name + ": broken local link: " + href)


def check_published_files(errors):
    for required in PUBLIC_FILES:
        if not (ROOT / required).exists(): errors.append("Missing required file: " + required)
    if not WORKFLOW.exists():
        errors.append("Missing workflow: " + str(WORKFLOW.relative_to(ROOT)))
        return
    text = WORKFLOW.read_text(encoding="utf-8")
    match = re.search(r"for file in ([^;]+); do", text)
    if not match:
        errors.append("Workflow staging step does not declare a file allowlist")
        return
    staged = match.group(1).split()
    missing = sorted(set(PUBLIC_FILES) - set(staged))
    extra = sorted(set(staged) - set(PUBLIC_FILES))
    if missing: errors.append("Workflow does not publish: " + ", ".join(missing))
    if extra: errors.append("Workflow publishes files not in PUBLIC_FILES: " + ", ".join(extra))


def main():
    errors = []
    for name in HTML_PAGES:
        check_page(name, errors)
    check_published_files(errors)
    if errors:
        print("FAIL: site checks found issues")
        for error in errors: print(" - " + error)
        return 1
    print("PASS: HTML landmarks, metadata, IDs, image alt text, inline styles, local links, published file allowlist")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Dependency-free checks for the Iwwwan-labs static website."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import sys

ROOT = Path(__file__).resolve().parents[1]
class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.missing_alt, self.inline_styles = [], [], [], []
        self.has_main = self.has_title = self.has_description = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs: self.ids.append(attrs["id"])
        if tag == "a" and "href" in attrs: self.links.append(attrs["href"])
        if tag == "img" and "alt" not in attrs: self.missing_alt.append(self.getpos())
        if tag == "main": self.has_main = True
        if tag == "title": self.has_title = True
        if tag == "meta" and attrs.get("name", "").lower() == "description" and attrs.get("content", "").strip(): self.has_description = True
        if "style" in attrs: self.inline_styles.append(self.getpos())

def main():
    errors = []
    page = ROOT / "index.html"
    if not page.exists():
        print("FAIL: index.html is missing")
        return 1
    parser = SiteParser()
    parser.feed(page.read_text(encoding="utf-8"))
    parser.close()
    duplicates = [key for key, count in Counter(parser.ids).items() if count > 1]
    if duplicates: errors.append("Duplicate IDs: " + ", ".join(duplicates))
    if not parser.has_main: errors.append("Missing <main> landmark")
    if not parser.has_title: errors.append("Missing <title>")
    if not parser.has_description: errors.append("Missing meta description")
    if parser.missing_alt: errors.append("Images missing alt attributes: " + str(parser.missing_alt))
    if parser.inline_styles: errors.append("Inline style attributes found: " + str(parser.inline_styles))
    for href in parser.links:
        if not href or href.startswith(("#", "mailto:", "tel:")): continue
        parsed = urlparse(href)
        if parsed.scheme in ("http", "https") or href.startswith("//"): continue
        target = (ROOT / parsed.path).resolve()
        if not target.is_relative_to(ROOT): errors.append("Local link escapes repository: " + href)
        elif parsed.path and not target.exists(): errors.append("Broken local link: " + href)
    for required in ("styles.css", "sitemap.xml", "robots.txt"):
        if not (ROOT / required).exists(): errors.append("Missing required file: " + required)
    if errors:
        print("FAIL: site checks found issues")
        for error in errors: print(" - " + error)
        return 1
    print("PASS: HTML landmarks, metadata, IDs, image alt text, inline styles, local links, and required files")
    return 0

if __name__ == "__main__":
    sys.exit(main())

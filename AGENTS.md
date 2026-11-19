# AGENTS.md

Guidance for AI agents working in this repository.

## What this is
The public website for Iwwwan-labs. It is intentionally built with semantic HTML, CSS, and a small progressive-enhancement script. Keep it dependency-free.

## Layout
- `index.html` — page content, metadata, structured data, and GitHub API integration.
- `styles.css` — all visual styles and design tokens.
- `404.html` — custom not-found page, styled from `styles.css`.
- `scripts/check_site.py` — dependency-free HTML, link, and published-file checks.
- `sitemap.xml` and `robots.txt` — search crawler metadata.
- `.github/workflows/pages.yml` — quality checks, then a gated Pages deployment.
- `.github/dependabot.yml` — weekly GitHub Actions updates.

## Publishing
- The `deploy` job `needs: static-checks`, so it never runs when checks fail, are skipped, or are cancelled.
- Only files listed in `PUBLIC_FILES` (`scripts/check_site.py`) are staged into `_site/` and published. Add a file there and to the workflow staging loop together.
- `404.html` uses root-absolute `/website/...` paths because Pages serves it for missing URLs at any depth.

## Rules
- Do not add a framework, bundler, package manager, or build step.
- Do not add JavaScript libraries. Small progressive enhancements are acceptable.
- Keep all styling in `styles.css`; do not add inline style attributes.
- Preserve semantic landmarks, skip navigation, heading order, and keyboard access.
- Use safe DOM APIs (`textContent` / `createElement`) for external API data. Never inject repository data with `innerHTML`.
- The site must remain useful if JavaScript or the GitHub API is unavailable.
- Respect `prefers-reduced-motion` and maintain readable contrast.

## Commands
```bash
python3 -m http.server 8000
python3 scripts/check_site.py
```

## Before committing
- Check at 320px, 768px, and 1440px widths.
- Check keyboard focus and skip navigation.
- Ensure external links use safe target/rel attributes.
- Ensure the quality workflow passes.
- Do not merge pull requests without explicit user approval.

Follow [Iwwwan-labs/.github conventions](https://github.com/Iwwwan-labs/.github/blob/main/docs/CONVENTIONS.md).

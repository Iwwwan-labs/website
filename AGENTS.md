# AGENTS.md

Guidance for AI agents working in this repository.

## What this is
The public website for Iwwwan-labs. It is intentionally built with semantic HTML, CSS, and a small progressive-enhancement script. Keep it dependency-free.

## Layout
- `index.html` — page content, metadata, structured data, and GitHub API integration.
- `styles.css` — all visual styles and design tokens.
- `scripts/check_site.py` — dependency-free HTML checks.
- `sitemap.xml` and `robots.txt` — search crawler metadata.
- `.github/workflows/` — quality checks and GitHub Pages deployment.

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

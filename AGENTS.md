# AGENTS.md

Guidance for AI agents working in this repository.

## What this is

The public landing page for Iwwwan-labs. Static HTML and CSS only. There is no
build step, no framework, and no dependencies.

## Layout

- `index.html` — the entire page. Copy lives here.
- `styles.css` — all styling. Design tokens are CSS custom properties in `:root`.
- `.github/workflows/deploy-pages.yml` — deploys the repository root to GitHub Pages.

## Rules

- Do not add a build step, bundler, or framework. This repository stays dependency-free.
- Do not add JavaScript beyond small progressive enhancements. The page must work with JS disabled.
- Keep all styling in `styles.css`. Do not add inline `style` attributes.
- Preserve accessibility: keep the skip link, the landmark elements (`header`, `main`, `footer`, `nav`), and heading order.
- Maintain the color contrast of the existing palette. Check any new color against the background before using it.
- Respect `prefers-reduced-motion`.

## Commands

```bash
# Serve locally
python3 -m http.server 8000
```

There is no test suite. Verify changes by loading the page and checking both the
desktop and the narrow (under 640px) layout.

## Before committing

- The page renders correctly at 320px, 768px, and 1440px widths.
- Keyboard navigation reaches every interactive element.
- No console errors.

Follow the organization conventions in
[`Iwwwan-labs/.github`](https://github.com/Iwwwan-labs/.github/blob/main/docs/CONVENTIONS.md).

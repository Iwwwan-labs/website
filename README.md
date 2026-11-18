# Iwwwan-labs website

The public landing page for Iwwwan-labs. Static HTML and CSS, no build step.

Live at **https://iwwwan-labs.github.io/website/** once GitHub Pages is enabled.

## Structure

| Path | Purpose |
| --- | --- |
| `index.html` | The page |
| `styles.css` | All styling, single stylesheet |
| `.github/workflows/deploy-pages.yml` | Deploys to GitHub Pages on push to `main` |

## Run locally

Any static file server works. For example:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Deploy

Push to `main`. The workflow deploys automatically. Before the first run, enable
Pages once: **Settings → Pages → Build and deployment → Source: GitHub Actions**.

## Editing

- Copy lives directly in `index.html`.
- Design tokens (colors, radius, width) are CSS custom properties at the top of `styles.css`.
- Replace the placeholder `hello@example.com` address with the real contact address.

## Conventions

Follow the organization conventions in
[`Iwwwan-labs/.github`](https://github.com/Iwwwan-labs/.github/blob/main/docs/CONVENTIONS.md).
Branch names use `feat/`, `fix/`, `docs/`, `chore/`. Commits follow
[Conventional Commits](https://www.conventionalcommits.org/).

## License

[MIT](LICENSE) © Iwwwan-labs

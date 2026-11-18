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

Push to `main`. The workflow deploys automatically.

On a brand-new repository, Pages is disabled, so the first run fails with
`Resource not accessible by integration` while trying to create the Pages site.
Enable it once by hand: **Settings → Pages → Build and deployment → Source:
GitHub Actions**. Later runs then succeed without intervention.

The published URL is <https://iwwwan-labs.github.io/website/>.

## Editing

- Copy lives directly in `index.html`.
- Design tokens (colors, radius, width) are CSS custom properties at the top of `styles.css`.
- Contact links point at the GitHub organization. Replace them with a real address or form when one exists.

## Conventions

Follow the organization conventions in
[`Iwwwan-labs/.github`](https://github.com/Iwwwan-labs/.github/blob/main/docs/CONVENTIONS.md).
Branch names use `feat/`, `fix/`, `docs/`, `chore/`. Commits follow
[Conventional Commits](https://www.conventionalcommits.org/).

## License

[MIT](LICENSE) © Iwwwan-labs

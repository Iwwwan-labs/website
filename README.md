# Iwwwan-labs website

Public website for Iwwwan-labs, an independent software engineering studio.

**Live:** https://iwwwan-labs.github.io/website/

## Stack
- Semantic HTML and CSS
- Small progressive-enhancement script for the public GitHub repository showcase
- No framework, bundler, package manager, or build step
- GitHub Pages deployment through GitHub Actions

## Structure
| Path | Purpose |
| --- | --- |
| `index.html` | Website content, SEO metadata, structured data, repository showcase |
| `styles.css` | Responsive styles and design tokens |
| `scripts/check_site.py` | Dependency-free HTML and local-link checks |
| `sitemap.xml` | Sitemap |
| `robots.txt` | Search crawler guidance |
| `.github/workflows/quality.yml` | Pull request and main-branch quality checks |
| `.github/workflows/deploy-pages.yml` | GitHub Pages deployment |

## Run locally
```bash
python3 -m http.server 8000
```
Open http://localhost:8000.

## GitHub integration
The Work section reads public repositories from the GitHub REST API at runtime:
`https://api.github.com/orgs/Iwwwan-labs/repos?type=public&sort=updated&per_page=100`

No token or secret is used. If the API is unavailable, the repository section displays a fallback message and the rest of the website remains usable.

## Checks
Run locally with `python3 scripts/check_site.py`. It uses only the Python standard library. The same check runs for pull requests and pushes to `main`.

## Deploy
Set Pages source to **GitHub Actions** in Settings → Pages. Pushes to `main` deploy automatically. Pull requests run quality checks but do not publish the site.

## Editing
- Keep visual styles in `styles.css`.
- Keep the site dependency-free and progressively enhanced.
- Use relative paths for local assets and links so the project works at `/website/`.
- Update `sitemap.xml` if the canonical public URL changes.

Follow [Iwwwan-labs/.github conventions](https://github.com/Iwwwan-labs/.github/blob/main/docs/CONVENTIONS.md).

## License
[MIT](LICENSE) © Iwwwan-labs

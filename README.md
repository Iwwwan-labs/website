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
| `404.html` | Custom not-found page |
| `scripts/check_site.py` | Dependency-free HTML, local-link, and published-file checks |
| `sitemap.xml` | Sitemap |
| `robots.txt` | Search crawler guidance |
| `.github/workflows/pages.yml` | Quality checks, then a gated GitHub Pages deployment |
| `.github/dependabot.yml` | Weekly GitHub Actions version updates |

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
Run locally with `python3 scripts/check_site.py`. It uses only the Python standard library. It validates every HTML page (`index.html`, `404.html`) and checks that the deploy workflow publishes exactly the allowlisted files in `PUBLIC_FILES`. The same check runs for pull requests and pushes to `main`.

## Deploy
One-time setup: set Pages source to **GitHub Actions** in Settings → Pages. The workflow does not enable Pages for you, because `GITHUB_TOKEN` cannot change that setting.

`.github/workflows/pages.yml` runs quality checks in the `static-checks` job and the `deploy` job `needs:` it, so a failed, skipped, or cancelled check never reaches deployment. Pull requests run `static-checks` only; pushes to `main` and manual dispatches run both. Only `index.html`, `styles.css`, `sitemap.xml`, `robots.txt`, and `404.html` are staged into `_site/` and published; documentation, scripts, and workflow files are never uploaded.

## Editing
- Keep visual styles in `styles.css`.
- Keep the site dependency-free and progressively enhanced.
- Use relative paths for local assets and links so the project works at `/website/`.
- Update `sitemap.xml` if the canonical public URL changes.

Follow [Iwwwan-labs/.github conventions](https://github.com/Iwwwan-labs/.github/blob/main/docs/CONVENTIONS.md).

## License
[MIT](LICENSE) © Iwwwan-labs

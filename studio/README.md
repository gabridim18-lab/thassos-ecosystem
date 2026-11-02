# Thassos Social Media Studio — v1

A standalone HTML/CSS/JS page at `studio/index.html`. It reads `catalog/thassos-catalog.json` and can also fall back to the public GitHub raw URL. It requires **no Supabase credentials** and does not write to the database.

## What's available

- All primary records in `destinations/thassos`: ten categories, six languages, searchable filter.
- **Actualizare baza de date** button re-fetches the latest generated catalog (no caching), preserving the selected record where possible.
- Original photograph paths, filenames, diacritics and casing are preserved. Missing photos are labeled; local user photos are temporary, browser-only.
- Square post (1080×1080), portrait flyer (1080×1350), story/video cover (1080×1920): client-side PNG download and caption text export.
- CapCut ZIP containing chosen original photos, localized SRT, `scene-plan.json` and instructions (not an MP4 or native CapCut project).

## Setup and publication

1. Run `python3 scripts/build_social_catalog.py` at repository root for a local catalog.
2. Serve the folder via `python3 -m http.server 8000`, then open `http://localhost:8000/studio/`.
3. Every push to `main` containing a Thassos record automatically triggers GitHub Actions to refresh `catalog/thassos-catalog.json` (requires Actions enabled and workflow write permissions). The refresh button loads the latest **published** catalog; it does not commit to GitHub or trigger workflow execution.
4. For a public-facing deployment, configure GitHub Pages or Cloudflare Pages to serve this folder, ideally protected by authentication before sharing the Studio URL publicly.

Do not embed private Supabase service keys or access tokens in the HTML. The catalog is **public**, so do not add private owner contact details or unpublished secrets to the source JSON. Draft records remain selectable for preparation, but drafts and image rights must be checked before posting.

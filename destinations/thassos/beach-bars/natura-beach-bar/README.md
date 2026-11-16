# Natura Beach Bar — Thassos ecosystem package

**Category:** `beach-bars`  
**Business slug:** `natura-beach-bar`  
**Primary beachSlug:** `dasilio`  
**Nearby beach:** `ilio-mare`  
**Menu:** **2026**, confirmed by user. The 134 structured menu records cover the seven photographed menu pages, not an independently verified current restaurant menu.

## Target folder

`destinations/thassos/beach-bars/natura-beach-bar/`

Contents:
- `beach-bar.json` — business details, coordinates, 6-language summaries, cover/gallery references and beach links.
- `catalog-entry.json` — lightweight `type: beach_bar` entry for beach cards / nearby results.
- `imagini_manifest.json` — all 15 exact source filenames and expected `.webp` names.
- `menu.json` — 2026 menu (134 entries, 19 categories, 6 sections), organized for a future digital menu.
- `previzualizare.html` — fully self-contained offline-friendly preview, using only local images (once you add them).
- `sources/verification.json` — source references, location evidence and confirmations still needed.
- `DE_CONFIRMAT.md` — publication checklist.
- `images/`, `videos/`, `documents/` — ready and intentionally empty.

## Images — important

**No images are included.** Place your optimized `.webp` photos yourself in `images/`.
Keep the **exact filename**, including spaces, accents and parentheses, and replace **only** `.png` with `.webp`.
The 15th-photo inventory contains two byte-identical files:
`Burger și cartofi cu brânză topită(1).png` and `Burger și cartofi cu brânză topită.png`.
Both are documented in the manifest. The active gallery contains 14 unique photos, using the version without `(1)`.
Do not rename any files to `cover.webp` or `gallery_01.webp`.

## Beach links

`beachSlug: "dasilio"` refers to the existing beach record in:
`destinations/thassos/beaches/dasilio/beach.json`.
The `nearbyBeachSlugs` array also preserves `ilio-mare` as a nearby point of interest (subject to actual existing repo path).
**No beach JSON is overwritten and no new beach is counted.** The package is designed to be merged into the existing project, not to modify it automatically.

## Menu version and ordering

Menu year: **2026**. All listed prices come from the user's 7 photographed pages; verify details with the venue before any public launch.
No order submission, payments, QR codes, inventory tracking or staff screens have been enabled.
The menu data is structured so those modules can be added later if the business agrees.

## Integration checklist

1. Unzip into the repo root preserving the path.
2. Add the 14 unique optimized `.webp` files under `images/` (or all 15 filenames if you want both identical copies).
3. Verify exact case/diacritics on hosting; case-sensitive hosts will not tolerate renaming.
4. Add `catalog-entry.json` to the project's existing Beach Bars index using its established loader format.
5. Ensure the Dasilio beach loader recognizes `beachSlug: "dasilio"`.
6. Review `DE_CONFIRMAT.md` before publication.

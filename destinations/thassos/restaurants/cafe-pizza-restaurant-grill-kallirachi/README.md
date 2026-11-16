# Cafe Pizza Restaurant Grill Kallirachi — Thassos ecosystem

**Category:** `restaurants` · **Folder:** `destinations/thassos/restaurants/cafe-pizza-restaurant-grill-kallirachi/`
**Status:** prepared / inactive (not yet merged or published)

## Contents

- `restaurant.json` — main listing in RO, EN, EL, DE, BG, SR.
- `catalog-entry.json` — compact card for the restaurants catalog.
- `imagini_manifest.json` — exactly 10 original names, with `.webp` replacing `.png`.
- `menu.json` — explicitly empty; no official menu was provided.
- `nearby-location-link-proposal.json` — candidate link to the Skala Kallirachis area, NOT an automatic beach edit.
- `sources.json` — supplied information and cross-check notes.
- `previzualizare.html` — standalone local design preview; photo placeholders until WebP files are copied.
- `DE_CONFIRMAT.md` — checks before publication.
- `images/` — **empty**, for you to fill with converted WebP files.

## Image workflow

1. Convert your **10 supplied PNG photographs** to WebP without changing their content, their original base names, or their orientation.
2. Place the WebP files in `destinations/thassos/restaurants/cafe-pizza-restaurant-grill-kallirachi/images/`.
3. Use `imagini_manifest.json` to verify that each expected filename exists.
4. Publish `restaurant.json` and `catalog-entry.json` only after checking your current GitHub folder conventions. **Do not copy blindly over existing files.**
5. After checking data paths, set `active` to `true` and `mediaMissing` to `false` in the catalog and update the main file status as appropriate.

**Important:** Changing `.png` to `.webp` in JSON does NOT convert the image file. The binary format must also be converted by you.

## Explicit limits

- No live Google rating or review count. Different public snapshots conflict.
- Reported 07:00–00:00 hours and €10–30 range are not current/seasonally guaranteed.
- Menu, online ordering and prices are not enabled.
- No new beach entity is created, and no existing beach JSON is modified.
- Venue is on the harbour promenade, not a beach bar.

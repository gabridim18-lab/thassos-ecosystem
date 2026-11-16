# Oasis Grill Restaurant — Thassos

**Path:** `destinations/thassos/restaurants/oasis-grill-restaurant/`

Prepared 2026-11-03, based on information and photographs provided by the user.

## Contents

- `restaurant.json` — full data, six languages (RO, EN, EL, DE, BG, SR), contact, GPS, services and local image links.
- `menu.json` — manually transcribed **2025 menu** including historical prices (NOT current prices).
- `imagini_manifest.json` — image filenames, order, captions, dimensions, source.
- `catalog-entry.json` — lightweight record for merging into the central restaurants registry; do not replace the global registry with this file.
- `previzualizare.html` — self-contained offline editorial preview.
- `images/` — **11 WebP photographs**, each retaining the full original filename except `.png` → `.webp`.
- `documents/menu-2025/` — **8 original PNG menu images**, preserving exact filenames.
- `DE_CONFIRMAT.md` — nonblocking notes for future seasonal updates.

## Import

1. Copy the `destinations/` tree over the existing Thassos database root, preserving UTF-8 filenames.
2. Merge the single `catalog-entry.json` object into your central `restaurants/index.json` using `id=oasis-grill-restaurant`.
3. Check how your frontend resolves image paths relative to `restaurant.json`: gallery paths use `images/...`.
4. For a 2027 public site, **do not display `price2025EUR` as live price**. The flags `pricesAreCurrent=false` and `showPricesPublicly=false` are set intentionally.
5. Do not show individual review texts. Google rating 4.2 / 203 is a dated user-provided snapshot (2026-11-03), not a live API response.
6. The Google Maps URL is a geocoordinate navigation/search URL; it is not a booking link.

## Source and verification limits

- Business name, contact, location, facilities and Google Maps details were supplied directly by the user.
- All 11 photos were explicitly confirmed by the user as belonging to Oasis Grill Restaurant.
- Menu transcription is based on the 2025 screenshots. Check the original source images for exact spelling and ambiguous labels.
- The previous Google Maps snippet was not enough to establish a complete, verified weekly opening schedule.
- There is no reservation booking page on record. Use phone for enquiries; do not invent a website or reservation URL.

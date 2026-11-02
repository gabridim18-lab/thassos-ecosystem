#!/usr/bin/env python3
"""Build a read-only, multi-category social media catalog from Thassos records.

Only explicit canonical records are included; never interpret menu or image
manifests as independent places. No external packages or network required.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
import os
from pathlib import Path

CATEGORIES = {
    "accommodations": "accommodation.json",
    "areas": "area.json",
    "attractions": "attraction.json",
    "beach-bars": "beach-bar.json",
    "beaches": "beach.json",
    "heritage": "heritage.json",
    "local-eats-drinks": "cafe-bar.json",
    "religious-sites": "religious-site.json",
    "restaurants": "restaurant.json",
    "services": "service.json",
}
LANGS = ("ro", "en", "el", "de", "bg", "sr")
PHOTO_EXT = {".webp", ".png", ".jpg", ".jpeg", ".avif"}


def value(*parts):
    for item in parts:
        if isinstance(item, str) and item.strip():
            return item.strip()
    return ""


def dct(v):
    return v if isinstance(v, dict) else {}


def get_photo_refs(media):
    """Only parse explicitly photo-bearing keys, never unrelated menu text."""
    result = []
    def walk(v):
        if isinstance(v, str):
            if Path(v).suffix.lower() in PHOTO_EXT:
                result.append(v)
        elif isinstance(v, list):
            for x in v:
                walk(x)
        elif isinstance(v, dict):
            if isinstance(v.get("file"), str):
                walk(v["file"])
            elif isinstance(v.get("path"), str):
                walk(v["path"])
            else:
                for child in v.values():
                    walk(child)
    for key in ("cover", "hero", "mobileCover", "sunsetImage", "logoOrEntrancePhoto", "galleryOrder", "gallery", "images"):
        walk(media.get(key))
    return result


def resolve_photo(ref, record_dir, root):
    """Return repository-relative POSIX path, rejecting escaping paths."""
    norm = ref.replace("\\", "/").lstrip("/")
    if norm.startswith("destinations/thassos/"):
        target = root / norm
    elif "/" not in norm and (record_dir / "images" / norm).is_file():
        target = record_dir / "images" / norm
    else:
        target = record_dir / norm
    target = target.resolve()
    try:
        return target.relative_to(root.resolve()).as_posix()
    except ValueError:
        return None


def normalize(record, record_path, root, category):
    slug = record_path.parent.name
    location = dct(record.get("location"))
    media = dct(record.get("media"))
    name = record.get("name")
    names = name if isinstance(name, dict) else {}
    identity = dct(record.get("identity"))
    label = value(name if isinstance(name, str) else None,
                  names.get("default"), names.get("en"),
                  record.get("displayName"), identity.get("international_name"), slug.replace("-", " ").title())
    content = dct(record.get("content"))
    translations = dct(record.get("translations"))
    seo = dct(record.get("seo"))
    localizations = {}
    for lang in LANGS:
        t = dct(translations.get(lang))
        c = dct(content.get(lang))
        s = dct(seo.get(lang))
        localizations[lang] = {
            "name": value(t.get("name"), t.get("title"), names.get(lang), c.get("title"), label),
            "tagline": value(t.get("tagline"), c.get("tagline"), c.get("hero")),
            "summary": value(t.get("summary"), t.get("shortDescription"), t.get("short_description"), c.get("shortDescription"), c.get("short"), c.get("summary")),
            "description": value(t.get("description"), t.get("long_description"), c.get("description"), c.get("long")),
            "social_caption": value(t.get("social_caption"), s.get("social_caption")),
            "seo_title": value(t.get("seoTitle"), t.get("seo_title"), c.get("seoTitle"), s.get("title")),
            "seo_description": value(t.get("seoDescription"), t.get("seo_description"), c.get("seoDescription"), s.get("description")),
        }
    available_files = sorted({p.relative_to(root).as_posix() for p in record_path.parent.rglob("*") if p.is_file() and p.suffix.lower() in PHOTO_EXT})
    refs = get_photo_refs(media)
    referenced = []
    seen = set()
    for ref in refs:
        path = resolve_photo(ref, record_path.parent, root)
        if path and path not in seen:
            seen.add(path)
            referenced.append(path)
    # Include manually supplied WebP photos even if not yet listed in the media field.
    for path in available_files:
        if path not in seen:
            referenced.append(path)
            seen.add(path)
    images = [{"path": path, "filename": Path(path).name, "available": (root / path).is_file()} for path in referenced]
    editorial = dct(record.get("editorial"))
    publication = dct(record.get("publication"))
    publish_ready = bool(editorial.get("publish_ready", publication.get("publishReady", False)))
    rights = editorial.get("rights_cleared_for_sale")
    if rights is None:
        rights = media.get("photoRightsConfirmed")
    if rights is None:
        rights = media.get("photoRightsStatus") == "confirmed"
    area_slug = value(location.get("areaSlug"), location.get("area_slug"), dct(record.get("related_places")).get("area_slug"), dct(record.get("connections")).get("area_slug")) or None
    beach_slug = value(location.get("beachSlug"), record.get("beachSlug")) or None
    center = dct(location.get("center"))
    lat = next((x for x in (location.get("latitude"), location.get("lat"), center.get("lat")) if isinstance(x, (float, int)) and not isinstance(x,bool)), None)
    lng = next((x for x in (location.get("longitude"), location.get("lng"), center.get("lng")) if isinstance(x, (float, int)) and not isinstance(x,bool)), None)
    return {
        "id": value(record.get("id"), f"thassos-{category}-{slug}"),
        "slug": slug, "category": category,
        "subcategory": value(record.get("subcategory"), record.get("venueType"), record.get("record_type")) or None,
        "name": label, "area_slug": area_slug, "beach_slug": beach_slug,
        "coordinates": {"lat": lat, "lng": lng},
        "source_file": record_path.relative_to(root).as_posix(),
        "publish_ready": publish_ready, "photo_rights_confirmed": bool(rights),
        "photos_available": sum(bool(i["available"]) for i in images),
        "photos_declared": len(images), "images": images,
        "translations": localizations,
    }


def build(root):
    root = Path(root).resolve()
    base = root / "destinations" / "thassos"
    if not base.is_dir():
        raise ValueError(f"Missing Thassos directory: {base}")
    items = []
    seen_ids = set()
    for category, filename in CATEGORIES.items():
        for path in sorted((base / category).glob(f"*/{filename}")):
            try:
                raw = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeError) as exc:
                raise ValueError(f"Invalid record {path}: {exc}") from exc
            if not isinstance(raw, dict):
                raise ValueError(f"Record must be an object: {path}")
            item = normalize(raw, path, root, category)
            if item["id"] in seen_ids:
                raise ValueError(f"Duplicate ID: {item['id']}")
            seen_ids.add(item["id"])
            items.append(item)
    items.sort(key=lambda x: (x["category"], x["name"].casefold(), x["slug"]))
    return {
        "schema_version": "thassos-social-catalog/v1",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": {"repository": "gabridim18-lab/thassos-ecosystem", "ref": "main", "commit": os.getenv("GITHUB_SHA")},
        "total": len(items), "counts": dict(sorted(Counter(i["category"] for i in items).items())),
        "items": items,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    p.add_argument("--output", default="catalog/thassos-catalog.json")
    args = p.parse_args()
    root = Path(args.root).resolve()
    output = root / args.output
    payload = build(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Catalog generated: {payload['total']} places, {len(payload['counts'])} categories -> {output}")

if __name__ == "__main__":
    main()

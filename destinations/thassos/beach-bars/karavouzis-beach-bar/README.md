# Karavouzis Beach Bar / Canopy Beach Bar — Thassos

## Categorie și plajă
- **Categorie:** `beach-bars`
- **Cale:** `destinations/thassos/beach-bars/karavouzis-beach-bar/`
- **Plajă canonică:** **Dasilio Beach**, `beachSlug: "dasilio"`
- **ID plajă:** `gr-thassos-beach-dasilio`
- **Fișier plajă existentă:** `destinations/thassos/beaches/dasilio/beach.json`
- **Zona:** `skala-prinos` (localitate, nu beach slug)
- **Fără asociere automată cu Ilio Mare / Etisies / Skala Prinos ca altă plajă.**

## Numele locației — important
În Google Maps apare ca `Karavouzis beach bar`. Pe website-ul familiei Karavouzis este prezentat un rebranding la **Canopy Beach Bar**, la **3 mai 2026**. Același telefon (+30 698 755 7903) este publicat de site-ul oficial. Pentru a evita dublurile, păstrăm slugul vechi stabil `karavouzis-beach-bar`, dar în identitate avem numele public nou **Canopy Beach Bar** și denumirea veche ca alias.

## Fotografii — NICIUNA inclusă
- Sunt **10 nume** în `imagini_manifest.json`, toate în format așteptat `.webp`.
- Tu le convertești / uniformizezi și le pui în `images/`. Nu schimba numele, diacriticele, spațiile ori literele mari.
- `cover`: `images/Apus peste un resort tropical.webp`.
- Fotografia `Prânz mediteranean la Karyouli Beach Bar.webp` are în nume alt beach bar; păstrată în manifest, dar de verificat atribuirea înainte de publicare.
- Fără imagini în ZIP, fără conversie, fără redimensionare.

## Fișiere
- `beach-bar.json`: înregistrarea principală + descrieri în 6 limbi (RO/EN/EL/DE/BG/SR).
- `catalog-entry.json`: card pentru indexul general.
- `beach-link-patch.json`: referința de card pentru plaja Dasilio, **nu este aplicată automat** în beach.json.
- `imagini_manifest.json`: inventar complet foto.
- `menu.json`: meniu indisponibil, fără preparate sau tarife inventate.
- `sources.json`: proveniență și rebranding.
- `previzualizare.html`: simulare standalone, imaginile apar automat după copierea fișierelor în images.
- `DE_CONFIRMAT.md`: verificările înainte de publicare.

## Legături de proximitate
- Pinch of Salt ≈439 m în linie dreaptă
- Oasis Grill Restaurant ≈512 m în linie dreaptă
- CAT Dive Center ≈730 m în linie dreaptă

Acestea sunt **vecine**, nu li se atribuie artificial `beachSlug: dasilio`. Referințele lor se păstrează pe propriile înregistrări.

## Publicare
1. Copiază folderul în repository sub calea indicată.
2. Introdu în `images/` toate cele zece fișiere `.webp`, numele exacte din manifest.
3. Actualizează indexul central conform arhitecturii repo-ului și asociază cardul la `beachSlug: dasilio`.
4. Nu crea un record nou separat pentru Canopy. Verifică fotografia cu Karyouli înainte de a o publica.
5. Verifică programul (Google: 09:00–02:00; website oficial: 09:00–23:00) și politica șezlongurilor. Până atunci NU afișa „open now” sau tarife ferme.

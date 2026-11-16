# Karibou Seaside Tavern — Thassos

**Categorie:** `restaurants` / `traditional-greek-tavern`  
**Zonă:** `skala-prinos` — Ormos Prinou  
**Plajă:** Prinos Beach (cunoscută și ca Skala Prinos Beach)  
**Slug al plajei din inventarul existent:** `skala-prinos`  
**Data pregătirii:** 2026-11-05

## Integrare

1. Copiază directorul `destinations/thassos/restaurants/karibou-seaside-tavern/` în proiect.
2. **Tu** convertești și uniformizezi imaginile; apoi copiezi cele **10** fișiere `.webp` cu exact numele din `imagini_manifest.json` în `images/`.
3. `images/` este intenționat **gol** în acest ZIP. Nu există imagini ascunse, duplicate sau fișiere de tip placeholder în el.
4. Indexează `catalog-entry.json` în categoria **Restaurants** după verificarea căilor și a formatului din sistemul real. Intrarea are `active:false` și `mediaMissing:true` până când sunt copiate fotografiile, ca să nu apară imagini lipsă în producție.
5. `beach-link-patch.json` conține legătura propusă pentru pagina **Prinos Beach**. Patch-ul nu modifică automat `beach.json`. Calea din registrul existent este `destinations/thassos/beaches/skala-prinos/beach.json`; verifică schema de legături în implementarea actuală și adaugă cardul în secțiunea Restaurants / Nearby.
6. `restaurant.json` include șase limbi: **ro, en, el, de, bg, sr**. `menu.json` este intenționat gol: nu a fost furnizat un meniu oficial.
7. `previzualizare.html` este o pagină independentă HTML/CSS/JS, utilizabilă local. Până la adăugarea imaginilor arată subtitluri în locul acestora.

## Reguli privind fotografiile

- **Nu redenumi fișierele**. Din numele original schimbă numai `.png` în `.webp`; păstrează diacriticele și majusculele.
- Unele ultime uploaduri au apărut în mediul conversației cu sufixul automat `(1)` fiindcă fotografiile au fost încărcate repetat. În manifest folosim numele originale, **fără** acel sufix duplicat.
- Nu copia `.png` în `images/`; aici se adaugă numai `.webp` după conversia ta.

## Precauții la publicare

- Prețul €15–30/persoană și programul 11:00–23:00 sunt informații orientative dintr-un instantaneu furnizat, **nu** date în timp real.
- Cele 98 de recenzii nu constituie un rating numeric. Nu se inventează nota în stele.
- Fotografiile cu preparate ilustrează locația, dar nu reprezintă un meniu verificat zilnic.
- Verifică drepturile de utilizare a imaginilor și exactitatea datelor cu proprietarul înainte de publicare.

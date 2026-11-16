# Mpes Sto Psito — Greek Grill & Gyros

## Local Eats & Drinks — categoria potrivită pentru snack bar

`destinations/thassos/local-eats-drinks/mpes-sto-psito/`

**Acest pachet NU conține fotografii sau capturi ale meniului.** Conține numai structura, fișierele JSON, documentația și o previzualizare HTML offline.

Încadrare în catalog: `category: local-eats-drinks`, `subcategory: snack-bar` (gyros / souvlaki / takeaway). Nu îl adăuga și în `restaurants`.

## Fișiere

- `snack-bar.json`: datele localului, descrieri în 6 limbi (RO/EN/EL/DE/BG/SR), facilități, contact, orar raportat, rating datat.
- `menu.json`: preparatele și băuturile identificate în 6 capturi; prețuri de referință, ascunse public până la verificare.
- `imagini_manifest.json`: numele exacte ale imaginilor ce trebuie copiate.
- `catalog-entry.json`: intrarea pentru catalogul central; `active=false` până la completare.
- `sources.json`: proveniența informațiilor și conflictul între programele afișate.
- `previzualizare.html`: previzualizare locală, funcțională și înainte de încărcarea fotografiilor.
- `DE_CONFIRMAT.md`: aspecte rămase de verificat.

## Adăugarea imaginilor de către tine

1. Redimensionează/optimizează cele 7 fotografii la rezoluția pe care o alegi, păstrând orientarea.
2. Exportă-le în **WebP** cu numele de mai jos (exact, inclusiv diacritice și spații).
3. Copiază-le în directorul `images/`.
4. Dacă dorești să păstrezi și capturile meniului, copiază fișierele PNG enumerate mai jos în `documents/menu-captures/` fără a le modifica.
5. Verifică `DE_CONFIRMAT.md`, apoi schimbă `status.published`, `status.active`, `active` și `catalog-entry.json.active` după validarea integrării.

### Fotografiile așteptate în `images/`

- `images/Taverna grecească lângă mare.webp` — hero
- `images/Farfurie grecească cu gyros și tzatziki.webp` — food
- `images/Gyros crocant sub luminile nopții.webp` — food
- `images/Cafenea la apus, lângă ferry.webp` — context
- `images/Gyros, cartofi și bere Mythos la cafenea.webp` — food
- `images/Ταβέρνα Μπες στο Ψητό τη Νύχτα.webp` — atmosphere
- `images/Cafenea mediteraneană la apus.webp` — exterior

### Capturile meniului (opțional, în `documents/menu-captures/`)

- `documents/menu-captures/image(20261104-095703).png`
- `documents/menu-captures/image(20261104-095723).png`
- `documents/menu-captures/image(20261104-095746).png`
- `documents/menu-captures/image(20261104-095800).png`
- `documents/menu-captures/image(20261104-095812).png`
- `documents/menu-captures/image(20261104-095830).png`

## Atenție

- Fotografiile **nu** au fost copiate sau modificate; lipsa lor în această arhivă este intenționată.
- Imaginea cu feribotul este doar context pentru zona portului, nu dovadă că restaurantul are propria terasă spre mare.
- Coordonatele GPS exacte nu sunt confirmate și sunt `null`. Nu copia coordonatele unui alt restaurant din vecinătate.
- În captura Google oferită de utilizator, localul are program vineri–duminică 12:00–21:00, iar o altă sursă publică afișează ore diferite. Verifică la proprietar.
- Ratingul 4,8 (279 recenzii) este o fotografie a datelor din 2026-11-04, nu o actualizare live.
- Poți păstra prețurile în JSON intern, însă nu le afișa ca actuale fără reconfirmare.
- Nu s-au preluat texte individuale ale recenziilor.

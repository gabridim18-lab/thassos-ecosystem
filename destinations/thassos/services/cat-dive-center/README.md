# CAT Dive Center — Thassos | Pachet pentru ecosistem

**Folder pentru import:** `destinations/thassos/services/cat-dive-center/`  
**Categorie:** `services` → `diving-and-water-activities`  
**Pregătit:** 2026-11-04 | **Publicat în GitHub:** NU

## Fișiere
- `service.json`: profil complet și prezentare RO, EN, EL, DE, BG, SR.
- `activities.json`: șapte tipuri de activități, fără prețuri sau durate inventate.
- `imagini_manifest.json`: toate cele 8 fotografii primite; 7 în galerie, una exclusă.
- `catalog-entry.json`: element pentru index central.
- `sources.json`: proveniența și statutul datelor.
- `previzualizare.html`: pagină demonstrativă self-contained, cu selector de limbă.
- `images/`: șapte WebP optimizate, denumiri păstrate.
- `documents/needs-review/`: steagul Pinch of Salt, **nu se afișează** la CAT.
- `DE_CONFIRMAT.md`: listă de verificări înainte de publicare.

## Integrare
Copiază directorul de mai sus în proiect. Adaugă conținutul din `catalog-entry.json` în indexul `services` doar după verificarea formatului folosit în aplicația reală. Nu modifica automat un index necunoscut. Căile din JSON sunt relative la directorul curent, cu excepția `detailPath` care pornește din `destinations/`.

## Politica editorială
- Fără recenzii individuale; 81 este numărul de review-uri furnizat ca snapshot, rating numeric necunoscut.
- Nu există date verificate de tarif, capacitate, durată sau locuri libere.
- Programul raportat de utilizator (08:00–23:00) diferă de programul SSI (10:00–22:00); înainte de publicare afișează „Contact for current hours”.
- Instruirea în română este listată oficial; confirmă disponibilitatea instructorului la rezervare.
- Fotografia cu steagul „Pinch of Salt Restaurant” nu aparține prezentării CAT și este arhivată separat.
- Fotografiile sunt primite de la utilizator; drepturile de publicare nu au fost verificate independent.
- Nu am scris în repository sau în baze de date online.

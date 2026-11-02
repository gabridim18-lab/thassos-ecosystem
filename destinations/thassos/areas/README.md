# Thassos Ecosystem — Areas (pachet inițial)

## Ce conține

- `index.json` — indexul celor 20 de zone (15 de coastă, 5 din interior)
- `<slug>/area.json` — 20 de fișiere individuale, bazate pe template-ul agreat
- `<slug>/images/.gitkeep` — 20 de foldere pregătite pentru imaginile WebP (GitHub nu păstrează directoare goale)
- `lista_imagini.csv` — lista exactă a celor 100 de fotografii de adăugat

## Instalare în GitHub

Dezarhivează pachetul în rădăcina repository-ului, astfel încât structura să fie:

`destinations/thassos/areas/limenas/area.json`
`destinations/thassos/areas/limenas/images/limenas1.webp`
`destinations/thassos/areas/limenas/images/limenas2.webp`
`...`

Toate cele cinci căi sunt DEJA în `area.json`: imaginea 1 în `media.cover`, celelalte patru în `media.gallery`. Adăugarea fotografiilor cu numele corecte nu mai necesită editarea JSON-ului.

## IMPORTANT — stare editorială

Acesta este pachetul de **structură**, nu un catalog gata de publicat. Sunt precompletate numele, clasificarea, GPS-uri **provizorii** din inventarul de planificare, 6 chei de limbă și căile fotografiilor.

Textele detaliate, verificarea GPS și a rutelor de acces, conexiunile cu plajele/atracțiile/restaurantele, documentarea surselor și drepturile foto rămân de completat localitate cu localitate. Pentru aceste lucrări editoriale vom actualiza `area.json`; pentru simpla adăugare a fotografiilor NU îl vom mai modifica.

`editorial.publish_ready` și `index.area_entries[].publish_ready` sunt false. `nearby_enabled` este false până la confirmarea pozițiilor GPS.

### Particularități
- `pachis`, `pefkari`, `alyki`, `chrysi-ammoudia`: sectoare turistice, nu orașe administrative.
- `kazaviti`: grup comun Megalo + Mikro Kazaviti; reperul provizoriu este Megalo Kazaviti, nu un centru oficial al grupului.
- Porturile `limenas` și `skala-prinos` au loc pentru o integrare viitoare cu ferry; nu stocăm orare schimbătoare în JSON.

## Nume fișiere

În fiecare folder se folosesc exact: `<slug>1.webp` ... `<slug>5.webp`, fără spații și cu litere mici. Recomandate: WebP landscape 16:9, optimizate pentru web, drepturi comerciale confirmate.

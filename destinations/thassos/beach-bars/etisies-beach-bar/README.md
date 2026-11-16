# Etisies Beach Bar — pachet pentru ecosistemul Thassos

**Categorie:** `beach-bars` · **Plajă:** `dasilio` (Dasilio Beach) · **Slug local:** `etisies-beach-bar`.

## Directorul corect
`destinations/thassos/beach-bars/etisies-beach-bar/`

## Fișiere
- `beach-bar.json` — fișa localului, 6 limbi, contact, coordonate, galerie, referință la meniu și plajă.
- `catalog-entry.json` — fișă simplificată pentru catalog; inactivă până la publicare.
- `imagini_manifest.json` — **exact** cele nouă nume originale, doar sufixul `.webp`.
- `menu.json` — transcrierea listei de prețuri fotografiate; **nevalidată, fără comenzi online**.
- `beach-link-patch.json` — legătură propusă către `destinations/thassos/beaches/dasilio/beach.json`; nu aplică automat modificări.
- `sources.json`, `DE_CONFIRMAT.md` — proveniență și verificări înainte de publicare.
- `previzualizare.html` — verificare locală simplă, nu pagină de producție.

## Ce faci cu fotografiile
Convertește local cele **9** fotografii PNG în WebP la rezoluția ta standard, **fără să schimbi baza numelui**, apoi copiază-le în `images/`. Păstrează spațiile, diacriticele, majusculele și sufixul `(1)` de unde există. `cover` este `images/Bar pe plajă sub umbrele aurii.webp`.

## Meniu
Prețurile au fost citite din panoul fotografiat, dar data fotografiei este necunoscută. Prețurile rămân o sursă internă, nu un meniu comercial curent până la confirmare cu proprietarul. Comenzile către șezlong **nu sunt activate**.

## Integrare
Copiază întregul folder în repository sub `destinations/thassos/beach-bars/`. Verifică structura actuală a `dasilio/beach.json` înainte de a integra cartea din `beach-link-patch.json`; nu suprascrie beach.json.

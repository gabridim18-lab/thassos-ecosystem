# Instalare Thassos Social Media Studio — pas cu pas

Pachet pregătit pentru **repository-ul existent** `gabridim18-lab/thassos-ecosystem`.
Nu se înlocuiesc și nu se modifică fișierele existente din `destinations/thassos/`.

## 1. Copiere pe calculator

1. În GitHub Desktop selectează repository-ul `thassos-ecosystem`.
2. Meniu **Repository → Show in Explorer**. Se deschide directorul local al repository-ului.
3. Extrage conținutul acestei arhive **direct în acel director**, păstrând subdirectoarele `.github`, `scripts`, `studio`, `tests`.
4. Trebuie să ai:
   - `.github/workflows/build-social-catalog.yml`
   - `scripts/build_social_catalog.py`
   - `tests/test_social_catalog.py`
   - `studio/index.html`
   - `studio/README.md`
   - `INSTALARE-RO.md` (opțional)

**Important:** Windows ascunde uneori folderele care încep cu punct. Verifică inclusiv `.github`.

## 2. Publicare prin GitHub Desktop

1. În GitHub Desktop verifică modificările. Nu șterge niciun fișier existent.
2. Scrie la **Summary**: `Add Thassos Social Media Studio and automatic catalog`.
3. Apasă **Commit to main**, apoi **Push origin**.
4. Deschide repository-ul pe GitHub → fila **Actions** → **Build Thassos social catalog**.
5. Dacă totul este configurat pentru GitHub Actions cu drept de scriere, workflow-ul creează automat `catalog/thassos-catalog.json` și îl adaugă la `main`.
6. În GitHub Desktop apasă **Fetch origin** și apoi **Pull origin** pentru a sincroniza noul catalog înapoi pe calculator.

Dacă apare eroare `403 Resource not accessible by integration`, în GitHub → Settings → Actions → General → Workflow permissions alege `Read and write permissions` (dacă ai această opțiune), apoi rulează workflow-ul din nou. Poți genera și local catalogul din terminal: `python scripts/build_social_catalog.py`, apoi faci Commit și Push.

## 3. Folosirea studioului local

În folderul local al repository-ului deschide un terminal și rulează:

```bash
python -m http.server 8000
```

Deschide în browser `http://localhost:8000/studio/`.
Apasă **Actualizează baza de date**. Selectează o locație și limba, alege imagini, exportă PNG sau ZIP pentru CapCut.

## 4. Actualizări ulterioare

- Când adaugi un JSON nou și faci **Push origin**, workflow-ul regenerează indexul de pe GitHub.
- Butonul din Studio descarcă acel index publicat. **Nu face singur commit, upload sau push**.
- Originalele WebP rămân cu numele lor, inclusiv diacritice/spații.
- Pentru studio online, se poate configura ulterior o adresă separată și autentificare; site-ul public tassos.forum este un proiect distinct.

## Ce NU face această versiune

Nu generează direct MP4. Exportă un pachet pentru CapCut (fotografii + SRT + plan). Nu modifică baza de date, nu urcă automat imagini locale pe GitHub și nu publică automat postări pe rețele sociale.

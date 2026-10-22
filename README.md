# Thassos Ecosystem — Model complet de plajă v1

Aceasta este **prima fișă editorială completă**, dedicată **Golden Beach / Χρυσή Αμμουδιά**. Fișierul `destinations/thassos/beaches/golden/beach.json` este standardul de lucru pentru următoarele plaje; nu este o listă de 65 plaje finalizate.

## Structură

- `identity` — nume, aliasuri, avertisment pentru duplicate și sectoare.
- `location` — coordonate pe un singur rând în JSON, link Google Maps și status de precizie. Punctul actual este de referință, nu un acces rutier certificat.
- `physical_profile` — nisip, fundul apei, adâncime, valuri, umbră.
- `visitor_experience` — recomandări pentru familii, activități, aglomerație.
- `facilities` + `access_and_cost` — dotări, acces, costuri necunoscute marcate explicit `null`.
- `certifications` — Blue Flag 2026 confirmată pentru **sectorul Golden Beach Camping**, nu atribuită automat întregului golf.
- `dynamic_fields` — valori meteo și temperatura apei lăsate goale pentru preluare live la afișare.
- `translations` — **ro, en, el, de, bg, sr**, fiecare cu nume, slogan, rezumat, descriere, recomandări practice, highlights, SEO și text social media.
- `media` — fotografii candidate Wikimedia Commons documentate, dar încă neimportate. `cover` și `gallery` rămân necompletate până la alegerea imaginilor finale.
- `source_references` și `editorial` — verificări și condiții de publicare.

## Ce facem la următoarea plajă

1. Păstrăm toate cheile și versiunea schemei.
2. Înlocuim `id`, `slug`, localizarea, caracteristicile verificate și textele în șase limbi.
3. Alegem și adăugăm fotografiile în folderul `images/`, cu atribuirea și licența fiecăreia.
4. Validăm fișierul JSON folosind `python scripts/validate_beach.py`.
5. Setăm `editorial.publish_ready=true` doar după verificare completă.

Nu sunt incluse fotografii descărcate. Linkurile Wikimedia sunt **candidați cu licența documentată**, iar conversia / decuparea trebuie însoțită de atribuiri și respectarea CC BY-SA.

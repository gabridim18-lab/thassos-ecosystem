#!/usr/bin/env python3
"""Validare minimă a fișelor; rulat din rădăcina repo-ului."""
import json
from pathlib import Path

root=Path(__file__).resolve().parent.parent
files=list((root/'destinations/thassos/beaches').glob('*/beach.json'))
if not files: raise SystemExit('Nu exista fișiere beach.json')
for p in files:
    x=json.loads(p.read_text(encoding='utf-8'))
    assert x['record_type']=='beach', p
    assert x['destination_id']=='gr-thassos', p
    assert x['id'].startswith('gr-thassos-beach-'), p
    assert x['slug']==p.parent.name, p
    assert set(x['translations'])=={'ro','en','el','de','bg','sr'}, p
    for lang,t in x['translations'].items():
        for key in ('name','tagline','summary','description','practical_tips','highlights','seo_title','seo_description','social_caption','photo_alt'):
            assert t.get(key), (p,lang,key)
    loc=x['location']
    assert loc.get('coordinate_source')=='google_maps', p
    if loc['lat'] is not None and loc['lng'] is not None:
        assert 40 < loc['lat'] < 41 and 24 < loc['lng'] < 25, p
    assert len(x['source_references'])>=2, p
    assert x['media']['cover'] is None or Path(root/x['media']['cover']).exists(), p
    for g in x['media']['gallery']:
        assert Path(root/g['path']).exists(), p
    if x['editorial']['publish_ready']:
        assert x['media']['cover'] is not None, f'{p}: publish_ready requires cover'
    print('OK',p.relative_to(root), 'translations:',len(x['translations']))
print('Total validate:',len(files))

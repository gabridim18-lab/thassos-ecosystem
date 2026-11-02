import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'build_social_catalog.py'
spec = importlib.util.spec_from_file_location('build_social_catalog', SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class CatalogTests(unittest.TestCase):
    def test_categories_and_paths_and_localizations(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            beach = root/'destinations/thassos/beaches/golden'
            beach.mkdir(parents=True)
            (beach/'images').mkdir()
            (beach/'images'/'Plajă însorită.webp').write_bytes(b'fake photo')
            (beach/'beach.json').write_text(json.dumps({
                'id':'beach-golden','slug':'golden','record_type':'beach',
                'identity':{'international_name':'Golden Beach'},
                'media':{'cover':'destinations/thassos/beaches/golden/images/Plajă însorită.webp',
                         'gallery':['images/future.webp']},
                'translations':{'ro':{'name':'Plaja de Aur','summary':'Nisip fin'},'en':{'name':'Golden Beach','social_caption':'Hello Thassos'}}
            }), encoding='utf-8')
            extra = root/'destinations/thassos/local-eats-drinks/cafe'
            extra.mkdir(parents=True)
            (extra/'cafe-bar.json').write_text(json.dumps({
                'id':'local-cafe','name':'Café House','media':{'hero':'images/Un nume.webp'},
                'content':{'ro':{'short':'Cafea bună','long':'Descriere.'},'en':{'short':'Great coffee'}},
                'location':{'areaSlug':'skala-sotiros','latitude':40.7,'longitude':24.5},
                'publication':{'publishReady': True}
            }), encoding='utf-8')
            (extra/'menu.json').write_text('{"id":"a-menu-that-must-not-appear"}',encoding='utf-8')
            catalog=mod.build(root)
            self.assertEqual(catalog['total'],2)
            self.assertEqual(set(catalog['counts']),{'beaches','local-eats-drinks'})
            b=next(x for x in catalog['items'] if x['category']=='beaches')
            self.assertEqual(b['images'][0]['filename'],'Plajă însorită.webp')
            self.assertTrue(b['images'][0]['available'])
            self.assertFalse(b['images'][1]['available'])
            self.assertEqual(b['translations']['ro']['name'],'Plaja de Aur')
            self.assertEqual(b['translations']['en']['social_caption'],'Hello Thassos')
            c=next(x for x in catalog['items'] if x['category']=='local-eats-drinks')
            self.assertEqual(c['translations']['ro']['description'],'Descriere.')
            self.assertEqual(c['area_slug'],'skala-sotiros')
            self.assertTrue(c['publish_ready'])
            self.assertFalse(c['images'][0]['available'])
            self.assertEqual(c['coordinates']['lat'],40.7)

    def test_no_escape_from_repository_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); rec=root/'destinations/thassos/services/a';rec.mkdir(parents=True)
            self.assertIsNone(mod.resolve_photo('../../../../../../etc/passwd.webp',rec,root))

    def test_duplicate_id_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for name in ['a','b']:
                folder=root/f'destinations/thassos/services/{name}';folder.mkdir(parents=True)
                (folder/'service.json').write_text('{"id":"duplicate","name":"Same"}',encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'Duplicate ID'):
                mod.build(root)

if __name__=='__main__':unittest.main()

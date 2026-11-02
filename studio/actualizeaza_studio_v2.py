#!/usr/bin/env python3
"""Safe, repeatable local upgrade for the existing self-contained Thassos Studio HTML."""
from pathlib import Path
from datetime import datetime
import os
import re
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
PAGE = ROOT / "studio" / "index.html"
VERSION = "THASSOS_STUDIO_V2_LOCALIZED_FACTS_20261102"

STYLE = r'''
    /* THASSOS_STUDIO_V2_LOCALIZED_FACTS_20261102 */
    .v2-editor{margin:17px 0 10px;padding:15px;border:1px solid #cae4e9;border-radius:13px;background:linear-gradient(130deg,#f7fbfc,#eaf5f6)}
    .v2-editor h3{margin:0 0 11px;font-size:15px;color:#0a536c}
    .v2-editor .v2-hint{font-size:12px;color:#607b87;margin:4px 0 12px}
    .v2-facts{display:grid;grid-template-columns:1fr;gap:6px;margin:8px 0 11px;max-height:210px;overflow-y:auto}
    .v2-facts label{display:flex;align-items:center;gap:9px;font-size:13px;font-weight:600;color:#25465b;cursor:pointer;margin:0;padding:8px 10px;background:#fff;border:1px solid #d9e8eb;border-radius:8px}
    .v2-facts input{flex-shrink:0;width:17px;height:17px;accent-color:#087f9d}
    .v2-editor .field{margin:8px 0}.v2-editor input[type=range]{width:100%;accent-color:#087f9d}
    .v2-flex{display:grid;grid-template-columns:1fr 1fr;gap:10px}
    .v2-editor .v2-empty{font-size:12px;color:#6b8490;padding:9px 0}
    @media(max-width:510px){.v2-flex{grid-template-columns:1fr}}
'''

EDITOR = r'''
    <!-- THASSOS_STUDIO_V2_LOCALIZED_FACTS_20261102 -->
    <section class="v2-editor" aria-label="Informații suplimentare pe flyer">
      <h3>Informații suplimentare pentru flyer</h3>
      <p class="v2-hint">Alege până la 3 detalii din fișa JSON. Sunt opționale și apar pe imagine, nu doar în descrierea postării.</p>
      <div id="v2Facts" class="v2-facts"><div class="v2-empty">Alege o locație pentru a citi fișa JSON...</div></div>
      <div class="field"><label for="v2CustomFact">Sau adaugă un detaliu propriu (opțional)</label><input id="v2CustomFact" type="text" maxlength="85" placeholder="Ex.: Terasă privată cu vedere la mare"></div>
      <div class="v2-flex">
        <div class="field"><label for="v2Eyebrow">Text mic în partea de sus</label><input id="v2Eyebrow" type="text" maxlength="85"></div>
        <div class="field"><label for="v2Position">Titlul și textul mai jos / mai sus</label><input id="v2Position" type="range" min="-100" max="130" step="10" value="45"><div class="tiny">Se repoziționează automat dacă adaugi mai multe detalii.</div></div>
      </div>
      <p class="v2-hint">Datele provin din JSON-ul original; verifică informațiile și drepturile fotografiilor înainte de publicare. Câmpurile introduse manual nu se traduc automat.</p>
    </section>
'''

SCRIPT = r'''
  // THASSOS_STUDIO_V2_LOCALIZED_FACTS_20261102
  const V2_DICT={
    ro:{top:'VACANȚĂ ÎN THASSOS',bottom:'THASSOS  ·  GRECIA',guests:'oaspeți',maxGuests:'până la {n} oaspeți',standardGuests:'{n} locuri standard',perRoom:'{n} oaspeți / cameră',bedrooms:'{n} dormitoare',bathrooms:'{n} băi',rooms:'{n} camere',tips:'Sfat',highlights:'Atracție',amenity:'Facilitate'},
    en:{top:'HOLIDAY IN THASSOS',bottom:'THASSOS  ·  GREECE',guests:'guests',maxGuests:'up to {n} guests',standardGuests:'{n} standard places',perRoom:'{n} guests / room',bedrooms:'{n} bedrooms',bathrooms:'{n} bathrooms',rooms:'{n} rooms',tips:'Tip',highlights:'Highlight',amenity:'Amenity'},
    el:{top:'ΔΙΑΚΟΠΕΣ ΣΤΗ ΘΑΣΟ',bottom:'ΘΑΣΟΣ  ·  ΕΛΛΑΔΑ',guests:'επισκέπτες',maxGuests:'έως {n} επισκέπτες',standardGuests:'{n} βασικές θέσεις',perRoom:'{n} άτομα / δωμάτιο',bedrooms:'{n} υπνοδωμάτια',bathrooms:'{n} μπάνια',rooms:'{n} δωμάτια',tips:'Συμβουλή',highlights:'Αξιοθέατο',amenity:'Παροχή'},
    de:{top:'URLAUB AUF THASSOS',bottom:'THASSOS  ·  GRIECHENLAND',guests:'Gäste',maxGuests:'bis zu {n} Gäste',standardGuests:'{n} reguläre Plätze',perRoom:'{n} Gäste / Zimmer',bedrooms:'{n} Schlafzimmer',bathrooms:'{n} Bäder',rooms:'{n} Zimmer',tips:'Tipp',highlights:'Highlight',amenity:'Ausstattung'},
    bg:{top:'ПОЧИВКА НА ТАСОС',bottom:'ТАСОС  ·  ГЪРЦИЯ',guests:'гости',maxGuests:'до {n} гости',standardGuests:'{n} стандартни места',perRoom:'{n} гости / стая',bedrooms:'{n} спални',bathrooms:'{n} бани',rooms:'{n} стаи',tips:'Съвет',highlights:'Акцент',amenity:'Удобство'},
    sr:{top:'ODMOR NA TASOSU',bottom:'TASOS  ·  GRČKA',guests:'gostiju',maxGuests:'do {n} gostiju',standardGuests:'{n} standardnih mesta',perRoom:'{n} gostiju / soba',bedrooms:'{n} spavaće sobe',bathrooms:'{n} kupatila',rooms:'{n} soba',tips:'Savet',highlights:'Istaknuto',amenity:'Pogodnost'}
  };
  const v2Language=()=>V2_DICT[$('language').value]||V2_DICT.ro;
  const v2FormatNumber=(template,n)=>{
    let value=template.replace('{n}',String(n));
    if(n===1){
      const pairs=[['oaspeți','oaspete'],['locuri standard','loc standard'],['dormitoare','dormitor'],['băi','baie'],['camere','cameră'],
        ['guests','guest'],['bedrooms','bedroom'],['bathrooms','bathroom'],['rooms','room'],['standard places','standard place'],
        ['υπνοδωμάτια','υπνοδωμάτιο'],['μπάνια','μπάνιο'],['δωμάτια','δωμάτιο'],
        ['спални','спалня'],['бани','баня'],['стаи','стая'],
        ['Bäder','Bad'],['spavaće sobe','spavaća soba'],['kupatila','kupatilo']];
      for(const [plural,singular] of pairs){if(value.includes(plural))value=value.replace(plural,singular);}
    }
    return value;
  };
  let v2Raw=null,v2Facts=[],v2SelectedFacts=new Set(),v2Request=0;
  function v2SyncTop(){$('v2Eyebrow').value=v2Language().top;}
  function v2GetSelectedTexts(){
    const lines=v2Facts.filter(f=>v2SelectedFacts.has(f.id)).map(f=>f.value);
    const extra=$('v2CustomFact').value.trim();
    // Manual detail takes priority, while the material stays within 3 lines.
    return extra?[...lines.slice(0,2),extra]:lines.slice(0,3);
  }
  function v2TextValues(value){
    if(typeof value==='string')return[value];
    if(Array.isArray(value))return value.flatMap(v2TextValues);
    if(value && typeof value==='object'){
      const a=[value.text,value.title,value.description,value.label].filter(v=>typeof v==='string');
      return a.length?[a[0]]:[];
    }
    return [];
  }
  function v2ExtractFacts(record){
    const facts=[],p=record?.property||{},units=Array.isArray(record?.unitTypes)?record.unitTypes:[],d=v2Language();
    const add=(id,val)=>{if(typeof val==='string'&&val.trim()&&!facts.some(f=>f.id===id))facts.push({id,value:val.trim()});};
    const number=(v)=>Number.isInteger(v)&&v>0?v:null;
    // Carefully distinguish advertised maximum from standard occupancy.
    const max=number(p.maximumGuests)||number(units.length===1?units[0].guestsMaximum:null);
    const standard=number(p.standardCapacityGuests);
    if(max)add('maxGuests',v2FormatNumber(d.maxGuests,max));
    else if(standard)add('standardGuests',v2FormatNumber(d.standardGuests,standard));
    const roomGuests=number(units.length===1?units[0].standardGuestsPerUnit:null);
    if(roomGuests)add('perRoom',v2FormatNumber(d.perRoom,roomGuests));
    const beds=number(p.bedroomsTotal);if(beds)add('bedrooms',v2FormatNumber(d.bedrooms,beds));
    const bathrooms=number(p.bathroomsTotal)||number(p.privateBathroomsTotal);if(bathrooms)add('bathrooms',v2FormatNumber(d.bathrooms,bathrooms));
    const rooms=number(p.roomsTotal);if(rooms)add('rooms',v2FormatNumber(d.rooms,rooms));
    const amenities=record?.amenities||{};
    const knownLabels={wifi:'Wi-Fi',internet:'Internet',private_parking:'Parcare privată',parking:'Parcare',barbecue_area:'BBQ',sunbeds_for_guests:'Șezlonguri pentru oaspeți',sun_umbrellas_for_guests:'Umbrele pentru oaspeți'};
    const localized={
      en:{private_parking:'Private parking',parking:'Parking',barbecue_area:'BBQ',sunbeds_for_guests:'Guest sunbeds',sun_umbrellas_for_guests:'Guest umbrellas'},
      de:{private_parking:'Privatparkplatz',parking:'Parkplatz',barbecue_area:'Grillplatz',sunbeds_for_guests:'Sonnenliegen',sun_umbrellas_for_guests:'Sonnenschirme'},
      el:{private_parking:'Ιδιωτικό πάρκινγκ',parking:'Πάρκινγκ',barbecue_area:'Μπάρμπεκιου',sunbeds_for_guests:'Ξαπλώστρες',sun_umbrellas_for_guests:'Ομπρέλες'},
      bg:{private_parking:'Частен паркинг',parking:'Паркинг',barbecue_area:'Барбекю',sunbeds_for_guests:'Шезлонги',sun_umbrellas_for_guests:'Чадъри'},
      sr:{private_parking:'Privatni parking',parking:'Parking',barbecue_area:'Roštilj',sunbeds_for_guests:'Ležaljke',sun_umbrellas_for_guests:'Suncobrani'}
    };
    // Only explicit first-party claims; never promote unverified third-party-only amenities.
    const confirmed=Array.isArray(amenities.confirmedByCurrentWebsite)?amenities.confirmedByCurrentWebsite:
       (Array.isArray(amenities.property)?amenities.property:[]);
    confirmed.filter(s=>typeof s==='string').forEach(s=>{
      if(knownLabels[s])add('amenity:'+s,(localized[$('language').value]||{})[s]||knownLabels[s]);
    });
    // Bilingual/six-language editorial fields are considered extra content choices.
    const lang=$('language').value;
    const t=record?.translations?.[lang]||record?.translations?.en||{};
    const c=record?.content?.[lang]||record?.content?.en||{};
    const highlightTexts=v2TextValues(t.highlights||c.highlights);
    highlightTexts.slice(0,4).forEach((s,i)=>{const v=s.trim();if(v&&v.length<=110)add('highlight:'+i,v);});
    const tips=v2TextValues(t.practical_tips||c.practicalTips);
    tips.slice(0,2).forEach((s,i)=>{const v=s.trim();if(v&&v.length<=110)add('tip:'+i,v);});
    return facts;
  }
  function v2RenderFacts(){
    const target=$('v2Facts');target.replaceChildren();
    if(!v2Facts.length){const e=document.createElement('div');e.className='v2-empty';e.textContent=v2Raw?'Fișa nu conține detalii suplimentare structurate pentru flyer. Poți adăuga un text propriu.':'Se încarcă detaliile din fișa JSON...';target.append(e);return;}
    for(const fact of v2Facts){
      const label=document.createElement('label');
      const checkbox=document.createElement('input');checkbox.type='checkbox';checkbox.checked=v2SelectedFacts.has(fact.id);
      checkbox.onchange=()=>{
        if(checkbox.checked&&v2SelectedFacts.size>=3){checkbox.checked=false;exportStatus('Maximum 3 detalii pe flyer, pentru a păstra lizibilitatea.',true);return;}
        if(checkbox.checked)v2SelectedFacts.add(fact.id);else v2SelectedFacts.delete(fact.id);draw();
      };
      const value=document.createElement('span');value.textContent=fact.value;label.append(checkbox,value);target.append(label);
    }
  }
  async function v2LoadFacts(item){
    const request=++v2Request;v2Raw=null;v2Facts=[];v2SelectedFacts.clear();$('v2CustomFact').value='';v2RenderFacts();
    if(!item?.source_file){v2RenderFacts();return;}
    const rel=item.source_file.split('/').map(encodeURIComponent).join('/');
    for(const url of ['../'+rel,RAW+rel]){
      try{
        const response=await fetch(url,{cache:'no-store'});
        if(!response.ok)continue;
        const json=await response.json();
        if(request!==v2Request||selected()?.id!==item.id)return;
        if(json.id!==item.id)continue;
        v2Raw=json;v2Facts=v2ExtractFacts(json);v2RenderFacts();draw();return;
      }catch(e){/* try source from remote repository */}
    }
    if(request===v2Request){v2Raw={};v2RenderFacts();}
  }
  function v2TextWidth(ctx,str,max){
    let v=String(str||'');while(v.length>1&&ctx.measureText(v).width>max)v=v.slice(0,-2)+'…';return v;
  }
'''

DRAW = r'''
  async function draw(){
    const current=++state.loadId,canvas=$('creativeCanvas'),ctx=canvas.getContext('2d'),format=$('format').value;
    const w=1080,h=format==='story'?1920:format==='flyer'?1350:1080;canvas.width=w;canvas.height=h;
    const bg=ctx.createLinearGradient(0,0,w,h);bg.addColorStop(0,'#087994');bg.addColorStop(1,'#062b4b');ctx.fillStyle=bg;ctx.fillRect(0,0,w,h);
    const photo=selectedPhotos()[0];if(photo){try{
      const img=await loadImage(photo);if(current!==state.loadId)return;
      const scale=Math.max(w/img.naturalWidth,h/img.naturalHeight);
      ctx.drawImage(img,(w-img.naturalWidth*scale)/2,(h-img.naturalHeight*scale)/2,img.naturalWidth*scale,img.naturalHeight*scale);
    }catch(e){exportStatus(e.message,true);}}
    if(current!==state.loadId)return;
    const gradient=ctx.createLinearGradient(0,h*.18,0,h);
    gradient.addColorStop(0,'rgba(2,21,38,0)');gradient.addColorStop(.51,'rgba(3,30,49,.24)');gradient.addColorStop(1,'rgba(2,24,41,.93)');
    ctx.fillStyle=gradient;ctx.fillRect(0,0,w,h);
    const pad=70,maxWidth=w-2*pad;
    const eyebrow=$('v2Eyebrow').value.trim()||v2Language().top;
    ctx.textBaseline='alphabetic';ctx.textAlign='left';ctx.font='700 27px system-ui';
    const topText=v2TextWidth(ctx,eyebrow,maxWidth-56);const topWidth=Math.min(ctx.measureText(topText).width+50,maxWidth);
    ctx.fillStyle='rgba(2,40,59,.58)';ctx.beginPath();ctx.roundRect(pad,58,topWidth,56,14);ctx.fill();
    ctx.fillStyle='#e7fafc';ctx.fillText(topText,pad+24,96);
    const name=$('headline').value||'Thassos';let font=format==='story'?77:format==='flyer'?73:69;
    let titleLines=[];for(let attempts=0;attempts<18;attempts++){
      ctx.font=`800 ${font}px system-ui`;titleLines=wrap(ctx,name,maxWidth,3);
      if(titleLines.every(line=>ctx.measureText(line).width<=maxWidth+1)||font<=38)break;
      font-=3;
    }
    const titleHeight=font+13,summaryFont=35,summaryHeight=47;
    ctx.font=`400 ${summaryFont}px system-ui`;
    const summaryLines=wrap(ctx,$('subtitle').value,maxWidth,3);
    const facts=v2GetSelectedTexts();
    const factsHeight=facts.length?facts.length*52+20:0;
    const blockHeight=titleLines.length*titleHeight+18+summaryLines.length*summaryHeight+factsHeight;
    const base=h-(format==='story'?600:format==='flyer'?465:385);
    const shift=Number($('v2Position').value)||0;
    const lastSafeStart=h-151-blockHeight;
    const start=Math.max(h*.22,Math.min(base+shift,lastSafeStart));
    ctx.fillStyle='#fff';ctx.shadowColor='rgba(0,0,0,.25)';ctx.shadowBlur=8;
    ctx.font=`800 ${font}px system-ui`;
    titleLines.forEach((line,i)=>ctx.fillText(line,pad,start+i*titleHeight));
    ctx.shadowBlur=0;ctx.font=`400 ${summaryFont}px system-ui`;
    let y=start+titleLines.length*titleHeight+16;
    summaryLines.forEach((line,i)=>ctx.fillText(line,pad,y+i*summaryHeight));
    y+=summaryLines.length*summaryHeight+22;
    for(const [i,fact] of facts.entries()){
      ctx.font='650 28px system-ui';
      const display=v2TextWidth(ctx,fact,maxWidth-57);const chipWidth=Math.min(ctx.measureText(display).width+48,maxWidth);
      const chipY=y+i*52;
      ctx.fillStyle='rgba(11,92,112,.85)';ctx.beginPath();ctx.roundRect(pad,chipY-31,chipWidth,43,10);ctx.fill();
      ctx.fillStyle='#fff';ctx.fillText(display,pad+23,chipY);
    }
    ctx.font='700 26px system-ui';ctx.fillStyle='#b9f2ef';ctx.fillText(v2Language().bottom,pad,h-74);
  }
'''


def replace_once(content, old, new, label):
    n = content.count(old)
    if n != 1:
        raise RuntimeError(f"Cannot safely update {label}: expected 1 match, found {n}. No files modified.")
    return content.replace(old, new, 1)


def main():
    if not PAGE.is_file():
        print("ERROR: Studio not found. Put BOTH installer files in the main thassos-ecosystem folder, beside the studio directory.")
        return 1
    html=PAGE.read_text(encoding='utf-8')
    if VERSION in html:
        print("Studio V2 already installed. No changes necessary.")
        return 0
    required=("const REPO='gabridim18-lab/thassos-ecosystem'", "function selectListing(id)", "async function draw()", "const slugify=", "$('language').onchange")
    if not all(marker in html for marker in required):
        print("ERROR: This Studio version is different from the checked V1. Please do not overwrite manually.")
        return 1
    # All transforms are in memory first. Do not modify original until validation succeeds.
    html=replace_once(html, '  </style>', STYLE+'\n  </style>', 'style')
    html=replace_once(html, '    <h3>Fotografii pentru material și video</h3>', EDITOR+'\n    <h3>Fotografii pentru material și video</h3>', 'editor')
    html=replace_once(html, '  async function draw(){', SCRIPT+'\n  async function draw(){', 'fact helpers')
    begin=html.index('  async function draw(){')
    end=html.index('  const slugify=',begin)
    if end-begin>5500:raise RuntimeError('Unexpected draw function length; aborting safely')
    html=html[:begin]+DRAW+'\n'+html[end:]
    html=replace_once(html,
        '    renderListings();renderPhotos();draw();exportStatus(item.photos_available?',
        '    v2SyncTop();v2LoadFacts(item);renderListings();renderPhotos();draw();exportStatus(item.photos_available?',
        'selected listing')
    html=replace_once(html,
        '    renderListings();draw();};',
        '    renderListings();v2SyncTop();if(v2Raw)v2Facts=v2ExtractFacts(v2Raw);v2RenderFacts();draw();};',
        'language handler') if '    renderListings();draw();};' in html else replace_once(html,
        '}renderListings();draw();};',
        '}renderListings();v2SyncTop();if(v2Raw)v2Facts=v2ExtractFacts(v2Raw);v2RenderFacts();draw();};',
        'language handler')
    html=replace_once(html,
        "  $('downloadVideo').onclick=exportVideo;draw();refresh();",
        "  $('v2Eyebrow').addEventListener('input',draw);$('v2Position').addEventListener('input',draw);$('v2CustomFact').addEventListener('input',draw);\n  $('downloadVideo').onclick=exportVideo;v2SyncTop();draw();refresh();",
        'initialization')
    if html.count(VERSION) < 3 or html.count('  async function draw(){') != 1:
        raise RuntimeError('Patch validation failed, original kept unchanged')
    backup_dir=Path(tempfile.gettempdir())/'thassos-studio-backups';backup_dir.mkdir(parents=True,exist_ok=True)
    backup=backup_dir/f"studio-index-before-v2-{datetime.now().strftime('%Y%m%d-%H%M%S')}.html"
    shutil.copy2(PAGE,backup)
    # Same-folder atomic replacement on Windows.
    staged=PAGE.with_name('index.html.v2.tmp');staged.write_text(html,encoding='utf-8')
    os.replace(staged,PAGE)
    print('SUCCESS: Studio V2 installed!')
    print(f'Edited: {PAGE}')
    print(f'Original backup: {backup}')
    print('Now refresh http://localhost:8000/studio/ with Ctrl+F5.')
    print('In GitHub Desktop, commit ONLY studio/index.html if you wish to publish the update.')
    return 0

if __name__=='__main__':
    try:sys.exit(main())
    except Exception as e:
        print('ERROR:',e)
        print('The existing Studio file was left unchanged if installation could not be completed.')
        sys.exit(1)

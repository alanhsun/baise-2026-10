"""Download explicitly selected Commons photographs and retain license metadata."""
import csv, json, re, time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    'baise-memorial': 'Baise Uprising Memorial Hall (20230403093401).jpg',
    'yuedong-hall': "Former site of the Headquarters of the 7th Army of Chinese Workers' and Peasants' Red Army (20230403090249).jpg",
    'quyang-lake': '渠洋湖-岜蒙水库，靖西，广西 Guangxi 05-10-13 - panoramio.jpg',
    'goose-spring-water': '20260212 E Quan (102247).jpg',
    'goose-spring-landscape': '20260212 E Quan (103545).jpg',
    'jiuzhou-wenchang': '文昌阁 (7164678729).jpg',
    'jiuzhou-village': '旧州 (7164677977).jpg',
    'tongling-waterfall': 'TongLing 03.jpg',
}

def get(url):
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers={'User-Agent': 'BaiseFamilyTravelGuide/1.0 (educational itinerary; Wikimedia Commons attribution)'}), timeout=50) as r:
                return r.read()
        except Exception:
            if attempt == 2: raise
            time.sleep(2)

def plain(value):
    return re.sub('<[^>]*>', '', value).strip()

def main():
    path = ROOT / 'research/photo-metadata.json'
    metadata = json.loads(path.read_text('utf-8')) if path.exists() else {}
    for slug, title in FILES.items():
        if slug not in metadata:
            params = dict(action='query', format='json', prop='imageinfo', iiprop='url|extmetadata', iiurlwidth=1600, titles='File:' + title)
            result = json.loads(get('https://commons.wikimedia.org/w/api.php?' + urlencode(params)))
            info = next(iter(result['query']['pages'].values()))['imageinfo'][0]
            metadata[slug] = info
            path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), 'utf-8')
        info = metadata[slug]
        ext = info['extmetadata']
        if slug == 'tongling-waterfall':
            # Manually verified on the Commons description page and embedded date.
            ext['Artist'] = {'value': 'SEVEN', 'source': 'manually verified Commons page'}
            ext['DateTimeOriginal'] = {'value': '2005-05-03', 'source': 'Commons page and visible date'}
            path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), 'utf-8')
        license_name = plain(ext['LicenseShortName']['value'])
        if not license_name.startswith(('CC BY', 'Public domain')):
            raise ValueError(f'License requires manual review: {slug}: {license_name}')
        out = ROOT / 'media' / (slug + '.jpg')
        if not out.exists():
            out.write_bytes(get(info.get('thumburl', info['url'])))
        print(slug, license_name, plain(ext.get('Artist', {}).get('value','')), plain(ext.get('DateTimeOriginal', {}).get('value','')), out.stat().st_size, flush=True)
    registry = ROOT / 'data/images.csv'
    with registry.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    rows = [r for r in rows if r['image_path'] not in ['media/'+s+'.jpg' for s in FILES]]
    for slug, info in metadata.items():
        ext = info['extmetadata']
        rows.append(dict(image_path='media/'+slug+'.jpg', source_url=info['descriptionurl'], license=plain(ext['LicenseShortName']['value']), credit=plain(ext['Artist']['value']), notes='摄影日期：'+plain(ext.get('DateTimeOriginal',{}).get('value','未注明'))+'；未裁剪或改色，使用Commons缩略版本；许可：'+ext.get('LicenseUrl',{}).get('value','')))
    with registry.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['image_path','source_url','license','credit','notes']); writer.writeheader(); writer.writerows(rows)

if __name__ == '__main__': main()

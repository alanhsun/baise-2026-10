"""Resolve licensed photo inserts and refresh the consolidated reading copy."""
import json, re, shutil
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
PHOTOS = {
    'baise-memorial': ('百色起义纪念馆正面', '2023-04-03'),
    'yuedong-hall': ('粤东会馆门楼', '2023-04-03'),
    'quyang-lake': ('渠洋湖峰林与水面', '2013-10-05'),
    'goose-spring-water': ('鹅泉泉水与岸边景观', '2026-02-12'),
    'goose-spring-landscape': ('鹅泉亭桥与游人', '2026-02-12'),
    'jiuzhou-wenchang': ('旧州文昌阁建筑细部，历史黑白照片', '2012-01-17'),
    'jiuzhou-village': ('旧州街巷，历史黑白照片', '2012-01-17'),
    'tongling-waterfall': ('通灵大瀑布，历史照片', '2005-05-03'),
}

def main():
    data = json.loads((ROOT/'research/photo-metadata.json').read_text('utf-8'))
    credits = ['# 景点实拍照片与许可', '', '照片来自Wikimedia Commons，保留原构图、色彩、边框与日期标记；使用站点提供的图片版本，没有AI生成或修补。拍摄日期不代表2026年10月现场。各照片沿用其自身许可，摄影者不为本攻略背书。', '']
    inserts = {}
    for slug, (title, date) in PHOTOS.items():
        info = data[slug]; meta = info['extmetadata']
        author = re.sub('<[^>]+>', '', meta['Artist']['value']).strip()
        license_name = meta['LicenseShortName']['value']
        url = quote(info['descriptionurl'], safe=':/%_-.,')
        license_url = meta['LicenseUrl']['value'].replace('http:', 'https:')
        credit = f'摄影：{author} · {date} · [照片来源]({url}) · [{license_name}]({license_url}) · 未裁剪或改色。'
        inserts[slug] = f'![{title} · 拍摄于{date}](media/{slug}.jpg)\n\n{credit}'
        credits += [f'## {title}', '', f'文件：media/{slug}.jpg', '', credit, '']
    for path in [ROOT/'content/overview.md', *sorted((ROOT/'content/days').glob('*.md'))]:
        value = path.read_text('utf-8')
        for slug, insert in inserts.items():
            value = value.replace('@@PHOTO:'+slug+'@@', insert)
        path.write_text(value, 'utf-8')
    (ROOT/'media/PHOTO-CREDITS.md').write_text('\n'.join(credits), 'utf-8')
    dining = (ROOT/'content/dining-guide.md').read_text('utf-8')
    meals = {int(n):body.strip() for n,body in re.findall(r'^## D(\d) [^\n]+\n(.*?)(?=^## D\d |\Z)', dining, re.M|re.S)}
    parts = [(ROOT/'content/overview.md').read_text('utf-8')]
    for n,path in enumerate(sorted((ROOT/'content/days').glob('day-*.md')), 1):
        value = path.read_text('utf-8')
        value = value.replace('## 看点与现场提醒', '## 当天美食\n\n'+meals[n]+'\n\n## 看点与现场提醒', 1)
        parts += ['\n---\n', value]
    (ROOT/'详尽攻略.md').write_text('\n'.join(parts), 'utf-8')
    shutil.copy2(ROOT/'research/social-validation.md', ROOT/'研究与核验说明.md')
    print('Resolved photo inserts and refreshed consolidated Markdown.')

if __name__ == '__main__': main()

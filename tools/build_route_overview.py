"""Render the original route diagram from labels; no third-party image editing."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONT = Path('C:/Windows/Fonts/msyh.ttc')

def main():
    image = Image.new('RGB', (1500, 600), '#f7f4ed')
    draw = ImageDraw.Draw(image)
    def label(x, y, text, size=24, color='#173e34'):
        draw.text((x, y), text, font=ImageFont.truetype(str(FONT), size), fill=color)
    label(50, 30, '六天五晚 · 三人山水旅行', 39)
    label(50, 100, 'D2 浩坤湖往返百色｜D3 渠洋湖后入住靖西｜D4 鹅泉｜D5 靖西乘火车到南宁', 24, '#5e6b63')
    nodes = [
        ('东莞南城', '10/1 出发', '高铁去百色'),
        ('百色', '10/1—3 · 2晚', 'D2 浩坤湖往返'),
        ('靖西', '10/3—5 · 2晚', '渠洋湖、鹅泉'),
        ('南宁', '10/5—6 · 1晚', 'K9304 已购'),
        ('东莞南城', '10/6 回家', 'D593 经广州南'),
    ]
    for i, (city, date, note) in enumerate(nodes):
        x = 50 + i * 295
        draw.rounded_rectangle((x, 210, x+220, 395), radius=20, fill='#fffdf8', outline='#c6cbbf', width=2)
        label(x+20, 228, city, 31)
        label(x+20, 287, date, 20, '#a94b2c')
        label(x+20, 335, note, 21, '#5e6b63')
        if i < 4:
            draw.line((x+230, 300, x+282, 300), fill='#245a4a', width=4)
            draw.polygon([(x+282, 300), (x+270, 291), (x+270, 309)], fill='#245a4a')
    label(50, 454, 'D5 K9304 靖西→南宁已购；D6 D593 南宁东→广州南已购，接番禺城际回东莞。', 26, '#a94b2c')
    label(50, 540, '3人｜每晚1间房｜5晚共5间夜｜南宁站附近住宿，次日提前打车去南宁东', 24)
    image.save(ROOT/'media/route-overview.png')
    print('Rendered current six-day route diagram.')

if __name__ == '__main__':
    main()

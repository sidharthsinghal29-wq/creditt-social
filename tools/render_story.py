"""Make a 1080x1920 (9:16) story image from a 4:5 feed image.

Usage: python3 tools/render_story.py <src.jpg> <dst.jpg> "<top label>" "<bottom line>" [accent]
- top label: short line above the post (e.g. "Buyer's market update"); "" for none
- bottom line: short CTA below the post (e.g. "Free chat: creditt.com.au"); "" for none
- accent: hex colour for the top label (default #FFD15D; use #FFD11F for Aussie)
"""
import sys
from PIL import Image, ImageDraw, ImageFont

F = '/usr/share/fonts/opentype/inter/'
W, H = 1080, 1920
PW, PH = 1000, 1250


def fit(d, text, name, size, maxw):
    f = ImageFont.truetype(F + name, size)
    while d.textlength(text, font=f) > maxw and size > 24:
        size -= 2
        f = ImageFont.truetype(F + name, size)
    return f


def story(src, dst, top, bottom, accent='#FFD15D'):
    im = Image.new('RGB', (W, H), '#413080')
    d = ImageDraw.Draw(im)
    post = Image.open(src).convert('RGB').resize((PW, PH), Image.LANCZOS)
    y = (H - PH) // 2
    im.paste(post, ((W - PW) // 2, y))
    if top:
        tf = fit(d, top, 'Inter-Bold.otf', 40, W - 120)
        d.text(((W - d.textlength(top, font=tf)) / 2, (y - tf.size) // 2), top, font=tf, fill=accent)
    if bottom:
        bf = fit(d, bottom, 'Inter-Bold.otf', 44, W - 120)
        yb = y + PH + ((H - y - PH) - bf.size) // 2
        d.text(((W - d.textlength(bottom, font=bf)) / 2, yb), bottom, font=bf, fill='white')
    im.save(dst, quality=92)


if __name__ == '__main__':
    a = sys.argv[1:]
    story(a[0], a[1], a[2], a[3], a[4] if len(a) > 4 else '#FFD15D')

"""Make a 1080x1350 Creditt social card that promotes a website guide.

Usage: python3 tools/make_guide_card.py <spec.json> <out.jpg>

spec.json:
{
  "kicker": "NEW GUIDE",                      # short label, upper case (e.g. NEW GUIDE, UPDATED FOR DECEMBER)
  "headline": ["Guarantor home loans:", "how a family", "guarantee works"],   # 2-4 short lines
  "highlight": [1, 2],                        # optional: indexes of headline lines drawn in yellow
  "points": ["Limited vs full guarantees", "..."],   # 3-4 short points (under ~45 chars each)
  "url": "creditt.com.au/guarantor-home-loans"       # shown on the button
}
Prints an error and exits 1 if any text would overflow; shorten and re-run.
"""
import json
import sys
from PIL import Image, ImageDraw, ImageFont

F = '/usr/share/fonts/opentype/inter/'
LOGO = 'brand/creditt/creditt-logo-light-text.png'
W, H, M = 1080, 1350, 72
PURPLE, FOOT, YEL, PEACH, LAV = '#4B1F68', '#413080', '#FFD15D', '#F19B70', '#D0B7EF'


def font(n, s):
    return ImageFont.truetype(F + n, s)


def wrap(d, text, f, w):
    words, lines, cur = text.split(), [], ''
    for wd in words:
        t = (cur + ' ' + wd).strip()
        if d.textlength(t, font=f) <= w:
            cur = t
        else:
            lines.append(cur)
            cur = wd
    lines.append(cur)
    return lines


def main(spec_path, out):
    s = json.load(open(spec_path))
    im = Image.new('RGB', (W, H), PURPLE)
    d = ImageDraw.Draw(im)
    # decorative shapes (top right)
    d.ellipse((W - 210, -150, W + 70, 110), fill=FOOT)
    d.ellipse((W - 165, 30, W - 105, 90), fill=PEACH)
    d.rectangle((W - 290, 50, W - 250, 90), fill=LAV)

    d.text((M, 80), s['kicker'].upper(), font=font('Inter-Bold.otf', 28), fill=PEACH)
    hl = s['headline']
    hi = set(s.get('highlight', []))
    size = 84
    hf = font('InterDisplay-ExtraBold.otf', size)
    while max(d.textlength(t, font=hf) for t in hl) > W - 2 * M - 40 and size > 56:
        size -= 2
        hf = font('InterDisplay-ExtraBold.otf', size)
    if max(d.textlength(t, font=hf) for t in hl) > W - 2 * M:
        sys.exit('headline too long')
    pf = font('Inter-SemiBold.otf', 40)
    plines = [wrap(d, p, pf, W - 2 * M - 60) for p in s['points']]
    lh_h = int(size * 1.12)
    content_h = len(hl) * lh_h + 40 + 8 + 50 + sum(len(pl) * 54 + 26 for pl in plines) - 26
    bh = 92
    by = H - 170 - bh - 60
    top, bottom = 150, by - 60
    if content_h > bottom - top:
        sys.exit('content too long for the card; shorten headline or points')
    y = top + (bottom - top - content_h) // 2
    for i, t in enumerate(hl):
        d.text((M, y), t, font=hf, fill=YEL if i in hi else 'white')
        y += lh_h
    y += 40
    d.rectangle((M, y, M + 120, y + 8), fill=YEL)
    y += 58
    for lines in plines:
        d.ellipse((M, y + 13, M + 22, y + 35), fill=PEACH)
        for ln in lines:
            d.text((M + 50, y), ln, font=pf, fill='white')
            y += 54
        y += 26

    # button
    uf = font('Inter-Bold.otf', 34)
    label = 'Read the guide: ' + s['url']
    while d.textlength(label, font=uf) > W - 2 * M - 80:
        uf = font('Inter-Bold.otf', uf.size - 2)
    bw = d.textlength(label, font=uf) + 80
    d.rounded_rectangle((M, by, M + bw, by + bh), radius=46, fill=YEL)
    d.text((M + 40, by + (bh - uf.size) / 2 - 4), label, font=uf, fill=PURPLE)

    # footer
    d.rectangle((0, H - 170, W, H), fill=FOOT)
    lg = Image.open(LOGO).convert('RGBA')
    lh = 58
    lg = lg.resize((int(lg.width * lh / lg.height), lh), Image.LANCZOS)
    im.paste(lg, (M, H - 170 + (170 - lh) // 2), lg)
    ff = font('Inter-SemiBold.otf', 26)
    for i, t in enumerate(['creditt.com.au', 'Sydney-based · Helping Australians nationwide']):
        d.text((W - M - d.textlength(t, font=ff), H - 122 + i * 40), t, font=ff, fill='white' if i == 0 else LAV)
    im.save(out, quality=92)
    print('saved', out)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

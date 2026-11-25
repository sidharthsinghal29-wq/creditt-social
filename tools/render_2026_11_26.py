from PIL import Image, ImageDraw, ImageFont
import os
F = '/usr/share/fonts/opentype/inter/'
def f(n, s): return ImageFont.truetype(F + n, s)
OUT = 'posts/2026-11/'
SLUG = '26-offset-refinance-check'

def wrap(d, text, font, w):
    words, lines, cur = text.split(), [], ''
    for wd in words:
        t = (cur + ' ' + wd).strip()
        if d.textlength(t, font=font) <= w: cur = t
        else: lines.append(cur); cur = wd
    lines.append(cur); return lines

def paste_logo(im, path, x, y, h):
    lg = Image.open(path).convert('RGBA')
    w = int(lg.width * h / lg.height)
    lg = lg.resize((w, h), Image.LANCZOS)
    im.paste(lg, (x, y), lg); return w

# ---------------- Creditt 1080x1350 ----------------
def creditt():
    W, H = 1080, 1350
    im = Image.new('RGB', (W, H), '#4B1F68'); d = ImageDraw.Draw(im)
    M = 72
    d.text((M, 70), 'HOME LOANS · NOVEMBER 2026', font=f('Inter-Bold.otf', 26), fill='#F19B70')
    hf = f('InterDisplay-ExtraBold.otf', 76)
    d.text((M, 120), "Refinancing?", font=hf, fill='white')
    d.text((M, 208), "Check your offset works.", font=hf, fill='#FFD15D')
    d.text((M, 322), 'Refinances are now about one in three home loan deals.',
           font=f('Inter-Medium.otf', 28), fill='#D0B7EF')
    # stat cards
    cy, ch, gap = 390, 250, 24
    cw = (W - 2 * M - gap) // 2
    stats = [('1 in 3', 'Deals are refinances', 'Up from about 1 in 4 a year ago (Quickli, Nov 2026)'),
             ('$349b', 'Held in offset accounts', 'March 2026, up 28% in two years (ASIC)')]
    for i, (big, lab, sub) in enumerate(stats):
        x = M + i * (cw + gap)
        d.rounded_rectangle((x, cy, x + cw, cy + ch), 28, fill='#5E2E80')
        d.text((x + 32, cy + 26), big, font=f('InterDisplay-ExtraBold.otf', 92), fill='#FFD15D')
        d.text((x + 32, cy + 140), lab, font=f('Inter-Bold.otf', 28), fill='white')
        yy = cy + 182
        for ln in wrap(d, sub, f('Inter-Medium.otf', 22), cw - 64):
            d.text((x + 32, yy), ln, font=f('Inter-Medium.otf', 22), fill='#D0B7EF'); yy += 30
    # action points
    y = 710
    d.text((M, y), 'What to do now', font=f('Inter-Bold.otf', 34), fill='white'); y += 66
    pts = ['Check your offset is linked to the right loan',
           'Re-check the link after any refinance or switch',
           'Look for the interest saving on your statements',
           'Weigh offset fees against redraw for your habits']
    bf = f('Inter-Medium.otf', 29)
    for p in pts:
        d.ellipse((M, y + 10, M + 18, y + 28), fill='#F19B70')
        for j, ln in enumerate(wrap(d, p, bf, W - 2 * M - 40)):
            d.text((M + 40, y), ln, font=bf, fill='white'); y += 40
        y += 34
    # footer
    fy = 1150
    d.rectangle((0, fy, W, H), fill='#413080')
    paste_logo(im, 'brand/creditt/creditt-logo-light-text.png', M, fy + 34, 66)
    rf = f('Inter-Bold.otf', 30)
    t = 'creditt.com.au'; d.text((W - M - d.textlength(t, font=rf), fy + 36), t, font=rf, fill='#FFD15D')
    sf = f('Inter-Medium.otf', 22)
    t = 'Sydney-based · Helping Australians nationwide'
    d.text((W - M - d.textlength(t, font=sf), fy + 78), t, font=sf, fill='white')
    nf = f('Inter-Regular.otf', 17)
    d.text((M, fy + 140), 'Sources: Quickli via Australian Broker (19 Nov 2026); ASIC Report 837 (29 Jul 2026).', font=nf, fill='#D0B7EF')
    d.text((M, fy + 166), 'General information only. Not personal advice.', font=nf, fill='#D0B7EF')
    im.save(OUT + SLUG + '.jpg', quality=92)

# ---------------- Aussie ----------------
def aussie(W, H, name):
    im = Image.new('RGB', (W, H), '#4B1F68'); d = ImageDraw.Draw(im)
    M = 64 if W == 1080 else 60
    tall = H > W
    paste_logo(im, 'brand/aussie/aussie-logo-white-landscape.png', M, 56, 70 if tall else 60)
    hf = f('InterDisplay-ExtraBold.otf', 78 if tall else 66)
    y = 180 if tall else 150
    d.text((M, y), 'Offset or redraw?', font=hf, fill='white'); y += hf.size + 14
    d.text((M, y), 'Pick what suits you.', font=hf, fill='#FFD11F'); y += hf.size + 30
    sub = 'Both can reduce the interest you pay. The better fit depends on how you use your savings day to day.'
    sf = f('Inter-Medium.otf', 28 if tall else 25)
    for ln in wrap(d, sub, sf, W - 2 * M):
        d.text((M, y), ln, font=sf, fill='#D0B7EF'); y += sf.size + 10
    y += 26
    fh = 200 if tall else 170
    pts = ['Offset: savings sit in an everyday account',
           'Redraw: extra repayments you can take back out',
           'Check any package fee or rate difference',
           'Refinancing? Confirm your offset is linked']
    bf = f('Inter-SemiBold.otf', 30 if tall else 26)
    bottom = H - fh - 40
    d.rounded_rectangle((M, y, W - M, bottom), 30, fill='#FFF0BA')
    # vertically distribute points
    lines = [wrap(d, p, bf, W - 2 * M - 120) for p in pts]
    total = sum(len(l) * (bf.size + 10) for l in lines)
    space = (bottom - y - total) / (len(pts) + 1)
    yy = y + space
    for l in lines:
        d.ellipse((M + 44, yy + 8, M + 66, yy + 30), fill='#FF9366')
        for ln in l:
            d.text((M + 90, yy), ln, font=bf, fill='#4B1F68'); yy += bf.size + 10
        yy += space
    fy = H - fh
    d.rectangle((0, fy, W, H), fill='#413080')
    nf = f('InterDisplay-ExtraBold.otf', 40 if tall else 36)
    d.text((M, fy + 30), 'Sidharth Singhal', font=nf, fill='white')
    tf = f('Inter-SemiBold.otf', 26 if tall else 23)
    d.text((M, fy + 30 + nf.size + 14), 'Aussie Mortgage Broker · Lane Cove', font=tf, fill='#FFD11F')
    lf = f('Inter-Regular.otf', 18 if tall else 16)
    d.text((M, fy + fh - 44), 'Credit Representative 533758 · Australian Credit Licence 246786 · General information only',
           font=lf, fill='#D0B7EF')
    im.save(OUT + SLUG + name, quality=92)

creditt()
aussie(1080, 1350, '-aussie-linkedin.jpg')
aussie(1200, 900, '-aussie-gbp.jpg')
print('ok')

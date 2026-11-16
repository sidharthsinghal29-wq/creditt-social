from PIL import Image, ImageDraw, ImageFont
import os
F = '/usr/share/fonts/opentype/inter/'
def f(n, s): return ImageFont.truetype(F + n, s)
OUT = 'posts/2026-11/'
SLUG = '17-business-debt-checkup'

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
    d.text((M, 70), 'BUSINESS FINANCE · NOVEMBER 2026', font=f('Inter-Bold.otf', 26), fill='#F19B70')
    hf = f('InterDisplay-ExtraBold.otf', 82)
    d.text((M, 120), "Five rate rises.", font=hf, fill='white')
    d.text((M, 212), "Time for a debt check", font=hf, fill='#FFD15D')
    d.text((M, 322), 'For many owners, rate rises land twice: business and home.',
           font=f('Inter-Medium.otf', 28), fill='#D0B7EF')
    # stat cards
    cy, ch, gap = 390, 250, 24
    cw = (W - 2 * M - gap) // 2
    stats = [('4.85%', 'RBA cash rate', '5th rise of 2026 (RBA, 3 Nov)'),
             ('~1 in 2', 'Small business credit', 'secured against residential property')]
    for i, (big, lab, sub) in enumerate(stats):
        x = M + i * (cw + gap)
        d.rounded_rectangle((x, cy, x + cw, cy + ch), 28, fill='#5E2E80')
        d.text((x + 32, cy + 26), big, font=f('InterDisplay-ExtraBold.otf', 92), fill='#FFD15D')
        d.text((x + 32, cy + 140), lab, font=f('Inter-Bold.otf', 28), fill='white')
        yy = cy + 182
        for ln in wrap(d, sub, f('Inter-Medium.otf', 22), cw - 64):
            d.text((x + 32, yy), ln, font=f('Inter-Medium.otf', 22), fill='#D0B7EF'); yy += 30
    # action points
    y = 680
    d.text((M, y), 'Your business finance check-up', font=f('Inter-Bold.otf', 34), fill='white'); y += 66
    pts = ['List every facility and what it is secured against',
           'Set up a cash flow buffer (e.g. a line of credit) before you need it',
           'Match finance to the asset: equipment and vehicle finance can keep the home out of it',
           'Check your pricing and structure are still competitive']
    bf = f('Inter-Medium.otf', 29)
    for p in pts:
        d.ellipse((M, y + 10, M + 18, y + 28), fill='#F19B70')
        for j, ln in enumerate(wrap(d, p, bf, W - 2 * M - 40)):
            d.text((M + 40, y), ln, font=bf, fill='white'); y += 40
        y += 22
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
    d.text((M, fy + 140), 'Sources: RBA cash rate decision 3 Nov 2026; small business credit share as reported by MPA, 4 Nov 2026.', font=nf, fill='#D0B7EF')
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
    d.text((M, y), 'Self-employed?', font=hf, fill='white'); y += hf.size + 14
    d.text((M, y), 'Check your home loan.', font=hf, fill='#FFD11F'); y += hf.size + 30
    sub = 'The cash rate is 4.85% after five rises this year. For business owners, the home loan often does double duty.'
    sf = f('Inter-Medium.otf', 28 if tall else 25)
    for ln in wrap(d, sub, sf, W - 2 * M):
        d.text((M, y), ln, font=sf, fill='#D0B7EF'); y += sf.size + 10
    y += 26
    fh = 200 if tall else 170
    pts = ['Review your rate and loan features regularly',
           'Keep business financials and statements up to date',
           'Know what your home is securing',
           'Check repayments work comfortably at today’s rates']
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

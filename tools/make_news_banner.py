from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys, json
W, H = 1920, 1080
F = "/usr/share/fonts/opentype/inter/"
def f(n, s): return ImageFont.truetype(F + n, s)
Y, Y2, WHITE, LAV = "#FFD11F", "#FFD15D", "#FFFFFF", "#D0B7EF"

cfg = json.load(open(sys.argv[1]))  # headline lines, subtitle, chips, out, headshot

# background: vertical-diagonal purple gradient
bg = Image.new("RGB", (W, H))
top, mid, bot = (43, 18, 71), (75, 31, 104), (65, 48, 128)
px = bg.load()
for y in range(H):
    for x in range(0, W, 2):
        t = (x / W) * 0.6 + (y / H) * 0.4
        if t < 0.5:
            k = t / 0.5; c = tuple(int(top[i] + (mid[i] - top[i]) * k) for i in range(3))
        else:
            k = (t - 0.5) / 0.5; c = tuple(int(mid[i] + (bot[i] - mid[i]) * k) for i in range(3))
        px[x, y] = c; px[min(x + 1, W - 1), y] = c
im = bg; d = ImageDraw.Draw(im)

# diagonal yellow band (left), echoing the reference
band = Image.new("RGBA", (W, H), (0, 0, 0, 0)); bd = ImageDraw.Draw(band)
bd.polygon([(0, 0), (150, 0), (900, H), (560, H), (0, 380)], fill=(255, 209, 31, 255))
bd.polygon([(0, 380), (560, H), (330, H), (0, 640)], fill=(240, 170, 60, 200))
im.paste(band, (0, 0), band)
# soft purple wash over the band's lower half for depth
wash = Image.new("RGBA", (W, H), (0, 0, 0, 0)); wd = ImageDraw.Draw(wash)
wd.polygon([(0, 700), (700, H), (0, H)], fill=(75, 31, 104, 170))
im.paste(wash, (0, 0), wash)
d = ImageDraw.Draw(im)
# dot grids
for gx, gy, cols, rows in [(40, 40, 10, 6), (40, 640, 6, 10)]:
    for r in range(rows):
        for c in range(cols):
            x, y = gx + c * 30, gy + r * 30
            d.ellipse((x, y, x + 7, y + 7), fill=Y)

# headshot in yellow ring
hs = Image.open(cfg["headshot"]).convert("RGB")
R = 245; cx, cy = 375, 395
hs = hs.resize((2 * R, 2 * R), Image.LANCZOS)
mask = Image.new("L", (2 * R, 2 * R), 0); ImageDraw.Draw(mask).ellipse((0, 0, 2 * R, 2 * R), fill=255)
d.ellipse((cx - R - 16, cy - R - 16, cx + R + 16, cy + R + 16), fill=Y)
im.paste(hs, (cx - R, cy - R), mask)

# right-side illustration: rate bars rising, value line falling
bx = 1640
for i, h in enumerate([50, 80, 110, 145, 185]):
    x = bx + i * 50
    d.rounded_rectangle((x, 815 - h, x + 34, 815), radius=8, fill=(255, 209, 31, 255) if i == 4 else (208, 183, 239))
pts = [(1640, 660), (1700, 680), (1760, 712), (1820, 726), (1880, 760)]
d.line(pts, fill=(241, 155, 112), width=6, joint="curve")
for p in pts: d.ellipse((p[0] - 7, p[1] - 7, p[0] + 7, p[1] + 7), fill=(241, 155, 112))
d.text((1800, 580), "%", font=f("InterDisplay-ExtraBold.otf", 80), fill=WHITE, anchor="mm")

# headline
x0 = 690; y = 150
for line, col in cfg["headline"]:
    d.text((x0, y), line, font=f("InterDisplay-ExtraBold.otf", 92), fill=Y if col == "y" else WHITE); y += 104
d.rectangle((x0, y + 18, x0 + 150, y + 26), fill=Y)
y += 58
for line in cfg["subtitle"]:
    d.text((x0, y), line, font=f("Inter-Medium.otf", 42), fill=WHITE); y += 56

# chips row
icons = cfg["chips"]
cx0 = 800; cyc = 930
for i, (glyph, l1, l2) in enumerate(icons):
    x = cx0 + i * 268
    d.ellipse((x, cyc - 42, x + 84, cyc + 42), fill=(43, 18, 71), outline=(168, 85, 247), width=5)
    d.text((x + 42, cyc), glyph, font=f("InterDisplay-ExtraBold.otf", 38), fill=Y, anchor="mm")
    d.text((x + 100, cyc - 30), l1, font=f("Inter-Medium.otf", 26), fill=WHITE)
    d.text((x + 100, cyc + 4), l2, font=f("Inter-Medium.otf", 26), fill=WHITE)
    if i < len(icons) - 1: d.line((x + 254, cyc - 36, x + 254, cyc + 36), fill=(208, 183, 239), width=2)
im.save(cfg["out"], quality=92)
print("saved", cfg["out"])

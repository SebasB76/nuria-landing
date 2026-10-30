"""Draws the Cerro Santa Ana illustration used in the landing page.

Run: python3 tools/cerro_santa_ana.py > site/assets/img/cerro-santa-ana.svg
"""

import math
import random

W, H, WATER = 1200, 360, 300
BG = "#173F25"  # the section background, used for cut-outs
FAR = "#21492C"
HILL = "#8FAE86"
PALE = "#D3E0C6"
BACK = "#A9C29E"
BIRD = "#E2D6A8"
CLOUD = "#1F4C2E"
RAIN = "#2F6743"
CREAM = "#ECE5CF"

rnd = random.Random(7)
out = []


def f(n):
    return f"{n:.1f}".rstrip("0").rstrip(".")


def hill_y(x):
    # asymmetric bump: steeper toward the river side (left), longer toward the city (right)
    sigma = 120 if x < 410 else 150
    return WATER - 182 * math.exp(-(((x - 410) / sigma) ** 2))


def rect(x, y, w, h, fill):
    out.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{fill}"/>')


def path(d, fill="none", stroke=None, width=None, extra=""):
    s = f' stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"' if stroke else ""
    out.append(f'<path d="{d}" fill="{fill}"{s}{extra}/>')


def circle(cx, cy, r, fill):
    out.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{fill}"/>')


def cloud(cx, cy, scale, fill):
    for dx, dy, r in [(-60, 8, 26), (-30, -10, 34), (8, -20, 40), (48, -6, 32), (78, 10, 22), (-8, 12, 30), (36, 14, 28)]:
        circle(cx + dx * scale, cy + dy * scale, r * scale, fill)


def canopy(cx, cy, size, fill):
    for _ in range(11):
        a = rnd.uniform(0, math.tau)
        d = rnd.uniform(0, size * 0.75)
        circle(cx + math.cos(a) * d * 1.5, cy + math.sin(a) * d * 0.55, rnd.uniform(size * 0.38, size * 0.6), fill)


def mangrove(x, top, size, fill):
    base = WATER - size * 0.55
    path(f"M{f(x - 3)} {f(base)} L{f(x - 2)} {f(top + size * 0.3)} L{f(x + 2)} {f(top + size * 0.3)} L{f(x + 3)} {f(base)} Z", fill)
    for dx in (-1.25, -0.8, -0.4, 0.05, 0.45, 0.85, 1.3):
        sx = x + dx * 4
        ex = x + dx * size * 0.62
        path(f"M{f(sx)} {f(base - 4)} Q{f(sx + (ex - sx) * 0.55)} {f(base - size * 0.28)} {f(ex)} {f(WATER + 2)}", stroke=fill, width=2.6)
    canopy(x, top + size * 0.25, size, fill)


def palm(x, height):
    base, topx, topy = WATER - 4, x + height * 0.14, WATER - 4 - height
    path(f"M{f(x - 2.5)} {f(base)} Q{f(x + height * 0.02)} {f(base - height * 0.55)} {f(topx - 1.5)} {f(topy)} L{f(topx + 1.5)} {f(topy)} Q{f(x + height * 0.06)} {f(base - height * 0.55)} {f(x + 2.5)} {f(base)} Z", PALE)
    for ang, length in [(-160, 34), (-125, 30), (-90, 22), (-55, 30), (-20, 34), (170, 26), (10, 26)]:
        a = math.radians(ang)
        ex, ey = topx + math.cos(a) * length, topy + math.sin(a) * length * 0.6 + length * 0.35
        cx, cy = topx + math.cos(a) * length * 0.5, topy + math.sin(a) * length * 0.6 - 6
        path(f"M{f(topx)} {f(topy)} Q{f(cx)} {f(cy)} {f(ex)} {f(ey)}", stroke=PALE, width=3.2)


def bird(x, y, s):
    path(f"M{f(x)} {f(y)} q{f(8 * s)} {f(-7 * s)} {f(17 * s)} {f(-2 * s)} q{f(4 * s)} {f(3 * s)} {f(6 * s)} {f(6 * s)} q{f(2 * s)} {f(-3 * s)} {f(6 * s)} {f(-6 * s)} q{f(9 * s)} {f(-5 * s)} {f(17 * s)} {f(2 * s)}", stroke=BIRD, width=2.2)


# far shore and the rain cloud over the mangrove
path(f"M0 {WATER} L0 258 C120 240 230 252 330 246 S560 236 700 250 S940 238 1200 252 L1200 {WATER} Z", FAR)
for i in range(26):
    x = 800 + i * 15 + rnd.uniform(-4, 4)
    y = 92 + rnd.uniform(0, 40)
    path(f"M{f(x)} {f(y)} l{f(-10)} {f(rnd.uniform(70, 150))}", stroke=RAIN, width=2)
cloud(960, 70, 1.25, CLOUD)
cloud(1110, 92, 0.85, CLOUD)

# satellite watching from above, with its line of sight to the cloud
path("M1128 30 L1020 74", stroke=BIRD, width=1.2, extra=' stroke-dasharray="2 5" opacity="0.7"')
rect(1124, 24, 12, 10, BIRD)
rect(1104, 26, 18, 6, BIRD)
rect(1138, 26, 18, 6, BIRD)

# Cerro Santa Ana
pts = " ".join(f"L{f(x)} {f(hill_y(x))}" for x in range(150, 711, 6))
path(f"M150 {WATER} {pts} L710 {WATER} Z", HILL)

# houses of Las Peñas in rows that follow the slope, drawn top to bottom so the lower rows sit in front
for depth in (4, 22, 40, 58, 76, 94):
    x = 160 + rnd.uniform(0, 12)
    while x < 700:
        w = rnd.uniform(12, 19)
        h = rnd.uniform(10, 15)
        base = hill_y(x + w / 2) + depth
        near_top = depth < 30 and 386 < x + w / 2 < 486
        if base < WATER - 6 and not near_top and rnd.random() < 0.86:
            out.append(f'<rect x="{f(x)}" y="{f(base - h)}" width="{f(w)}" height="{f(h)}" fill="{PALE}" stroke="{HILL}" stroke-width="1"/>')
            if rnd.random() < 0.55:
                path(f"M{f(x - 1.5)} {f(base - h)} L{f(x + w / 2)} {f(base - h - 5)} L{f(x + w + 1.5)} {f(base - h)} Z", PALE)
            for wx in (x + 2.5, x + w - 6) if w > 16 else (x + w / 2 - 1.75,):
                rect(wx, base - h + 3.5, 3.5, 4, BG)
        x += w + rnd.uniform(0.5, 3)

# the lighthouse at the top, with its stripes cut out
top = hill_y(410)
path(f"M399 {f(top + 4)} L403 {f(top - 58)} L417 {f(top - 58)} L421 {f(top + 4)} Z", PALE)
rect(397, top - 62, 26, 4, PALE)
rect(404, top - 74, 12, 12, PALE)
path(f"M402 {f(top - 74)} L410 {f(top - 84)} L418 {f(top - 74)} Z", PALE)
rect(407.5, top - 71, 5, 6, BG)
rect(401, top - 40, 18, 5, BG)
rect(400, top - 20, 20, 5, BG)

# the chapel next to the lighthouse
cy = hill_y(462) + 4
rect(450, cy - 16, 26, 16, PALE)
path(f"M448 {f(cy - 16)} L463 {f(cy - 24)} L478 {f(cy - 16)} Z", PALE)
rect(441, cy - 30, 9, 30, PALE)
path(f"M440 {f(cy - 30)} L445.5 {f(cy - 37)} L451 {f(cy - 30)} Z", PALE)
path(f"M445.5 {f(cy - 37)} V{f(cy - 45)} M442 {f(cy - 42)} H449", stroke=PALE, width=1.6)
path(f"M460 {f(cy)} V{f(cy - 8)} a3 3 0 0 1 6 0 V{f(cy)} Z", BG)

# malecón with lamps and palms
rect(0, WATER - 5, 770, 6, PALE)
for x in range(20, 770, 64):
    path(f"M{x} {WATER - 5} V{WATER - 30}", stroke=PALE, width=1.8)
    circle(x, WATER - 32, 3, PALE)
for x, height in [(96, 92), (128, 70), (742, 86)]:
    palm(x, height)

# mangrove: back layer first, then the pale front trees
for x, top, size in [(860, 196, 46), (1010, 186, 52), (1150, 200, 44)]:
    mangrove(x, top, size, BACK)
for x, top, size in [(800, 214, 40), (930, 200, 54), (1080, 206, 50), (1190, 222, 38)]:
    mangrove(x, top, size, PALE)

# river, a floating house like the ones in the 1846 painting, and the ripples
rect(0, WATER + 1, W, H - WATER, "#1C4A2C")
rect(520, WATER + 38, 96, 6, PALE)
rect(536, WATER + 22, 64, 16, PALE)
path(f"M528 {WATER + 24} L568 {WATER + 4} L608 {WATER + 24} Z", PALE)
rect(562, WATER + 27, 10, 11, BG)
for i in range(34):
    x = rnd.uniform(0, W - 60)
    y = rnd.uniform(WATER + 12, H - 8)
    length = rnd.uniform(18, 60)
    path(f"M{f(x)} {f(y)} h{f(length)}", stroke=PALE, width=1.6, extra=' opacity="0.32"')

# frigatebirds over the river
for x, y, s in [(560, 70, 1.0), (618, 104, 0.8), (690, 58, 0.9), (760, 120, 0.7), (250, 92, 0.75)]:
    bird(x, y, s)

# Nuria on the malecón, waving
nx, ny = 700, WATER - 5
path(f"M{nx} {ny - 34} C{nx} {ny - 34} {nx - 13} {ny - 18} {nx - 13} {ny - 10} a13 13 0 0 0 26 0 C{nx + 13} {ny - 18} {nx} {ny - 34} {nx} {ny - 34} Z", CREAM)
circle(nx - 4.5, ny - 11, 1.6, BG)
circle(nx + 4.5, ny - 11, 1.6, BG)
path(f"M{nx - 3} {ny - 6} q3 2.6 6 0", stroke=BG, width=1.4)
path(f"M{nx + 12} {ny - 15} q6 -4 6 -11", stroke=CREAM, width=2.2)

print(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Ilustración del Cerro Santa Ana con el faro, las casas de Las Peñas, el malecón, el río Guayas y el manglar bajo un aguacero">')
print("\n".join(out))
print("</svg>")

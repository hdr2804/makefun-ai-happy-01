"""Draw the happy picture for the make.fun ai-happy-01 entry.

Flat, bright illustration drawn with PIL (build-time only; the entry
itself ships the resulting art.png and main.py copies it). Everything in
the scene smiles: sun, cloud, rainbow, hills, flowers and a little robot
waving with a balloon, hearts floating up.
"""

from PIL import Image, ImageDraw

S = 1024
img = Image.new("RGB", (S, S), (135, 206, 250))
d = ImageDraw.Draw(img)

# --- sky gradient (flat bands, palette friendly) ---
for i in range(40):
    y0 = i * 16
    r = int(120 + i * 2.2)
    g = int(195 + i * 1.2)
    b = 250
    d.rectangle([0, y0, S, y0 + 16], fill=(r, g, b))

# --- rainbow (right side arcs) ---
rainbow = [(255, 89, 89), (255, 165, 66), (255, 224, 102), (106, 204, 110), (66, 165, 245)]
for i, col in enumerate(rainbow):
    box = [470 - i * 26, 120 - i * 26, 1150 - i * 26, 800 - i * 26]
    d.arc(box, start=180, end=290, fill=col, width=24)

# --- sun with a smile (top left) ---
d.ellipse([70, 60, 330, 320], fill=(255, 213, 74), outline=(245, 178, 30), width=6)
for ang in range(0, 360, 30):
    import math
    x1 = 200 + 150 * math.cos(math.radians(ang))
    y1 = 190 + 150 * math.sin(math.radians(ang))
    x2 = 200 + 185 * math.cos(math.radians(ang))
    y2 = 190 + 185 * math.sin(math.radians(ang))
    d.line([x1, y1, x2, y2], fill=(245, 178, 30), width=10)
d.ellipse([148, 158, 178, 188], fill=(60, 50, 30))   # eye L
d.ellipse([222, 158, 252, 188], fill=(60, 50, 30))   # eye R
d.arc([150, 190, 250, 270], start=15, end=165, fill=(60, 50, 30), width=9)  # smile
d.ellipse([112, 205, 162, 235], fill=(255, 160, 160))  # cheek L
d.ellipse([238, 205, 288, 235], fill=(255, 160, 160))  # cheek R

# --- clouds (rounded, one smiling) ---
def cloud(cx, cy, scale=1.0):
    w = int(90 * scale)
    for dx, dy, r in [(-70, 10, 45), (0, -18, 60), (70, 8, 48), (0, 18, 55)]:
        d.ellipse([cx + dx - r, cy + dy - r, cx + dx + r, cy + dy + r], fill=(255, 255, 255))

cloud(760, 150, 1.1)
cloud(430, 90, 0.8)
d.ellipse([742, 138, 756, 152], fill=(90, 90, 110))
d.ellipse([776, 138, 790, 152], fill=(90, 90, 110))
d.arc([748, 148, 784, 176], start=15, end=165, fill=(90, 90, 110), width=5)

# --- rolling hills ---
d.ellipse([-260, 640, 620, 1150], fill=(124, 205, 110))
d.ellipse([420, 680, 1300, 1200], fill=(96, 186, 92))
d.rectangle([0, 950, S, S], fill=(96, 186, 92))

# --- flowers ---
import random
random.seed(7)
for _ in range(46):
    x = random.randint(30, 994)
    y = random.randint(800, 990)
    petal = random.choice([(255, 120, 170), (255, 200, 90), (255, 255, 255), (200, 150, 255)])
    for dx, dy in [(-9, 0), (9, 0), (0, -9), (0, 9)]:
        d.ellipse([x + dx - 8, y + dy - 8, x + dx + 8, y + dy + 8], fill=petal)
    d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=(255, 160, 40))
    d.line([x, y + 8, x, y + 26], fill=(46, 130, 50), width=4)

# --- happy robot waving, holding a balloon ---
# balloon
d.line([618, 470, 668, 330], fill=(90, 90, 90), width=4)
d.ellipse([610, 170, 730, 330], fill=(255, 92, 132))
d.polygon([(662, 330), (678, 330), (670, 348)], fill=(255, 92, 132))
d.ellipse([632, 196, 664, 248], fill=(255, 150, 175))
# body
d.rounded_rectangle([420, 560, 620, 780], radius=42, fill=(120, 190, 250), outline=(40, 90, 160), width=6)
d.ellipse([478, 640, 562, 724], fill=(255, 255, 255))          # belly heart plate
d.ellipse([489, 653, 515, 679], fill=(255, 92, 132))           # heart lobe L
d.ellipse([525, 653, 551, 679], fill=(255, 92, 132))           # heart lobe R
d.polygon([(491, 668), (549, 668), (520, 708)], fill=(255, 92, 132))  # heart point
# head
d.rounded_rectangle([428, 380, 612, 566], radius=48, fill=(170, 220, 255), outline=(40, 90, 160), width=6)
d.line([520, 380, 520, 322], fill=(40, 90, 160), width=7)      # antenna
d.ellipse([502, 296, 538, 332], fill=(255, 92, 132))           # antenna heart tip
d.ellipse([462, 446, 496, 492], fill=(30, 40, 60))             # eye L (happy, big)
d.ellipse([544, 446, 578, 492], fill=(30, 40, 60))             # eye R
d.ellipse([472, 452, 486, 466], fill=(255, 255, 255))
d.ellipse([554, 452, 568, 466], fill=(255, 255, 255))
d.arc([472, 478, 568, 548], start=10, end=170, fill=(30, 40, 60), width=8)  # big smile
d.ellipse([436, 500, 478, 532], fill=(255, 160, 170))          # cheek L
d.ellipse([562, 500, 604, 532], fill=(255, 160, 170))          # cheek R
# arms: one waving up, one down
d.line([428, 610, 336, 520], fill=(40, 90, 160), width=26)
d.ellipse([310, 486, 356, 532], fill=(255, 213, 120), outline=(40, 90, 160), width=5)
d.line([612, 610, 690, 540], fill=(40, 90, 160), width=26)
d.ellipse([678, 506, 724, 552], fill=(255, 213, 120), outline=(40, 90, 160), width=5)
# feet
d.rounded_rectangle([448, 778, 512, 812], radius=14, fill=(40, 90, 160))
d.rounded_rectangle([528, 778, 592, 812], radius=14, fill=(40, 90, 160))

# --- floating hearts ---
def heart(cx, cy, s, col):
    d.ellipse([cx - s, cy - s // 2, cx, cy + s // 2], fill=col)
    d.ellipse([cx, cy - s // 2, cx + s, cy + s // 2], fill=col)
    d.polygon([(cx - s, cy + s // 4), (cx + s, cy + s // 4), (cx, cy + s)], fill=col)

heart(180, 480, 26, (255, 110, 150))
heart(290, 400, 18, (255, 150, 180))
heart(830, 430, 22, (255, 110, 150))
heart(880, 540, 15, (255, 150, 180))

img.save("/home/hatch/workspace/makefun/entries/ai-happy-01/art.png", optimize=True)
print("saved art.png")

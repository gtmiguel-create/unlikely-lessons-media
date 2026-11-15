import random


def tree(d, x, y, s, fill, ink, kind):
    if kind == "spruce":
        d.polygon([(x, y - 2.4 * s), (x - s, y), (x + s, y)], fill=fill, outline=ink)
        d.line([x, y, x, y + 0.4 * s], fill=ink, width=3)
    else:
        d.line([x, y - 0.2 * s, x, y + 0.6 * s], fill=ink, width=3)
        d.ellipse([x - s, y - 1.8 * s, x + s, y], fill=fill, outline=ink)


def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, WATER, MUTED = k["INK"], k["OCHRE"], k["WATER"], k["MUTED"]
    lab, small = k["sans"](26, 700), k["sans"](24, 500)
    mid = (x0 + x1) // 2
    gap = 30
    top, bot = y0 + 60, y1 - 70
    greens = [(96, 128, 82), (128, 150, 90), (70, 105, 80), (160, 140, 80), (110, 140, 110)]

    # labels
    for t, cx, col in (("BEFORE: A WILD FOREST", (x0 + mid - gap) // 2, INK),
                       ("AFTER: A LEGIBLE FOREST", (mid + gap + x1) // 2, OCHRE)):
        d.text((cx - d.textlength(t, font=lab) / 2, y0 + 4), t, font=lab, fill=col)

    # panels
    d.rectangle([x0, top, mid - gap, bot], outline=INK, width=3)
    d.rectangle([mid + gap, top, x1, bot], outline=INK, width=3)

    # wild side
    rnd = random.Random(7)
    pts = []
    for _ in range(26):
        s = rnd.randint(14, 30)
        x = rnd.randint(x0 + 20 + s, mid - gap - 20 - s)
        y = rnd.randint(top + 20 + int(2.4 * s), bot - 20 - int(0.6 * s))
        pts.append((y, x, s))
    for y, x, s in sorted(pts):
        tree(d, x, y, s, rnd.choice(greens), INK, rnd.choice(["spruce", "broad", "broad"]))
    # undergrowth dots
    for _ in range(40):
        x = rnd.randint(x0 + 12, mid - gap - 12)
        y = rnd.randint(bot - 40, bot - 10)
        d.ellipse([x - 4, y - 4, x + 4, y + 4], fill=(130, 110, 70))

    # legible side: grid of identical spruces
    cols, rows = 5, 5
    pw = (x1 - (mid + gap)) / cols
    ph = (bot - top) / rows
    for r in range(rows):
        for c in range(cols):
            cx = mid + gap + pw * (c + 0.5)
            cy = top + ph * (r + 0.5) + 30
            tree(d, cx, cy, 18, (70, 105, 80), INK, "spruce")

    # bottom captions
    for t, cx in (("many species, ages, life", (x0 + mid - gap) // 2),
                  ("one species, one age, rows", (mid + gap + x1) // 2)):
        d.text((cx - d.textlength(t, font=small) / 2, bot + 18), t, font=small, fill=MUTED)

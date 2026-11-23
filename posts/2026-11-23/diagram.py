import math


def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, WATER, OCHRE = k["INK"], k["WATER"], k["OCHRE"]
    lab, small = k["sans"](28, 700), k["sans"](26, 400)
    w, h = x1 - x0, y1 - y0
    sh = int(h * 0.50)                # scene height
    gy = y0 + int(sh * 0.62)          # ground line

    def label(x, y, t, f=lab, fill=INK):
        tw = d.textlength(t, font=f)
        d.text((x - tw / 2, y), t, font=f, fill=fill)

    bx, sx = x0 + int(w * 0.20), x0 + int(w * 0.80)
    # old tree
    d.line([bx, gy, bx, gy - int(sh * 0.30)], fill=INK, width=14)
    d.ellipse([bx - 90, gy - int(sh * 0.52), bx + 90, gy - int(sh * 0.22)], fill=WATER, outline=INK, width=4)
    label(bx + 150, gy - int(sh * 0.45), "old tree", small)
    # seedling
    d.line([sx, gy, sx, gy - int(sh * 0.14)], fill=INK, width=8)
    d.ellipse([sx - 45, gy - int(sh * 0.26), sx + 45, gy - int(sh * 0.11)], fill=WATER, outline=INK, width=4)
    label(sx, gy - int(sh * 0.26) - 36, "seedling", small)
    d.line([x0, gy, x1, gy], fill=INK, width=4)
    for dx in (-55, -20, 20, 55):
        d.line([bx, gy, bx + dx, gy + 50], fill=INK, width=4)
    for dx in (-25, 25):
        d.line([sx, gy, sx + dx, gy + 35], fill=INK, width=3)
    # fungal threads
    ty = gy + 60
    xa, xb = bx + 55, sx - 25
    for off, ph in ((0, 0.0), (18, 1.7)):
        pts = [(xa + t / 40 * (xb - xa), ty + off + 10 * math.sin(t / 40 * math.pi * 3 + ph)) for t in range(41)]
        for i in range(0, 40, 2):
            d.line([pts[i], pts[i + 1]], fill=OCHRE, width=4)
    label((xa + xb) // 2, ty + 40, "fungal network?", lab, OCHRE)

    # verdict rows
    rows = [("Networks common in forests?", "only 2 field studies show it"),
            ("Seedlings helped by them?", "mixed, mostly no effect"),
            ("Trees send warnings through them?", "no field study")]
    ry = y0 + sh + 30
    rh = (y1 - ry) // 3
    for i, (q, a) in enumerate(rows):
        yy = ry + i * rh
        d.text((x0, yy), q, font=small, fill=INK)
        d.text((x0, yy + 36), "→ " + a, font=lab, fill=WATER)

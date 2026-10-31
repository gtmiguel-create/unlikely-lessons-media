import math


def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, WATER, OCHRE, MUTED = k["INK"], k["WATER"], k["OCHRE"], k["MUTED"]
    lab, small = k["sans"](28, 600), k["sans"](24, 400)
    hh = min(190, (y1 - y0 - 130) // 2)
    cy = y0 + 20 + hh
    B = 110                                   # max bulge of the ordinary lens

    def face(y):                              # bulge of a circular curve at height y
        r = (hh * hh + B * B) / (2 * B)
        return math.sqrt(max(0, r * r - (y - cy) ** 2)) - (r - B)

    pw = (x1 - x0) // 2

    def panel(px, fresnel, label):
        lamp = px + 30
        lx = px + 150                         # flat back of the lens
        d.ellipse([lamp - 14, cy - 14, lamp + 14, cy + 14], fill=OCHRE, outline=INK, width=3)
        for f in (-0.75, -0.3, 0.3, 0.75):
            yy = cy + f * hh
            d.line([lamp, cy, lx, yy], fill=OCHRE, width=3)
            d.line([lx + B + 12, yy, px + pw - 20, yy], fill=OCHRE, width=3)
            d.polygon([(px + pw - 14, yy), (px + pw - 32, yy - 9), (px + pw - 32, yy + 9)], fill=OCHRE)
        if not fresnel:
            pts = [(lx, cy - hh)] + [(lx + 6 + face(y), y) for y in range(int(cy - hh), int(cy + hh) + 1, 3)] + [(lx, cy + hh)]
            d.polygon(pts, fill=WATER, outline=INK)
        else:
            n = 9
            step = 2 * hh / n
            for i in range(n):
                ya, yb = cy - hh + i * step, cy - hh + (i + 1) * step
                ys = [ya + j * (yb - ya) / 10 for j in range(11)]
                lo = min(face(y) for y in ys)
                pts = [(lx, ya)] + [(lx + 6 + face(y) - lo, y) for y in ys] + [(lx, yb)]
                d.polygon(pts, fill=WATER, outline=INK)
        d.line([lx, cy - hh, lx, cy + hh], fill=INK, width=4)
        tw = d.textlength(label, font=lab)
        d.text((lx + 40 - tw / 2, cy + hh + 26), label, font=lab, fill=INK)

    panel(x0, False, "ordinary lens")
    panel(x0 + pw, True, "Fresnel lens")
    t = "Same beam. A fraction of the glass."
    d.text(((x0 + x1) / 2 - d.textlength(t, font=small) / 2, cy + hh + 78), t, font=small, fill=MUTED)

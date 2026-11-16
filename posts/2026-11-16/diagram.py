import random

RED = (178, 48, 52)
LIVER = (150, 120, 110)


def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, MUTED = k["INK"], k["MUTED"]
    lab = k["sans"](30, 700)
    small = k["sans"](26, 400)
    gap = 60
    pw = (x1 - x0 - gap) // 2
    ph = y1 - y0
    for i, (title, note, asleep) in enumerate([("AWAKE", "red cells everywhere", False),
                                               ("ASLEEP", "~90% packed in liver", True)]):
        px = x0 + i * (pw + gap)
        tw = d.textlength(title, font=lab)
        d.text((px + (pw - tw) / 2, y0), title, font=lab, fill=INK)
        top = y0 + 60
        bh = min(ph - 130, 360)
        bw = pw - 40
        bx0, by0 = px + 20, top
        bx1, by1 = bx0 + bw, top + bh
        d.ellipse([bx0, by0, bx1, by1], outline=INK, width=5)
        lx0 = bx0 + bw * 0.30
        ly0 = by0 + bh * 0.42
        lx1 = bx0 + bw * 0.70
        ly1 = by0 + bh * 0.72
        d.ellipse([lx0, ly0, lx1, ly1], outline=INK, width=4, fill=LIVER if asleep else None)
        rnd = random.Random(7 + i)
        cx, cy = (bx0 + bx1) / 2, (by0 + by1) / 2
        rx, ry = bw / 2 - 22, bh / 2 - 22
        n = 0
        while n < 46:
            u, v = rnd.uniform(-1, 1), rnd.uniform(-1, 1)
            if u * u + v * v > 1:
                continue
            x, y = cx + u * rx, cy + v * ry
            inliver = ((x - (lx0 + lx1) / 2) / ((lx1 - lx0) / 2)) ** 2 + ((y - (ly0 + ly1) / 2) / ((ly1 - ly0) / 2)) ** 2 < 0.75
            if asleep and n < 41:
                if not inliver:
                    continue
            elif not asleep and inliver:
                continue
            r = 7 if asleep and inliver else 9
            d.ellipse([x - r, y - r, x + r, y + r], fill=RED)
            n += 1
        nw = d.textlength(note, font=small)
        d.text((px + (pw - nw) / 2, by1 + 22), note, font=small, fill=MUTED)

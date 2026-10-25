def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, WATER, MUTED = k["INK"], k["OCHRE"], k["WATER"], k["MUTED"]
    big, lab, small = k["serif"](58), k["sans"](28, 600), k["sans"](24, 400)
    h = y1 - y0
    # a page on the left
    pw, ph = 300, min(400, h - 20)
    px, py = x0 + 10, y0 + (h - ph) // 2
    d.rectangle([px + 14, py + 14, px + pw + 14, py + ph + 14], fill=(225, 217, 200))
    d.rectangle([px, py, px + pw, py + ph], fill=(252, 249, 242), outline=INK, width=4)
    import random
    rnd = random.Random(7)
    ly = py + 30
    while ly < py + ph - 30:
        w = rnd.randint(int(pw * 0.55), pw - 50)
        d.line([px + 26, ly, px + 26 + w, ly], fill=MUTED, width=4)
        ly += 22
    # highlighted line
    hy = py + 30 + 22 * 6
    d.line([px + 26, hy, px + pw - 26, hy], fill=OCHRE, width=6)
    # numbers on the right
    tx = px + pw + 70
    rows = [("410", "pages per book"), ("40", "lines per page"), ("80", "letters per line"), ("25", "symbols: 22 letters, space, comma, full stop")]
    ry = py + 4
    step = (ph - 10) // 4
    for num, txt in rows:
        d.text((tx, ry - 6), num, font=big, fill=OCHRE)
        lines = k["wrap"](txt, small, x1 - tx - 130)
        yy = ry + 8 if len(lines) == 1 else ry - 4
        for ln in lines:
            d.text((tx + 125, yy + 10), ln, font=small, fill=INK)
            yy += 30
        ry += step

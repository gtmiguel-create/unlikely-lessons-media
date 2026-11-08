def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, WATER, OCHRE, MUTED = k["INK"], k["WATER"], k["OCHRE"], k["MUTED"]
    lab = k["sans"](26, 600)
    cx = (x0 + x1) // 2
    h = y1 - y0
    sea = y0 + int(h * 0.62)
    # mast and sail
    mast_top = y0 + 20
    d.line([cx, mast_top, cx, sea - 40], fill=INK, width=6)
    d.polygon([(cx + 8, mast_top + 10), (cx + 8, sea - 110), (cx + 170, sea - 110)], outline=INK, fill=None, width=5)
    # waves
    import math
    for row in range(2):
        yy = sea + 20 + row * 46
        pts = [(x, yy + 10 * math.sin((x - x0) / 38.0 + row)) for x in range(x0, x1 + 1, 6)]
        d.line(pts, fill=WATER, width=5)
    # hull: trapezoid of planks
    top_w, bot_w = 620, 440
    hy0, hy1 = sea - 100, sea + 60
    n = 4
    ph = (hy1 - hy0) / n
    for i in range(n):
        ya, yb = hy0 + i * ph, hy0 + (i + 1) * ph
        wa = top_w - (top_w - bot_w) * i / n
        wb = top_w - (top_w - bot_w) * (i + 1) / n
        poly = [(cx - wa / 2, ya), (cx + wa / 2, ya), (cx + wb / 2, yb), (cx - wb / 2, yb)]
        fill = OCHRE if i == 1 else k["CREAM"]
        d.polygon(poly, fill=fill, outline=INK, width=5)
    # label for new plank
    t = "new plank"
    d.text((x1 - d.textlength(t, font=lab) - 10, hy0 + ph * 1.1), t, font=lab, fill=OCHRE)
    # old plank floating away, bottom-left
    py = sea + 110
    d.polygon([(x0 + 20, py), (x0 + 200, py - 12), (x0 + 204, py + 14), (x0 + 24, py + 26)], fill=MUTED, outline=INK, width=4)
    d.text((x0 + 230, py - 14), "old plank", font=lab, fill=MUTED)

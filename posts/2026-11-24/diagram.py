def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, WATER, MUTED = k["INK"], k["OCHRE"], k["WATER"], k["MUTED"]
    lab, small = k["sans"](30, 700), k["sans"](28, 400)
    w, h = x1 - x0, y1 - y0
    top = y0 + 30
    # main cord
    d.line([x0 + 10, top, x0 + int(w * 0.52), top], fill=INK, width=10)
    # pendant cords (decorative), one highlighted
    cols = [WATER, MUTED, OCHRE, WATER, MUTED]
    xs = [x0 + 40 + i * int(w * 0.10) for i in range(5)]
    bottom = y1 - 20
    for i, (x, c) in enumerate(zip(xs, cols)):
        hi = i == 2
        d.line([x, top, x, bottom if hi else top + int(h * (0.55 + 0.08 * (i % 3)))],
               fill=c, width=9 if hi else 6)
    cx = xs[2]
    span = bottom - top
    # hundreds: 7 knots
    def knot(y, r=10):
        d.ellipse([cx - r, y - r, cx + r, y + r], fill=INK)
    hy = top + int(span * 0.10)
    for j in range(7):
        knot(hy + j * 23)
    ty = top + int(span * 0.58)
    for j in range(3):
        knot(ty + j * 23)
    uy = top + int(span * 0.86)
    # figure-eight knot
    d.ellipse([cx - 14, uy - 30, cx + 14, uy - 2], outline=INK, width=7)
    d.ellipse([cx - 14, uy - 2, cx + 14, uy + 26], outline=INK, width=7)
    lx = x0 + int(w * 0.58)
    rows = [(hy + 6 * 23 + 10, "7 knots", "hundreds = 700"),
            (ty + 23, "3 knots", "tens = 30"),
            (uy, "figure-eight knot", "ones = 1")]
    for y, a, b in rows:
        d.line([cx + 30, y, lx - 20, y], fill=MUTED, width=2)
        d.text((lx, y - 34), a, font=small, fill=INK)
        d.text((lx, y + 2), b, font=lab, fill=OCHRE)
    t = "= 731"
    f = k["serif"](64)
    d.text((lx, top - 10), "one cord", font=small, fill=MUTED)
    d.text((lx, top + 24), t, font=f, fill=INK)

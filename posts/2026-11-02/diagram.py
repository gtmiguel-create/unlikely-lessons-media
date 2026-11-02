def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, WATER, OCHRE, MUTED = k["INK"], k["WATER"], k["OCHRE"], k["MUTED"]
    lab, small = k["sans"](26, 600), k["sans"](24, 400)
    midy = (y0 + y1) // 2 + 10

    # Sargasso Sea (left)
    sx, sy, r = x0 + 120, midy + 90, 95
    d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=OCHRE)
    t = "SARGASSO SEA"
    d.text((sx - d.textlength(t, font=lab) / 2, sy + r + 14), t, font=lab, fill=INK)

    # Europe (right): plain coast block
    ex = x1 - 150
    d.rectangle([ex, y0 + 30, x1, y0 + 260], fill=INK)
    t = "EUROPE"
    d.text((ex + (x1 - ex - d.textlength(t, font=lab)) / 2, y0 + 130), t, font=lab, fill=(243, 238, 227))

    # Larvae: thin leaf shapes, growing as they drift east
    n = 5
    ax, ay = sx + r + 30, sy - 40
    bx, by = ex - 90, y0 + 150
    for i in range(n):
        f = i / (n - 1)
        cx = ax + (bx - ax) * f
        cy = ay + (by - ay) * f
        L = 14 + 46 * f
        H = 3 + 10 * f
        d.ellipse([cx - L, cy - H, cx + L, cy + H], fill=WATER)

    # Arrow to the coast
    ax2 = bx + 66
    d.line([ax2, by, ex - 12, by], fill=WATER, width=6)
    d.polygon([(ex - 4, by), (ex - 24, by - 12), (ex - 24, by + 12)], fill=WATER)

    t1 = "smallest larvae"
    d.text((sx + r + 30, sy + 10), t1, font=small, fill=MUTED)
    t2 = "larger as they drift east"
    d.text((bx - d.textlength(t2, font=small) - 10, by - 80), t2, font=small, fill=MUTED)

def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, MUTED = k["INK"], k["OCHRE"], k["MUTED"]
    BARK = (226, 205, 168)
    LINE = (120, 90, 60)
    small = k["sans"](24, 400)
    lab = k["sans"](26, 600)

    # birch-bark strip
    bx0, bx1 = x0 + 10, x1 - 10
    by0, by1 = y0 + 10, y1 - 50
    pts = [(bx0, by0 + 8), (bx0 + 120, by0), (bx0 + 300, by0 + 10), (bx0 + 520, by0 + 2),
           (bx1, by0 + 12), (bx1 - 6, by1 - 10), (bx1 - 260, by1), (bx0 + 340, by1 - 8),
           (bx0 + 6, by1)]
    d.polygon(pts, fill=BARK, outline=LINE)
    for i, (lx, ly) in enumerate([(40, 30), (760, 25), (40, 400), (760, 420)]):
        if by0 + ly < by1 - 20:
            d.line([bx0 + lx, by0 + ly, bx0 + lx + 50 + (i % 3) * 20, by0 + ly], fill=LINE, width=3)

    # alphabet exercise along the top
    alpha = k["sans"](50, 500)
    text = "А Б В Г Д Е Ж З И К"
    tw = d.textlength(text, font=alpha)
    d.text(((bx0 + bx1 - tw) / 2, by0 + 50), text, font=alpha, fill=INK)

    # stick-figure rider (in the style of his drawings)
    cx = (bx0 + bx1) // 2 - 40
    gy = by1 - 60                       # ground
    hy = gy - 90                        # horse body line
    w = 6
    # horse
    d.line([cx - 150, hy, cx + 110, hy], fill=INK, width=w)
    for lx in (cx - 140, cx - 100, cx + 70, cx + 105):
        d.line([lx, hy, lx + (8 if lx > cx else -8), gy], fill=INK, width=w)
    d.line([cx + 110, hy, cx + 150, hy - 40], fill=INK, width=w)          # neck
    d.ellipse([cx + 135, hy - 70, cx + 190, hy - 30], outline=INK, width=w)  # head
    d.line([cx - 150, hy, cx - 200, hy + 40], fill=INK, width=w)          # tail
    # rider
    ry = hy - 20
    d.line([cx - 20, ry, cx - 20, ry - 120], fill=INK, width=w)            # body
    d.ellipse([cx - 52, ry - 190, cx + 12, ry - 126], outline=INK, width=w)  # head
    d.line([cx - 20, ry, cx - 60, hy + 50], fill=INK, width=w)             # leg
    d.line([cx - 20, ry - 90, cx + 60, ry - 110], fill=INK, width=w)       # arm
    # too many fingers
    for a in range(-3, 4):
        d.line([cx + 60, ry - 110, cx + 88, ry - 112 + a * 10], fill=INK, width=4)
    # spear
    d.line([cx + 70, ry - 112, cx + 300, ry - 170], fill=INK, width=w)
    d.polygon([(cx + 300, ry - 186), (cx + 300, ry - 154), (cx + 335, ry - 178)], fill=OCHRE)

    note = "7 fingers"
    d.line([cx + 92, ry - 92, cx + 205, ry - 62], fill=OCHRE, width=3)
    d.text((cx + 212, ry - 80), note, font=lab, fill=OCHRE)

    cap = "Our sketch, in the style of Onfim's drawings"
    cw = d.textlength(cap, font=small)
    d.text(((x0 + x1 - cw) / 2, y1 - 36), cap, font=small, fill=MUTED)

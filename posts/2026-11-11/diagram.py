def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, MUTED = k["INK"], k["OCHRE"], k["MUTED"]
    lab, small = k["sans"](28, 700), k["sans"](24, 500)
    r = 26
    gap = 14

    def card(top, n, pre, label, note):
        d.text((x0, top), label, font=lab, fill=INK)
        cw = n * (2 * r) + (n - 1) * gap + 48
        cx0 = x0
        cy0 = top + 48
        d.rounded_rectangle([cx0, cy0, cx0 + cw, cy0 + 2 * r + 48], radius=18, outline=INK, width=4)
        for i in range(n):
            cx = cx0 + 24 + r + i * (2 * r + gap)
            cy = cy0 + 24 + r
            if i < pre:
                d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=OCHRE, outline=INK, width=3)
                d.line([cx - 11, cy + 1, cx - 3, cy + 10], fill=INK, width=5)
                d.line([cx - 3, cy + 10, cx + 13, cy - 9], fill=INK, width=5)
            else:
                d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=INK, width=3)
        d.text((x0, cy0 + 2 * r + 64), note, font=small, fill=MUTED)

    h = (y1 - y0)
    card(y0 + 10, 8, 0, "CARD A  ·  8 SPACES", "0 of 8 done  ·  8 washes to go")
    card(y0 + 10 + h // 2, 10, 2, "CARD B  ·  10 SPACES, 2 FREE STAMPS", "2 of 10 done  ·  still 8 washes to go")

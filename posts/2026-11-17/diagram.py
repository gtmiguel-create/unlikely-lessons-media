def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, MUTED, CREAM = k["INK"], k["OCHRE"], k["MUTED"], k["CREAM"]
    lab = k["sans"](30, 700)
    small = k["sans"](26, 400)
    big = k["serif"](44)
    cols, rows, gap = 5, 2, 22
    cw = min((x1 - x0 - (cols - 1) * gap) // cols, 150)
    gw = cols * cw + (cols - 1) * gap
    gx = x0 + (x1 - x0 - gw) // 2
    title = "FRANCE'S BILL: 600,000 PESOS"
    tw = d.textlength(title, font=lab)
    d.text((x0 + (x1 - x0 - tw) / 2, y0 + 10), title, font=lab, fill=INK)
    gy = y0 + 70
    for i in range(cols * rows):
        r, c = divmod(i, cols)
        bx, by = gx + c * (cw + gap), gy + r * (cw + gap)
        if i == 0:
            d.rounded_rectangle([bx, by, bx + cw, by + cw], 14, fill=OCHRE, outline=INK, width=4)
        else:
            d.rounded_rectangle([bx, by, bx + cw, by + cw], 14, outline=INK, width=4)
        s = "60k"
        sw = d.textlength(s, font=small)
        d.text((bx + (cw - sw) / 2, by + cw / 2 - 16), s, font=small, fill=CREAM if i == 0 else MUTED)
    ly = gy + rows * cw + (rows - 1) * gap + 30
    d.rounded_rectangle([gx, ly + 4, gx + 30, ly + 34], 6, fill=OCHRE, outline=INK, width=3)
    d.text((gx + 45, ly), "the pastry shop", font=small, fill=INK)
    d.rounded_rectangle([gx, ly + 50, gx + 30, ly + 80], 6, outline=INK, width=3)
    d.text((gx + 45, ly + 46), "other claims, loans and interest", font=small, fill=INK)

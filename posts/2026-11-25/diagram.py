def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, MUTED = k["INK"], k["OCHRE"], k["MUTED"]
    lab = k["sans"](30, 600)
    num = k["serif"](56)
    cols, rows = 10, 4
    r = 26
    gx = (x1 - x0 - 2 * r) / (cols - 1)
    top = y0 + 50
    gy = 78
    n = 0
    for j in range(rows):
        for i in range(cols):
            if n >= 38:
                break
            cx = x0 + r + i * gx
            cy = top + j * gy
            if n < 6:
                d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=OCHRE)
            else:
                d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=MUTED, width=5)
            n += 1
    ly = top + rows * gy + 10
    d.ellipse([x0, ly, x0 + 34, ly + 34], fill=OCHRE)
    d.text((x0 + 50, ly - 2), "saw part of the attack (about 6)", font=lab, fill=INK)
    ly += 56
    d.ellipse([x0, ly, x0 + 34, ly + 34], outline=MUTED, width=5)
    d.text((x0 + 50, ly - 2), "heard something, or nothing clear", font=lab, fill=INK)

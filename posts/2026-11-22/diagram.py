def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, WATER, OCHRE = k["INK"], k["WATER"], k["OCHRE"]
    lab, small = k["sans"](26, 700), k["sans"](24, 400)
    cx = (x0 + x1) // 2
    h = y1 - y0
    # left: one press -> many copies
    lx = x0 + (cx - x0) // 2
    rx = cx + (x1 - cx) // 2
    top = y0 + 30
    def label(x, y, t, f=lab, fill=INK):
        tw = d.textlength(t, font=f)
        d.text((x - tw / 2, y), t, font=f, fill=fill)
    label(lx, top, "MANY COPIES")
    label(rx, top, "3 SOURCES")
    # press box
    py = top + 50
    d.rectangle([lx - 70, py, lx + 70, py + 60], outline=INK, width=5, fill=OCHRE)
    label(lx, py + 14, "1 press", small)
    # fan of papers
    ny = py + 200
    for i in range(5):
        px = lx - 160 + i * 80
        d.line([lx, py + 60, px + 25, ny], fill=INK, width=3)
        d.rectangle([px, ny, px + 50, ny + 66], outline=INK, width=4, fill=(255, 252, 245))
        for j in range(3):
            d.line([px + 9, ny + 16 + j * 15, px + 41, ny + 16 + j * 15], fill=INK, width=2)
    label(lx, ny + 86, "one story, repeated", small, WATER)
    # right: three independent sources -> one claim
    sy = py
    for i, t in enumerate(["witness", "record", "expert"]):
        bx = rx - 150 + i * 150
        d.ellipse([bx - 42, sy, bx + 42, sy + 60], outline=INK, width=5, fill=WATER)
        label(bx, sy + 68, t, small)
        d.line([bx, sy + 104, rx, ny], fill=INK, width=3)
    d.rectangle([rx - 25, ny, rx + 25, ny + 66], outline=INK, width=4, fill=(255, 252, 245))
    for j in range(3):
        d.line([rx - 16, ny + 16 + j * 15, rx + 16, ny + 16 + j * 15], fill=INK, width=2)
    label(rx, ny + 86, "one claim, checked", small, WATER)
    d.line([cx, top, cx, ny + 120], fill=INK, width=2)

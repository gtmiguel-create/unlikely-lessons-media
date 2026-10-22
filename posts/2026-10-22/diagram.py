def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, WATER, OCHRE = k["INK"], k["WATER"], k["OCHRE"]
    lab, small = k["sans"](26, 600), k["sans"](24, 400)
    cx = (x0 + x1) // 2
    top = y0 + 50

    def tank(x, y, w, h, level, label, above=False):
        d.rectangle([x, y, x + w, y + h], outline=INK, width=5)
        d.rectangle([x + 5, y + h - int(h * level), x + w - 5, y + h - 5], fill=WATER)
        tw = d.textlength(label, font=lab)
        d.text((x + (w - tw) / 2, y - 40 if above else y + h + 14), label, font=lab, fill=INK)

    tank(cx - 130, top, 260, 120, 0.6, "INCOME", above=True)
    split, row = top + 160, top + 240
    for x2 in (x0 + 110, cx, x1 - 110):
        d.line([cx, top + 120, cx, split], fill=INK, width=6)
        d.line([cx, split, x2, split], fill=INK, width=6)
        d.line([x2, split, x2, row], fill=INK, width=6)
        d.ellipse([x2 - 13, split + 25, x2 + 13, split + 51], fill=OCHRE, outline=INK, width=3)
    tank(x0 + 30, row, 160, 170, 0.35, "TAXES")
    tank(cx - 80, row, 160, 170, 0.7, "SPENDING")
    tank(x1 - 190, row, 160, 170, 0.5, "SAVINGS")
    rx = k["W"] - 60
    d.line([x1 - 30, row + 120, rx, row + 120], fill=WATER, width=6)
    d.line([rx, row + 120, rx, top + 60], fill=WATER, width=6)
    d.line([rx, top + 60, cx + 152, top + 60], fill=WATER, width=6)
    d.polygon([(cx + 132, top + 60), (cx + 156, top + 47), (cx + 156, top + 73)], fill=WATER)
    d.text((cx + 175, top + 20), "pumped back up", font=small, fill=WATER)

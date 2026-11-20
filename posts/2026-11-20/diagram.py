def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, WATER, MUTED, CREAM = k["INK"], k["OCHRE"], k["WATER"], k["MUTED"], k["CREAM"]
    name, lab, yr = k["sans"](34, 700), k["sans"](28, 600), k["sans"](24, 400)
    rows = [
        ("WALTER WINANS (USA)", [("GOLD", "1908", "Shooting", WATER), ("GOLD", "1912", "Sculpture", OCHRE)]),
        ("ALFRÉD HAJÓS (HUNGARY)", [("GOLD", "1896", "Swimming", WATER), ("SILVER", "1924", "Architecture", OCHRE)]),
    ]
    rh = 210
    gap = max(20, (y1 - y0 - 2 * rh) // 3)
    y = y0 + gap
    colw = (x1 - x0) // 2
    for title, medals in rows:
        d.text((x0, y), title, font=name, fill=INK)
        my = y + 60
        for i, (kind, year, what, col) in enumerate(medals):
            cx = x0 + i * colw
            r = 55
            d.ellipse([cx, my, cx + 2 * r, my + 2 * r], fill=col, outline=INK, width=4)
            t = year
            tw = d.textlength(t, font=lab)
            d.text((cx + r - tw / 2, my + r - 17), t, font=lab, fill=CREAM)
            d.text((cx + 2 * r + 22, my + 18), kind, font=lab, fill=INK)
            d.text((cx + 2 * r + 22, my + 58), what, font=yr, fill=MUTED)
        if title.startswith("WALTER"):
            d.line([x0, y + rh + gap // 2, x1, y + rh + gap // 2], fill=MUTED, width=2)
        y += rh + gap
    lx = x1 - 300
    d.ellipse([lx, y1 - 34, lx + 26, y1 - 8], fill=WATER)
    d.text((lx + 36, y1 - 40), "sport", font=yr, fill=INK)
    d.ellipse([lx + 140, y1 - 34, lx + 166, y1 - 8], fill=OCHRE)
    d.text((lx + 176, y1 - 40), "art", font=yr, fill=INK)

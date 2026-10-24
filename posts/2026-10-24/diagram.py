def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, MUTED = k["INK"], k["OCHRE"], k["MUTED"]
    lab = k["sans"](26, 700)
    small = k["sans"](24, 500)
    pattern = [0, 1, 0, 0, 1, 1, 0, 1]          # 0 = dot / narrow, 1 = dash / wide
    unit = 26
    widths = [unit if p == 0 else unit * 3 for p in pattern]
    gap = 26
    total = sum(widths) + gap * (len(widths) - 1)
    sx = (x0 + x1 - total) // 2
    h = y1 - y0
    my = y0 + 70                                 # Morse row
    d.text((x0, y0), "MORSE", font=lab, fill=MUTED)
    ty = my + 50
    by0, by1 = ty + 90, y1 - 50                  # bars
    d.text((x0, by0 - 50), "BARCODE", font=lab, fill=OCHRE)
    x = sx
    for w, p in zip(widths, pattern):
        if p == 0:
            d.ellipse([x, my - unit // 2, x + unit, my + unit // 2], fill=INK)
        else:
            d.rounded_rectangle([x, my - unit // 2, x + w, my + unit // 2], radius=12, fill=INK)
        cx = x + w // 2
        for yy in range(my + 26, by0 - 14, 14):
            d.line([cx, yy, cx, yy + 6], fill=MUTED, width=3)
        d.rectangle([x, by0, x + w, by1], fill=INK)
        x += w + gap
    note = "dot = narrow line      dash = wide line"
    tw = d.textlength(note, font=small)
    d.text(((x0 + x1 - tw) / 2, by1 + 16), note, font=small, fill=MUTED)

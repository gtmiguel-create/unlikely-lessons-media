def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, CREAM, MUTED = k["INK"], k["OCHRE"], k["CREAM"], k["MUTED"]
    pages = [("SWEDEN", "30", "FEB", True, "its own calendar"),
             ("JULIAN", "29", "FEB", False, "the old calendar"),
             ("GREGORIAN", "11", "MAR", False, "the new calendar")]
    gap = 30
    w = (x1 - x0 - 2 * gap) // 3
    h = min(y1 - y0 - 70, 380)
    top = y0 + (y1 - y0 - h - 50) // 2
    num, mon, lab, sub = k["serif"](120), k["sans"](34, 700), k["sans"](25, 700), k["sans"](25, 400)

    def centred(cx, y, t, font, fill):
        d.text((cx - d.textlength(t, font=font) / 2, y), t, font=font, fill=fill)

    for i, (name, day, month, hot, note) in enumerate(pages):
        x = x0 + i * (w + gap)
        cx = x + w // 2
        col = OCHRE if hot else INK
        d.rectangle([x, top, x + w, top + h], fill=CREAM, outline=col, width=5)
        d.rectangle([x, top, x + w, top + 66], fill=col)
        centred(cx, top + 19, name, lab, CREAM)
        centred(cx, top + 105, day, num, col)
        centred(cx, top + 270, month, mon, col)
        centred(cx, top + h + 16, note, sub, MUTED)

def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, WATER, MUTED, CREAM = k["INK"], k["OCHRE"], k["WATER"], k["MUTED"], k["CREAM"]
    lab, small = k["sans"](30, 700), k["sans"](26, 400)
    glyph = k["serif"](84)
    colw = (x1 - x0) // 3
    cxs = [x0 + colw // 2 + i * colw for i in range(3)]
    base = y0 + 300        # shared baseline for the three objects
    label_y = base + 28

    def centred(cx, y, text, font, fill):
        d.text((cx - d.textlength(text, font=font) / 2, y), text, font=font, fill=fill)

    def letter(cx, cy, fill):
        bb = d.textbbox((0, 0), "a", font=glyph)
        d.text((cx - (bb[0] + bb[2]) / 2, cy - (bb[1] + bb[3]) / 2), "a", font=glyph, fill=fill)

    # 1. PUNCH: tall steel bar carrying the letter at its tip
    cx = cxs[0]
    d.rectangle([cx - 52, base - 280, cx + 52, base - 110], fill=(150, 155, 160), outline=INK, width=5)
    d.polygon([(cx - 52, base - 110), (cx + 52, base - 110), (cx + 66, base), (cx - 66, base)], fill=INK)
    letter(cx, base - 55, CREAM)

    # 2. MATRIX: copper block with the letter sunk into it
    cx = cxs[1]
    d.rectangle([cx - 85, base - 170, cx + 85, base], fill=OCHRE, outline=INK, width=5)
    d.rectangle([cx - 54, base - 138, cx + 54, base - 32], fill=INK)
    letter(cx, base - 85, OCHRE)

    # 3. TYPE: metal sort with the letter raised on top
    cx = cxs[2]
    d.rectangle([cx - 56, base - 280, cx + 56, base - 110], fill=INK)
    letter(cx, base - 195, CREAM)
    d.rectangle([cx - 56, base - 110, cx + 56, base], fill=(90, 96, 104), outline=INK, width=5)

    # arrows between columns
    for i in range(2):
        ax0, ax1 = cxs[i] + 92, cxs[i + 1] - 98
        ay = base - 85
        d.line([ax0, ay, ax1 - 14, ay], fill=INK, width=6)
        d.polygon([(ax1, ay), (ax1 - 20, ay - 13), (ax1 - 20, ay + 13)], fill=INK)

    rows = [("PUNCH", "steel", "cut by hand"),
            ("MATRIX", "copper", "the mould"),
            ("TYPE", "cast metal", "what prints")]
    for cx, (a, b, c) in zip(cxs, rows):
        centred(cx, label_y, a, lab, INK)
        centred(cx, label_y + 42, b, small, MUTED)
        centred(cx, label_y + 76, c, small, MUTED)

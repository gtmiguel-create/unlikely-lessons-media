def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, MUTED = k["INK"], k["OCHRE"], k["MUTED"]
    head, lab = k["sans"](30, 700), k["sans"](28, 500)
    val = k["sans"](30, 700)
    FIN, UNF = INK, OCHRE

    # legend
    ly = y0 + 4
    d.rectangle([x0, ly + 7, x0 + 24, ly + 31], fill=UNF)
    d.text((x0 + 36, ly), "Unfinished tasks", font=lab, fill=INK)
    lx = x0 + 330
    d.rectangle([lx, ly + 7, lx + 24, ly + 31], fill=FIN)
    d.text((lx + 36, ly), "Finished tasks", font=lab, fill=INK)

    d.text((x0, ly + 48), "Tasks recalled, with finished set at 1", font=k["sans"](26, 400), fill=MUTED)

    base = y1 - 58
    top = ly + 150
    unit = (base - top) / 1.61   # height of a ratio of 1.0
    groups = [("Zeigarnik, 1927", x0 + 40, 1.61, "1.6"), ("2025 review", (x0 + x1) // 2 + 40, 0.99, "0.99")]
    bw = 130
    for name, gx, r, label in groups:
        for i, (v, c, t) in enumerate(((r, UNF, label), (1.0, FIN, "1.0"))):
            bx = gx + i * (bw + 8)
            h = int(unit * v)
            d.rounded_rectangle([bx, base - h, bx + bw, base], radius=4, fill=c)
            tw = d.textlength(t, font=val)
            d.text((bx + (bw - tw) / 2, base - h - 44), t, font=val, fill=INK)
        tw = d.textlength(name, font=head)
        d.text((gx + (2 * bw + 8 - tw) / 2, base + 14), name, font=head, fill=INK)
    d.line([x0, base, x1, base], fill=MUTED, width=2)

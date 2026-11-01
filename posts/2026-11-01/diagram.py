def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, WATER, OCHRE, MUTED, CREAM = k["INK"], k["WATER"], k["OCHRE"], k["MUTED"], k["CREAM"]
    head, lab, small = k["sans"](30, 700), k["sans"](25, 600), k["sans"](22, 500)
    SEA = (205, 222, 230)
    gap = 44
    pw = (x1 - x0 - gap) // 2
    for i, (name, col) in enumerate((("EGYPT", OCHRE), ("SUDAN", WATER))):
        lx = x0 + i * 220
        d.rectangle([lx, y0 + 4, lx + 30, y0 + 34], fill=col)
        d.text((lx + 44, y0 + 4), name, font=lab, fill=INK)
    top = y0 + 80

    def centred(text, cx, y, font, fill):
        d.text((cx - d.textlength(text, font=font) / 2, y), text, font=font, fill=fill)

    def panel(px, title, halaib, bir, straight):
        d.text((px, top), title, font=head, fill=INK)
        t = top + 60
        par = t + 170
        sea = px + pw - 26
        d.rectangle([sea, t, px + pw, par + 150], fill=SEA)
        q = px + int(pw * 0.40)                 # quadripoint
        hal = [q, t + 40, sea, par]             # Halaib: big, north of parallel, on the coast
        bir_b = [q - 120, par, q, par + 110]    # Bir Tawil: small, south of parallel
        d.rectangle(hal, fill=halaib)
        d.rectangle(bir_b, fill=bir)
        centred("Halaib", (q + sea) / 2, par - 85, lab, CREAM)
        centred("Bir Tawil", q - 60, par + 125, lab, INK)
        if straight:
            d.line([px, par, sea, par], fill=INK, width=6)
            cap = "straight line: 22nd parallel"
        else:
            # faint parallel for reference
            for xx in range(px, sea, 24):
                d.line([xx, par, xx + 12, par], fill=MUTED, width=2)
            pts = [(px, par + 110), (q, par + 110), (q, t + 40), (sea, t + 40)]
            d.line(pts, fill=INK, width=6, joint="curve")
            cap = "bent line: who used the land"
        d.text((px, par + 190), cap, font=small, fill=MUTED)

    panel(x0, "1899", OCHRE, WATER, True)
    panel(x0 + pw + gap, "1902", WATER, OCHRE, False)

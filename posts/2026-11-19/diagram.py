def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, WATER, OCHRE, MUTED = k["INK"], k["WATER"], k["OCHRE"], k["MUTED"]
    lab, big = k["sans"](28, 700), k["sans"](30, 600)
    bw = x1 - x0
    bh = 120
    rows = [("BEFORE", 0.86), ("RICE GETS CHEAPER", 0.66)]
    gap = (y1 - y0 - 2 * bh - 2 * 50) // 3
    y = y0 + gap
    for title, share in rows:
        d.text((x0, y), title, font=lab, fill=MUTED)
        y += 46
        rx = x0 + int(bw * share)
        d.rectangle([x0, y, rx, y + bh], fill=WATER)
        d.rectangle([rx, y, x1, y + bh], fill=OCHRE)
        d.rectangle([x0, y, x1, y + bh], outline=INK, width=5)
        t = "RICE"
        d.text((x0 + 30, y + (bh - 34) // 2), t, font=big, fill=(243, 238, 227))
        t2 = "OTHER FOOD"
        if x1 - rx > 240:
            d.text((rx + 25, y + (bh - 34) // 2), t2, font=big, fill=INK)
        else:
            tw = d.textlength(t2, font=big)
            d.text((x1 - tw, y + bh + 12), t2, font=big, fill=OCHRE)
        y += bh + gap

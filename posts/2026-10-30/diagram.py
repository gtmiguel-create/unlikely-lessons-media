BROWN = (110, 70, 42)
PITCH = (60, 52, 46)
MYRRH = (196, 150, 84)


def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, CREAM, MUTED = k["INK"], k["OCHRE"], k["CREAM"], k["MUTED"]
    lab, small, op = k["sans"](28, 700), k["sans"](24, 400), k["sans"](60, 700)
    cy = y0 + (y1 - y0) // 2 - 60
    r = 70
    items = [("MUMMY", "ground up", BROWN), ("PITCH", "resin", PITCH), ("MYRRH", "resin", MYRRH)]
    xs = [x0 + 80, x0 + 330, x0 + 580]
    for i, ((name, note, col), cx) in enumerate(zip(items, xs)):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col, outline=INK, width=4)
        tw = d.textlength(name, font=lab)
        d.text((cx - tw / 2, cy + r + 18), name, font=lab, fill=INK)
        tw = d.textlength(note, font=small)
        d.text((cx - tw / 2, cy + r + 56), note, font=small, fill=MUTED)
        if i < 2:
            px = (cx + xs[i + 1]) / 2
            tw = d.textlength("+", font=op)
            d.text((px - tw / 2, cy - 38), "+", font=op, fill=INK)
    # arrow
    ax = xs[2] + r + 20
    d.line([ax, cy, ax + 50, cy], fill=INK, width=6)
    d.polygon([(ax + 66, cy), (ax + 44, cy - 14), (ax + 44, cy + 14)], fill=INK)
    # paint tube (vertical)
    tx = x1 - 70
    top, bot = cy - 130, cy + 110
    d.rectangle([tx - 14, top - 30, tx + 14, top], fill=INK)          # cap
    d.polygon([(tx - 22, top), (tx + 22, top), (tx + 50, top + 40), (tx - 50, top + 40)], fill=CREAM, outline=INK)
    d.rectangle([tx - 50, top + 40, tx + 50, bot], fill=CREAM, outline=INK, width=4)
    d.rectangle([tx - 50, top + 90, tx + 50, bot - 40], fill=BROWN, outline=INK, width=3)
    d.polygon([(tx - 56, bot), (tx + 56, bot), (tx + 56, bot + 18), (tx - 56, bot + 18)], fill=INK)
    for i, word in enumerate(("MUMMY", "BROWN")):
        tw = d.textlength(word, font=lab)
        d.text((tx - tw / 2, bot + 34 + i * 36), word, font=lab, fill=OCHRE)

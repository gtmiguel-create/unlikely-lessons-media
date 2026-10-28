def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, WATER, OCHRE, MUTED = k["INK"], k["WATER"], k["OCHRE"], k["MUTED"]
    lab, small = k["sans"](26, 600), k["sans"](24, 400)
    top, bot = y0 + 70, y0 + 370
    cx = (x0 + x1) // 2
    gap = 46
    # two rooms sharing a wall with a doorway
    d.rectangle([x0 + 20, top, cx, bot], outline=INK, width=5)
    d.rectangle([cx, top, x1 - 20, bot], outline=INK, width=5)
    dm = bot - 90
    d.rectangle([cx - 5, dm - gap, cx + 5, dm + gap], fill=k["CREAM"])
    d.line([cx, dm - gap, cx + 62, dm - gap - 44], fill=OCHRE, width=6)  # open door leaf
    for t, xx in (("ROOM A", x0 + 20), ("ROOM B", cx)):
        tw = d.textlength(t, font=lab)
        d.text((xx + ((cx - x0 - 20) - tw) / 2, top - 42), t, font=lab, fill=INK)
    # thought bubble in A: the plan
    ax = (x0 + 20 + cx) // 2
    d.ellipse([ax - 95, top + 30, ax + 95, top + 100], outline=WATER, width=4)
    t = "get scissors"
    d.text((ax - d.textlength(t, font=small) / 2, top + 50), t, font=small, fill=WATER)
    # path with arrow
    py = dm
    d.line([ax - 60, py, cx + 120, py], fill=INK, width=5)
    d.polygon([(cx + 140, py), (cx + 116, py - 13), (cx + 116, py + 13)], fill=INK)
    # B: empty bubble with ?
    bx = (cx + x1 - 20) // 2
    d.ellipse([bx - 95, top + 30, bx + 95, top + 100], outline=MUTED, width=4)
    q = k["serif"](54)
    d.text((bx - d.textlength("?", font=q) / 2, top + 30), "?", font=q, fill=MUTED)
    # boundary label under the door
    t1, t2 = "the doorway:", "“new episode, file the old one”"
    d.line([cx, bot + 10, cx, bot + 40], fill=OCHRE, width=4)
    for i, t in enumerate((t1, t2)):
        f = lab if i == 0 else small
        d.text((cx - d.textlength(t, font=f) / 2, bot + 50 + i * 36), t, font=f, fill=OCHRE)

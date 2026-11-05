def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, MUTED = k["INK"], k["OCHRE"], k["MUTED"]
    place, note = k["sans"](34, 700), k["sans"](28, 400)
    stops = [
        ("Cape Town", "the start", False),
        ("London", "interpreters and desert gear", False),
        ("Paris", "a feather merchant", False),
        ("River Niger", "steamboat, about 500 miles", False),
        ("Kano", "by train", False),
        ("Zinder", "by desert, into French territory", True),
    ]
    gap = (y1 - y0 - 74) / (len(stops) - 1)
    lx = x0 + 22
    d.line([lx, y0 + 22, lx, y0 + 22 + gap * (len(stops) - 1)], fill=INK, width=5)
    for i, (name, sub, end) in enumerate(stops):
        y = y0 + 22 + gap * i
        r = 20 if end else 14
        d.ellipse([lx - r, y - r, lx + r, y + r], fill=OCHRE if end else INK)
        d.text((lx + 50, y - 40), name, font=place, fill=OCHRE if end else INK)
        d.text((lx + 50, y + 2), sub, font=note, fill=MUTED)

def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, MUTED = k["INK"], k["OCHRE"], k["MUTED"]
    head = k["sans"](26, 700)
    lab = k["sans"](32, 500)
    num = k["serif"](54)
    items = [("A shirt, on average", "80"), ("A pastel portrait", "30"), ("Pressing a uniform", "12"),
             ("A cup of coffee", "2"), ("Washing one garment", "2")]
    top = y0 + 30
    d.text((x0, top), "CAMP PRICES", font=head, fill=OCHRE)
    t = "IN CIGARETTES"
    d.text((x1 - d.textlength(t, font=head), top), t, font=head, fill=OCHRE)
    y = top + 50
    d.line([x0, y, x1, y], fill=INK, width=4)
    row = 78
    for name, p in items:
        cy = y + row // 2
        d.text((x0, cy - 20), name, font=lab, fill=INK)
        # cigarette icon
        cx = x1 - 230
        d.rectangle([cx, cy - 9, cx + 70, cy + 9], outline=INK, width=3)
        d.rectangle([cx + 70, cy - 9, cx + 92, cy + 9], fill=OCHRE, outline=INK, width=3)
        pw = d.textlength(p, font=num)
        d.text((x1 - pw, cy - 34), p, font=num, fill=INK)
        y += row
        d.line([x0, y, x1, y], fill=MUTED, width=1)

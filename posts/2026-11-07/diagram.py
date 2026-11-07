import math


def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, WATER, MUTED, CREAM = k["INK"], k["OCHRE"], k["WATER"], k["MUTED"], k["CREAM"]
    lab = k["sans"](26, 700)
    small = k["sans"](22, 400)
    colw = (x1 - x0) / 4
    cxs = [x0 + colw / 2 + i * colw for i in range(4)]
    cy = (y0 + y1) // 2 - 20
    label_y = cy + 120

    def centred(cx, y, text, font, fill):
        d.text((cx - d.textlength(text, font=font) / 2, y), text, font=font, fill=fill)

    def arrow(xa, xb, y, col):
        d.line([xa, y, xb - 14, y], fill=col, width=6)
        d.polygon([(xb, y), (xb - 20, y - 12), (xb - 20, y + 12)], fill=col)

    # 1. ROTORS: three toothed wheels stacked
    cx = cxs[0]
    for i, (r, teeth) in enumerate([(34, 8), (34, 12), (34, 16)]):
        yy = cy - 80 + i * 80
        pts = []
        for j in range(teeth * 2):
            a = math.pi * j / teeth
            rr = r if j % 2 == 0 else r - 9
            pts.append((cx + rr * math.cos(a), yy + rr * math.sin(a)))
        d.polygon(pts, fill=OCHRE, outline=INK)
        d.ellipse([cx - 7, yy - 7, cx + 7, yy + 7], fill=INK)
    centred(cx, label_y, "ROTORS", lab, INK)
    centred(cx, label_y + 36, "one pitch each", small, MUTED)

    # 2. KEYBOARD
    cx = cxs[1]
    kw, kh = 130, 84
    kx, ky = cx - kw / 2, cy - kh / 2
    d.rectangle([kx, ky, kx + kw, ky + kh], fill=CREAM, outline=INK, width=4)
    for i in range(1, 6):
        xx = kx + i * kw / 6
        d.line([xx, ky, xx, ky + kh], fill=INK, width=3)
    for i in (1, 2, 4, 5):
        xx = kx + i * kw / 6
        d.rectangle([xx - 8, ky, xx + 8, ky + kh * 0.58], fill=INK)
    centred(cx, label_y, "KEYBOARD", lab, INK)
    centred(cx, label_y + 36, "mixes the notes", small, MUTED)

    # 3. PHONE LINE: two poles with a wire
    cx = cxs[2]
    for px in (cx - 55, cx + 55):
        d.line([px, cy - 70, px, cy + 70], fill=INK, width=7)
        d.line([px - 22, cy - 55, px + 22, cy - 55], fill=INK, width=6)
    d.line([cx - 55, cy - 55, cx + 55, cy - 55], fill=WATER, width=5)
    centred(cx, label_y, "PHONE LINE", lab, INK)
    centred(cx, label_y + 36, "across the city", small, MUTED)

    # 4. HORN on a receiver
    cx = cxs[3]
    d.rectangle([cx - 60, cy - 14, cx - 30, cy + 14], fill=INK)
    d.polygon([(cx - 30, cy - 10), (cx + 60, cy - 62), (cx + 60, cy + 62), (cx - 30, cy + 10)],
              fill=OCHRE, outline=INK)
    d.ellipse([cx + 48, cy - 62, cx + 72, cy + 62], fill=CREAM, outline=INK, width=4)
    centred(cx, label_y, "HORN", lab, INK)
    centred(cx, label_y + 36, "in a restaurant", small, MUTED)

    # arrows between stages
    for i in range(3):
        arrow(cxs[i] + colw * 0.36, cxs[i + 1] - colw * 0.33, cy, WATER)

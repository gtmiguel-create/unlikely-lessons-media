import math


def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, MUTED, CREAM = k["INK"], k["OCHRE"], k["MUTED"], k["CREAM"]
    lab = k["sans"](22, 700)
    mid = k["serif"](64)
    small = k["sans"](22, 500)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    R = min(x1 - x0, y1 - y0) // 2 - 85
    nr = 64
    names = ["BAKER", "BUILDER", "HOTEL", "PRINTER", "GARAGE", "FARM"]
    n = len(names)
    # dashed outer boundary of the circle
    Rb = R + nr + 18
    for i in range(72):
        if i % 2:
            continue
        a0, a1 = i * 5, i * 5 + 5
        d.arc([cx - Rb, cy - Rb, cx + Rb, cy + Rb], a0, a1, fill=MUTED, width=3)
    # arrows between neighbours
    for i in range(n):
        a = math.radians(-90 + i * 360 / n)
        b = math.radians(-90 + (i + 1) * 360 / n)
        p = (cx + R * math.cos(a), cy + R * math.sin(a))
        q = (cx + R * math.cos(b), cy + R * math.sin(b))
        dx, dy = q[0] - p[0], q[1] - p[1]
        L = math.hypot(dx, dy)
        ux, uy = dx / L, dy / L
        s = (p[0] + ux * (nr + 10), p[1] + uy * (nr + 10))
        e = (q[0] - ux * (nr + 14), q[1] - uy * (nr + 14))
        d.line([s, e], fill=OCHRE, width=6)
        px, py = -uy, ux
        tip = e
        base = (e[0] - ux * 24, e[1] - uy * 24)
        d.polygon([tip, (base[0] + px * 13, base[1] + py * 13), (base[0] - px * 13, base[1] - py * 13)], fill=OCHRE)
    # nodes
    for i, nm in enumerate(names):
        a = math.radians(-90 + i * 360 / n)
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        d.ellipse([x - nr, y - nr, x + nr, y + nr], fill=CREAM, outline=INK, width=5)
        tw = d.textlength(nm, font=lab)
        d.text((x - tw / 2, y - 14), nm, font=lab, fill=INK)
    # centre
    tw = d.textlength("WIR", font=mid)
    d.text((cx - tw / 2, cy - 44), "WIR", font=mid, fill=OCHRE)
    t2 = "paid in WIR"
    d.text((cx - d.textlength(t2, font=small) / 2, cy + 34), t2, font=small, fill=MUTED)

import math


def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, MUTED, WATER = k["INK"], k["OCHRE"], k["MUTED"], k["WATER"]
    lab = k["sans"](26, 700)
    gy = y1 - 90                      # ground line
    # distant hills
    d.polygon([(x0, gy), (x0 + 180, gy - 70), (x0 + 360, gy - 30), (x0 + 560, gy - 95),
               (x1 - 120, gy - 40), (x1, gy - 60), (x1, gy)], fill=(220, 212, 196))
    d.line([x0, gy, x1, gy], fill=INK, width=5)
    # camera on tripod
    cx, cy = x0 + 70, gy - 90
    d.line([cx, cy + 20, cx - 30, gy], fill=INK, width=5)
    d.line([cx, cy + 20, cx + 30, gy], fill=INK, width=5)
    d.line([cx, cy + 20, cx, gy], fill=INK, width=5)
    d.rectangle([cx - 30, cy - 22, cx + 34, cy + 20], fill=INK)
    d.rectangle([cx + 34, cy - 12, cx + 52, cy + 10], fill=INK)
    # moon
    ang = math.radians(28)
    L = (x1 - 110) - (cx + 52)
    mx, my = cx + 52 + L, cy - L * math.tan(ang)
    if my < y0 + 70:
        my = y0 + 70
        L = (cy - my) / math.tan(ang)
        mx = cx + 52 + L
    # dashed sight line
    sx, sy = cx + 52, cy
    n = 40
    for i in range(0, n, 2):
        a, b = i / n, (i + 1) / n
        d.line([sx + (mx - sx) * a, sy + (my - sy) * a, sx + (mx - sx) * b, sy + (my - sy) * b],
               fill=OCHRE, width=5)
    r = 50
    d.ellipse([mx - r, my - r, mx + r, my + r], fill=(250, 248, 240), outline=INK, width=4)
    t = "MOON"
    d.text((mx - d.textlength(t, font=lab) / 2, my - r - 44), t, font=lab, fill=INK)
    # horizontal reference
    d.line([sx, sy, sx + 330, sy], fill=MUTED, width=3)
    # angle arc
    R = 230
    d.arc([sx - R, sy - R, sx + R, sy + R], -28, 0, fill=OCHRE, width=6)
    d.text((sx + R + 16, sy - 70), "HEIGHT", font=lab, fill=OCHRE)
    # direction arrow along ground
    ay = gy + 36
    d.line([cx, ay, x1 - 28, ay], fill=WATER, width=5)
    d.polygon([(x1 - 28, ay - 13), (x1, ay), (x1 - 28, ay + 13)], fill=WATER)
    t = "DIRECTION"
    f = k["sans"](24, 700)
    d.text((x1 - d.textlength(t, font=f), ay + 18), t, font=f, fill=WATER)

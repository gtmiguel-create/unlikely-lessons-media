import math


def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, WATER, OCHRE, MUTED = k["INK"], k["WATER"], k["OCHRE"], k["MUTED"]
    lab = k["sans"](26, 600)
    cx = (x0 + x1) // 2
    h = y1 - y0
    # fjord cross-section: steep walls, U-shaped bottom
    top = y0 + 30
    bot = y0 + int(h * 0.62)
    lw, rw = x0 + 70, x1 - 70       # wall x at water level
    water = top + int((bot - top) * 0.35)
    tilt = 38
    # water body: tilted surface (left high, right low)
    def wx(y, side):
        f = (y - (water - 60)) / ((bot - 40) - (water - 60))
        return lw + 30 * f + 6 if side < 0 else rw - 30 * f - 6
    yl, yr = water - tilt, water + tilt
    poly = [(wx(yl, -1), yl), (wx(yr, 1), yr), (rw - 30, bot - 40), (rw - 120, bot), (lw + 120, bot), (lw + 30, bot - 40)]
    d.polygon(poly, fill=WATER)
    # dashed opposite tilt (the swing back)
    for i in range(0, 20):
        if i % 2 == 0:
            ax = lw + 12 + (rw - lw - 24) * i / 20
            bx = lw + 12 + (rw - lw - 24) * (i + 1) / 20
            ay = water + tilt - 2 * tilt * i / 20
            by = water + tilt - 2 * tilt * (i + 1) / 20
            d.line([ax, ay, bx, by], fill=OCHRE, width=5)
    # rock walls
    d.line([lw - 40, top - 20, lw, water - 60, lw + 30, bot - 40, lw + 120, bot, rw - 120, bot, rw - 30, bot - 40, rw, water - 60, rw + 40, top - 20], fill=INK, width=7, joint="curve")
    # double arrow above water
    ay = top - 5
    d.line([cx - 150, ay, cx + 150, ay], fill=INK, width=5)
    d.polygon([(cx - 170, ay), (cx - 145, ay - 13), (cx - 145, ay + 13)], fill=INK)
    d.polygon([(cx + 170, ay), (cx + 145, ay - 13), (cx + 145, ay + 13)], fill=INK)
    t = "every ~90 seconds"
    d.text((cx - d.textlength(t, font=lab) / 2, ay - 48), t, font=lab, fill=INK)
    # seismogram trace below
    sy = bot + 70
    d.text((x0, sy - 6), "SEISMOMETERS", font=k["sans"](22, 700), fill=MUTED)
    sx0 = x0 + 220
    base = sy + 8
    pts = []
    for x in range(sx0, x1 + 1, 3):
        f = (x - sx0) / (x1 - sx0)
        amp = 30 * math.exp(-1.6 * f)
        pts.append((x, base + amp * math.sin((x - sx0) / 13.0)))
    d.line(pts, fill=OCHRE, width=4)
    t2 = "9 days, slowly fading"
    d.text((x1 - d.textlength(t2, font=lab), base + 44), t2, font=lab, fill=MUTED)

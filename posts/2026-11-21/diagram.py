import math


def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, WATER, OCHRE, MUTED = k["INK"], k["WATER"], k["OCHRE"], k["MUTED"]
    lab, small = k["sans"](26, 600), k["sans"](22, 400)
    waves = [("MOON", 1.0, 2.0, 0.0), ("SUN", 0.45, 2.07, 1.1), ("DAILY CYCLE", 0.35, 1.0, 0.6)]
    H = y1 - y0
    lw = 210                      # label column
    gx0, gx1 = x0 + lw, x1 - 10
    small_h = H * 0.15
    gap = H * 0.05
    y = y0 + gap

    def curve(yc, amp_px, fn, col, width):
        pts = []
        n = 240
        for i in range(n + 1):
            t = i / n
            pts.append((gx0 + t * (gx1 - gx0), yc - amp_px * fn(t)))
        d.line(pts, fill=col, width=width, joint="curve")

    for name, a, f, p in waves:
        yc = y + small_h / 2
        d.text((x0, yc - 16), name, font=lab, fill=INK)
        d.line([gx0, yc, gx1, yc], fill=MUTED, width=1)
        curve(yc, small_h * 0.45 * a, lambda t, a=a, f=f, p=p: math.sin(2 * math.pi * f * t * 2 + p), WATER, 5)
        y += small_h + gap * 0.6
    # plus signs / equals bar
    d.line([x0, y, x1, y], fill=INK, width=3)
    d.text((x0, y + 6), "ADD THEM UP", font=small, fill=MUTED)
    big_h = y1 - y - gap * 1.2
    yc = y + gap + big_h / 2
    d.text((x0, yc - 16), "THE TIDE", font=lab, fill=OCHRE)
    tot = sum(a for _, a, _, _ in waves)
    def total(t):
        return sum(a * math.sin(2 * math.pi * f * t * 2 + p) for _, a, f, p in waves) / tot
    d.line([gx0, yc, gx1, yc], fill=MUTED, width=1)
    curve(yc, big_h * 0.45, total, OCHRE, 7)

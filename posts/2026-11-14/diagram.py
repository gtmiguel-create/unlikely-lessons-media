import math


def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, WATER, MUTED = k["INK"], k["OCHRE"], k["WATER"], k["MUTED"]
    lab, small = k["sans"](26, 700), k["sans"](24, 500)
    cy = (y0 + y1) // 2 + 10

    # listening post (building) on the left
    bx0, bx1 = x0 + 10, x0 + 170
    d.rectangle([bx0, cy - 110, bx1, cy + 120], outline=INK, width=5)
    for r in range(3):
        for c in range(2):
            wx = bx0 + 28 + c * 62
            wy = cy - 80 + r * 62
            d.rectangle([wx, wy, wx + 42, wy + 38], fill=INK)
    d.line([bx1 - 30, cy - 110, bx1 - 30, cy - 160], fill=INK, width=4)
    d.line([bx1 - 50, cy - 150, bx1 - 10, cy - 150], fill=INK, width=4)
    t = "LISTENING POST"
    d.text((x0, cy + 138), t, font=lab, fill=INK)

    # the seal (wooden plaque) with the bug inside
    sx, r = x1 - 230, 120
    d.ellipse([sx - r, cy - r, sx + r, cy + r], fill=(214, 176, 120), outline=INK, width=5)
    d.ellipse([sx - r + 16, cy - r + 16, sx + r - 16, cy + r - 16], outline=INK, width=2)
    # cylinder + membrane + antenna
    d.rectangle([sx - 22, cy - 6, sx + 22, cy + 50], fill=(150, 150, 150), outline=INK, width=4)
    d.line([sx - 22, cy - 6, sx + 22, cy - 6], fill=OCHRE, width=6)
    d.line([sx, cy + 50, sx, cy + 50], fill=INK, width=4)
    d.line([sx, cy - 6, sx, cy - 85], fill=INK, width=4)
    t = "THE SEAL"
    d.text((sx - d.textlength(t, font=lab) / 2, cy + r + 18), t, font=lab, fill=INK)

    # voices in the room (right of seal)
    vx = sx + r + 18
    for i in range(3):
        rr = 22 + i * 22
        d.arc([vx + 70 - rr, cy - rr, vx + 70 + rr, cy + rr], 150, 210, fill=INK, width=4)
    t = "voices"
    d.text((min(x1 - d.textlength(t, font=small), vx + 40 - d.textlength(t, font=small) / 2), cy + 80), t, font=small, fill=INK)

    # 1. beam in (straight, ochre)
    ax0, ax1 = bx1 + 20, sx - r - 14
    ya = cy - 45
    d.line([ax0, ya, ax1 - 18, ya], fill=OCHRE, width=7)
    d.polygon([(ax1, ya), (ax1 - 24, ya - 13), (ax1 - 24, ya + 13)], fill=OCHRE)
    t = "1. radio beam in"
    d.text(((ax0 + ax1) / 2 - d.textlength(t, font=small) / 2, ya - 44), t, font=small, fill=OCHRE)

    # 2. beam back with voices (wavy, blue)
    yb = cy + 55
    pts = []
    x = ax1
    while x >= ax0 + 18:
        pts.append((x, yb + 11 * math.sin((ax1 - x) / 11)))
        x -= 3
    d.line(pts, fill=WATER, width=6)
    d.polygon([(ax0, yb), (ax0 + 24, yb - 13), (ax0 + 24, yb + 13)], fill=WATER)
    t = "2. back out,"
    t2 = "carrying voices"
    mx = (ax0 + ax1) / 2
    d.text((mx - d.textlength(t, font=small) / 2, yb + 28), t, font=small, fill=WATER)
    d.text((mx - d.textlength(t2, font=small) / 2, yb + 60), t2, font=small, fill=WATER)

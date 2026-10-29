WOOD = (214, 178, 122)
GRAIN = (170, 128, 72)


def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, CREAM, MUTED = k["INK"], k["OCHRE"], k["CREAM"], k["MUTED"]
    lab, small = k["sans"](30, 700), k["sans"](27, 400)
    h = 110
    L = x1 - x0
    # notch positions (fractions of width) and widths: £1000, £100, £100, £20, £20, £1, £1
    notches = [(0.34, 70), (0.48, 40), (0.57, 40), (0.66, 24), (0.73, 24), (0.81, 12), (0.87, 12)]
    gap = 110
    mid = (y0 + y1) // 2 + 10
    ya = mid - gap // 2 - h          # stock (top)
    yb = mid + gap // 2              # foil (bottom)
    foil_x = x0 + int(L * 0.24)

    def half(x, y, xe, cut_top):
        d.rectangle([x, y, xe, y + h], fill=WOOD, outline=INK, width=4)
        for gy in (y + 34, y + 72):
            for gx in range(int(x) + 24, int(xe) - 40, 110):
                d.line([gx, gy, gx + 60, gy], fill=GRAIN, width=3)
        for f, w in notches:
            nx = x0 + L * f
            ey = y + h if cut_top else y   # notches on the split edge
            dy = -46 if cut_top else 46
            d.polygon([(nx - w / 2, ey), (nx + w / 2, ey), (nx, ey + dy)], fill=CREAM, outline=INK)
            d.line([nx - w / 2, ey, nx + w / 2, ey], fill=CREAM, width=5)

    half(x0, ya, x1, True)
    half(foil_x, yb, x1, False)

    # split line
    for gx in range(x0 + 100, x1, 32):
        d.line([gx, mid, gx + 16, mid], fill=OCHRE, width=4)
    d.text((x0, mid - 17), "split", font=small, fill=OCHRE)

    d.text((x0, ya - 52), "STOCK  ·  the longer half, for the lender", font=lab, fill=INK)
    d.text((foil_x, yb + h + 18), "FOIL  ·  the shorter half", font=lab, fill=INK)

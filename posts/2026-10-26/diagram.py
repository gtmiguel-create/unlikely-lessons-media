def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, WATER, OCHRE, MUTED = k["INK"], k["WATER"], k["OCHRE"], k["MUTED"]
    lab, small = k["sans"](30, 700), k["sans"](26, 400)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    bw, bh = 330, 120
    dx, dy = (x1 - x0) // 2 - bw // 2 - 10, (y1 - y0) // 2 - bh // 2 - 10
    nodes = [
        ((cx, cy - dy), "WATER SEEPS IN", "slows neutrons", WATER),
        ((cx + dx, cy), "REACTOR ON", "about 30 min", OCHRE),
        ((cx, cy + dy), "WATER BOILS OFF", "heat drives it out", OCHRE),
        ((cx - dx, cy), "REACTOR OFF", "about 2.5 hours", INK),
    ]
    # arrows between nodes (clockwise)
    import math
    for i in range(4):
        (ax, ay), (bx, by) = nodes[i][0], nodes[(i + 1) % 4][0]
        # start/end at box edges along the corner path
        if i == 0:
            p = [(ax + bw // 2, ay), (bx, ay), (bx, by - bh // 2)]
        elif i == 1:
            p = [(ax, ay + bh // 2), (ax, by), (bx + bw // 2, by)]
        elif i == 2:
            p = [(ax - bw // 2, ay), (bx, ay), (bx, by + bh // 2)]
        else:
            p = [(ax, ay - bh // 2), (ax, by), (bx - bw // 2, by)]
        d.line(p, fill=MUTED, width=5, joint="curve")
        (px, py), (qx, qy) = p[-2], p[-1]
        ang = math.atan2(qy - py, qx - px)
        s = 22
        tip = (qx, qy)
        l = (qx - s * math.cos(ang) + s * 0.6 * math.sin(ang), qy - s * math.sin(ang) - s * 0.6 * math.cos(ang))
        r = (qx - s * math.cos(ang) - s * 0.6 * math.sin(ang), qy - s * math.sin(ang) + s * 0.6 * math.cos(ang))
        d.polygon([tip, l, r], fill=MUTED)
    for (nx, ny), t, sub, col in nodes:
        d.rounded_rectangle([nx - bw // 2, ny - bh // 2, nx + bw // 2, ny + bh // 2], radius=18,
                            fill=k["CREAM"], outline=col, width=6)
        tw = d.textlength(t, font=lab)
        d.text((nx - tw / 2, ny - 40), t, font=lab, fill=col)
        sw = d.textlength(sub, font=small)
        d.text((nx - sw / 2, ny + 8), sub, font=small, fill=INK)

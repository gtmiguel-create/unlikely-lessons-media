def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, WATER, OCHRE, MUTED = k["INK"], k["WATER"], k["OCHRE"], k["MUTED"]
    lab, small = k["sans"](26, 600), k["sans"](23, 400)
    h = y1 - y0
    cy = y0 + h // 2 + 10
    # sun
    sx, sy = x0 + 70, y0 + 60
    d.ellipse([sx - 38, sy - 38, sx + 38, sy + 38], fill=OCHRE)
    for dx, dy in [(0, -60), (0, 60), (-60, 0), (60, 0), (42, 42), (-42, -42), (42, -42), (-42, 42)]:
        d.line([sx + dx * 0.75, sy + dy * 0.75, sx + dx, sy + dy], fill=OCHRE, width=5)
    d.text((sx - 30, sy + 70), "SUN", font=lab, fill=INK)
    # mirror at speaking tube
    mx = x0 + 250
    d.line([sx + 30, sy + 30, mx, cy], fill=OCHRE, width=5)
    d.line([mx, cy - 70, mx + 14, cy + 70], fill=INK, width=8)
    # speaking tube
    d.rectangle([mx + 14, cy + 50, mx + 120, cy + 80], outline=INK, width=4)
    d.polygon([(mx + 120, cy + 40), (mx + 160, cy + 25), (mx + 160, cy + 105), (mx + 120, cy + 90)], outline=INK, width=4)
    t = "VOICE"
    d.text((mx + 70, cy + 120), t, font=lab, fill=INK)
    d.text((mx - 60, cy - 120), "THIN MIRROR", font=lab, fill=INK)
    # beam
    rx = x1 - 230
    for i, off in enumerate((-12, 0, 12)):
        d.line([mx + 10, cy + off, rx, cy + off * 3], fill=OCHRE, width=4)
    d.text((mx + 150, cy - 60), "flickering light beam", font=small, fill=MUTED)
    # parabolic dish
    d.arc([rx - 40, cy - 110, rx + 120, cy + 110], 270, 90, fill=INK, width=8)
    d.ellipse([rx + 22, cy - 14, rx + 50, cy + 14], fill=WATER)
    d.text((rx - 40, cy - 165), "SELENIUM CELL", font=lab, fill=INK)
    # wire to earpiece
    ex = x1 - 70
    d.line([rx + 50, cy, rx + 90, cy, rx + 90, cy + 170, ex, cy + 170], fill=WATER, width=5)
    d.ellipse([ex - 30, cy + 140, ex + 30, cy + 200], outline=INK, width=6, fill=WATER)
    d.text((rx + 30, cy + 215), "EARPIECE", font=lab, fill=INK)

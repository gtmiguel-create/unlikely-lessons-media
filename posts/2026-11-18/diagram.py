def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, OCHRE, MUTED = k["INK"], k["OCHRE"], k["MUTED"]
    lab = k["sans"](28, 700)
    small = k["sans"](26, 400)
    W = x1 - x0
    sx, fx = x0 + 70, x1 - 70          # start / finish x
    lanes = [("NEAR BUCKET", 0.22, "carried the long way"),
             ("FAR BUCKET", 0.72, "carried a short way")]
    lane_h = 170
    top = y0 + 40
    for i, (name, pos, note) in enumerate(lanes):
        cy = top + i * (lane_h + 40) + 70
        d.text((sx + 20, cy - 95), name, font=lab, fill=INK)
        d.line([sx, cy - 45, sx, cy + 45], fill=INK, width=4)
        d.line([fx + 34, cy - 45, fx + 34, cy + 45], fill=INK, width=4)
        bx = sx + (fx - sx) * pos
        # walk empty (thin dashed)
        x = sx
        while x < bx - 30:
            d.line([x, cy, min(x + 18, bx - 30), cy], fill=MUTED, width=4)
            x += 32
        # carry (thick ochre)
        d.line([bx + 30, cy, fx, cy], fill=OCHRE, width=12)
        d.polygon([(fx, cy - 18), (fx + 30, cy), (fx, cy + 18)], fill=OCHRE)
        # bucket
        d.polygon([(bx - 26, cy - 30), (bx + 26, cy - 30), (bx + 18, cy + 30), (bx - 18, cy + 30)],
                  fill=None, outline=INK, width=5)
        d.arc([bx - 22, cy - 56, bx + 22, cy - 6], 180, 360, fill=INK, width=4)
        nw = d.textlength(note, font=small)
        d.text((fx - 20 - nw, cy + 40), note, font=small, fill=INK)
    # start / finish markers
    yb = top + 2 * (lane_h + 40) - 10
    for txt, x in (("START", sx), ("FINISH", fx + 34)):
        tw = d.textlength(txt, font=lab)
        d.text((x - tw / 2, yb - 40), txt, font=lab, fill=INK)
    # legend
    ly = yb + 20
    d.line([x0, ly + 16, x0 + 60, ly + 16], fill=OCHRE, width=12)
    d.text((x0 + 75, ly), "carrying", font=small, fill=INK)
    lx = x0 + 280
    for j in range(2):
        d.line([lx + j * 32, ly + 16, lx + j * 32 + 18, ly + 16], fill=MUTED, width=4)
    d.text((lx + 75, ly), "walking empty-handed", font=small, fill=INK)

import math


def draw(d, box, k):
    x0, y0, x1, y1 = box
    INK, WATER, OCHRE, MUTED = k["INK"], k["WATER"], k["OCHRE"], k["MUTED"]
    lab = k["sans"](26, 700)
    small = k["sans"](24, 500)

    P = (x0 + 330, y1 - 30)                 # where the three planes meet

    def pt(angle_deg, dist):
        a = math.radians(angle_deg)
        return (P[0] + dist * math.cos(a), P[1] - dist * math.sin(a))

    def dashed(a, b, col, w=3, on=14, off=10):
        L = math.dist(a, b)
        n = int(L // (on + off)) + 1
        for i in range(n):
            s, e = i * (on + off) / L, min(1, (i * (on + off) + on) / L)
            d.line([(a[0] + (b[0] - a[0]) * s, a[1] + (b[1] - a[1]) * s),
                    (a[0] + (b[0] - a[0]) * e, a[1] + (b[1] - a[1]) * e)], fill=col, width=w)

    h = y1 - y0
    # film plane: steep, up-left
    fa, f0, f1 = 104, h * 0.55, h * 0.92
    dashed(P, pt(fa, f0), MUTED)
    d.line([pt(fa, f0), pt(fa, f1)], fill=INK, width=10)
    # lens plane: up-right
    la, lc = 78, h * 0.80
    dashed(P, pt(la, lc - 70), MUTED)
    cx, cy = pt(la, lc)
    # lens drawn as an ellipse rotated along its plane (polygon)
    ang = math.radians(la)
    pts = []
    for t in range(0, 360, 10):
        r = math.radians(t)
        u, v = 70 * math.cos(r), 18 * math.sin(r)        # u along plane, v across
        pts.append((cx + u * math.cos(ang) + v * math.sin(ang),
                    cy - u * math.sin(ang) + v * math.cos(ang)))
    d.polygon(pts, fill=OCHRE, outline=INK, width=3)
    # sharp plane: shallow, to the right
    sa, s0, s1 = 22, 260, x1 - P[0] + 10
    dashed(P, pt(sa, s0), MUTED)
    d.line([pt(sa, s0), pt(sa, s1 / math.cos(math.radians(sa)) * 0.98)], fill=WATER, width=10)

    # meeting point
    d.ellipse([P[0] - 14, P[1] - 14, P[0] + 14, P[1] + 14], fill=INK)
    d.text((P[0] + 26, P[1] - 14), "they all meet here", font=small, fill=INK)

    # labels
    fx, fy = pt(fa, f1)
    d.text((fx - 40, fy - 44), "FILM", font=lab, fill=INK)
    d.text((cx + 40, cy - 70), "LENS (tilted)", font=lab, fill=INK)
    ex, ey = pt(sa, s1 * 0.9)
    tw = d.textlength("SHARP PLANE", font=lab)
    d.text((min(ex, x1 - tw) - tw * 0.3, ey - 60), "SHARP PLANE", font=lab, fill=WATER)

"""Render an Unlikely Lessons carousel from a post.json spec.

Usage:  python3 tools/render.py posts/2026-10-23/post.json
Writes slide_01.jpg ... next to post.json (1080x1350, JPEG, Instagram-ready).

Slide types in post.json["slides"]:
  {"type": "cover",   "title": "...", "accent": "...", "sub": "..."}
  {"type": "text",    "kicker": "...", "body": "..."}          (\n\n = paragraph)
  {"type": "diagram", "kicker": "...", "script": "diagram.py", "body": "..."}
        script (next to post.json) defines  draw(d, box, kit)  where box=(x0,y0,x1,y1)
        is the free area and kit gives colours/fonts/helpers (see KIT below).
  {"type": "moral",   "lead": "...", "accent": "..."}
  {"type": "cta"}
The cover keeps all content inside the profile-grid safe zone (the grid shows
a centred 810x1080 crop), so the thumbnail is never cut.
"""
import json
import os
import runpy
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FD = os.path.join(ROOT, "fonts")

CREAM = (243, 238, 227)
INK = (27, 36, 48)
OCHRE = (200, 134, 42)
WATER = (47, 111, 143)
MUTED = (110, 112, 115)
MUTED_DARK = (150, 155, 160)
W, H = 1080, 1350
M = 96          # normal side margin
SAFE = 180      # cover margin: grid thumbnail crops ~135px each side


def serif(size, italic=False):
    return ImageFont.truetype(os.path.join(FD, f"DMSerif{'Italic' if italic else ''}.ttf"), size)


def sans(size, weight=400):
    f = ImageFont.truetype(os.path.join(FD, "Inter.ttf"), size)
    f.set_variation_by_axes([min(32, max(14, size)), weight])
    return f


_probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))


def wrap(text, font, width):
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(), ""
        for w in words:
            t = (cur + " " + w).strip()
            if _probe.textlength(t, font=font) <= width:
                cur = t
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def block(d, x, y, text, font, fill, width, lh):
    for ln in wrap(text, font, width):
        d.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y


def fit(text, width, max_lines, sizes, italic=False):
    """Largest serif size whose wrap fits in max_lines."""
    for s in sizes:
        if len(wrap(text, serif(s, italic), width)) <= max_lines:
            return s
    return sizes[-1]


def frame(dark, n, total, margin=M):
    bg, fg = (INK, CREAM) if dark else (CREAM, INK)
    im = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(im)
    d.text((margin, 80), "UNLIKELY LESSONS", font=sans(24, 600), fill=OCHRE)
    pg = f"{n:02d} / {total:02d}"
    f = sans(24, 500)
    d.text((W - margin - d.textlength(pg, font=f), 80), pg, font=f, fill=MUTED_DARK if dark else MUTED)
    return im, d, fg


def swipe(d, fg, margin=M):
    f = sans(26, 500)
    t = "swipe  →"
    d.text((W - margin - d.textlength(t, font=f), H - 120), t, font=f, fill=fg)


def rule(d, x, y):
    d.rectangle([x, y, x + 90, y + 6], fill=OCHRE)


def cover(s, n, total):
    im, d, _ = frame(True, n, total, SAFE)
    width = W - 2 * SAFE
    ts = fit(s["title"], width, 5, [92, 84, 76, 68])
    tl = wrap(s["title"], serif(ts), width)
    acc = s.get("accent", "")
    al = wrap(acc, serif(ts, True), width) if acc else []
    lh = int(ts * 1.13)
    hgt = (len(tl) + len(al)) * lh + (20 if al else 0) + (110 if s.get("sub") else 0)
    y = max(220, (H - hgt) // 2 - 30)
    for ln in tl:
        d.text((SAFE, y), ln, font=serif(ts), fill=CREAM)
        y += lh
    if al:
        y += 20
        for ln in al:
            d.text((SAFE, y), ln, font=serif(ts, True), fill=OCHRE)
            y += lh
    if s.get("sub"):
        y += 50
        d.text((SAFE, y), s["sub"], font=sans(40, 500), fill=CREAM)
    swipe(d, CREAM, SAFE)
    return im


def text(s, n, total, extra_h=0):
    im, d, _ = frame(False, n, total)
    width = W - 2 * M
    kf, bf = serif(80), sans(44, 400)
    hk = len(wrap(s["kicker"], kf, width)) * 92 + 106 if s.get("kicker") else 0
    hb = len(wrap(s.get("body", ""), bf, width)) * 64 if s.get("body") else 0
    y = max(200, (H - hk - hb - extra_h) // 2 - 20)
    if s.get("kicker"):
        y = block(d, M, y, s["kicker"], kf, INK, width, 92) + 40
        rule(d, M, y)
        y += 60
    return im, d, y


def plain(s, n, total):
    im, d, y = text(s, n, total)
    block(d, M, y, s.get("body", ""), sans(44, 400), INK, W - 2 * M, 64)
    swipe(d, INK)
    return im


def diagram(s, n, total, base):
    im, d, _ = frame(False, n, total)
    width = W - 2 * M
    y = 190
    if s.get("kicker"):
        y = block(d, M, y, s["kicker"], serif(72), INK, width, 84) + 30
        rule(d, M, y)
        y += 50
    body = s.get("body", "")
    bh = len(wrap(body, sans(42, 400), width)) * 60 if body else 0
    box = (M, y + 20, W - M, H - 160 - bh - 40)
    kit = dict(CREAM=CREAM, INK=INK, OCHRE=OCHRE, WATER=WATER, MUTED=MUTED, W=W, H=H, M=M,
               serif=serif, sans=sans, wrap=wrap, block=block)
    runpy.run_path(os.path.join(base, s["script"]))["draw"](d, box, kit)
    if body:
        block(d, M, H - 160 - bh, body, sans(42, 400), INK, width, 60)
    swipe(d, INK)
    return im


def moral(s, n, total):
    im, d, _ = frame(True, n, total)
    width = W - 2 * M
    sz = fit(s["lead"] + " " + s.get("accent", ""), width, 9, [80, 72, 64])
    lh = int(sz * 1.18)
    n1 = len(wrap(s["lead"], serif(sz), width))
    n2 = len(wrap(s.get("accent", ""), serif(sz, True), width)) if s.get("accent") else 0
    y = max(220, (H - (n1 + n2) * lh - 120) // 2)
    d.text((M, y), "THE LESSON", font=sans(28, 700), fill=OCHRE)
    y = block(d, M, y + 80, s["lead"], serif(sz), CREAM, width, lh) + 40
    if s.get("accent"):
        block(d, M, y, s["accent"], serif(sz, True), OCHRE, width, lh)
    swipe(d, CREAM)
    return im


def cta(s, n, total):
    im, d, _ = frame(False, n, total)
    y = block(d, M, 340, "One unlikely story.\nOne lesson.\nEvery day.", serif(92), INK, W - 2 * M, 112) + 60
    rule(d, M, y)
    y += 60
    d.text((M, y), "Follow @unlikely.lessons", font=sans(40, 600), fill=INK)
    d.text((M, y + 66), s.get("line", "Save this for later."), font=sans(32, 400), fill=MUTED)
    return im


def main(path):
    base = os.path.dirname(os.path.abspath(path))
    spec = json.load(open(path))
    slides = spec["slides"]
    total = len(slides)
    assert 2 <= total <= 10, "Instagram carousels need 2-10 slides"
    for i, s in enumerate(slides, 1):
        t = s["type"]
        if t == "cover":
            im = cover(s, i, total)
        elif t == "text":
            im = plain(s, i, total)
        elif t == "diagram":
            im = diagram(s, i, total, base)
        elif t == "moral":
            im = moral(s, i, total)
        elif t == "cta":
            im = cta(s, i, total)
        else:
            raise ValueError(t)
        out = os.path.join(base, f"slide_{i:02d}.jpg")
        im.save(out, quality=92)
        print(out)


if __name__ == "__main__":
    main(sys.argv[1])

"""Render a 1080x1920 Instagram story teaser from a post's cover slide.

Usage:  python3 tools/story.py posts/2026-11-02/post.json
Writes story.jpg next to post.json. Keeps text clear of the story UI
(top ~250px, bottom ~340px). Stories can't carry links via the API, so the
footer points people to the profile.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw  # noqa: E402
from render import CREAM, INK, OCHRE, MUTED_DARK, serif, sans, wrap, fit  # noqa: E402

SW, SH, SM = 1080, 1920, 110


def main(path):
    base = os.path.dirname(os.path.abspath(path))
    spec = json.load(open(path))
    c = next(s for s in spec["slides"] if s["type"] == "cover")
    im = Image.new("RGB", (SW, SH), INK)
    d = ImageDraw.Draw(im)
    width = SW - 2 * SM
    d.text((SM, 300), "NEW POST", font=sans(30, 700), fill=OCHRE)
    ts = fit(c["title"], width, 6, [104, 96, 88, 80, 72])
    lh = int(ts * 1.13)
    tl = wrap(c["title"], serif(ts), width)
    al = wrap(c.get("accent", ""), serif(ts, True), width) if c.get("accent") else []
    hgt = (len(tl) + len(al)) * lh + (24 if al else 0)
    y = max(400, (SH - hgt) // 2 - 60)
    for ln in tl:
        d.text((SM, y), ln, font=serif(ts), fill=CREAM)
        y += lh
    if al:
        y += 24
        for ln in al:
            d.text((SM, y), ln, font=serif(ts, True), fill=OCHRE)
            y += lh
    if c.get("sub"):
        d.text((SM, y + 50), c["sub"], font=sans(42, 500), fill=CREAM)
    d.rectangle([SM, SH - 470, SM + 90, SH - 464], fill=OCHRE)
    d.text((SM, SH - 440), "The full story is on the feed.", font=sans(38, 600), fill=CREAM)
    d.text((SM, SH - 385), "@unlikely.lessons", font=sans(34, 500), fill=MUTED_DARK)
    out = os.path.join(base, "story.jpg")
    im.save(out, quality=92)
    print(out)


if __name__ == "__main__":
    main(sys.argv[1])

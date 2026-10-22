# Unlikely Lessons — media

Public image host for the Instagram account @unlikely.lessons.
Instagram's publishing API needs public image URLs, so each day's slides are pushed
here, published via the Windsor.ai Instagram connector, and then removed.

- `tools/render.py` — renders a carousel from `posts/<date>/post.json` (see docstring).
- `fonts/` — DM Serif Display, Inter (SIL Open Font License).
- `posts/<date>/` — one folder per post: `post.json`, optional `diagram.py`, `slide_XX.jpg`.
- `log.md` — one line per published post (date | topic | title), used to avoid repeats.

Style: cream #F3EEE3, ink #1B2430, ochre #C8862A, 1080×1350 JPEG.
Slide flow: cover (hook) → 4–6 story slides → THE LESSON (generalised moral) → CTA.

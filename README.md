### Lecture notes of the 2023 fall semester edition of the CS-433 EPFL Machine Learning course.

[Link to the website](https://yannickdetrois.github.io/ML2023_notes/)

#### Layout

- `notes/` — one Markdown file per chapter (the source of truth). Math is TeX in `$…$` / `$$…$$`; Notion's text colors are kept as `<span class="c-red">` etc.
- `images/` — figures referenced from the notes.
- `index.html` — generated page served by GitHub Pages. Don't edit it by hand; run `npm install && npm run build`.
- `scripts/convert_notion.py` — the one-off converter that produced `notes/` from `notion-export/` (the original Notion export, kept for reference).

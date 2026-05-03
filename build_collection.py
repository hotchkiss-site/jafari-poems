#!/usr/bin/env python3
"""
build_collection.py — render all .poem files in a folder to one HTML file.
Sorted by page_number. Includes a table of contents with first lines and dates.

Usage: python build_collection.py poems/
Output: index.html (or pass --out to specify)
Command while in folder: python build_collection.py poems/
"""

import sys
import argparse
import re
from pathlib import Path


CSS = """
    *, *::before, *::after { box-sizing: border-box; }

    body {
      background: #f5f0e8;
      color: #2a1f14;
      font-family: 'Crimson Text', serif;
      font-size: 1.31rem;
      margin: 0;
      padding: 2rem 1rem 4rem;
    }

    .page {
      max-width: 900px;
      margin: 0 auto;
    }

    .book-header {
      text-align: center;
      margin-bottom: 3rem;
      padding-bottom: 2rem;
      border-bottom: 2px solid #c9843a;
    }

    .book-title-persian {
      font-size: 2.5rem;
      font-weight: 700;
      direction: rtl;
      margin: 0 0 0.4rem;
    }

    .book-title-english {
      font-size: 1.63rem;
      font-style: italic;
      color: #6b5240;
      margin: 0 0 0.6rem;
    }

    .book-author {
      font-size: 1.25rem;
      color: #9c7f60;
      letter-spacing: 0.05em;
    }

    .toc-wrapper {
      width: 100%;
      background: #f5f0e8;
      padding: 0 2rem 3.5rem;
      margin-bottom: 3.5rem;
    }

    .toc {
      max-width: 1400px;
      margin: 0 auto;
    }

    .toc-title {
      font-size: 1.75rem;
      font-weight: 600;
      color: #2a1f14;
      text-align: center;
      display: block;
      margin-bottom: 1.8rem;
      padding-bottom: 0.8rem;
      border-bottom: 2px solid #c9843a;
      letter-spacing: 0.04em;
    }

    .toc-table {
      width: 100%;
      border-collapse: collapse;
    }

    .toc-table tr {
      border-bottom: 1px solid #e8dfc8;
      position: relative;
      cursor: pointer;
    }

    .toc-table tr:last-child {
      border-bottom: none;
    }

    .toc-table tr:hover {
      background: rgba(201, 132, 58, 0.06);
    }

    .toc-table td {
      padding: 0.55rem 0.4rem;
      vertical-align: top;
    }

    .toc-row-link {
      position: absolute;
      inset: 0;
      z-index: 0;
    }

    .toc-table td > * {
      position: relative;
      z-index: 1;
    }

    /* TOC three-column layout */
    .toc-col-english { width: 40%; }
    .toc-col-dates   { width: 20%; }
    .toc-col-persian { width: 40%; }

    .toc-table th {
      font-variant: small-caps;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      font-size: 0.94rem;
      color: #b8923a;
      font-weight: normal;
      padding: 0 0.4rem 0.6rem;
      border-bottom: 1px solid #ddd0b8;
    }

    /* header row doesn't get hover or pointer */
    .toc-table tr.toc-header {
      cursor: default;
      border-bottom: none;
    }
    .toc-table tr.toc-header:hover {
      background: none;
    }

    .toc-english-row {
      display: flex;
      align-items: flex-start;
      gap: 0.8rem;
    }

    .toc-page-num {
      font-size: 1.13rem;
      color: #9c7f60;
      white-space: nowrap;
      padding-top: 0.1rem;
      flex-shrink: 0;
      min-width: 1.8rem;
      text-align: right;
    }

    .toc-english-text {
      flex: 1;
    }

    .toc-english-title {
      color: #2a1f14;
      font-size: 1.25rem;
    }

    .toc-first-line {
      font-size: 1.1rem;
      font-style: italic;
      color: #7a6050;
      margin-top: 0.1rem;
    }

    /* center column: two sub-cells side by side */
    .toc-dates-inner {
      display: flex;
      justify-content: space-between;
      gap: 0.5rem;
      font-size: 1.13rem;
      color: #9c7f60;
    }

    /* persian column */
    .toc-persian-col {
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      direction: rtl;
      gap: 1.2rem;
    }

    .toc-persian-text {
      flex: 1;
      text-align: right;
    }

    .toc-persian-title-text {
      font-size: 1.25rem;
      color: #4a3525;
    }

    .toc-persian-first-line {
      font-size: 1.06rem;
      font-style: italic;
      color: #7a6050;
      margin-top: 0.1rem;
    }

    .toc-persian-page {
      font-size: 1.13rem;
      color: #9c7f60;
      white-space: nowrap;
      padding-right: 1.2rem;
      padding-left: 0.3rem;
      direction: ltr;
      flex-shrink: 0;
      min-width: 2.2rem;
      text-align: left;
    }

    .poem-section {
      margin-bottom: 4rem;
    }

    .poem-section + .poem-section {
      border-top: 1px solid #ddd0b8;
      padding-top: 3rem;
    }

    .poem-header {
      text-align: center;
      margin-bottom: 2rem;
    }

    .poem-header-persian {
      font-size: 2rem;
      font-weight: 700;
      direction: rtl;
      margin: 0 0 0.3rem;
    }

    .poem-header-english {
      font-size: 1.44rem;
      font-style: italic;
      color: #6b5240;
      margin: 0 0 0.4rem;
    }

    .poem-header-meta {
      font-size: 1.1rem;
      color: #9c7f60;
      letter-spacing: 0.04em;
    }

    .pair {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.5rem;
      padding: 1.8rem 0;
    }

    .persian {
      direction: rtl;
      font-size: 1.44rem;
      line-height: 2;
      border-right: 3px solid #c9843a;
      padding-right: 1.2rem;
    }

    .english {
      direction: ltr;
      font-size: 1.31rem;
      line-height: 1.9;
      border-left: 3px solid #8aab72;
      padding-left: 1.2rem;
    }

    .poem-block {
      background: rgba(255,255,255,0.45);
      border-radius: 6px;
      padding: 1rem 1.2rem;
    }

    .poem-block.persian-poem {
      text-align: right;
      font-size: 1.38rem;
      line-height: 2.2;
    }

    .poem-block.english-poem {
      font-style: italic;
      font-size: 1.25rem;
      line-height: 2.1;
    }

    .poem-block p {
      margin: 0;
      white-space: pre-wrap;
    }

    .label {
      font-variant: small-caps;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      font-size: 0.98rem;
      color: #b8923a;
      margin-bottom: 0.7rem;
      display: block;
    }

    .footnotes {
      margin-top: 1.5rem;
      padding-top: 1rem;
      border-top: 1px solid #ddd0b8;
      font-size: 1.15rem;
      color: #5a4432;
      line-height: 1.7;
    }

    .footnotes p {
      margin: 0.3rem 0;
      white-space: pre-wrap;
    }

    @media (max-width: 640px) {
      .pair {
        grid-template-columns: 1fr;
        gap: 1.2rem;
      }
      .persian {
        border-right: none;
        border-bottom: 3px solid #c9843a;
        padding-right: 0;
        padding-bottom: 1rem;
      }
      .english {
        border-left: none;
        border-top: 3px solid #8aab72;
        padding-left: 0;
        padding-top: 1rem;
      }
    }
"""


def parse_poem(text):
    poem = {}
    current_section = None
    current_lines = []

    def flush():
        if current_section:
            poem[current_section] = "\n".join(current_lines).strip()

    for line in text.splitlines():
        m = re.match(r'^===(\w+)===$', line.strip())
        if m:
            flush()
            current_section = m.group(1)
            current_lines = []
        elif current_section is None:
            if ':' in line:
                key, _, val = line.partition(':')
                poem[key.strip()] = val.strip()
        else:
            current_lines.append(line)

    flush()
    return poem


def extract_year(date_string):
    """Pull a 4-digit year from a string like 'Autumn 1989' or '1959'."""
    if not date_string:
        return None
    m = re.search(r'\b(1[0-9]{3}|20[0-9]{2})\b', str(date_string))
    return int(m.group(1)) if m else None


def meta_line(poem):
    parts = []
    if poem.get("date_written"):
        parts.append(str(poem["date_written"]))
    if poem.get("page_number"):
        parts.append("p.\u00a0" + poem["page_number"])
    if poem.get("date_translated"):
        parts.append("translated " + str(poem["date_translated"]))
    return " \u00b7 ".join(parts)


def first_line(text):
    if not text:
        return ""
    for line in text.splitlines():
        line = line.strip()
        if line:
            return line
    return ""


def render_toc(poems):
    header = (
        '<tr class="toc-header">'
        '<th class="toc-col-english" style="text-align:left;">Page &amp; Title</th>'
        '<th class="toc-col-dates" style="text-align:left;">Translated'
        '<span style="float:right;">Written</span></th>'
        '<th class="toc-col-persian" style="display:flex;justify-content:space-between;">'
        '<span style="direction:rtl;">عنوان</span>'
        '<span>صفحه</span>'
        '</th>'
        '</tr>'
    )

    rows = []
    for p in poems:
        poem_id       = p.get("id", "")
        page          = str(p.get("page_number", ""))
        persian_page  = str(p.get("persian_page_number", ""))
        date_written  = str(p.get("date_written", ""))
        date_trans    = str(p.get("date_translated", ""))
        english_title = p.get("english_title", "")
        persian_title = p.get("persian_title", "")
        fl_en         = first_line(p.get("translation", ""))
        fl_fa         = first_line(p.get("persian", ""))

        onclick = 'onclick="location.href=\'' + '#' + poem_id + '\'"'

        # Left column: page number left, title + first line stacked beside it
        col_english = (
            f'<td class="toc-col-english">'
            f'<div class="toc-english-row">'
            f'<span class="toc-page-num">{page}</span>'
            f'<div class="toc-english-text">'
            f'<div class="toc-english-title">{english_title}</div>'
            f'<div class="toc-first-line">{fl_en}</div>'
            f'</div>'
            f'</div>'
            f'</td>'
        )

        # Center column: translated (left) · written (right)
        col_dates = (
            f'<td class="toc-col-dates">'
            f'<div class="toc-dates-inner">'
            f'<span>{date_trans}</span>'
            f'<span>{date_written}</span>'
            f'</div>'
            f'</td>'
        )

        # Right column: persian title + first line (RTL), persian page number
        col_persian = (
            f'<td class="toc-col-persian">'
            f'<div class="toc-persian-col">'
            f'<span class="toc-persian-page">{persian_page}</span>'
            f'<div class="toc-persian-text">'
            f'<div class="toc-persian-title-text">{persian_title}</div>'
            f'<div class="toc-persian-first-line">{fl_fa}</div>'
            f'</div>'
            f'</div>'
            f'</td>'
        )

        rows.append(f"<tr {onclick}>{col_english}{col_dates}{col_persian}</tr>")

    return (
        '<div class="toc">'
        '<span class="toc-title">Poems — اشعار</span>'
        '<table class="toc-table">'
        + header
        + "".join(rows)
        + "</table></div>"
    )


def render_poem_section(poem):
    footnotes_html = ""
    if poem.get("footnotes"):
        footnotes_html = (
            '<div class="footnotes">'
            '<span class="label">Translator\'s Notes</span>'
            "<p>" + poem["footnotes"] + "</p>"
            "</div>"
        )

    return (
        f'<div class="poem-section" id="{poem.get("id", "")}">'
        '<div class="poem-header">'
        f'<p class="poem-header-persian">{poem.get("persian_title", "")}</p>'
        f'<p class="poem-header-english">{poem.get("english_title", "")}</p>'
        f'<p class="poem-header-meta">{meta_line(poem)}</p>'
        "</div>"
        '<div class="pair">'
        '<div class="persian">'
        '<span class="label">\u0645\u062a\u0646 \u0627\u0635\u0644\u06cc</span>'
        '<div class="poem-block persian-poem"><p>' + poem.get("persian", "") + "</p></div>"
        "</div>"
        '<div class="english">'
        '<span class="label">Translation</span>'
        '<div class="poem-block english-poem"><p>' + poem.get("translation", "") + "</p></div>"
        "</div>"
        "</div>"
        + footnotes_html
        + "</div>"
    )


def render_collection(poems, book_persian, book_english, author):
    toc = render_toc(poems)
    sections = "\n".join(render_poem_section(p) for p in poems)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{book_english} \u2014 {author}</title>
  <link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
  <style>
{CSS}
  </style>
</head>
<body>
<div class="page">
  <div class="book-header">
    <p class="book-title-persian">{book_persian}</p>
    <p class="book-title-english">{book_english}</p>
    <p class="book-author">{author}</p>
  </div>
</div>

<div class="toc-wrapper">
  {toc}
</div>

<div class="page">
  {sections}
</div>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(description="Render all .poem files in a folder to one HTML.")
    parser.add_argument("folder", help="Path to folder containing .poem files")
    parser.add_argument("--out", default="index.html", help="Output HTML path")
    parser.add_argument("--book-persian", default="\u0628\u0648\u06cc \u06a9\u0627\u0647\u06af\u0644 \u0648 \u0622\u0648\u0627\u0632 \u067e\u0631\u0646\u062f\u0647")
    parser.add_argument("--book-english", default="The Smell of Adobe and Birdsong")
    parser.add_argument("--author", default="Mohammad Ebrahim Jafari")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.is_dir():
        print(f"Error: {folder} is not a directory.")
        sys.exit(1)

    poem_files = sorted(folder.glob("*.poem"))
    if not poem_files:
        print(f"No .poem files found in {folder}.")
        sys.exit(1)

    poems = [parse_poem(f.read_text(encoding="utf-8")) for f in poem_files]

    def sort_key(p):
        pn = p.get("page_number")
        try:
            return (0, int(pn))
        except (TypeError, ValueError):
            return (1, 0)

    poems.sort(key=sort_key)

    html = render_collection(poems, args.book_persian, args.book_english, args.author)

    out_path = Path(args.out)
    out_path.write_text(html, encoding="utf-8")
    print(f"Written: {out_path} ({len(poems)} poem{'s' if len(poems) != 1 else ''})")


if __name__ == "__main__":
    main()

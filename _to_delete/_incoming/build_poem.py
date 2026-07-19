#!/usr/bin/env python3
"""
build_poem.py — render a single poem to a styled HTML page.
Usage: python build_poem.py ancient-tree
       python build_poem.py ancient-tree --poems poems/
Output: ancient-tree.html (or pass --out to specify)

Reads from:
    poems/<id>.poem  — self-contained: ===meta=== TOML + ===section=== text blocks
"""

import sys
import argparse
import re
from pathlib import Path


HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{english_title} — Mohammad Ebrahim Jafari</title>
  <link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; }}

    body {{
      background: #f5f0e8;
      color: #2a1f14;
      font-family: 'Crimson Text', serif;
      font-size: 1.05rem;
      margin: 0;
      padding: 2rem 1rem 4rem;
    }}

    .page {{
      max-width: 900px;
      margin: 0 auto;
    }}

    header {{
      text-align: center;
      margin-bottom: 2.5rem;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid #ddd0b8;
    }}

    .header-persian {{
      font-size: 1.8rem;
      font-weight: 700;
      direction: rtl;
      margin: 0 0 0.3rem;
      color: #2a1f14;
    }}

    .header-english {{
      font-size: 1.2rem;
      font-style: italic;
      color: #6b5240;
      margin: 0 0 0.5rem;
    }}

    .header-meta {{
      font-size: 0.9rem;
      color: #9c7f60;
      letter-spacing: 0.04em;
    }}

    .pair {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.5rem;
      padding: 1.8rem 0;
      border-bottom: 1px solid #ddd0b8;
    }}

    .pair:last-of-type {{
      border-bottom: none;
    }}

    .persian {{
      direction: rtl;
      font-size: 1.15rem;
      line-height: 2;
      border-right: 3px solid #c9843a;
      padding-right: 1.2rem;
    }}

    .english {{
      direction: ltr;
      font-size: 1.05rem;
      line-height: 1.9;
      border-left: 3px solid #8aab72;
      padding-left: 1.2rem;
    }}

    .poem-block {{
      background: rgba(255,255,255,0.45);
      border-radius: 6px;
      padding: 1rem 1.2rem;
    }}

    .poem-block.persian-poem {{
      text-align: right;
      font-size: 1.1rem;
      line-height: 2.2;
    }}

    .poem-block.english-poem {{
      font-style: italic;
      font-size: 1rem;
      line-height: 2.1;
    }}

    .poem-block p {{
      margin: 0;
      white-space: pre-wrap;
    }}

    .label {{
      font-variant: small-caps;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      font-size: 0.78rem;
      color: #b8923a;
      margin-bottom: 0.7rem;
      display: block;
    }}

    .footnotes {{
      margin-top: 2.5rem;
      padding-top: 1.2rem;
      border-top: 1px solid #ddd0b8;
      font-size: 0.92rem;
      color: #5a4432;
      line-height: 1.7;
    }}

    .footnotes p {{
      margin: 0.3rem 0;
      white-space: pre-wrap;
    }}

    @media (max-width: 640px) {{
      .pair {{
        grid-template-columns: 1fr;
        gap: 1.2rem;
      }}
      .persian {{
        border-right: none;
        border-bottom: 3px solid #c9843a;
        padding-right: 0;
        padding-bottom: 1rem;
      }}
      .english {{
        border-left: none;
        border-top: 3px solid #8aab72;
        padding-left: 0;
        padding-top: 1rem;
      }}
    }}
  </style>
</head>
<body>
<div class="page">

  <header>
    <p class="header-persian">{persian_title}</p>
    <p class="header-english">{english_title}</p>
    <p class="header-meta">{meta_line}</p>
  </header>

  <div class="pair">
    <div class="persian">
      <span class="label">متن اصلی</span>
      <div class="poem-block persian-poem"><p>{persian}</p></div>
    </div>
    <div class="english">
      <span class="label">Translation</span>
      <div class="poem-block english-poem"><p>{translation}</p></div>
    </div>
  </div>

{footnotes_block}

</div>
</body>
</html>
"""

FOOTNOTES_BLOCK = """\
  <div class="footnotes">
    <span class="label">Translator's Notes</span>
    <p>{footnotes}</p>
  </div>
"""


def parse_toml(text: str) -> dict:
    """Parse a flat TOML file with string values and string arrays."""
    result = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '=' not in line:
            continue
        key, _, val = line.partition('=')
        key = key.strip()
        val = val.strip()
        if val.startswith('[') and val.endswith(']'):
            result[key] = re.findall(r'"([^"]*)"', val)
        elif val.startswith('"') and val.endswith('"'):
            result[key] = val[1:-1]
        elif val.lstrip('-').isdigit():
            result[key] = int(val)
        else:
            result[key] = val
    return result


def parse_sections(text: str) -> dict:
    """Parse ===section=== blocks from a .poem file."""
    sections = {}
    current_section = None
    current_lines = []

    def flush():
        if current_section:
            sections[current_section] = "\n".join(current_lines).strip()

    for line in text.splitlines():
        m = re.match(r'^===(\w+)===$', line.strip())
        if m:
            flush()
            current_section = m.group(1)
            current_lines = []
        elif current_section is not None:
            current_lines.append(line)
    flush()
    return sections


def load_poem(poem_id: str, poems_dir: Path) -> dict:
    """Parse the self-contained poems/<id>.poem: ===meta=== TOML + text sections."""
    poem_path = poems_dir / f"{poem_id}.poem"
    if not poem_path.exists():
        print(f"Error: {poem_path} not found.")
        sys.exit(1)
    sections = parse_sections(poem_path.read_text(encoding="utf-8"))
    poem = parse_toml(sections.pop("meta", ""))
    poem["id"] = poem_id
    poem.update(sections)
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
    parts.append("Mohammad Ebrahim Jafari")
    if poem.get("date_translated"):
        parts.append("translated " + str(poem["date_translated"]))
    return " \u00b7 ".join(parts)


def render_poem(poem):
    footnotes_block = ""
    if poem.get("footnotes"):
        footnotes_block = FOOTNOTES_BLOCK.format(footnotes=poem["footnotes"])

    return HTML_TEMPLATE.format(
        persian_title=poem.get("persian_title", ""),
        english_title=poem.get("english_title", ""),
        meta_line=meta_line(poem),
        persian=poem.get("persian", ""),
        translation=poem.get("translation", ""),
        footnotes_block=footnotes_block,
    )


def main():
    parser = argparse.ArgumentParser(description="Render a single poem to HTML.")
    parser.add_argument("id", help="Poem ID / slug (e.g. ancient-tree)")
    parser.add_argument("--poems", default="poems", help="Path to poems/ folder (default: poems)")
    parser.add_argument("--out", help="Output HTML path (default: <id>.html)")
    args = parser.parse_args()

    poem = load_poem(args.id, Path(args.poems))
    html = render_poem(poem)

    out_path = Path(args.out) if args.out else Path(args.id + ".html")
    out_path.write_text(html, encoding="utf-8")
    print(f"Written: {out_path}")


if __name__ == "__main__":
    main()

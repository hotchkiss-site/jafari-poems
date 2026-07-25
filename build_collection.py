#!/usr/bin/env python3
"""
build_collection.py — render all .poem files in a folder to one HTML file.
Sorted by page_number. Includes a table of contents with first lines and dates.

Each .poem file is self-contained: a ===meta=== TOML section followed by the
text sections (===persian===, ===machine===, ===lantern===, ===translation===,
===footnotes===). There is no separate meta/ directory.

Usage: python build_collection.py poems/
Output: index.html (or pass --out to specify)
Command while in folder: python build_collection.py poems/
"""

import sys
import argparse
import re
from pathlib import Path


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
        elif val in ('true', 'false'):
            result[key] = (val == 'true')
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


def load_poem(poem_path: Path) -> dict:
    """Parse a self-contained .poem file: ===meta=== TOML + text sections.

    The metadata fields come from the ===meta=== section (flat TOML); every
    other ===section=== is attached as a text field. Text sections win on a
    key collision, matching the old meta/ + poems/ merge order.
    """
    sections = parse_sections(poem_path.read_text(encoding="utf-8"))
    poem = parse_toml(sections.pop("meta", ""))
    if poem.get("id", poem_path.stem) != poem_path.stem:
        print(f"Warning: meta id '{poem.get('id')}' != filename stem "
              f"'{poem_path.stem}' in {poem_path} — using the filename.")
    poem["id"] = poem_path.stem
    poem.update(sections)
    return poem


def load_preface_section(path: Path) -> dict:
    """Parse a preface/*.html fragment: a <!--meta ... --> header + HTML body.

    The meta header holds the bilingual section labels and date that drive the
    section heading. The body is verbatim HTML (the .pair / .signature blocks),
    rendered as-is inside the namespaced .preface container.
    """
    text = path.read_text(encoding="utf-8")
    meta = {}
    body = text

    m = re.search(r"<!--\s*meta\s*(.*?)-->", text, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            line = line.strip()
            if not line or ":" not in line:
                continue
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip()
        body = text[m.end():]

    return {
        "stem": path.stem,
        "label_fa": meta.get("label_fa", ""),
        "label_en": meta.get("label_en", ""),
        "date": meta.get("date", ""),
        "body": body.strip(),
    }


def load_preface(preface_dir: Path) -> list:
    """Load all preface/*.html fragments, ordered by filename (NN- prefix)."""
    if not preface_dir.is_dir():
        return []
    return [load_preface_section(f) for f in sorted(preface_dir.glob("*.html"))]


CSS = """
    *, *::before, *::after { box-sizing: border-box; }

    /* ── illumination tokens (unwan carpet) ── */
    :root {
      --lapis: #24407e;
      --gold: #cfa64b;
      --gold-line: rgba(207, 166, 75, 0.4);
      --gold-faint: rgba(207, 166, 75, 0.22);
      --lapis-cream: #e9dcc0;
      --lapis-muted: #a9b7d8;
      --lapis-slug: #7d8db4;
    }

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

    /* ── the unwan carpet: lapis field holding header + tabs (and, on the
       Poems tab, extending through the TOC below it) ── */
    .carpet {
      position: relative;
      background: var(--lapis);
      padding: 2.8rem 1rem 0.8rem;
      margin-bottom: 2.5rem;
    }

    body.poems-open .carpet {
      margin-bottom: 0;
      padding-bottom: 0.2rem;
    }

    .corner {
      position: absolute;
      width: min(9vw, 84px);
      height: min(9vw, 84px);
      background: var(--gold);
      opacity: 0.92;
      pointer-events: none;
      -webkit-mask: __CORNER_MASK__ center / contain no-repeat;
              mask: __CORNER_MASK__ center / contain no-repeat;
    }

    .c-tl { top: 10px; left: 10px; }
    .c-tr { top: 10px; right: 10px; transform: scaleX(-1); }
    .c-bl { bottom: 10px; left: 10px; transform: scaleY(-1); }
    .c-br { bottom: 10px; right: 10px; transform: scale(-1, -1); }

    /* when the carpet continues into the poems TOC, its own bottom pair
       yields to the pair at the TOC's foot */
    body.poems-open .carpet .carpet-close { display: none; }

    @media (max-width: 900px) {
      .c-bl, .c-br { display: none; }
    }

    .book-header {
      text-align: center;
      margin: 0 auto;
      max-width: 900px;
      padding-bottom: 1.8rem;
    }

    .book-title-persian {
      font-size: 2.5rem;
      font-weight: 700;
      direction: rtl;
      margin: 0 0 0.4rem;
      color: var(--gold);
    }

    .book-title-english {
      font-size: 1.63rem;
      font-style: italic;
      color: var(--lapis-cream);
      margin: 0 0 0.6rem;
    }

    .book-author {
      font-size: 1.25rem;
      color: var(--lapis-muted);
      letter-spacing: 0.05em;
    }

    .toc-wrapper {
      width: 100%;
      background: #f5f0e8;
      padding: 0 2rem 3.5rem;
      margin-bottom: 3.5rem;
    }

    /* ── poems TOC: the carpet continues (drafts TOC stays cream — only the
       finished book is illuminated) ── */
    #tab-poems .toc-wrapper {
      position: relative;
      background: var(--lapis);
      padding-top: 0.2rem;
      margin-top: 0;
    }

    /* dogmoj dash opens the table in place of a repeated "Poems" title */
    .toc-rule {
      width: min(300px, 55%);
      aspect-ratio: 16;
      margin: 1.6rem auto 1.5rem;
      background: var(--gold);
      opacity: 0.85;
      -webkit-mask: __RULE_MASK__ center / contain no-repeat;
              mask: __RULE_MASK__ center / contain no-repeat;
    }

    #tab-poems .toc-table tr { border-bottom-color: var(--gold-faint); }
    #tab-poems .toc-table tr:hover { background: rgba(207, 166, 75, 0.08); }
    #tab-poems .toc-table tr.toc-header:hover { background: none; }
    #tab-poems .toc-table th { color: var(--gold); border-bottom-color: var(--gold-line); }
    #tab-poems .toc-english-title { color: var(--lapis-cream); }
    #tab-poems .toc-first-line,
    #tab-poems .toc-persian-first-line { color: var(--lapis-muted); }
    #tab-poems .toc-slug { color: var(--lapis-slug); }
    #tab-poems .toc-page-num,
    #tab-poems .toc-persian-page,
    #tab-poems .toc-dates-inner { color: var(--lapis-muted); }
    #tab-poems .toc-persian-title-text { color: var(--lapis-cream); }

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
      table-layout: fixed;
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

    /* slug = filename stem / anchor, shown under the title in the TOC */
    .toc-slug {
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 0.82rem;
      color: #b3a78f;
      letter-spacing: 0.02em;
      margin-top: 0.2rem;
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

    /* File handle: the poem's id == filename stem (poems/<id>.poem, meta/<id>.toml)
       and the anchor (#<id>). Shown muted/monospace so it reads as a handle, not
       part of the poem. */
    .poem-header-slug {
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 0.92rem;
      color: #b0a48f;
      letter-spacing: 0.02em;
      margin: 0.35rem 0 0;
    }

    .poem-status {
      display: inline-block;
      margin-top: 0.6rem;
      font-variant: small-caps;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      font-size: 0.85rem;
      padding: 0.15rem 0.7rem;
      border-radius: 1rem;
      border: 1px solid currentColor;
    }

    .poem-status.is-rendered {
      color: #5e7a4a;
    }

    .poem-status.is-draft {
      color: #b8702a;
    }

    .drafts-note {
      max-width: 900px;
      margin: 0 auto 2rem;
      padding: 0 2rem;
      font-size: 1.1rem;
      font-style: italic;
      color: #7a6050;
      text-align: center;
    }

    /* ── Draft layer toggles (Drafts tab only) ──────────── */
    .layer-badges {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-top: 0.7rem;
    }

    .layer-badge {
      font-family: inherit;
      font-variant: small-caps;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      font-size: 0.85rem;
      padding: 0.15rem 0.85rem;
      border-radius: 1rem;
      border: 1px solid #b8702a;
      color: #b8702a;
      background: transparent;
      cursor: pointer;
      transition: background 0.15s, color 0.15s;
    }

    .layer-badge:hover {
      background: rgba(184,112,42,0.12);
    }

    .layer-badge.is-active {
      background: #b8702a;
      color: #f5f0e8;
    }

    /* Drafts use a full-width canvas: each column keeps a fixed ~single-column
       width so adding a layer adds width rather than compressing line breaks.
       An over-wide poem scrolls horizontally within its own section. */
    #tab-drafts .page {
      max-width: none;
      padding: 0 1.5rem;
    }

    #tab-drafts .poem-section {
      overflow-x: auto;
    }

    #tab-drafts .pair {
      display: flex;
      gap: 2.5rem;
      align-items: flex-start;
      width: max-content;
      margin: 0 auto;
      padding: 1.8rem 0;
    }

    #tab-drafts .persian {
      flex: 0 0 27rem;
    }

    #tab-drafts .english-layers {
      flex: 0 0 auto;
      display: flex;
      gap: 1.5rem;
      align-items: flex-start;
      direction: ltr;
      border-left: 3px solid #8aab72;
      padding-left: 1.2rem;
      min-height: 2rem;
    }

    #tab-drafts .english-layer {
      flex: 0 0 27rem;
      font-size: 1.31rem;
      line-height: 1.9;
    }

    #tab-drafts .english-layer:not(.is-active) {
      display: none;
    }

    .poems .pair {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.5rem;
      padding: 1.8rem 0;
    }

    .poems .persian {
      direction: rtl;
      font-size: 1.44rem;
      line-height: 2;
      border-right: 3px solid #c9843a;
      padding-right: 1.2rem;
    }

    .poems .english {
      direction: ltr;
      font-size: 1.31rem;
      line-height: 1.9;
      border-left: 3px solid #8aab72;
      padding-left: 1.2rem;
    }

    .poems .poem-block {
      background: rgba(255,255,255,0.45);
      border-radius: 6px;
      padding: 1rem 1.2rem;
    }

    .poems .poem-block.persian-poem {
      text-align: right;
      font-size: 1.38rem;
      line-height: 2.2;
    }

    .poems .poem-block.english-poem {
      font-style: italic;
      font-size: 1.25rem;
      line-height: 2.1;
    }

    .poems .poem-block p {
      margin: 0;
      white-space: pre-wrap;
    }

    .poems .label {
      font-variant: small-caps;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      font-size: 0.98rem;
      color: #b8923a;
      margin-bottom: 0.7rem;
      display: block;
    }

    .poems .footnotes {
      margin-top: 1.5rem;
      padding-top: 1rem;
      border-top: 1px solid #ddd0b8;
      font-size: 1.15rem;
      color: #5a4432;
      line-height: 1.7;
    }

    .poems .footnotes p {
      margin: 0.3rem 0;
      white-space: pre-wrap;
    }

    .back-to-toc {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      width: 2.8rem;
      height: 2.8rem;
      background: #c9843a;
      color: #f5f0e8;
      border-radius: 50%;
      display: none;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      font-size: 1.4rem;
      line-height: 1;
      opacity: 0.65;
      transition: opacity 0.2s;
      z-index: 100;
      box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    }

    body.on-poems .back-to-toc {
      display: flex;
    }

    .back-to-toc:hover {
      opacity: 1;
    }

    @media (max-width: 640px) {
      .poems .pair {
        grid-template-columns: 1fr;
        gap: 1.2rem;
      }
      .poems .persian {
        border-right: none;
        border-bottom: 3px solid #c9843a;
        padding-right: 0;
        padding-bottom: 1rem;
      }
      .poems .english {
        border-left: none;
        border-top: 3px solid #8aab72;
        padding-left: 0;
        padding-top: 1rem;
      }
      #tab-drafts .pair {
        flex-direction: column;
        gap: 1.2rem;
        width: auto;
      }
      #tab-drafts .persian,
      #tab-drafts .english-layer {
        flex-basis: auto;
        width: 100%;
      }
      #tab-drafts .english-layers {
        flex-direction: column;
        gap: 1.2rem;
        border-left: none;
        border-top: 3px solid #8aab72;
        padding-left: 0;
        padding-top: 1rem;
      }
    }

    /* ── Tabs: typography only (no ornament on chrome); the active tab is a
       gold cartouche pill echoing the .poem-status badge vocabulary ── */
    .tabs {
      max-width: 700px;
      margin: 0 auto;
      display: flex;
      justify-content: center;
      gap: 0.6rem;
      padding: 0.4rem 0 0.8rem;
    }

    .tab-btn {
      appearance: none;
      background: none;
      border: 1px solid transparent;
      font-family: inherit;
      font-size: 1.18rem;
      color: var(--lapis-muted);
      cursor: pointer;
      padding: 0.32rem 1.15rem;
      border-radius: 1.4rem;
      transition: color 0.15s, border-color 0.15s, background 0.15s;
    }

    .tab-btn:hover {
      color: var(--lapis-cream);
    }

    .tab-btn.active {
      color: var(--gold);
      border-color: var(--gold);
      background: rgba(207, 166, 75, 0.09);
    }

    .tab-btn:focus-visible {
      outline: 2px solid var(--lapis-cream);
      outline-offset: 2px;
    }

    @media (max-width: 640px) {
      .tabs { gap: 0.3rem; }
      .tab-btn { font-size: 1.02rem; padding: 0.26rem 0.8rem; }
    }

    .tab-panel {
      display: none;
    }

    .tab-panel.active {
      display: block;
    }

    /* ── Preface (namespaced; mirrors the standalone intro page) ─ */
    .preface {
      max-width: 900px;
      margin: 0 auto;
      padding: 1rem 1.5rem 4rem;
    }

    .preface .section-break {
      text-align: center;
      margin: 3rem 0 2rem;
    }

    .preface .section-break:first-child {
      margin-top: 0;
    }

    .preface .section-break::before {
      content: '';
      display: block;
      border-top: 1px solid #c9b89a;
      margin-bottom: 1.5rem;
    }

    .preface .section-label-fa {
      font-size: 1.4rem;
      direction: rtl;
      color: #6b4f2f;
      font-weight: bold;
      display: block;
      margin-bottom: 0.2rem;
    }

    .preface .section-label-en {
      font-size: 1.05rem;
      font-style: italic;
      color: #9a7a55;
      letter-spacing: 0.04em;
      display: block;
      margin-bottom: 0.4rem;
    }

    .preface .section-meta {
      font-size: 1rem;
      color: #b0956e;
    }

    .preface .pair {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.5rem;
      margin-bottom: 2.5rem;
      padding-bottom: 2.5rem;
      border-bottom: 1px solid #ddd0b8;
    }

    .preface .pair:last-of-type {
      border-bottom: none;
    }

    .preface .persian {
      direction: rtl;
      font-size: 1.3rem;
      line-height: 2;
      color: #2a1f14;
      border-right: 3px solid #c9843a;
      padding-right: 1.2rem;
    }

    .preface .english {
      direction: ltr;
      font-size: 1.2rem;
      line-height: 1.9;
      color: #3a2e22;
      border-left: 3px solid #8aab72;
      padding-left: 1.2rem;
    }

    .preface .poem-block {
      background: rgba(255,255,255,0.45);
      border-radius: 6px;
      padding: 1rem 1.5rem;
      margin: 1rem 0;
    }

    .preface .poem-fa {
      direction: rtl;
      font-size: 1.25rem;
      line-height: 2.2;
      text-align: right;
    }

    .preface .poem-en {
      font-size: 1.15rem;
      line-height: 2.1;
      font-style: italic;
    }

    .preface .label {
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: #9a7a55;
      margin-bottom: 0.8rem;
      display: block;
    }

    .preface .aphorism {
      font-style: italic;
      color: #4a3520;
    }

    .preface .footnotes {
      margin-top: 1.5rem;
      font-size: 1rem;
      color: #7a5e40;
      line-height: 1.8;
      border-top: 1px dashed #c9b89a;
      padding-top: 1rem;
    }

    .preface .footnotes-fa {
      direction: rtl;
      text-align: right;
    }

    .preface .signature {
      margin-top: 3rem;
      text-align: center;
      color: #6b4f2f;
      font-style: italic;
      font-size: 1.15rem;
    }

    .preface .needs-work {
      opacity: 0.75;
      font-style: italic;
    }

    .preface .needs-work-note {
      font-size: 0.9rem;
      color: #a07850;
      display: block;
      margin-top: 0.5rem;
    }

    @media (max-width: 640px) {
      .preface .pair {
        grid-template-columns: 1fr;
        gap: 1.2rem;
      }
      .preface .persian {
        border-right: none;
        border-bottom: 2px solid #c9843a;
        padding-right: 0;
        padding-bottom: 1rem;
      }
      .preface .english {
        border-left: none;
        border-top: 2px solid #8aab72;
        padding-left: 0;
        padding-top: 1rem;
      }
    }
"""



def is_draft(poem):
    """True if the poem is still a raw machine draft (no finished translation).

    Accepts a real bool from parse_toml or a stray 'true'/'True' string.
    """
    v = poem.get("draft", False)
    return v is True or (isinstance(v, str) and v.strip().lower() == "true")


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


def render_toc(poems, english_source="translation", title="Poems — اشعار", heading_html=None):
    header = (
        '<tr class="toc-header">'
        '<th class="toc-col-english" style="text-align:left;">Page &amp; Title</th>'
        '<th class="toc-col-dates" style="text-align:left;">Translated'
        '<span style="float:right;">Written</span></th>'
        '<th class="toc-col-persian">'
        '<div style="display:flex;">'
        '<span style="flex:1;direction:rtl;text-align:right;">عنوان</span>'
        '<span style="flex-shrink:0;min-width:2.2rem;padding-right:1.2rem;padding-left:0.3rem;text-align:left;white-space:nowrap;">صفحه</span>'
        '</div>'
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
        fl_en         = first_line(english_source(p) if callable(english_source) else p.get(english_source, ""))
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
            f'<div class="toc-slug">{poem_id}</div>'
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

    if heading_html is None:
        heading_html = f'<span class="toc-title">{title}</span>'
    return (
        '<div class="toc">'
        + heading_html +
        '<table class="toc-table">'
        + header
        + "".join(rows)
        + "</table></div>"
    )


# The English layers a draft can carry, in increasing order of refinement.
# Each is an independent ===section=== in the .poem file; the badge label is what
# the reader sees in the Drafts tab. A layer with no text shows no badge.
DRAFT_LAYERS = [
    ("machine",     "Machine"),   # raw OCR / machine translation (scratch)
    ("lantern",     "Lantern"),   # working interpretive draft
    ("translation", "Ben"),       # the finished human translation
]


def render_footnotes(poem):
    if not poem.get("footnotes"):
        return ""
    return (
        '<div class="footnotes">'
        '<span class="label">Translator\'s Notes</span>'
        "<p>" + poem["footnotes"] + "</p>"
        "</div>"
    )


def draft_english(poem):
    """Best available English for a draft's TOC snippet (most refined first)."""
    for key in ("translation", "lantern", "machine"):
        if poem.get(key, "").strip():
            return poem[key]
    return ""


def render_draft_section(poem):
    """A draft poem with one latching badge + column per non-empty English layer."""
    poem_id   = poem.get("id", "")
    available = [(k, lbl) for k, lbl in DRAFT_LAYERS if poem.get(k, "").strip()]
    # Default the most refined available layer to visible.
    default_key = available[-1][0] if available else None

    badges = "".join(
        f'<button type="button" class="layer-badge{" is-active" if k == default_key else ""}" '
        f'data-poem="{poem_id}" data-layer="{k}">{lbl}</button>'
        for k, lbl in available
    )
    badges_html = (
        f'<div class="layer-badges" role="group" aria-label="Translation layers">{badges}</div>'
    )

    layers = "".join(
        f'<div class="english-layer{" is-active" if k == default_key else ""}" '
        f'data-poem="{poem_id}" data-layer="{k}">'
        f'<span class="label">{lbl}</span>'
        '<div class="poem-block english-poem"><p>' + poem.get(k, "") + "</p></div>"
        "</div>"
        for k, lbl in available
    )

    return (
        f'<div class="poem-section" id="{poem_id}">'
        '<div class="poem-header">'
        f'<p class="poem-header-persian">{poem.get("persian_title", "")}</p>'
        f'<p class="poem-header-english">{poem.get("english_title", "")}</p>'
        f'<p class="poem-header-meta">{meta_line(poem)}</p>'
        f'<p class="poem-header-slug">{poem_id}</p>'
        f'{badges_html}'
        "</div>"
        '<div class="pair">'
        '<div class="persian">'
        '<span class="label">متن اصلی</span>'
        '<div class="poem-block persian-poem"><p>' + poem.get("persian", "") + "</p></div>"
        "</div>"
        f'<div class="english-layers">{layers}</div>'
        "</div>"
        + render_footnotes(poem)
        + "</div>"
    )


def render_poem_section(poem, english_field="translation", english_label="Translation"):
    footnotes_html = render_footnotes(poem)

    if is_draft(poem):
        status_html = '<span class="poem-status is-draft">Draft</span>'
    else:
        status_html = '<span class="poem-status is-rendered">Rendered</span>'

    return (
        f'<div class="poem-section" id="{poem.get("id", "")}">'
        '<div class="poem-header">'
        f'<p class="poem-header-persian">{poem.get("persian_title", "")}</p>'
        f'<p class="poem-header-english">{poem.get("english_title", "")}</p>'
        f'<p class="poem-header-meta">{meta_line(poem)}</p>'
        f'<p class="poem-header-slug">{poem.get("id", "")}</p>'
        f'{status_html}'
        "</div>"
        '<div class="pair">'
        '<div class="persian">'
        '<span class="label">\u0645\u062a\u0646 \u0627\u0635\u0644\u06cc</span>'
        '<div class="poem-block persian-poem"><p>' + poem.get("persian", "") + "</p></div>"
        "</div>"
        '<div class="english">'
        f'<span class="label">{english_label}</span>'
        '<div class="poem-block english-poem"><p>' + poem.get(english_field, "") + "</p></div>"
        "</div>"
        "</div>"
        + footnotes_html
        + "</div>"
    )


def render_preface_section(section):
    header = ""
    if section.get("label_fa") or section.get("label_en") or section.get("date"):
        meta = (
            f'<span class="section-meta">{section["date"]}</span>'
            if section.get("date") else ""
        )
        header = (
            '<div class="section-break">'
            f'<span class="section-label-fa">{section.get("label_fa", "")}</span>'
            f'<span class="section-label-en">{section.get("label_en", "")}</span>'
            f'{meta}'
            '</div>'
        )
    return f'{header}\n{section.get("body", "")}'


def render_preface(sections):
    return "\n".join(render_preface_section(s) for s in sections)


TAB_SCRIPT = """
  (function () {
    var buttons = document.querySelectorAll('.tab-btn');
    var panels = document.querySelectorAll('.tab-panel');
    var backToToc = document.querySelector('.back-to-toc');
    function activate(name) {
      buttons.forEach(function (b) {
        b.classList.toggle('active', b.dataset.tab === name);
      });
      panels.forEach(function (p) {
        p.classList.toggle('active', p.id === 'tab-' + name);
      });
      var onPoems = name === 'poems' || name === 'drafts';
      document.body.classList.toggle('on-poems', onPoems);
      document.body.classList.toggle('poems-open', name === 'poems');
      if (backToToc) {
        backToToc.setAttribute('href', name === 'drafts' ? '#toc-drafts' : '#toc');
      }
      if (history.replaceState) history.replaceState(null, '', '#' + name);
    }
    buttons.forEach(function (b) {
      b.addEventListener('click', function () { activate(b.dataset.tab); });
    });
    // Open the tab whose panel contains the hash target; else the named tab; else poems.
    var hash = (location.hash || '').replace('#', '');
    function panelHas(tab) {
      return hash && document.getElementById('tab-' + tab) &&
        document.getElementById('tab-' + tab).querySelector('#' + CSS.escape(hash));
    }
    if (hash === 'drafts' || hash === 'toc-drafts' || panelHas('drafts')) {
      activate('drafts');
    } else if (hash === 'preface' || panelHas('preface')) {
      activate('preface');
    } else {
      activate('poems');
    }
  })();
"""


LAYER_SCRIPT = """
  (function () {
    var badges = document.querySelectorAll('.layer-badge');
    badges.forEach(function (badge) {
      badge.addEventListener('click', function () {
        var poem = badge.dataset.poem;
        var layer = badge.dataset.layer;
        var on = badge.classList.toggle('is-active');
        var sel = '.english-layer[data-poem="' + poem + '"][data-layer="' + layer + '"]';
        var col = document.querySelector(sel);
        if (col) col.classList.toggle('is-active', on);
      });
    });
  })();
"""


# ── ornaments — vendored masks from the tazhib found-object library ──
# ornaments/corner-bhutan.svg  (corner/bhutan — quarter design, mirrored ×4)
# ornaments/rule-dogmoj.svg    (rule/dogmoj — diamond-and-leaf dash, 16:1)
# Inlined as data URIs at build time so index.html works over file:// (CSS
# mask-image is CORS-restricted; external URLs fail on a null origin).
ORNAMENTS = {
    "__CORNER_MASK__": "corner-bhutan.svg",
    "__RULE_MASK__":   "rule-dogmoj.svg",
}


def ornament_css(css: str, ornaments_dir: Path) -> str:
    """Substitute ornament mask data-URIs into the CSS; degrade to hidden if absent."""
    import base64
    missing = []
    for token, fname in ORNAMENTS.items():
        path = ornaments_dir / fname
        if path.is_file():
            b64 = base64.b64encode(path.read_bytes()).decode()
            css = css.replace(token, f'url("data:image/svg+xml;base64,{b64}")')
        else:
            missing.append(fname)
            css = css.replace(token, "none")
    if missing:
        print(f"Warning: missing ornament file(s) {missing} in {ornaments_dir} — "
              "corners/rule will not render.")
        css += "\n    .corner, .toc-rule { display: none; }\n"
    return css


def render_collection(poems, preface, book_persian, book_english, author, ornaments_dir):
    rendered = [p for p in poems if not is_draft(p)]
    drafts   = [p for p in poems if is_draft(p)]

    css = ornament_css(CSS, ornaments_dir)
    toc = render_toc(rendered, heading_html='<div class="toc-rule" aria-hidden="true"></div>')
    sections = "\n".join(render_poem_section(p) for p in rendered)

    drafts_toc = render_toc(drafts, english_source=draft_english, title="Drafts — پیش‌نویس‌ها")
    drafts_sections = "\n".join(render_draft_section(p) for p in drafts)
    preface_html = render_preface(preface)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{book_english} \u2014 {author}</title>
  <link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
  <style>
{css}
  </style>
</head>
<body class="on-poems poems-open">
<div class="carpet">
  <div class="corner c-tl" aria-hidden="true"></div>
  <div class="corner c-tr" aria-hidden="true"></div>
  <div class="corner c-bl carpet-close" aria-hidden="true"></div>
  <div class="corner c-br carpet-close" aria-hidden="true"></div>
  <div class="book-header">
    <p class="book-title-persian">{book_persian}</p>
    <p class="book-title-english">{book_english}</p>
    <p class="book-author">{author}</p>
  </div>
  <div class="tabs">
    <button class="tab-btn" data-tab="preface">Preface &middot; \u067e\u06cc\u0634\u06af\u0641\u062a\u0627\u0631</button>
    <button class="tab-btn active" data-tab="poems">Poems &middot; \u0627\u0634\u0639\u0627\u0631</button>
    <button class="tab-btn" data-tab="drafts">Drafts &middot; \u067e\u06cc\u0634\u200c\u0646\u0648\u06cc\u0633</button>
  </div>
</div>

<div id="tab-preface" class="tab-panel preface">
  {preface_html}
</div>

<div id="tab-poems" class="tab-panel poems active">
  <div id="toc" class="toc-wrapper">
    <div class="corner c-bl" aria-hidden="true"></div>
    <div class="corner c-br" aria-hidden="true"></div>
    {toc}
  </div>
  <div class="page">
    {sections}
  </div>
</div>

<div id="tab-drafts" class="tab-panel poems">
  <p class="drafts-note">Work in progress \u2014 toggle the layers under each poem to compare them side by side: <b>Machine</b> (raw OCR) \u00b7 <b>Lantern</b> (a working draft) \u00b7 <b>Ben</b> (the finished translation). Empty layers are hidden.</p>
  <div id="toc-drafts" class="toc-wrapper">
    {drafts_toc}
  </div>
  <div class="page">
    {drafts_sections}
  </div>
</div>

<a href="#toc" class="back-to-toc" title="Back to contents">^</a>
<script>{TAB_SCRIPT}</script>
<script>{LAYER_SCRIPT}</script>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(description="Render all self-contained .poem files to one HTML file.")
    parser.add_argument("folder", nargs="?", default="poems", help="Path to poems/ folder (default: poems)")
    parser.add_argument("--preface", default=None, help="Path to preface/ folder (default: sibling of poems/)")
    parser.add_argument("--out", default="index.html", help="Output HTML path")
    parser.add_argument("--book-persian", default="\u0628\u0648\u06cc \u06a9\u0627\u0647\u06af\u0644 \u0648 \u0622\u0648\u0627\u0632 \u067e\u0631\u0646\u062f\u0647")
    parser.add_argument("--book-english", default="The Smell of Adobe and Birdsong")
    parser.add_argument("--author", default="Mohammad Ebrahim Jafari")
    args = parser.parse_args()

    poems_dir   = Path(args.folder)
    preface_dir = Path(args.preface) if args.preface else poems_dir.parent / "preface"

    if not poems_dir.is_dir():
        print(f"Error: poems folder '{poems_dir}' not found.")
        sys.exit(1)

    poem_files = sorted(poems_dir.glob("*.poem"))
    if not poem_files:
        print(f"No .poem files found in {poems_dir}.")
        sys.exit(1)

    poems = [load_poem(f) for f in poem_files]

    def sort_key(p):
        pn = p.get("page_number")
        try:
            return (0, int(pn))
        except (TypeError, ValueError):
            return (1, 0)

    poems.sort(key=sort_key)

    preface = load_preface(preface_dir)

    ornaments_dir = poems_dir.parent / "ornaments"
    html = render_collection(poems, preface, args.book_persian, args.book_english,
                             args.author, ornaments_dir)

    out_path = Path(args.out)
    out_path.write_text(html, encoding="utf-8")
    n = len(poems)
    s = len(preface)
    print(f"Written: {out_path} ({n} poem{'s' if n != 1 else ''}, "
          f"{s} preface section{'s' if s != 1 else ''})")


if __name__ == "__main__":
    main()

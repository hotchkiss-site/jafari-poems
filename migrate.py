#!/usr/bin/env python3
"""
migrate.py — one-time migration from single .poem files to meta/ + poems/ layout.

For each poems/*.poem file:
  - Extracts the key:value header into meta/{id}.toml
  - Rewrites poems/{id}.poem with only the ===section=== content
  - Renames the .poem file if the filename didn't match its internal id

Run once from the repo root:
    python migrate.py
"""

import re
from pathlib import Path

POEMS_DIR = Path("poems")
META_DIR  = Path("meta")
META_DIR.mkdir(exist_ok=True)


def toml_str(value: str) -> str:
    value = value.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{value}"'


def migrate_poem(path: Path):
    text = path.read_text(encoding="utf-8")

    # Split at the first ===section=== marker
    m = re.search(r'^===\w+===$', text, re.MULTILINE)
    header_text = text[:m.start()] if m else text
    body_text   = text[m.start():] if m else ""

    # Parse key: value header lines
    meta: dict[str, str] = {}
    for line in header_text.splitlines():
        if ':' in line:
            key, _, val = line.partition(':')
            meta[key.strip()] = val.strip()

    poem_id = meta.get("id") or path.stem

    # Write meta/<id>.toml
    toml_path = META_DIR / f"{poem_id}.toml"
    lines = [
        f'id                  = {toml_str(poem_id)}',
        f'english_title       = {toml_str(meta.get("english_title", ""))}',
        f'persian_title       = {toml_str(meta.get("persian_title", ""))}',
        f'date_written        = {toml_str(meta.get("date_written", ""))}',
        f'date_translated     = {toml_str(meta.get("date_translated", ""))}',
        f'page_number         = {toml_str(meta.get("page_number", ""))}',
        f'persian_page_number = {toml_str(meta.get("persian_page_number", ""))}',
        f'source              = ""',
        f'tags                = []',
        f'notes               = ""',
    ]
    toml_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Write poems/<id>.poem (sections only, no header)
    new_poem_path = POEMS_DIR / f"{poem_id}.poem"
    new_poem_path.write_text(body_text, encoding="utf-8")

    renamed = ""
    if path != new_poem_path:
        path.unlink()
        renamed = f" (renamed from {path.name})"

    print(f"  {poem_id}{renamed}")


def main():
    poem_files = sorted(POEMS_DIR.glob("*.poem"))
    if not poem_files:
        print("No .poem files found in poems/.")
        return

    print(f"Migrating {len(poem_files)} poems...\n")
    for p in poem_files:
        migrate_poem(p)

    print(f"\nDone. meta/ now has {len(list(META_DIR.glob('*.toml')))} .toml files.")
    print("Review them, then delete migrate.py if you no longer need it.")


if __name__ == "__main__":
    main()

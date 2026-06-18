# Jafari Poems — Codebase Guide

A git-based bilingual poetry collection. The poems are translations of Mohammad Ebrahim Jafari's Persian verse. The working language of the repo is English; poem content is bilingual (Persian + English).

## Repository layout

```
poems/          one .poem file per poem — text sections only
meta/           one .toml file per poem — structured metadata
schema.toml     authoritative list of allowed metadata fields
build_collection.py   renders all poems → index.html
build_poem.py         renders a single poem → <id>.html
new-poem.sh     interactive scaffolding for a new poem (both files)
migrate.py      one-time migration script (kept for reference)
index.html      generated output — do not edit by hand
```

## File formats

### `poems/<id>.poem`
Plain text with named section delimiters. No metadata header.

```
===persian===
<original Persian text>

===machine===
<raw machine translation — scratch only, not rendered>

===translation===
<finished English translation>

===footnotes===
<translator's notes — word choices, cultural context, variants>
```

### `meta/<id>.toml`
Flat TOML. All fields defined in `schema.toml`. Every field is present in every file (empty string or empty array if unused).

```toml
id                  = "ancient-tree"
english_title       = "Ancient Tree"
persian_title       = "درختی کهن"
date_written        = "1961 - ۱۳۴۰"
date_translated     = "3/22/26"
page_number         = "35"
persian_page_number = "۳۵"
source              = ""
tags                = ["nature", "solitude"]
notes               = ""
```

The `id` field must match the filename stem exactly. It is the link between the two files — there is no other join key.

## Adding a new poem

```bash
./new-poem.sh
```

The script prompts for all fields, writes both files, and guards against duplicate IDs. Open `poems/<id>.poem` to add text; open `meta/<id>.toml` to edit metadata later.

## Adding a new metadata field

1. Add it to `schema.toml` with `type`, `required`, and `description`.
2. Backfill existing files:
   ```bash
   for f in meta/*.toml; do echo 'new_field = ""' >> "$f"; done
   ```
3. If the field should appear in the rendered HTML, update `build_collection.py` (see `render_poem_section` and `render_toc`).

## Building

```bash
# Full collection → index.html
python build_collection.py poems/

# Single poem → <id>.html
python build_poem.py ancient-tree
```

Both scripts read from `meta/` (defaults to sibling of `poems/`) and `poems/`. Pass `--meta <path>` to override.

CI runs `build_collection.py` automatically on pushes to `main` that touch `poems/`, `meta/`, or the build script, and commits the updated `index.html`.

## Conventions

- **Slugs** are lowercase, hyphen-separated English words (`shadow-daughter`, `ancient-tree`). The slug is the filename stem for both `poems/` and `meta/`, and the HTML anchor id.
- **Dates** are freeform strings. Both Gregorian and Solar Hijri dates are welcome in the same field, separated by ` - `.
- **Tags** are lowercase English words. Add new ones freely; update `schema.toml` notes if a tag develops a specific meaning.
- **The `machine` section** is a scratch space — it is parsed but never rendered in the HTML output.
- `index.html` is committed by CI and should not be edited manually.

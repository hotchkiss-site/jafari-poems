# Jafari Poems — Codebase Guide

A git-based bilingual poetry collection. The poems are translations of Mohammad Ebrahim Jafari's Persian verse. The working language of the repo is English; poem content is bilingual (Persian + English).

## Repository layout

```
poems/          one .poem file per poem — text sections only
meta/           one .toml file per poem — structured metadata
preface/        front matter — one self-contained HTML fragment per section
schema.toml     authoritative list of allowed metadata fields
build_collection.py   renders preface + poems → index.html (tabbed)
build_poem.py         renders a single poem → <id>.html
new-poem.sh     interactive scaffolding for a new poem (both files)
migrate.py      one-time migration script (kept for reference)
index.html      generated output — do not edit by hand
```

The rendered `index.html` has three tabs below a shared book header:
**Preface** (the `preface/` sections), **Poems** (the TOC + finished poem sections),
and **Drafts** (poems with `draft = true` — machine-only English awaiting a finished translation).

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
draft               = false
```

The `id` field must match the filename stem exactly. It is the link between the two files — there is no other join key.

`draft = true` marks a poem whose English is still a raw machine draft (the `===translation===` section is empty and only `===machine===` is filled). Drafts are pulled out of the **Poems** tab and shown under a separate **Drafts** tab, where the English column renders the `machine` text and the poem carries a "Draft" badge. All finished poems are `draft = false` and carry a "Rendered" badge. Promote a poem by writing its finished `===translation===` and flipping `draft` to `false`.

### `preface/<NN-slug>.html`
Front matter is richer than the poems (prose interleaved with quoted poems, footnotes, signatures), so each section is a **self-contained HTML fragment** rather than a `.poem`/`.toml` pair. Metadata lives inline in a `<!--meta-->` header; there is no sidecar TOML. Files are rendered in filename order, so the `NN-` numeric prefix controls section order.

```html
<!--meta
label_fa: محمد ابراهیم جعفری
label_en: Mohammad Ibrahim Jafari
date: ۱۳۹۶ / 2017
-->

<div class="pair">
  <div class="persian">…Persian (RTL) prose, <span class="aphorism">…</span>, <div class="poem-block"><div class="poem-fa">…</div></div></div>
  <div class="english">…English prose, <div class="poem-block"><div class="poem-en">…</div></div></div>
</div>
<div class="signature">…author · date…</div>
```

The build reads the `<!--meta-->` header (drives the `.section-break` heading) and drops the body verbatim into the namespaced `.preface` container. Available classes: `pair` / `persian` / `english` (bilingual column), `poem-block` + `poem-fa` / `poem-en` (a quoted poem), `aphorism`, `footnotes` (+ `footnotes-fa`), `signature`, `label`, `needs-work` (+ `needs-work-note`). Preface CSS is scoped under `.preface` and poem CSS under `.poems`, so the shared class names (`pair`, `persian`, …) never collide between tabs.

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

## Adding / editing a preface section

Create or edit a file in `preface/` (e.g. `preface/05-afterword.html`). Give it a `NN-` prefix to place it in the running order, add a `<!--meta-->` header, and write the bilingual body using the classes listed above. No scaffolding script — just write the HTML and rebuild. To restyle the preface, edit the `.preface …` rules in `CSS` inside `build_collection.py` (and `render_preface_section` for the heading markup).

## Building

```bash
# Full collection → index.html
python build_collection.py poems/

# Single poem → <id>.html
python build_poem.py ancient-tree
```

Both scripts read from `meta/` (defaults to sibling of `poems/`) and `poems/`. `build_collection.py` also reads `preface/` (sibling of `poems/`). Pass `--meta <path>` / `--preface <path>` to override. If `preface/` is absent the Preface tab is simply empty.

CI runs `build_collection.py` automatically on pushes to `main` that touch `poems/`, `meta/`, `preface/`, or the build script, and commits the updated `index.html`.

## Conventions

- **Slugs** are lowercase, hyphen-separated English words (`shadow-daughter`, `ancient-tree`). The slug is the filename stem for both `poems/` and `meta/`, and the HTML anchor id.
- **Dates** are freeform strings. Both Gregorian and Solar Hijri dates are welcome in the same field, separated by ` - `.
- **Tags** are lowercase English words. Add new ones freely; update `schema.toml` notes if a tag develops a specific meaning.
- **The `machine` section** is a scratch space — it is parsed but never rendered in the HTML output.
- `index.html` is committed by CI and should not be edited manually.

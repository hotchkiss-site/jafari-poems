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
and **Drafts** (poems with `draft = true` — English still in draft: a literal `machine` pass, an optional `lantern` crib, and sometimes a staged-but-unreleased "Ben" translation).

## File formats

### `poems/<id>.poem`
Plain text with named section delimiters. No metadata header.

```
===persian===
<original Persian text>

===machine===
<raw OCR / machine translation — the literal first pass>

===lantern===
<working interpretive draft — a step between machine and the finished hand>

===translation===
<finished English translation>

===footnotes===
<translator's notes — word choices, cultural context, variants>
```

The three English sections are **layers** of increasing refinement, and **who writes which layer matters** — read this before translating:

- **`machine`** — the raw OCR / machine-translation literal first pass. Scratch input, nobody's considered rendering. Leave it as the literal you started from.
- **`lantern`** — the **agent's interpretive working draft**: a crib that steps from the literal `machine` toward faithful English — resolving idiom, image, and ambiguity — without claiming to be the final hand. **This is the home for an AI collaborator's own translation work.** Optional in principle, but when an agent translates, its rendering goes here.
- **`translation`** — **Ben's finished human translation.** **Ben is the repo owner — the human you (the agent) are working with** — and this layer is labelled "Ben" in the UI because it is *his* hand. **It is Ben's slot. By default an agent does NOT write its own rendering into `===translation===`; put your work in `lantern` and leave `translation` empty for Ben.** The one exception is when Ben explicitly asks you to stand in and draft a translation for him to revise later (e.g. the page 61–69 bulk import) — then you may stage a translation here, but keep the poem `draft = true` so it stays out of the Poems tab until Ben signs off.

`lantern` is optional and need not be present in every file. In the **Drafts** tab each non-empty layer gets a clickable, latching badge under the poem; click one or several to show those layers side by side on the English side (empty layers show no badge). The **Poems** tab renders only the finished `translation`. The `===section===` parser is generic, so adding another layer later is a builder change, not a parser one.

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

`draft = true` marks a poem whose English is not yet a finished translation. Drafts are pulled out of the **Poems** tab into a separate **Drafts** tab, where each non-empty English layer (`machine` / `lantern` / `translation`→"Ben") is shown as a togglable badge for side-by-side comparison (see the `.poem` format above); the most refined available layer is shown by default. A draft *may* already carry a finished `===translation===` that is staged but withheld from the Poems tab — it surfaces as the "Ben" layer in Drafts and stays out of Poems until you flip `draft` to `false` (e.g. poems imported in bulk as drafts that already had a human translation in the source). Finished poems are `draft = false`, carry a "Rendered" badge, and appear in **Poems** with their `translation`. Promote a poem by writing its finished `===translation===` and flipping `draft` to `false`.

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

- **Slugs** are lowercase, hyphen-separated English words (`shadow-daughter`, `ancient-tree`). The slug is the filename stem for both `poems/` and `meta/`, and the HTML anchor id. It is also shown on the rendered site as a muted monospace tag — under each title in the TOC and in each poem's header — so a poem on the page maps straight back to its `poems/<slug>.poem` + `meta/<slug>.toml` files.
- **Dates** are freeform strings. Both Gregorian and Solar Hijri dates are welcome in the same field, separated by ` - ` (Gregorian first), e.g. `1988 - ۱۳۶۷`. Convention for the Gregorian half: map the Solar Hijri year by **its actual overlap, not a fixed offset** — a SH year runs ~21 Mar to ~20 Mar, so it spans two Gregorian years. If the source names a month or season, pin the Gregorian year to it: **months 1–9 (spring → autumn, Farvardin–Azar) → SH year + 621; the winter months 10–12 (Dey–Bahman–Esfand) → SH year + 622** (Dey itself straddles the New Year, so round it to +622). Thus `بهار ۱۳۶۸` (spring) → **1989**, `اسفند ۱۳۶۷` and `زمستان ۱۳۶۷` (Esfand / winter) → **1989**, but `۱۳۶۷/۲` or `۱۳۶۷/۹` (spring/autumn) → **1988**. With no month or season given, default a bare `۱۳xx` to + 621. Keep the season/month in the Persian half (`1989 - اسفند ۱۳۶۷`).
- **`meta` `notes` vs `===footnotes===`** — opposite audiences, easy to mix up. The `===footnotes===` section of a `.poem` is **published**: it renders under the poem as "Translator's Notes" (word choices, cultural context, variants — for the reader). The `notes` field in `meta/*.toml` is **private**: it is parsed but never shown on the site — curator/provenance commentary for collaborators (source file, OCR caveats, why a slug or rendering was chosen). Put reader-facing notes in `===footnotes===`; put behind-the-scenes notes in meta `notes`.
- **Tags** are lowercase English words. Add new ones freely; update `schema.toml` notes if a tag develops a specific meaning.
- **The `machine` section** is a scratch space — the raw literal pass. It is **not** rendered in the **Poems** tab (which shows only `translation`), but in the **Drafts** tab it *does* surface as a togglable "Machine" badge alongside `lantern` and "Ben", for side-by-side comparison.
- `index.html` is committed by CI and should not be edited manually.

## Documenting session decisions (files, not memory)

Durable knowledge produced in a working session — process learnings, translation
rationale, naming/format decisions, grammar explanations — is recorded in **versioned
repo files, not in agent memory.** Memory is per-machine, invisible to collaborators and
CI, and does not travel with the repo; the repo is the shared source of truth. So when a
session generates something meant to outlast it, write it into the right file:

- **Conversion / import process** → `jafari-conversion-skill.md`
- **Repo structure, file formats, build behavior** → this file (`CLAUDE.md`)
- **Farsi grammar explanations** → `farsi-grammar.md` — one section per point; **append**
  a new section, never overwrite earlier entries or recreate the file
- **Per-poem editorial notes** → the `notes` field in that poem's `meta/*.toml`

When asked to "remember" a convention or explanation, default to documenting it in one of
these files rather than to memory.

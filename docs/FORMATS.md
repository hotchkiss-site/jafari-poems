---
type: spec
scope: project
domain: websites
title: Jafari Poems — file formats
status: active
inherits: ../CLAUDE.md
applies_to:
  - "poems/**"
  - "preface/**"
  - "schema.toml"
  - "build_collection.py"
  - "new-poem.sh"
last_verified: 2026-10-01
built_against: corpus-conventions@v3
supersedes: null
---

# Jafari Poems — file formats

*Moved verbatim from `CLAUDE.md` when the records were adopted (2026-10-01; the whole file is
frozen as `archive/CLAUDE_2026-10-01.md`), except the three-layer rule, which stays in
`CLAUDE.md`. Paths are written from the repo root.*

## File formats

### `poems/<id>.poem`
Plain text with named section delimiters. The first section is `===meta===`,
holding the poem's structured metadata as flat TOML; every other section is text.

```
===meta===
<flat TOML — all fields defined in schema.toml>

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

*Who writes which English layer is in `CLAUDE.md` → *The three English layers*; read it
before translating.*

`lantern` is optional and need not be present in every file. In the **Drafts** tab each non-empty layer gets a clickable, latching badge under the poem; click one or several to show those layers side by side on the English side (empty layers show no badge). The **Poems** tab renders only the finished `translation`. The `===section===` parser is generic, so adding another layer later is a builder change, not a parser one.

### The `===meta===` section
Flat TOML inside the poem file. All fields defined in `schema.toml`. Every field is present in every poem (empty string or empty array if unused).

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

The `id` field must match the `.poem` filename stem exactly (the build warns on mismatch and trusts the filename).

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

The build reads the `<!--meta-->` header (drives the `.section-break` heading) and drops the body verbatim into the namespaced `.preface` container. Preface CSS is scoped under `.preface` and poem CSS under `.poems`, so the shared class names (`pair`, `persian`, …) never collide between tabs.

Available classes:

| class | what it is |
| --- | --- |
| `pair` / `persian` / `english` | the bilingual two-column block (Persian RTL, English LTR) |
| `poem-block` + `poem-fa` / `poem-en` | **a quoted poem.** Renders as a tinted, gold-framed plate with a dogmoj flourish at its head, in type a size larger than the prose around it — the essayists' prose and the verse they quote share a column, so the verse has to announce itself. Verse type matches the Poems tab, so a poem looks the same wherever it appears in the book. |
| `poem-block[data-poet="…"]` | names the poet under the plate, in the plate's own language. **Used only for verse by another hand** (Wang Wei, Bashō, MacLeish); an unattributed plate is Jafari's own. |
| `poem-cite` | a muted monospace slug link inside a plate (`→ drunk-waterfall`) for a quoted poem that also stands in this collection. English column only. Clicking it opens the tab holding that poem — see the cross-tab note in `docs/translation-conventions.md`. |
| `aphorism` | one of Jafari's standalone maxims. Block-level and deliberately unmarked — the printed page stacks the maxims as tight separate paragraphs with no bullet and no blank line between, so the CSS reproduces that and nothing more. Put each maxim in its own span rather than joining them with `<br><br>`. Any footnote `<sup>` belongs *inside* the span. |
| `tnote` | a **`<details>`** element — an editorial aside in the translator's voice, kept visibly separate from the authors' own footnotes and folded shut so it neither competes with the poem nor shoves the two columns out of register. Write it as `<details class="tnote"><summary>Translator's note</summary><p>…</p></details>` in the English column. Use it where an etymology or a dialect fact actually unlocks a line; a page of open notes drowns the verse. |
| `lacuna` | `⟨…⟩` standing for a passage that **cannot be read** in a damaged source — an unread patch, not an authorial ellipsis. |
| `footnotes` (+ `footnotes-fa`) | the section author's own footnotes |
| `signature`, `label` | author/date sign-off; the فارسی / ENGLISH column labels |
| `needs-work` (+ `needs-work-note`) | provisional English, with a bracketed status line |

## Adding a new poem

```bash
./new-poem.sh
```

The script prompts for all fields, writes the single `poems/<id>.poem` (===meta=== section pre-filled), and guards against duplicate IDs. Open the file to add text or edit metadata later.

## Adding a new metadata field

1. Add it to `schema.toml` with `type`, `required`, and `description`.
2. Backfill existing files — append the field at the end of each ===meta=== block:
   ```bash
   python3 - <<'EOF'
   from pathlib import Path
   for f in Path('poems').glob('*.poem'):
       lines = f.read_text(encoding='utf-8').splitlines(keepends=True)
       i = next(k for k, ln in enumerate(lines) if ln.startswith('===persian==='))
       while i > 0 and lines[i-1].strip() == '':
           i -= 1
       lines.insert(i, 'new_field           = ""\n')
       f.write_text(''.join(lines), encoding='utf-8')
   EOF
   ```
   (or simply hand-edit — the field goes at the end of the ===meta=== block, aligned like its neighbours)
3. If the field should appear in the rendered HTML, update `build_collection.py` (see `render_poem_section` and `render_toc`).

## Adding / editing a preface section

Create or edit a file in `preface/` (e.g. `preface/05-afterword.html`). Give it a `NN-` prefix to place it in the running order, add a `<!--meta-->` header, and write the bilingual body using the classes listed above. No scaffolding script — just write the HTML and rebuild. To restyle the preface, edit the `.preface …` rules in `CSS` inside `build_collection.py` (and `render_preface_section` for the heading markup).

# Jafari Conversion Skill

How to turn a **raw OCR/Adobe text dump** of Jafari's poetry (e.g. `raw_Jafari-adobe-2.txt`)
into the repo's `poems/*.poem` + `meta/*.toml` pair. Written for the next agent doing this job.

## What the raw dumps look like

Each dump is plain text exported from a PDF/scan. Multiple poems are concatenated with
no machine-readable delimiters. A typical poem block contains, in roughly this order:

1. A **page-number marker** — the page printed as both Persian-Indic (`۲۵`) and/or Western
   (`25`) digits, often on its own line, sometimes repeated mid-poem where the scan broke a page.
2. The **Persian text** (RTL), line per line.
3. A **date line** in Persian digits, sometimes with a place and month
   (`تهران دی ماه ۱۳۵۱`, `۱۳۴۷`, `دهه ۱۳۶۰`).
4. An **English machine translation** of the whole poem — recognisably machine-made
   (awkward literalisms like "Wow, if it weren't for your imagination", "songless iron volumes").
5. Occasionally a second, **polished human translation**, often prefixed `ME:`.

Boundaries between poems are just blank lines + a shift back to Persian or a new page number.
Read the whole file first and segment it by eye before touching anything.

## Before creating anything: dedupe

Some poems in a dump are **already in the repo**. Always check before adding.

- List existing ids: `ls poems/` and `ls meta/`.
- For each candidate poem, grep the repo for a distinctive Persian line, e.g.
  `Grep` for `لحظه ها` (a first line) across `poems/`.
- Match on the Persian text, **not** on title or page number — titles are often absent and
  page numbers can repeat. In the `-2` dump, the "To my daughter, Shadow" poem was already
  present as `shadow-daughter`; only two of the three blocks were new.

## Mapping a poem block → the four `.poem` sections

The `.poem` format has four named sections. Map the dump as follows:

| Source material in the dump        | `.poem` section   |
| ---------------------------------- | ----------------- |
| Persian text (RTL)                 | `===persian===`   |
| English **machine** translation    | `===machine===`   |
| Polished **human** translation (`ME:` block, if any) | `===translation===` |
| Translator's notes (rare in dumps) | `===footnotes===` |

There is also an optional **`===lantern===`** section: a working *interpretive* draft, a step
between the literal `machine` pass and a finished `translation`. It is **authored**, not lifted from
the dump — leave it empty during a bulk import unless you're deliberately drafting. In the Drafts tab
each non-empty layer (`machine` / `lantern` / `translation`→"Ben") becomes a togglable badge for
side-by-side comparison, so an empty layer simply shows no badge. See CLAUDE.md → `.poem` format.

Key conventions, learned from the existing files:

- **Keep the machine draft, don't promote it.** The `machine` section is scratch and is *never
  rendered*. The `translation` section is the *finished human* English and *is* rendered. Do **not**
  paste the machine output into `translation` — that would misrepresent raw MT as a finished
  translation and pollute the rendered collection. If the dump has no `ME:`/human version, leave
  `translation` **empty** and let the human translator finish it later. (See `shadow-daughter`: the
  machine "Moments are like small seeds" went to `machine`; the human "moments are as small grains"
  went to `translation`.)
- **Preserve the Persian verbatim** — keep the original line breaks, the trailing `...`/`....`
  ellipses, and spacing. Do not "clean up" OCR punctuation; it carries the poet's rhythm.
- **Keep the date line inside the section** it belongs to (Persian date at the end of the Persian
  block, English date at the end of the machine/translation block), mirroring how the poet laid it out.
- Leave a blank line after each `===header===`, matching the existing files.

## Writing the `meta/*.toml`

Every field in `schema.toml` must be present (empty string / empty array if unused). Field rules:

- **`id`** — must equal the filename stem of *both* files. Pick a lowercase two-word, hyphenated
  English slug from the poem's central image, matching existing style (`heart-partridge`,
  `water-cage`, `snow-beautiful`). No `of`/articles (`city-smoke`, not `city-of-smoke`).
- **`english_title` / `persian_title`** — the dumps are usually **untitled**. Leave both empty
  rather than inventing a title (precedent: `quiet-moon`). The descriptive slug carries the identity.
  Only fill a title if the source explicitly gives one.
- **`date_written`** — freeform. Put both calendars separated by ` - `, Gregorian first
  (`1968 - ۱۳۴۷`, `January 1972 - تهران دی ماه ۱۳۵۱`). Convert Solar Hijri → Gregorian by
  **+621** (1347 → 1968, 1351 → 1972); only state a Gregorian year you can justify, and keep the
  poet's original Persian date string intact alongside it.
- **`page_number` / `persian_page_number`** — from the page marker, Western and Persian-Indic
  digits respectively. If the dump shows no page number for that block, leave both empty.
- **`source`** — the dump filename (e.g. `raw_Jafari-adobe-2.txt`) so provenance is traceable.
- **`tags`** — lowercase English theme words drawn from the imagery (`city`, `longing`, `exile`,
  `aging`, `moon`). Reuse existing tags where they fit.
- **`notes`** — record anything an editor needs: "Untitled in source", and especially
  "English block is a raw machine draft (kept in the machine section); finished translation pending"
  so it's obvious the `translation` section was intentionally left empty.
- **`draft`** — set `draft = true` for every poem you convert this way (Persian + machine English,
  empty `translation`). The build pulls these out of the **Poems** tab into a separate **Drafts**
  tab, where the English column shows the `machine` text and the poem gets a "Draft" badge. Finished
  poems are `draft = false` ("Rendered"). When a human later writes the real `===translation===`,
  flip `draft` to `false` to graduate the poem into the main collection.

## Scaffolding shortcut

`./new-poem.sh` interactively writes both files and guards against duplicate ids. It's the blessed
path, but it's interactive — when batch-converting a dump, writing the two files directly (as here)
is fine as long as you reproduce the exact section/field layout above.

## Verify

Always rebuild and confirm the count went up by the number you added:

```bash
python build_collection.py poems/      # prints "Written: index.html (N poems, …)"
```

Don't hand-edit `index.html` — CI regenerates it. A successful build with the expected poem count
is the sign the new `.poem`/`.toml` pairs parse and join correctly (the join is `id` ↔ filename stem).

## Edge cases (learned from real dumps)

These all came up converting `raw-jafari-adobe-1.txt`. Handle them the same way next time.

- **Stray page markers inside a block.** A scan often drops the page number (`۲۶`) onto its own
  line *in the middle* of a poem where the page broke. A page-number-only line is not text — pull
  the number into `page_number` / `persian_page_number` and **delete the line from the body**.
- **Title printed as a heading line.** When the dump prints the poem's title on its own line above
  the verse (`گل های بادام`, `پرستوها به طاق آسمونند`), move it into `persian_title` /
  `english_title` and **drop it from the body** — don't duplicate it as the first line of
  `===persian===`. This is the one case where a dump *does* give a title; most blocks are untitled.
- **OCR markup vs. the poet's punctuation.** Keep ellipses, `....`, and odd spacing — they carry
  rhythm. But strip stray *markup* tokens that leaked from the source, e.g. literal `<br>` / `<Br>`
  tags (`with-you` had them); they would render verbatim in the HTML. Note the removal in `notes`.
- **The human translation isn't always labelled `ME:`.** A polished version may appear as a second,
  cleaner English block with no prefix. Recognise it by quality — real line breaks, em-dashes,
  deliberate word choice ("adobe" over "straw") — and route it to `===translation===`, not `machine`.
- **"Import the whole batch as drafts" + a human translation exists.** If you're told to bring a
  batch in as drafts but a block already carries a finished human translation, don't discard it:
  put it in `===translation===`, set `draft = true`, and add a `notes` line "flip `draft` to `false`
  to render." The Drafts tab renders `machine` regardless, so the staged translation stays hidden
  until promoted — lossless. (`rain-forgotten`, `nightingale-cloud` were imported this way.)
- **`source` convention.** Set `source` to the dump filename for every block in a batch (uniform
  provenance). If a block names its *original* publication (`beggar-dogs`: نشریه نامه دانشجو),
  record that in `notes`, not `source`.
- **Dedupe false positives.** Match on the whole first line / overall text, never a single recurring
  image. `wooden-horse` opens `شهر دود` ("city of smoke") — a keyword grep for that phrase hits the
  *existing, different* `city-smoke`. And two distinct poems can share a date (`bird-behind-wall` and
  `rain-forgotten` are both Tehran, Autumn ۱۳۶۸). Read the block before calling it a duplicate.

## Checklist

- [ ] Read & segment the whole dump into poem blocks.
- [ ] Dedupe each block against `poems/` by Persian first line (read the block — don't trust a
      single-phrase grep; shared imagery causes false matches).
- [ ] For each new block: Persian → `persian`, MT → `machine`, human translation (labelled `ME:`
      *or* an unlabelled polished block) → `translation`.
- [ ] Drop title-heading lines and stray page markers / `<br>` tokens from the body.
- [ ] Leave `translation` empty when no human version exists, and set `draft = true`.
- [ ] Write `meta/<id>.toml` with all `schema.toml` fields; record `source` and a `notes` provenance line.
- [ ] `python build_collection.py poems/`; check the poem count rose by the number you added **and**
      that the new ids actually landed under the **Drafts** tab.

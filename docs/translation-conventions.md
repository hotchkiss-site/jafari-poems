---
type: spec
scope: project
domain: websites
title: Jafari Poems — translation and transcription conventions
status: active
inherits: ../CLAUDE.md
applies_to:
  - "poems/**"
  - "preface/**"
last_verified: 2026-10-01
built_against: corpus-conventions@v3
supersedes: null
---

# Jafari Poems — translation and transcription conventions

*Moved verbatim from `CLAUDE.md` when the records were adopted (2026-10-01; the whole file is
frozen as `archive/CLAUDE_2026-10-01.md`). Paths are written from the repo root; "under
Conventions" in older docs means this file.*

## Conventions

- **Titles.** The book itself carries hardly any — most poems are untitled and the slug does the
  identifying. So `english_title` is normally **Ben's** to fill, as a translator's title, while he
  works on a poem (`war-delirium` → "Shell Shock"); `persian_title` holds only a title actually
  printed above the poem. An agent should still not invent one: leave both empty, and if a title
  seems called for, propose it rather than write it. Where Ben has titled an untitled poem, say so in
  meta `notes` so the English title is never mistaken for the Persian's.
- **The English does not have to mimic the Persian's punctuation.** Ben's direction: it has to breathe
  on its own. Where the Persian's pointing carries meaning worth keeping — a repetition that is doing
  structural work, an ellipsis that holds a pause, a bare plural — say so in `===footnotes===` and
  keep *that*, rather than reproducing comma placement.
- **Slugs** are lowercase, hyphen-separated English words (`shadow-daughter`, `ancient-tree`). The slug is the filename stem for both `poems/` and `meta/`, and the HTML anchor id. It is also shown on the rendered site as a muted monospace tag — under each title in the TOC and in each poem's header — so a poem on the page maps straight back to its `poems/<slug>.poem` file.
- **Dates** are freeform strings. Both Gregorian and Solar Hijri dates are welcome in the same field, separated by ` - ` (Gregorian first), e.g. `1988 - ۱۳۶۷`. Convention for the Gregorian half: map the Solar Hijri year by **its actual overlap, not a fixed offset** — a SH year runs ~21 Mar to ~20 Mar, so it spans two Gregorian years. If the source names a month or season, pin the Gregorian year to it: **months 1–9 (spring → autumn, Farvardin–Azar) → SH year + 621; the winter months 10–12 (Dey–Bahman–Esfand) → SH year + 622** (Dey itself straddles the New Year, so round it to +622). Thus `بهار ۱۳۶۸` (spring) → **1989**, `اسفند ۱۳۶۷` and `زمستان ۱۳۶۷` (Esfand / winter) → **1989**, but `۱۳۶۷/۲` or `۱۳۶۷/۹` (spring/autumn) → **1988**. With no month or season given, default a bare `۱۳xx` to + 621. **When the source gives a day**
  (`۱۳۶۸/۱۰/۶`), compute the Gregorian date instead of rounding — 6 Dey ۱۳۶۸ is 27 December 1989,
  where the +622 winter rounding would say 1990. The rounding rule exists for month-only and
  season-only dates; a day-level date can honour the actual-overlap principle exactly. Keep the season/month in the Persian half (`1989 - اسفند ۱۳۶۷`).
- **meta `notes` vs `===footnotes===`** — opposite audiences, easy to mix up. The `===footnotes===` section of a `.poem` is **published**: it renders under the poem as "Translator's Notes" (word choices, cultural context, variants — for the reader). The `notes` field in the `===meta===` section is **private**: it is parsed but never shown on the site — curator/provenance commentary for collaborators (source file, OCR caveats, why a slug or rendering was chosen). Put reader-facing notes in `===footnotes===`; put behind-the-scenes notes in meta `notes`.
- **Photograph the page before trusting a transcription.** Two preface sections were rebuilt
  from photographs of the printed/handwritten source (`preface/01`, `preface/04`), and in both
  cases the inherited transcription had errors no amount of close reading could have caught:
  a `دائم` read as `دانم` (which inverted a Szymborska quotation), two footnote markers
  attached to the wrong sentences, and — on the handwritten final page — invented words
  (`گاتهام‌ها`, `کامنگل`) that a previous English had faithfully translated. **Read the image
  directly; do not run it through OCR and translate the output.** When a reading stays
  uncertain, mark it `lacuna` (`⟨…⟩`) rather than guessing, and record the superseded
  transcription in an HTML comment so nothing is lost. See `docs/adr/0002-*`. A withdrawn line
  that is good English but nobody's translation goes in `docs/ghost-lines.md` rather than quietly
  out of existence.
- **The book is chronological** — 99% concordant across every poem with both a page and a date, so
  an unconverted page's date can be interpolated from its neighbours and a poem whose date fights
  its page number is worth re-checking. `docs/chronology.md` holds the page↔year map, what the
  remaining pages should contain, and which gaps are worth photographing next; regenerate it after
  each conversion batch.
- **Preface quotations vs. the canonical English.** Several poems quoted in the preface also
  stand in `poems/` — sometimes in a variant wording, since the essayists quote from the printed
  book. The preface keeps its **own rendering**, pitched to serve the argument the essayist is
  making around it (Farrokhi glosses `تا ماه با تو بگوید` as the moon *speaking for* the poet, so
  the preface reads "so that the moon… may speak with you," where Ben's finished `quiet-moon`
  reads "until you hear from the moon"). The canonical English for the poem itself is always the
  one in `poems/`; the `poem-cite` slug link is what ties the two together, so the difference is
  visible to the reader instead of hidden. Do not silently overwrite either side to match the other.
- **Cross-tab anchors.** Any in-page `#slug` link whose target lives in a different tab panel
  activates that panel before scrolling (handled in `TAB_SCRIPT`). This is what makes a preface
  `poem-cite` work, and it lands on drafts as well as finished poems.
- **Text encoding.** All files are **UTF-8, no BOM, already NFC**. Persian diacritics are stored the
  only way Unicode allows: as **separate combining codepoints following the base letter** in logical
  order — `دِ` is `U+062F` + `U+0650`, two codepoints, and NFC does *not* fuse them. So a "character"
  count is not a letter count, and any regex that strips or matches diacritics must target the
  combining range `U+064B–U+0652` (`ً ٌ ٍ َ ُ ِ ّ ْ`) plus `U+0654` (hamza above, which is how the
  ezāfe on a word ending in ه is written: `هٔ` = `ه` + `U+0654`, *not* the precomposed `ۀ` U+06C0).
  In use across the corpus: kasra (mostly ezāfe) ≫ hamza-above > fatha > damma > shadda > fathatan.
  Note `آ` (U+0622) *is* precomposed and would split under NFD — which is why the files must stay NFC.
- **`U+200C` ZWNJ is not a diacritic but is load-bearing** — `می‌شود` vs `میشود` — and the printed book
  is inconsistent about it. **Transcribe it as printed** and note the omission rather than tidying it;
  several pages (129, 138, 188, 189) deliberately keep the book's missing joiners.
- **Use the Persian letterforms, never the Arabic lookalikes.** `ی` U+06CC not `ي` U+064A; `ک` U+06A9
  not `ك` U+0643; digits `۰-۹` U+06F0–06F9 not `٠-٩` U+0660–0669. They render near-identically and
  **silently break grep and the dedupe similarity check**, which is how four strays survived for
  months. Never use Arabic Presentation Forms (U+FB50–FDFF, U+FE70–FEFF) — those are positional
  glyph shapes, not text. A quick audit:
  ```bash
  python -c "from pathlib import Path;t=''.join(f.read_text(encoding='utf-8') for f in list(Path('poems').glob('*.poem'))+[Path('raw photos/persian_poems.md')]);print({n:t.count(c) for n,c in [('ي',chr(0x064A)),('ك',chr(0x0643)),('ة',chr(0x0629)),('ۀ',chr(0x06C0))]})"
  ```
  All four counts should be **0**.
- **Tags** are lowercase English words. Add new ones freely; update `schema.toml` notes if a tag develops a specific meaning.
- **The `machine` section** is a scratch space — the raw literal pass. It is **not** rendered in the **Poems** tab (which shows only `translation`), but in the **Drafts** tab it *does* surface as a togglable "Machine" badge alongside `lantern` and "Ben", for side-by-side comparison.
- `index.html` is committed by CI and should not be edited manually.

# 2. Preface presentation, and rebuilding two sections from source photographs

- **Status:** Accepted
- **Date:** 2026-07-27
- **Scope:** `preface/*.html`, the `.preface` CSS and `TAB_SCRIPT` in `build_collection.py`
- **Supersedes in part:** ADR 0001 §5 (the coda) — the page has now been photographed

## Context

ADR 0001 revised the preface English but left two problems standing. First, presentation:
the essayists' prose and the poems they quote shared one visual register, and the quoted
verse was actually set *smaller* than the prose around it, so a poem read as a parenthesis.
Second, provenance: §1 and §4 were transcriptions of unknown fidelity, and §4's was known
to be corrupt OCR that ADR 0001 declined to translate.

The owner then photographed both pages. Reading the images directly — rather than
re-transcribing or re-OCRing them — settled several questions that no amount of close
reading of the transcription could have settled, and falsified a few earlier decisions
(including some made in the same session that wrote this ADR's first draft).

## Decision

### Presentation

1. **A quoted poem renders as a plate**: tinted ground, gold hairline frame, a dogmoj
   flourish at its head, and verse type sized to match the Poems tab, so a poem looks the
   same wherever it appears in the book. Prose no longer outweighs verse.

2. **Verse by another hand names its poet** via `data-poet` (Wang Wei, Bashō, MacLeish,
   Szymborska). An unattributed plate is Jafari's own. This distinction was previously
   invisible: MacLeish's *Ars Poetica* sat in the same anonymous box as Jafari's own credo.

3. **A quoted poem that also stands in `poems/` carries its slug as a link** (`poem-cite`),
   and `TAB_SCRIPT` now activates the tab containing an anchor's target before scrolling,
   so the citation works across tabs and onto drafts.

4. **Translator's notes are `<details>`**, folded shut. Open notes competed with the verse
   and pushed the two bilingual columns out of register.

5. **Maxims are unmarked.** An earlier pass in this session gave each maxim a gold ◇ and
   generous spacing, which turned a dense page into a list of fortunes. The photograph shows
   a tight stack of separate paragraphs, no markers, no blank lines; the CSS now reproduces
   exactly that. Continuous prose would have been equally wrong — the print keeps the
   maxims on separate lines.

### §1, from the photograph of the printed page (p. ۷)

6. **The two footnote markers move.** ¹ and ² sit on the two closing quotations in the
   print, not on the second and fourth maxims where the transcription had them.

7. **`دانم` was never there.** The line reads
   «الهام هرچه باشد از نمی‌دانم **دائم** می‌روید.» — "whatever inspiration may be, it grows
   **continually** out of *I do not know*." With footnote ¹ this is Szymborska's Nobel
   lecture ("whatever inspiration is, it's born from a continuous *I don't know*"), with
   her *born* replaced by می‌روید, the plant-verb that runs through the page. The previous
   reading — "out of *I do not know* grows *I know*" — was an OCR artifact, and both ADR
   0001's commentary and this session's first translator's note had built on it.

8. **Punctuation restored to the print**: the colon in `شنیده‌ام:` (which marks the sentence
   as reported speech, supporting "I have heard it said: art is a life intensified"), the
   comma in `مگذار،`, no comma inside the MacLeish line, and the footnote wording and
   spellings as printed (`آرچی بالد مکلیش`, `امریکایی`).

### §4, from the photograph of the closing page

9. **The page is handwritten and signed** — a fast shekasteh cursive in the poet's own hand.
   ADR 0001 assumed print. The signature block now says so.

10. **The poet separates lines with a slash on the page.** The flat OCR ignored those
    slashes, which is why the section had been running as prose. They are rendered as line
    breaks, so the poem has its real lineation for the first time.

11. **This page gives the book its title.** Its last lines are
    بوی کاهگل / آواز پرنده — *the smell of adobe, the song of a bird*.

12. **The Persian is replaced by a direct provisional reading of the manuscript**, with
    `lacuna` (`⟨…⟩`) where the hand cannot be read with confidence, and the superseded OCR
    preserved in an HTML comment. The manuscript confirms `شناختم` (first person),
    gives `خط آبی رنگ` ("the blue line" — a painter's line) for the OCR's `خط آلی`, gives
    `کودکی‌ام را نقاشی کردم` ("I painted my childhood"), and shows `کاش باران ببارد` once
    rather than twice. It contains no `گاتهام‌ها`, `کامنگل`, `کارپوری`, or
    `گردان نان‌های ناز`; the conjectures `جوانی` and `شب‌تابی` offered earlier are withdrawn.
    One word in the sixth line is struck through by the poet himself.

## Consequences

- A new rule, recorded in `CLAUDE.md`: **read the source image directly; do not translate
  OCR output.** Every error in 6–12 above was invisible from the transcription alone, and
  one of them (`دانم`) had already been reasoned about at length and confidently defended.
- Two withdrawn English lines were good enough to keep as English, and are recorded in
  `docs/ghost-lines.md` so they neither re-enter the book as translations nor disappear: "tonight I
  painted the bruise-blue sound of my song" (from §4, an OCR split of `کبوترانم`, "my doves") and
  "out of *I do not know* grows *I know*" (from §1, the `دائم`/`دانم` misreading).
- §4 is still marked `needs-work`. It is no longer nonsense, but the ⟨…⟩ patches want a
  fluent reader of the hand. That is now a reading problem, not a sourcing problem.
- Open follow-up carried over from ADR 0001 §6: whether to reconcile the preface's quotation
  of the tower poem with Ben's finished `old-news`. Current policy — the preface keeps its
  own rendering, pitched to the essayist's argument, and the `poem-cite` link exposes the
  divergence rather than hiding it — is written into `CLAUDE.md` under Conventions.

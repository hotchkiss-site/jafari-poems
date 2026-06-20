# 1. Preface translation revision and rendering conventions

- **Status:** Accepted
- **Date:** 2026-06-19
- **Scope:** `preface/*.html` (front matter only)

## Context

The four preface sections (`preface/01`–`04`) were carried over as lightly-edited Google
Translate output. A close read against the Persian (recorded in `claude-comment.md`)
found one outright error, several places where loaded terms and wordplay had collapsed,
and inconsistent rendering of recurring keywords across the three essayists (Jafari,
Khosrow Sinai, Bajlan Farrokhi). The owner asked that the recommendations be applied to
the files.

This ADR records the editorial decisions, since they are judgment calls a future editor
(or a re-translation pass) should be able to see and revisit.

## Decision

1. **Apply the reworked English** from `claude-comment.md` to the `english` columns of
   `preface/01`, `02`, and `03`. Persian source text is left intact (it is the original),
   except two clear transcription typos in §2 corrected so the words are readable:
   `غیبغب → غبغب` (the pigeon-throat/dewlap idiom) and `تقرعن → تفرعن` ("playing the
   pharaoh").

2. **Fix the one hard error:** `صورتگر` (sūrat-gar, *image-maker / painter*) was rendered
   "sculptor" in Farrokhi's introduction. Corrected to "image-maker / painter" in all
   three places it occurs. (Where Farrokhi genuinely means sculptor — Michelangelo — he
   uses `پیکرتراش`, which stays "sculptor.")

3. **Adopt cross-cutting rendering conventions** so the same Persian reads the same way
   throughout the book:
   - `شوق` → *ardor / ardent longing* (not "passion")
   - `شدن` → *becoming* (kept as a noun where Farrokhi uses it as one)
   - `تابلو` → *tableau / painting* (Farrokhi's keyword: poem-as-painting)
   - `هم‑` compounds rendered as parallel "one-heart / one-tongue / one-voice" chains
   - `رندی` → *roguish grace* (the Hafezian libertine-sage sense), not "wit"
   - `غبطه` → *admiring envy* (the benign kind, distinct from malicious `حسد`)
   - the satirical cluster kept vivid: *puffs out his jowls*, *plays the pharaoh*,
     *breeds a retinue of yes-men*, *force-feed* (`حقنه`)
   - `خاک` → *clay* (so the book's title phrase *بوی خاک*, "smell of clay," rings inside
     Farrokhi's love-poem quotation)
   - one misparse fixed: the waterfall poem's opening is first-person identification —
     *"I am that blithe and drunken waterfall…"*, not "That waterfall — I am its joy."

4. **Standardize romanization to "Ebrahim"** (`Mohammad Ebrahim Jafari`) across the
   preface, matching `meta/*.toml`, `CLAUDE.md`, and the build's default author string.
   The preface had used "Ibrahim."

5. **Leave §4 (the coda) provisional.** Its Persian is corrupt OCR (e.g. `گاتهام‌ها`
   reads "Gothams"; several other tokens are scanner artifacts), not difficult Persian.
   No faithful translation is possible. The section keeps its existing
   `needs-work` / "retranslation needed" marking. The correct fix is to re-source the
   lines from the printed book, not to translate scanner noise.

6. **Do not rewrite the translator's finished `poems/old-news.poem`.** Farrokhi block 8
   quotes the same poem that lives in the collection as `old-news` (*آخرین خبر*); the two
   English versions diverge. The preface quote was tightened to a closer literal
   rendering, but the collection poem — the translator's own freer, finished work — is
   left untouched. The divergence is surfaced here as an open editorial decision for the
   owner rather than resolved unilaterally.

## Consequences

- The preface now reads as considered translation rather than machine draft, and key
  terms are consistent across the three essays.
- `claude-comment.md` remains the working analysis with the etymological reasoning behind
  each change; this ADR is the durable summary.
- Open follow-ups for the owner: (a) recover and re-translate the §4 coda from the print
  source; (b) decide whether to reconcile the two `old-news` / tower-poem translations,
  and in which direction.
- A new convention is established: architecture/editorial decisions live in
  `docs/adr/NNNN-title.md`.

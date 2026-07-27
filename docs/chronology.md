# Chronology: what the page order tells us

**The book is arranged by composition date.** Of the 87 poems converted so far, 82 carry both a
page number and a datable year, and they are **98% concordant** — 57 out-of-order pairs out of
3,321. That is strong enough to plan by: an unconverted page's date can be interpolated from its
neighbours, and a poem whose date fights its page number is worth re-checking against the
photograph.

Generated from `poems/*.poem` metadata; regenerate after each conversion batch.

## Page → year, as it stands

| pages | Solar Hijri | Gregorian | what is there |
| --- | --- | --- | --- |
| 13–40 | ۱۳۳۷–۱۳۴۲ | 1958–1963 | the earliest work: Borujerd, the road, the waterfall, the peasant |
| 48–65 | ۱۳۶۰–۱۳۶۷ | 1981–1988 | **the Iran–Iraq war** |
| 66–100 | ۱۳۶۸ | 1989–90 | the year after the ceasefire — painting, doves, the Alizadeh letter |
| 101–109 | ۱۳۶۹ | 1990 | Isfahan, Nowruz, the young painters, the doves let go |
| 127–131 | ۱۳۷۰ | 1991 | |
| 149 | ۱۳۷۲ | 1993 | |
| 202 | ۱۳۸۰ | 2001 | |

Rate of travel between page 89 and page 202: about **9 pages per year**.

## The war window is pages 48–65, and it is done

Nineteen converted poems fall inside ۱۳۵۹–۱۳۶۷ (Sept 1980 – Aug 1988), and every one of them
sits between pages 48 and 65: `shadow-daughter`, `shepherd-figs`, `bomb-kiss`, `green-woodpecker`,
`barren-cloud`, `drink-sea`, `horse-hooves`, `sunless-gaze`, `green-pond`, `gray-kisses`,
`one-thing`, `shelter-wall`, `jungle-bomb`, `jungle-refuge`, `laugh-cry`, `laughed-wept`,
`snow-without-you`, `dotar-player`, `jungle-to-sea`.

Page 66 onward is ۱۳۶۸ — entirely after the August 1988 ceasefire. So **the front-line material
is behind us, not ahead**: the bombs, the shelter, the missiles over Tehran, and the nights Sinai
describes in his preface (the dutar, "the woods are full o' brambleberries") all belong to
pages 58–65. What follows is war-haunted rather than war-time — `war-delirium` (p68) and
`two-explosions` (p83) are both ۱۳۶۸ retrospects.

**Two gaps are where more war material would be.** Both are behind us in the book, and neither is
photographed yet:

- **Pages 42–46** — the largest chronological hole in the book, and now known to be five pages
  rather than seven. Ben confirmed against the printed book (July 2026) that `oldest-song` (۱۳۴۵) is
  page **41** and `fifty-moons` (۱۳۵۱) is page **47**, so the two poems already in the collection
  *bracket* the gap rather than sitting inside it. What is missing therefore runs ۱۳۴۵–۱۳۵۱ at the
  edges and, by interpolation, ۱۳۴۶–۱۳۵۹ in between: the late Pahlavi years, the revolution
  (۱۳۵۷), and the war's outbreak (Shahrivar ۱۳۵۹). **Still the highest-value pages in the book to
  photograph.**
- ~~Pages 27, 55~~ — **not missing.** Poems in this book run onto a second page often enough that
  an absent page number is more likely a continuation than a gap. Eight are known so far:
  `almond-flowers` 23-24, `drunk-waterfall` 26-27, `with-you` 38-39, `horse-hooves` 54-55,
  `letter-alizadeh` 79-82, `sparrow-hunter` 102-103, `look-again` 104-105, `not-having` 108-109.
  **Check the neighbours before calling a page missing.**

## What the remaining ~200 pages should hold

At roughly 9 pages a year from page 89 (۱۳۶۸) through page 202 (۱۳۸۰), pages 90–300 run about
**۱۳۶۸ to ۱۳۹۰ — 1989 to 2011**: the reconstruction years and then two decades of late work, the
poet from his mid-fifties into his seventies. Expect the painting poems to keep going (they
dominate pages 71–89), and expect aging, and the deaths of contemporaries, rather than the war.

## Recovering page numbers from the Adobe dumps

The three `raw-jafari-adobe-*.txt` dumps preserve the printed page footers, twice per block —
once after the Persian half and once after the English. So a block falling wholly between two
marker pairs is on the page between them, and two consecutive markers *inside* a block mean the
printed page broke mid-poem. That is enough to place poems the dumps left unnumbered:

| poem | page | basis |
| --- | --- | --- |
| `blowing-winds` | **29** | between the 28 pair and the 30 pair; only one page available |
| `longest-shadow` | **31** | between the 30 pair and the 32 marker |
| `half-ghazal` | **33** | between the 32 pair and `road-peasant` on 34 |
| `moon-crystal` | **37** | bounded 37–39 by the markers; forced once `with-you` was confirmed |
| `with-you` | **38-39** | bounded 37–39; Ben confirmed the span |
| `oldest-song` | **41** | follows the 40 pair immediately; Ben confirmed |
| `fifty-moons` | **47** | inferred 41–47 by date; Ben confirmed the page |

All seven are now set. The first three were tight enough to assert from the markers alone; the last
four were left as bounded inferences in each poem's meta `notes` — a page can hold two poems (25,
61, 62 and 66 each do), so one-poem-one-page is not safe on its own — and Ben confirmed them
against the book. Every inference the markers produced turned out right, which is worth knowing
next time: **the dumps' footers are trustworthy, the one-poem-per-page assumption is not.**

`rain-forgotten` (۱۳۶۸) and `nightingale-cloud` (۱۳۸۰) have no markers anywhere near them; by
date they belong around pages 66–100 and 202 respectively.

**The dumps are fully harvested.** Every run of Persian in all three of them is already in a
`.poem` file — checked line by line, normalised. There is no unconverted material hiding in the
text sources, so new poems can only come from photographs.

## Pages still unconverted

Behind the front: **1–11, 14–21, 42–46** — twenty-four pages, down from thirty once the recovered
and confirmed page numbers landed. These are holes in the Adobe dumps, not
deliberate omissions; anything photographed there is new material.

Ahead: **110–126, 132–148, 150–201, 204+.** Pages 61–109 are transcribed in
`raw photos/persian_poems.md` and fully converted; the next photograph batch continues at page 110.

## Three inversions worth checking against the page

- **`winter-studio` (p90, ۱۳۷۰/۹/۲۷ = 18 December 1991)** sits among pages dated ۱۳۶۸–۱۳۶۹. It is
  the single largest local inversion in the book and the reason the concordance slipped from 99% to
  98% when pages 90–109 came in. Confirm the folio digit and the date line against the photograph.

- **`snow-beautiful` (p203, ۱۳۷۰) after `morning-glory` (p202, ۱۳۸۰).** One of the two dates is
  probably wrong, or the book's last section is not chronological. Check both when those pages are
  photographed.
- **`dark-city` (p13, ۱۳۴۷) and `city-smoke` (p25, ۱۳۴۷)** sit among ۱۳۳۷–۱۳۴۱ material. Both came
  from the Adobe dumps rather than a photograph, so the dates are the likelier suspect.

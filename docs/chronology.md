# Chronology: what the page order tells us

**The book is arranged by composition date.** Pages **1–20 are the preface**; page **21** carries
the book's one out-of-sequence poem, a frontispiece; the chronological run proper begins on page 22.
Across that run, 80 poems carry both a page number and a datable year and they are **99.2%
concordant** — 26 out-of-order pairs out of 3,160. That is strong enough to plan by: an unconverted
page's date can be interpolated from its neighbours, and a poem whose date fights its page number is
worth re-checking against the page — three times now, doing so has found a wrong page number rather
than a wrong date.

Generated from `poems/*.poem` metadata; regenerate after each conversion batch. **Parse both
calendars when you do** — an earlier pass of this file read only the Persian half of `date_written`
and so missed the book's largest anomaly entirely, because that poem's date is recorded as
"Autumn 1989" with no `۱۳xx` in it.

## Page → year, as it stands

| pages | Solar Hijri | Gregorian | what is there |
| --- | --- | --- | --- |
| 1–20 | — | 2017 | the preface: Jafari's own page (۷), Sinai, Farrokhi |
| 21 | ۱۳۶۸ | 1989 | `bird-behind-wall` — the opening poem, out of sequence by design |
| 22–40 | ۱۳۳۷–۱۳۴۲ | 1958–1963 | the earliest work: Borujerd, the road, the waterfall, the peasant |
| 41–47 | ۱۳۴۵–۱۳۵۱ | 1966–1972 | the gallows, the dark city, the city of smoke |
| 48–65 | ۱۳۶۰–۱۳۶۷ | 1981–1988 | **the Iran–Iraq war** |
| 66–100 | ۱۳۶۸ | 1989–90 | the year after the ceasefire — painting, doves, the Alizadeh letter |
| 101–109 | ۱۳۶۹ | 1990 | Isfahan, Nowruz, the young painters, the doves let go |
| 127–131 | ۱۳۷۰ | 1991 | |
| 149 | ۱۳۷۲ | 1993 | |
| 202 | ۱۳۸۰ | 2001 | |

Rate of travel between page 89 and page 202: about **9 pages per year**.

## The war window is pages 48–65, and it is done

Seventeen converted poems fall inside ۱۳۵۹–۱۳۶۷ (Sept 1980 – Aug 1988), and every one of them
sits between pages 48 and 65: `shadow-daughter`, `shepherd-figs`, `bomb-kiss`, `green-woodpecker`, `barren-cloud`, `drink-sea`, `horse-hooves`, `sunless-gaze`, `green-pond`, `gray-kisses`, `one-thing`, `shelter-wall`, `jungle-bomb`, `laugh-cry`, `snow-without-you`, `dotar-player`, `jungle-to-sea`.

Page 66 onward is ۱۳۶۸ — entirely after the August 1988 ceasefire. So **the front-line material
is behind us, not ahead**: the bombs, the shelter, the missiles over Tehran, and the nights Sinai
describes in his preface (the dutar, "the woods are full o' brambleberries") all belong to
pages 58–65. What follows is war-haunted rather than war-time — `war-delirium` (p68) and
`two-explosions` (p83) are both ۱۳۶۸ retrospects.

## The revolution is missing from the book, not from the photographs

Pages 42–46 were photographed in July 2026 and the eighteen-year jump they were thought to hide is
gone. The run 41–47 is now continuous and it is **all early**:

| page | poem | date |
| --- | --- | --- |
| 40 | `life-tune` | ۱۳۴۲ (1963) |
| 41 | `oldest-song` | ۱۳۴۵ (1966) |
| 42 | `lone-cross` | ۱۳۴۷ (1968) |
| 43–44 | `dark-city` | ۱۳۴۷ (1968) |
| 45–46 | `city-smoke` | ۱۳۴۷ (1968) |
| 47 | `fifty-moons` | ۱۳۵۱ (1972) |
| 48 | `shadow-daughter` | ۱۳۶۰ (1981) |

**Pages 47 and 48 are adjacent, and nine years apart.** ۱۳۵۲–۱۳۵۹ — 1973 to 1980, the last years of
the Shah, the revolution of ۱۳۵۷, and the war's outbreak in Shahrivar ۱۳۵۹ — has no page in this
book. Nor can it be hiding behind page 22: pages 1–20 are the preface and page 21 is the
frontispiece. Whatever the reason — not written, not kept, not chosen for
this volume — the silence is the book's own, and it is worth knowing before anyone goes looking for
more.

Pages 42–46 also turned out to be the darkest stretch of the early book rather than the political
one: gallows and hyenas in ۱۳۴۷, a city whose constables burn the brushwood of ignorance, a city of
smoke. That is 1968, a decade before the revolution.

## Poems that run onto a second page

An absent page number is more often a continuation than a gap. Ten are known:
`almond-flowers` 23-24, `drunk-waterfall` 26-27, `with-you` 38-39, `dark-city` 43-44,
`city-smoke` 45-46, `horse-hooves` 54-55, `letter-alizadeh` 79-82, `sparrow-hunter` 102-103,
`look-again` 104-105, `not-having` 108-109. **Check the neighbours before calling a page missing** —
27 and 55 both looked like holes and were not.

## What the remaining ~200 pages should hold

At roughly 9 pages a year from page 89 (۱۳۶۸) through page 202 (۱۳۸۰), pages 110–300 run about
**۱۳۶۹ to ۱۳۹۰ — 1990 to 2011**: the reconstruction years and then two decades of late work, the
poet from his mid-fifties into his seventies. Expect the painting poems to keep going (they
dominate pages 71–109), and expect aging, and the deaths of contemporaries, rather than the war.

## Recovering page numbers from the Adobe dumps

The three `raw-jafari-adobe-*.txt` dumps preserve the printed page footers, twice per block — once
after the Persian half and once after the English. So a block falling wholly between two marker
pairs is on the page between them, and two consecutive markers *inside* a block mean the printed
page broke mid-poem. That is enough to place poems the dumps left unnumbered:

| poem | page | basis |
| --- | --- | --- |
| `blowing-winds` | **29** | between the 28 pair and the 30 pair; only one page available |
| `longest-shadow` | **31** | between the 30 pair and the 32 marker |
| `half-ghazal` | **33** | between the 32 pair and `road-peasant` on 34 |
| `moon-crystal` | **37** | bounded 37–39 by the markers; forced once `with-you` was confirmed |
| `with-you` | **38-39** | bounded 37–39; Ben confirmed the span |
| `oldest-song` | **41** | follows the 40 pair immediately; Ben confirmed |
| `fifty-moons` | **47** | inferred 41–47 by date; Ben confirmed the page |

Every inference the markers produced turned out right, which is worth knowing next time: **the
dumps' footers are trustworthy where they are legible, and the one-poem-per-page assumption is
not.** But two markers were legible and *wrong* — see the next section — so a marker-derived page
number is a hypothesis until a photograph confirms it.

`nightingale-cloud` (۱۳۸۰) has no marker anywhere near it and is the one poem still without a page
number; by date it belongs near 202. (`rain-forgotten` was in the same position until it was merged
with the page-73 conversion.)

**The dumps are fully harvested.** Every run of Persian in all three of them is already in a
`.poem` file — checked line by line, normalised. There is no unconverted material hiding in the
text sources, so new poems can only come from photographs.

## Corrections a photograph has made

- **`dark-city`: page 13 → 43-44.** The `۱۳` / `13` markers bracketing it in
  `raw-jafari-adobe-1.txt` are almost certainly `۴۳` with the `۴` lost.
- **`city-smoke`: page 25 → 45-46.** From a `25` marker in `raw_Jafari-adobe-2.txt`; page 25 belongs
  to `sky-swallows` alone.

Both were flagged in an earlier version of this file as inversions, with the guess that "the dates
are the likelier suspect." **That guess was wrong in both cases** — the ۱۳۴۷ dates were right and
the page numbers were wrong. Worth remembering: dates in this book come from the poet's own line at
the foot of the poem and are hard to corrupt; page numbers come from scanner footers and are easy to.

Both poems' Persian has also been re-transcribed from the photographs, which restored the ezāfe
diacritics, the line breaks the dumps had merged, and one real semantic aid — the fatha on `مانَد`
("resembles"), where the dump's bare `ماند` could be read as "remained."

## Pages still unconverted

**Behind the front: none.** Pages 1–20 are the preface and pages 21–109 are complete — every page
accounted for, either by a poem or as the second page of one. The run of "missing" early pages that
this file tracked for several revisions was an artifact of two wrong page numbers and of not knowing
where the preface ended.

Ahead: **110–126, 132–148, 150–201, 204+.** Pages 42–46 and 61–109 are transcribed in
`raw photos/persian_poems.md` and fully converted; the next photograph batch continues at page 110.
`nightingale-cloud` (۱۳۸۰) is the only poem in the collection without a page number; by date it
belongs near 202.

## Inversions worth checking against the page

- ~~`bird-behind-wall`~~ — **resolved, and not an error.** Recorded as page 12, it looked like the
  book's largest anomaly: a ۱۳۶۸ poem sitting on one side of 40 inverted pairs. Ben confirmed it is
  page **21** — the first page after the preface, before the chronological sequence starts on 22. It
  is the book's frontispiece, placed for effect. The lesson is the one this file keeps learning from
  a different direction: *the page number was wrong, and then the anomaly was not an anomaly at all.*
- **`winter-studio` (p90, ۱۳۷۰/۹/۲۷ = 18 December 1991)** sits among pages dated ۱۳۶۸–۱۳۶۹. The
  largest *local* inversion. Confirm the folio digit and the date line against the photograph.
- **`snow-beautiful` (p203, ۱۳۷۰) after `morning-glory` (p202, ۱۳۸۰).** One of the two dates is
  probably wrong, or the book's last section is not chronological. Check both when those pages are
  photographed.

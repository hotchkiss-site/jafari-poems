# 3. The translation layer is Ben's; resolving the pages 61–69 import

- **Status:** Accepted
- **Date:** 2026-07-27
- **Scope:** `poems/*.poem` — 11 files corrected, 4 duplicate files removed
- **Rule it enforces:** `CLAUDE.md` → `.poem` format → the three English layers

## Context

`CLAUDE.md` reserves `===translation===` for Ben's own hand and sends agent work to
`===lantern===`. It also permits one exception: *"when Ben explicitly asks you to stand in and draft
a translation for him to revise later (e.g. the page 61–69 bulk import) — then you may stage a
translation here, but keep the poem `draft = true`."*

That exception was taken, and it did not survive contact with the UI. Eleven poems ended up with an
agent rendering in the translation slot, which the Drafts tab labels **"Ben"** — so the site was
attributing agent English to the owner of the book, in his own repo, under his own name. Ben read the
page and said, correctly, "I'm pretty sure those aren't mine — those are yours."

The same import had a second failure. It did not dedupe against poems already in the repo, so it
created **four duplicate files** — and in three of those cases the duplicate carried an agent
translation while the original carried Ben's, which is how one poem came to exist twice with two
different "finished" Englishes.

## Decision

1. **Withdraw every agent rendering from `===translation===`.** Where the poem already had a lantern,
   the staged rendering (the more refined of the two agent passes) becomes the lantern and the
   earlier crib is superseded — git history keeps it. `date_translated` is cleared, since it recorded
   the date of an agent pass, and each file's meta `notes` records what moved and why.

   Affected: `snow-without-you`, `dotar-player`, `jungle-to-sea`, `drop-of-red`, `war-delirium`,
   `desert-moonlight`, `nightingale-cloud`, and — via the merges below — `jungle-bomb`, `laugh-cry`,
   `soul-mold`, `rain-forgotten`.

2. **Merge the four duplicates into one file each.** Ben's file survives, keeping its slug and its
   translation untouched; the import's better Persian, machine pass, footnotes and metadata come
   across; the import's staged rendering becomes the lantern.

   | page | Ben's file (kept) | duplicate (deleted) | why the import's Persian was better |
   | --- | --- | --- | --- |
   | 61 | `jungle-bomb` | `jungle-refuge` | the older text read `نمناران`, a corruption of `بمباران` |
   | 62 | `laugh-cry` | `laughed-wept` | the older text had dropped the `۱۳۶۷/۹` dateline |
   | 66 | `soul-mold` | `lovers-breath` | the older text lost the trailing `...؟...` and carried a stray tab |
   | 73 | `rain-forgotten` | `rain-memory` | both agent-made; the page-73 side is photograph-derived |

3. **Abandon the standing exception.** An agent may draft a rendering, and it goes in `lantern`. If
   Ben wants a translation stood up for him to revise, that is a request per poem, and the file must
   say so in its `notes` — not a general licence that a later reader has no way to detect.

## How to tell whose English it is

Written down because it was not obvious from the files, and cost a session to reconstruct:

- **`draft = false` + a translation is Ben's.** All 18 of them. That is the reliable signal.
- **`draft = true` + a translation was the import's.** After this ADR, no file is in that state, so
  the state itself is now the alarm.
- **Ben's voice is recognisable.** Lower case where a machine would capitalise; `&` for *and*;
  bracketed glosses (`[there is] a lady [that] I love`); contractions and asides (`Y'know`); dates as
  `4-3-2026`; a willingness to be loose where an agent is careful. Agent English runs to em-dashes,
  consistent ellipses, and tidy line breaks.

## Consequences

- 84 poems, down from 88; no poem exists twice; no `draft = true` poem holds a translation; the
  "Ben" badge in the Drafts tab now appears only where Ben wrote the words.
- Ben's 18 finished translations are byte-identical to what they were before this change.
- Three of the four merges also fixed the Persian, so the deduplication improved the text as well as
  the count.
- **The dedupe step in `jafari-conversion-skill.md` needs teeth**: exact-match grep was what failed.
  One-letter OCR differences (`نمناران`/`بمباران`, `باران`/`یاران`) defeat it, and both defeated it
  here. That file now specifies a similarity check over normalised Persian.
- Open question for Ben, recorded in `rain-forgotten`'s notes: page 73 reads `های... یاران...`
  ("hey... friends...") in the photograph transcription and `های... باران...` ("hey... rain...") in
  the Adobe dump. The poem's next line is `تو می‌باری`, "you are raining", and page 95 addresses
  `بارانِ من` — so the sense favours `باران`. Needs the page.

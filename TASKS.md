---
type: tasks
scope: project
domain: websites
title: jafari-poems — tasks
status: active
inherits: CLAUDE.md
applies_to: []
last_verified: 2026-10-01
built_against: corpus-conventions@v3
supersedes: null
---

# jafari-poems — tasks

*One line per open item. A closed line is deleted; how it closed goes in the log entry. The
order under *Now* is Ben's call. The page-by-page detail is in `docs/chronology.md`.*

## Now — Ben

- [ ] 🧑 **Photograph page 200 onward** — the next batch. 200–201 and 204+ are unconverted; 202–203 came from the Adobe dumps and were never photographed. `photo-batch-200`
- [ ] 🧑 **Photograph pages 21–41 and 47–60** — the Adobe-dump imports, never photographed; ten poems there carry suspect readings (`docs/chronology.md` lists them). `early-pages-photos`
- [ ] 🧑 **Page 73, `rain-forgotten`** — یاران or باران? The sense favours باران; needs the page (ADR 0003). `rain-forgotten-p73`
- [ ] 🧑 **The preface's §4 coda** — still `needs-work`: the ⟨…⟩ patches want a fluent reader of the hand (ADRs 0001, 0002). `preface-coda`
- [ ] 🧑 **`old-news` and the preface's tower poem** — reconcile the two translations, and in which direction, or keep both (the current policy, ADR 0002). `old-news-reconcile`
- [ ] 🧑 **Delete `_to_delete/`** — tracked in git, cited nowhere: the June incoming bundle and the split-era `meta/` files. `to-delete`

## Agent work

- [ ] 🤖 **Convert the next batch** — per `jafari-conversion-skill.md`; drafts, `translation` left empty; regenerate `docs/chronology.md`. Waits on: `photo-batch-200`. `convert-200`
- [ ] 🤖 **Re-read the early pages** — check the ten suspect readings against the photographs, the image read directly. Waits on: `early-pages-photos`. `early-pages-verify`

## Unknowns

- [ ] ❓ **`snow-beautiful`'s place** — page 203, dated to the ۱۳۷۰s decade, after page 199's ۱۳۸۶. Test: the photograph of pages 200–204. `snow-beautiful-date`

## Later

- [ ] 🧑 **Translate the drafts** — 144 of 164 poems are `draft = true`, their `translation` left for Ben. `translate-drafts`
- [ ] 🧑 **What Pages serves** — it publishes the repo root, so `/CLAUDE.md` and the raw dumps answer on the live site. Publish only the book (an Actions artifact)? `pages-scope`

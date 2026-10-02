---
type: log
scope: project
domain: websites
title: '2026-10-01 · desk — records adopted, lightly; the changelog split; CLAUDE.md cut to the layers rule'
status: active
inherits: ../CLAUDE.md
applies_to: []
last_verified: 2026-10-01
built_against: corpus-conventions@v3
supersedes: null
---

# 2026-10-01 · desk — records adopted, lightly; the changelog split; CLAUDE.md cut to the layers rule

*From the websites root session (entry `2026-10-01-3` there). Tier: minimum, with the ADRs as
the decision record, and a light sort (Ben). Done in the `corpus/websites` clone; the
`jaanam/translation` clone was level with it at `66d8d93`. Later the same day Ben retired
that clone, so this is the repo's only home (the settings file and `CLAUDE.md` say so).*

## The history split

`CHANGELOG.md` held five dated blocks, newest first. Each is now an entry, verbatim, gaining
front matter and one italic provenance line:

- `log/`: `2026-07-27-1`, `2026-07-19-2`, `2026-07-19-1`, `2026-07-11-1`.
- `archive/log/`: `2026-06-18-1`, the sixth-newest once this entry exists.

**Non-blank lines in = out: 134 = 134, identical and in order** (re-read from the written
files). The two 2026-07-19 blocks landed in one commit (`8fb8848`); file order puts *Recombine
metadata* first (`-1`) and *Unwan carpet header* second (`-2`). The changelog itself is frozen
as `archive/CHANGELOG_2026-07-27.md`; nothing live cited it.

## The sort

| Doc | Kind · state | Now |
|---|---|---|
| `CLAUDE.md` (3,043 words) | agents doc | frozen as `archive/CLAUDE_2026-10-01.md`; rewritten at 927 words. It keeps the layout, **the three English layers** verbatim, building, and where knowledge goes |
| — its *File formats* … *Adding a preface section* | spec · live | `docs/FORMATS.md`, verbatim but for the layers rule (a pointer) |
| — its *Conventions* | spec · live | `docs/translation-conventions.md`, verbatim |
| `claude-comment.md` | the preface analysis ADR 0001 applied · ran | `archive/claude-comment_2026-06-19.md` |
| `farsi-grammar.md`, `jafari-conversion-skill.md` | live references | stay at the root by name (light sort) |
| `docs/adr/0001–0004` | decisions | stay; named in the settings file as the decision record |

Repointed:
- ADR 0001 ×3 and `docs/ghost-lines.md` → the archived analysis;
- `docs/chronology.md`, `docs/ghost-lines.md`, `jafari-conversion-skill.md` ×2 and
  `raw photos/persian_poems.md` ×3 → the new docs. The skill's `../CLAUDE.md` was already wrong from the root.

ADR 0002's "recorded in `CLAUDE.md`" lines say where a rule was written on its date, so they
stand; the conventions doc's header says what "under Conventions" means now. ADR 0003's
citation of the layers still lands.

## Stale claims fixed

`README.md` taught the pre-June `.poem` format (an `id:` header, no `===meta===`, no
`machine`/`lantern`). Its format section is now a short summary pointing at
`docs/FORMATS.md`. Two more fixes:
- The CI paths now include `preface/` and `ornaments/`.
- The address is `jafari.bbben.org`; the github.io URL 301s there.

## Checked

- **Live:** `jafari.bbben.org` answers 200.
- **Branches:** `main` only, level with `origin`, no stashes.
- **Poems:** 164, of which 144 are drafts and 20 finished.
- **Served from the repo root:** Pages serves the root, so `/CLAUDE.md`,
  `/claude-comment.md` and `/raw-jafari-adobe-1.txt` answer 200 on the site. The repo is
  public anyway; that's `pages-scope`.
- **`_to_delete/`:** tracked, cited nowhere. That's `to-delete`.

## Legacy and memory

- The logbook's legacy entry `jaanam/translation/jafari-poems/jafari-conversion-skill.md` is
  **dropped**: its checklist is a per-batch procedure, not open work. The root removes it
  from `logbook.config.json`.
- Project memory (`C--Dev-…-jafari-poems`) holds only the rule "files, not memory", which
  `CLAUDE.md` keeps.
- Jaanam's `lachak-persian-pages` cited the changelog; it now names entry `2026-07-11-1`.

**Tasks:** opened `photo-batch-200`, `early-pages-photos`, `rain-forgotten-p73`, `to-delete`,
`convert-200`, `early-pages-verify`, `snow-beautiful-date`, `translate-drafts`, `pages-scope`,
`preface-coda`, `old-news-reconcile` (the last two ADR-held follow-ups).
**Decisions:** none (the ADRs are unchanged).

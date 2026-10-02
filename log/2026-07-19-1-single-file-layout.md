---
type: log
scope: project
domain: websites
title: '2026-07-19 — Recombine metadata into the poem files (single-file layout)'
status: active
inherits: ../CLAUDE.md
applies_to: []
last_verified: 2026-07-19
built_against: corpus-conventions@v3
supersedes: null
---

*Moved verbatim from `CHANGELOG.md` on 2026-10-01, when each session became its own file (kind:
build). Nothing below this line was edited.*

## 2026-07-19 — Recombine metadata into the poem files (single-file layout)

### Why
The 2026-06-18 split (`meta/*.toml` + `poems/*.poem`) traded one editing friction for
another: every poem became two files linked only by filename stem, and day-to-day work
(translating, promoting drafts, editing notes) almost always touches both. Reversed by
preference — one poem, one file.

### What changed
- Each `poems/<id>.poem` now begins with a `===meta===` section holding the same flat
  TOML that used to live in `meta/<id>.toml`, byte-for-byte. The `meta/` directory is
  retired.
- `build_collection.py` / `build_poem.py` read the `===meta===` section from the poem
  file; the `--meta` CLI flag is gone. Rendered output verified byte-identical to the
  two-file pipeline across the collection page and all 55 single-poem pages.
- `new-poem.sh` scaffolds one file; CI no longer watches `meta/**.toml`; `schema.toml`
  wording, `CLAUDE.md`, and `jafari-conversion-skill.md` updated.
- The concern that motivated the split — backfilling a new metadata field across all
  poems — is covered by a documented one-liner in CLAUDE.md ("Adding a new metadata
  field").
- `migrate.py` (the split-era script) is kept for reference only.

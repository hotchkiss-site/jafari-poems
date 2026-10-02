---
type: log
scope: project
domain: websites
title: '2026-07-19 — Unwan carpet header (found-object ornaments; lachak retired)'
status: active
inherits: ../CLAUDE.md
applies_to: []
last_verified: 2026-07-19
built_against: corpus-conventions@v3
supersedes: null
---

*Moved verbatim from `CHANGELOG.md` on 2026-10-01, when each session became its own file (kind:
build). Nothing below this line was edited.*

## 2026-07-19 — Unwan carpet header (found-object ornaments; lachak retired)

### What changed
- The book header, tab row, and (on the Poems tab) the TOC now sit on a single
  lapis field — an unwan/carpet-page treatment. Persian title in gold; new
  tokens `--lapis` / `--gold` in build_collection.py.
- Ornaments come from the tazhib found-object library, vendored into
  `ornaments/` (corner-bhutan.svg, rule-dogmoj.svg) and inlined as data URIs at
  build time (CSS mask-image is CORS-blocked on file://, so external mask URLs
  would vanish when index.html is opened locally). The dogmoj dash replaces the
  redundant "Poems — اشعار" TOC title; Bhutanese quarter-corners mirror into
  the carpet's corners (bottom pair hides <900px and yields to the TOC's foot
  when the carpet extends).
- Tabs restyled for the lapis ground: typography only (no ornament on
  interaction chrome per WEB-ADAPTATION), active tab = gold cartouche pill
  echoing the .poem-status badge; cream focus-visible ring.
- The Drafts tab TOC deliberately stays cream — only the finished book is
  illuminated.
- lachak.js corner spandrels retired (LACHAK_CSS/LACHAK_CORNERS and the
  kit/lachak.js include removed). Register: single (interlace corners + one
  geometric dash); the palmette band auditioned well but was cut to let the
  header and TOC merge seamlessly. Candidate for reintroduction if
  Persian-specific bands join the library.

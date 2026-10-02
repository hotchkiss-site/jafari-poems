---
type: log
scope: project
domain: websites
title: '2026-07-11 — Lachak corner spandrels (shared kit ornament)'
status: active
inherits: ../CLAUDE.md
applies_to: []
last_verified: 2026-07-11
built_against: corpus-conventions@v3
supersedes: null
---

*Moved verbatim from `CHANGELOG.md` on 2026-10-01, when each session became its own file (kind:
build). Nothing below this line was edited.*

## 2026-07-11 — Lachak corner spandrels (shared kit ornament)

### What changed
- `build_collection.py` now emits four `.lachak-corner` divs (page corners), their
  positioning CSS (`LACHAK_CSS`), and a `<script src="../../kit/lachak.js">` include.
  The barg draws a static lapis/gold/ivory Persian tile spandrel (quarter-dome girih
  fan) into each; bottom pair hides below 900px so the foot stays clear.
- The ornament code itself lives in the shared jaanam kit (canonical home
  `corpus/websites/kit/lachak.js`, mirrored to `jaanam/kit/`) — not in this repo.
  **Note:** the include path assumes the jaanam layout (`translation/<coll>/` two
  levels below `kit/`); a standalone deploy of this repo would need the barg vendored
  or the path adjusted.

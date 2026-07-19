# Changelog

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

## 2026-06-18 — Split metadata from poem text (meta/ + poems/ layout)

### Why
The single-file-per-poem format (metadata header + text sections in one `.poem` file) worked well at small scale but created friction as the collection grew:
- Adding a new metadata field (e.g. `tags`, `source`) required manually editing every existing poem file to add the new key
- Metadata and poem text were edited with different cadences but lived in the same file
- The header format was informal and had accumulated inconsistencies (mismatched filenames and internal ids)

### What changed

**New layout:**
- `poems/<id>.poem` — text sections only (`===persian===`, `===machine===`, `===translation===`, `===footnotes===`), no header
- `meta/<id>.toml` — all structured metadata in flat TOML format
- The two files are linked solely by sharing the same `id` slug as their filename stem

**New files:**
- `schema.toml` — defines every allowed metadata field with type, required flag, and description. The schema is the single source of truth; new fields go here first
- `new-poem.sh` — interactive script that scaffolds both files in one step, enforcing the id slug as the link
- `migrate.py` — one-time script that performed this migration; kept for reference

**Updated:**
- `build_collection.py` — now reads `meta/*.toml` files and pairs each with its `poems/<id>.poem` counterpart; `--meta` flag added to override the meta directory path
- `build_poem.py` — updated to accept a poem ID instead of a file path; reads from both directories
- `.github/workflows/build.yml` — trigger paths updated to include `meta/` so metadata-only changes (adding a tag, updating a source) also trigger a rebuild

**Filename corrections** (mismatches between filename and internal `id` field, fixed during migration):
- `poems/adobe.poem` → `poems/bird-behind-wall.poem`
- `poems/life-tone.poem` → `poems/life-tune.poem`
- `poems/soul-mould.poem` → `poems/soul-mold.poem`

### Metadata fields (as of this migration)

| Field | Type | Notes |
|---|---|---|
| `id` | string | Required. URL-safe slug, matches filename |
| `english_title` | string | |
| `persian_title` | string | Unicode RTL |
| `date_written` | string | Freeform; may include Solar Hijri date |
| `date_translated` | string | |
| `page_number` | string | Arabic numeral, references source book |
| `persian_page_number` | string | Persian-Indic numerals |
| `source` | string | Journal, app, manuscript, etc. — new |
| `tags` | array | Thematic tags — new |
| `notes` | string | Curator/editorial notes — new |

# Changelog

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

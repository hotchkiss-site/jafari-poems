# Close-out settings — jafari-poems

*Read by the `close-out` skill (the method) and by the logbook, which reads the first table only.
The contract is `RECORDS.md` in the logbook repo. Adopted 2026-10-01.*

## Where the records are

| Record | File |
|---|---|
| Tasks | `TASKS.md` |
| Log | `log/` — the 5 newest; older in `archive/log/` |

*Minimum tier, adopted lightly (Ben, 2026-10-01). The settled calls are ADRs in `docs/adr/`,
one file each, numbered; they stand in for `DECISIONS.md`, and a new call is a new ADR. The
repo lives in `corpus/websites/` only (Ben, 2026-10-01); jaanam's homepage shelf reads it from
here by path.*

## Root exceptions

- `index.html`, `CNAME`: GitHub Pages serves the root; CI commits `index.html`, and jaanam's
  homepage (`jaanam/home/build_catalogue.py`) reads `poems/` from this clone by path and links
  the live site.
- `build_collection.py`, `build_poem.py`, `new-poem.sh`, `schema.toml`: the build and its
  schema; CI (`.github/workflows/build.yml`) runs the build by path.
- `migrate.py`: historic, kept for reference (`CLAUDE.md` → layout).
- `farsi-grammar.md`, `jafari-conversion-skill.md`: living references kept by name; Ben edits
  the grammar notes on GitHub, and `CLAUDE.md` routes knowledge to both.
- `raw-jafari-adobe-1.txt`, `raw_Jafari-adobe-2.txt`, `raw-jafari-adobe-3.txt`,
  `jafari_intro_full1.html`, `raw photos/`: the raw sources; poems' meta `source` fields cite
  the dumps by path.
- `_to_delete/`: Ben's, pending `to-delete`.

## Extra interview questions

- **Which pages or poems?** Page numbers and slugs; for a conversion batch, the count before
  and after.
- **Whose hand?** Anything written into `===translation===` is Ben's alone; an agent's English
  is `lantern`. Say which layers changed.
- **Was `draft` flipped?** Name each poem that moved to the Poems tab.
- **Did it reach the live site?** CI rebuilds `index.html` on push to `main`; say whether the
  rebuild commit landed.
- **Which task-list items did this touch?** Close, open, change, by id.

## Downstream docs to walk

1. **`CLAUDE.md`**: layout, the three layers, building. It carries no status.
2. **`docs/FORMATS.md`** / **`schema.toml`**: a field or section added or changed.
3. **`docs/translation-conventions.md`**: a convention made or changed (often with an ADR).
4. **`docs/chronology.md`**: regenerate after every conversion batch.
5. **`jafari-conversion-skill.md`**: what a batch taught.
6. **`farsi-grammar.md`**: append, never rewrite.
7. **`../STATUS.md`** (websites root): this site's row, when its stage changes.

## Commit message

`Close out YYYY-MM-DD <translation|build|desk>: <headline>`

## Kinks

- Pages serves the whole repo root (`pages-scope`): anything committed is public on the site
  too, not only on GitHub.

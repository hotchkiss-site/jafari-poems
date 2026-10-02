---
type: agents
scope: project
domain: websites
title: Jafari Poems — codebase guide
status: active
inherits: ../CLAUDE.md
applies_to:
  - "poems/**"
  - "preface/**"
  - "build_collection.py"
  - "build_poem.py"
  - "schema.toml"
last_verified: 2026-10-01
built_against: corpus-conventions@v3
supersedes: null
---

# Jafari Poems — Codebase Guide

A git-based bilingual poetry collection. The poems are translations of Mohammad Ebrahim Jafari's Persian verse. The working language of the repo is English; poem content is bilingual (Persian + English).

## Where things are

- **`docs/FORMATS.md`**: the `.poem` format, the `===meta===` fields, the preface fragments,
  adding a poem, a field or a preface section.
- **`docs/translation-conventions.md`**: titles, punctuation, slugs, dates, notes vs footnotes,
  photographing the page, the chronology, preface quotations, encoding, letterforms, tags.
- **`docs/adr/`**: the settled calls, one ADR each. **`TASKS.md`** and **`log/`**: open work
  and what each session did; settings in `.claude/close-out.md`.
- **One clone.** This repo lives at `corpus/websites/jafari-poems` only (Ben, 2026-10-01;
  the `jaanam/translation/` clone is retired). jaanam's homepage shelf reads it from here by
  path and links to the live site: experiments can read production, production never
  depends on experiments.

## Repository layout

```
poems/          one self-contained .poem file per poem — ===meta=== TOML + text sections
preface/        front matter — one self-contained HTML fragment per section
ornaments/      vendored SVG masks from the tazhib found-object library
                (corner-bhutan, rule-dogmoj) — inlined as data URIs at build time
schema.toml     authoritative list of allowed metadata fields
build_collection.py   renders preface + poems → index.html (tabbed)
build_poem.py         renders a single poem → <id>.html
new-poem.sh     interactive scaffolding for a new poem (one file)
migrate.py      historic one-time script from the 2026-06 split (kept for reference;
                the split was reversed 2026-07 — poems are single-file again)
index.html      generated output — do not edit by hand
docs/           FORMATS.md (the .poem / meta / preface formats), translation-conventions.md,
                chronology.md, ghost-lines.md, khak-sweep.md, adr/ (the decisions)
farsi-grammar.md, jafari-conversion-skill.md   kept at the root by name (farsi-grammar.md
                is edited on GitHub)
raw-jafari-adobe-*.txt, raw_Jafari-adobe-2.txt, jafari_intro_full1.html, raw photos/
                the raw sources; poems' meta `source` fields cite the dumps and
                raw photos/persian_poems.md by name
TASKS.md, log/  the records (archive/ holds what is past, never corrected)
```

The rendered `index.html` has three tabs below a shared book header:
**Preface** (the `preface/` sections), **Poems** (the TOC + finished poem sections),
and **Drafts** (poems with `draft = true` — English still in draft: a literal `machine` pass, an optional `lantern` crib, and sometimes a staged-but-unreleased "Ben" translation).

## The three English layers

The three English sections are **layers** of increasing refinement, and **who writes which layer matters** — read this before translating:

- **`machine`** — the raw OCR / machine-translation literal first pass. Scratch input, nobody's considered rendering. Leave it as the literal you started from.
- **`lantern`** — the **agent's interpretive working draft**: a crib that steps from the literal `machine` toward faithful English — resolving idiom, image, and ambiguity — without claiming to be the final hand. **This is the home for an AI collaborator's own translation work.** Optional in principle, but when an agent translates, its rendering goes here.
- **`translation`** — **Ben's finished human translation.** **Ben is the repo owner — the human you (the agent) are working with** — and this layer is labelled "Ben" in the UI because it is *his* hand. **It is Ben's slot. By default an agent does NOT write its own rendering into `===translation===`; put your work in `lantern` and leave `translation` empty for Ben.** The one exception is when Ben explicitly asks you to stand in and draft a translation for him to revise later (e.g. the page 61–69 bulk import) — then you may stage a translation here, but keep the poem `draft = true` so it stays out of the Poems tab until Ben signs off.

**This went wrong once, so it is worth stating flatly: do not put your English in
`===translation===`, even when asked to make it finished.** The Drafts tab labels that layer "Ben",
so an agent rendering placed there is published under his name. Eleven poems were in that state and
are recorded in `docs/adr/0003-translation-layer-ownership.md`, along with how to tell his hand from
an agent's — `draft = false` plus a translation is his; lower case, `&` for *and*, bracketed glosses
and contractions are his voice.

## Building

```bash
# Full collection → index.html
python build_collection.py poems/

# Single poem → <id>.html
python build_poem.py ancient-tree
```

Both scripts read self-contained `.poem` files from `poems/`. `build_collection.py` also reads `preface/` (sibling of `poems/`); pass `--preface <path>` to override. If `preface/` is absent the Preface tab is simply empty.

CI runs `build_collection.py` automatically on pushes to `main` that touch `poems/`, `preface/`, `ornaments/`, or the build script, and commits the updated `index.html`.

## Documenting session decisions (files, not memory)

Durable knowledge produced in a working session — process learnings, translation
rationale, naming/format decisions, grammar explanations — is recorded in **versioned
repo files, not in agent memory.** Memory is per-machine, invisible to collaborators and
CI, and does not travel with the repo; the repo is the shared source of truth. So when a
session generates something meant to outlast it, write it into the right file:

- **Conversion / import process** → `jafari-conversion-skill.md`
- **Repo structure and build behavior** → this file (`CLAUDE.md`); file formats →
  `docs/FORMATS.md`; translation conventions → `docs/translation-conventions.md`
- **A settled call** → a new ADR in `docs/adr/`; **what a session did** → a `log/` entry
  (the `close-out` skill)
- **Farsi grammar explanations** → `farsi-grammar.md` — one section per point; **append**
  a new section, never overwrite earlier entries or recreate the file
- **Per-poem editorial notes** → the `notes` field in that poem's `===meta===` section

When asked to "remember" a convention or explanation, default to documenting it in one of
these files rather than to memory.

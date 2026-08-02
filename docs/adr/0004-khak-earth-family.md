# 4. خاک is earth — the earth-family renderings, and how to read a recurring phrase

- **Status:** Accepted
- **Date:** 2026-07-31
- **Scope:** agent layers (`lantern`, staged translations) and `===footnotes===` across `poems/`;
  the `machine` layer is scratch and is left as imported; Ben's `===translation===` is his own hand
  and is not governed by any ADR
- **Supersedes:** the خاک → "clay" convention cited in two poem notes as "ADR 0001"

## Context

Two poem notes (`rain-complaint`, `old-blue`) cite an "ADR 0001" ruling خاک → *clay*, adopted so
that the book's بوی خاک / بوی کاهگل family would stay audible as one substance. No such file exists
in `docs/adr/` — and ADR 0002 cites "ADR 0001" as a *different* decision entirely (a revision of the
preface English). Whatever was decided in conversation, the number carries two attributions and the
file was never committed. This ADR records the خاک ruling properly; the preface ADR that 0002 cites
remains unwritten (open item below).

The 2026-07-31 review found the actual scatter: across the draft corpus خاک was rendered *clay* in
three lantern lines, *earth* in roughly a dozen, *soil* in another dozen, *dust* in two — and,
decisively, **Ben's own finished translations have always said earth** (`shadow-daughter`: "good
earth… loving earth… moist earth… fruitful earth"; `morning-glory`: "wet the dry earth").

Persian's material ladder is tidy, and the ruling follows it. خاک is the dry loose stuff — dirt,
soil, earth, dust; by extension ground, land, homeland (خاکِ وطن), and the grave. Wet it and work it
and it becomes گِل (mud); mix in straw and it is کاهگل; mold it and it is خشت. "Clay" pushed خاک one
rung up that ladder, toward the potter's bench — a stylization, not a lexical fact. And بوی خاک is
Persian's stock name for the smell of earth after rain, which is exactly the register the poems
want.

## Decision

1. **خاک → "earth" by default.** *Soil* is acceptable where roots and growing genuinely want it
   (ریشه در خاک); *dust* where the context is dry wind, ruin, or the grave. A rendering other than
   "earth" inside one of the fixed formulas (below) needs a footnote.
2. **Recurring formulas get fixed renderings**, because a formula should sound like itself wherever
   it lands: بوی خاک → **"the smell of earth"**; the triad رنگ ابر / بوی خاک / طعم اشک → **"the
   colour of cloud, the smell of earth, the taste of tears"** (old-blue and oldest-song must match).
3. **کاهگل → "adobe"** (established lantern practice, and the word family of the book's own title
   image). **گِل → "mud." خشت → "mud-brick."** "Clay" is reserved for رس / potter's contexts, of
   which the corpus so far has none.
4. خاکستری ("gray," from خاکستر *ash*) is outside this family and unaffected.

## How to read a recurring phrase (the Homer principle)

Jafari was an oral poet; he never published in his lifetime, and this book is posthumous. When a
phrase recurs across poems — بوی خاک, the cloud/earth/tears triad, مربع خنده‌ها — read it as an oral
poet's formula: a good line, easy to remember, that plays on the tongue. Not as a designed arc
through the book. Consequences for how we write about the poems:

- **Render a recurring formula consistently.** The formula is a unit of the poet's voice, and a
  reader should be able to hear that it is the same phrase — this is the argument *for* rule 2.
- **State recurrence as fact, not intention.** A note or footnote may say the triad also stands at
  page 41; it should not claim the later poem "answers," "quotes," or "completes" the earlier one.
  The book's page order is the editors'; only the formulas are the poet's.
- Existing notes written in the arc-reading register (old-blue's among them) can be softened as
  their poems come up for finalization; no bulk rewrite.

## Consequences

- Lantern lines changed 2026-07-31, each recorded in its poem's meta notes: `old-blue`
  ("smell of clay" → "smell of earth"), `rain-complaint` ("tell the clay" → "tell the earth"),
  `water-trap` ("beginning of clay" → "beginning of earth"), `oldest-song` ("smell of soil" →
  "smell of earth").
- The full inventory — every خاک / کاهگل line in the corpus and how each layer renders it, with a
  disposition per line — is in `docs/khak-sweep.md`.
- The two poem notes that cited "ADR 0001" for clay now cite this ADR.
- **Open item:** the preface-revision ADR that 0002 cites as "ADR 0001" is still missing from
  `docs/adr/`; reconstruct it from git/session history or renumber the citations in 0002.

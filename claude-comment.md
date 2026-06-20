# Preface — Translation Analysis & Recommendations

A close read of the four preface sections against the Persian. The existing English
is lightly-edited machine translation; below, each section is reworked in plain text,
followed by etymological reasoning for the changes. **Nothing in the `preface/*.html`
files was touched** — this is a working document only.

A note on method: I flag (a) outright errors, (b) places where Persian wordplay or a
loaded term collapsed in translation, and (c) recurring keywords that should be rendered
*consistently* across all three essayists. Where the Persian is dialectal or garbled by
scanning, I say so plainly rather than guess.

---

## Cross-cutting issues (read first)

These recur across sections; deciding them once keeps the preface coherent.

1. **`صورتگر` is *not* "sculptor."** In Farrokhi's opening line the machine renders
   *صورتگر و نقاش بزرگ* as "great painter and **sculptor**." `صورتگر` (sūrat-gar) =
   *image-maker / portraitist / limner* — `صورت` (ṣūra, Arabic "form, face, image") +
   `گر` (agent). It's a near-synonym of `نقاش` (painter), doubled for emphasis. Jafari
   was a painter, not a sculptor. Note that when Farrokhi *does* mean sculptor a few
   lines later — Michelangelo — he uses a different word, `پیکرتراش` (*peykar-tarāsh*,
   "figure-carver"). This is the one hard error in the preface; it recurs wherever
   `صورتگر` appears (blocks 1, 5, 8) and should be "image-maker / painter" each time.

2. **`تابلو` is Farrokhi's keyword — keep it "painting/tableau" everywhere.** He
   repeatedly calls the poems `تابلو` (tableau, the French loanword), insisting a poem
   *is* a painting. Rendering it variously ("painting," "canvas," "a remarkable
   painting") is fine, but the through-line — poem = painted tableau — should stay
   audible.

3. **`شوق` is "ardent longing," not just "passion."** `شوق` (shawq, Arabic) is *eager
   yearning, zeal, the pull toward something*. It appears in §1 ("the bridge crossed on
   the feet of `شوق`"), in the §1 poem fragment, and in Farrokhi's "in the `شوق` to
   become one." Translate it consistently as *ardor / ardent longing* so the reader
   hears it as a motif.

4. **`شدن` / "becoming."** Farrokhi twice leans on `شدن` ("to become") as a noun —
   *مدام در شدن است* ("constantly in becoming"), *در خود شدن* ("becoming inward"). Keep
   "becoming" in both; it's a deliberate, almost philosophical refrain.

5. **The `هم‑` ("co-/one-") compounds.** Persian builds intimacy by prefixing `هم`
   ("same, co-"): `همدل` (one-heart), `همزبان` (one-tongue), `هم‌آواز` (one-voice),
   `همدم` (one-breath = confidant), `همسر` (one-head = spouse), `همدلی` (one-
   heartedness), `همسرایی` (singing-as-one). The machine flattens these into "sympathy,"
   "in unison," "companion." Where the Persian stacks them rhetorically (§2 block 2; §3
   block 1) the English should preserve the parallel.

6. **Name transliteration.** The preface uses **"Ibrahim"**; the rest of the repo
   (`meta/*.toml`, `CLAUDE.md`) uses **"Ebrahim"** (*Mohammad Ebrahim Jafari*). Pick one
   and standardize. I'd keep the repo's "Ebrahim."

7. **The tower poem is a duplicate.** Farrokhi block 8 quotes the poem that already
   lives in the collection as `poems/old-news.poem` (*آخرین خبر*). The two English
   versions diverge noticeably (the standalone one is looser and longer). Worth
   reconciling so the same Persian doesn't read two different ways in one book.

---

## Section 1 — Jafari's Own Words

### Reworked translation

> The shortest ghazal I know is the weeping willow.
>
> I have heard that vital art has intensified. Love begins with an intensified gaze —
> a gaze glittering and radiant.¹
>
> If you drink today's wonder to the last drop, tomorrow you will be thirstier still.
>
> Don't carry one breath of today over into tomorrow. Whoever breathes in yesterday
> has no fresh song today.²
>
> Between tradition and modernism stands a bridge, crossed on the feet of ardent longing.
>
> > From the embracing of my soul with ardor,
> > in the wake of a writhing twist and fever,
> > a shadow sprouts
> > behind the veil of nothingness…
>
> When you look at the real anew, the real turns into an occurrence.
>
> My garden of poetry has flowered among these shadows.
>
> I believe that…
>
> > Whatever inspiration may be, out of "I do not know" grows "I know."
>
> I believe that…
>
> > "A poem should not mean, but be."
>
> — Mohammad Ebrahim Jafari, 1396 / 2017

### Notes

- **"The Mad Willow" → "the weeping willow."** `بید مجنون` (*bid-e majnun*) *is* the
  botanical weeping willow (Salix babylonica). `مجنون` (Arabic, "possessed, mad," the
  root of `جن` *jinn* and of Majnun in *Layla & Majnun*) names the tree for its drooping,
  disheveled branches. "Mad Willow" is both botanically wrong and opaque; "weeping
  willow" actually *keeps* the joke — the shortest love-poem (ghazal) he knows is a tree
  that weeps. (A footnote on the Majnun pun would be a bonus, not a necessity.)

- **Preserve the repeated `شدت یافته`.** The aphorism repeats "intensified" — *art has
  intensified… love begins with an intensified gaze*. The machine broke the parallel
  ("become more vital" vs. "intensified gaze"); the repetition is the rhetorical point.
  `درخشنده و تابناک` are two shine-words (`درخشیدن` "to glitter" / `تاب` "radiance,
  heat") — "glittering and radiant."

- **"That which breathes" → "Whoever breathes."** `آن که` is *the one who* (a person),
  not "that which." `آوازی تازه` = *a fresh song* (`تازه` "fresh"). This and the previous
  aphorism are attributed (Szymborska, MacLeish), so they read as borrowed maxims.

- **`نوگرایی` = "modernism," not "modernity."** `نو` ("new") + `گرایی` ("-ism, leaning")
  is the *movement/ism*, not the *condition* (modernity). Jafari is talking craft, not
  epoch. `پیمودن` ("to traverse, to measure out a distance") → "crossed."

- **The lost pun: `واقعیت` → `واقعه`.** "Reality becomes an event" hides that both words
  share the Arabic root **و‑ق‑ع** (w-q-ʿ, "to fall, to occur"): `واقعیت` (the real) and
  `واقعه` (the occurrence) are cognates. The aphorism literally turns one into the other.
  English can't easily mirror the shared root; "the real turns into an occurrence" at
  least keeps "the real / the occurring" audible. Worth a margin note.

- **The "sprouting" motif: `می‌روید`.** `روییدن` is *to grow as a plant sprouts*. It
  appears in the poem fragment (*a shadow sprouts*) **and** in "out of 'I don't know'
  *grows* 'I know.'" Same verb, same image — inspiration as germination. Keep "sprout/
  grow" in both so the link survives. `تاب و تب` ("twist-and-fever") is a rhyming
  doublet for feverish agitation; `پردهٔ هیچ` is *the veil of nothingness* (`پرده` carries
  the Sufi "veil," not just stage "curtain").

- **The MacLeish line is restored correctly.** `شعر نباید معنی داشته باشد، شعر باید باشد`
  back-translates Archibald MacLeish's *Ars Poetica* ("A poem should not mean / But be").
  Restoring the source quotation rather than re-translating the Persian is exactly right.

---

## Section 2 — Khosrow Sinai's Preface: *The Redness of the Pomegranate Seed*

### Reworked translation

> Finally, after years of delay, what had to happen has happened. I am not merely
> glad — I am thrilled. And I know well that this delight is not simply a matter of my
> comradeship with Mohammad Ebrahim Jafari. I remember, a few years ago, a critic asked
> me: "Do you think you yourself are an artist?!" I answered: "I don't know!"
>
> …But I know this much: for some sixty years I have kept friendships, near and far,
> with artists of every kind — poets… painters… musicians… and at last filmmakers — and
> I have learned to tell who is an artist by his very nature, and who puffs out his
> jowls, plays the pharaoh, breeds a retinue of yes-men, and forces his work on people.
> In all those years, how rare were the ones whose artistic essence struck me with
> wonder — and Mohammad Ebrahim Jafari is, beyond doubt, one of them.
>
> The biting satire of some of his poems always set me somewhere between the verse of
> Obeyd Zakani and Iraj Mirza. I will never forget those nights when bombs and missiles
> rained down on our heads — he would take up his dutar among friends, work a rhythm
> over and over, and sing to us in his raspy voice: "The woods are full o'
> brambleberries!" And we friends, on those grief-laden nights, with a feeling caught
> between weeping and laughter, would become of one heart, one tongue, one voice with
> him. Did he not say, at the close of one poem:
>
> > "Sometimes, laughing, I weep…
> > Sometimes, weeping, I laugh…
> > The sensible ones say:
> > I am an artist!"
>
> Later, others took up his way of singing — Iranian, regional, unconventional, yet
> rooted and of-the-moment — and rose to fame, while few knew he had been the one to
> open that road.
>
> Sometimes the humility and heartfelt warmth of his songs put me in mind of Baba
> Taher. When he says:
>
> > Two doves, white and saffron,
> > settled in the shade of the arbor —
> > the white one moaned toward the light… the dawn-glow flooded red,
> > three coos… the sun, tasting like youth.
>
> And sometimes, in the roguish grace and delicacy of his verse, I find the very stuff
> of that poetic being which gave a Hafez to the history of our culture. He has always
> called to my mind the troubadours of medieval Europe — those wandering singers who
> went from town to town in song, for whom composing was simply part of being alive.
>
> I have always told him: the poetic mind wells up in you so abundantly that — like
> children who don't know the worth of their father's wealth — you spend the wealth
> native to you so prodigally, and so humbly, that those without your artistic sense may
> pass it by, and wait instead for "poets"! who puff out their jowls and, with much pomp,
> force-feed others what neither they nor their listeners understand.
>
> If we grant that the embryo of a poem takes life and grows in the poet's mind, then
> what makes it manifest beyond that mind — what carries it to the listener — is nothing
> but the instrument the poet has mastered. That instrument may be the word, or music,
> or painting, or any other art in which the poetic creative force plays a part. Over the
> years Jafari has used two instruments — word and painting — and in the second he spent
> years as a master, nurturing the young. One of his students, himself now a renowned
> painter, once said to me of him: "Most teachers taught us the techniques of painting —
> but he, beyond that, woke the artist's soul in us."
>
> He was right. As his friend, I have always known him as the delicate string of a
> setar: when it is set trembling, it stirs into vibration only those strings that share
> its delicacy. This one poem of his is one of many witnesses to what I mean:
>
> > My heart is a pomegranate of a thousand seeds,
> > holding a love's red power
> > in every seed…
> > When you look at me,
> > one of the seeds turns redder.
>
> I confess that, as one of art's own people, I have at times felt an admiring envy at
> the poetic welling of his mind.
>
> — Khosrow Sinai, Ordibehesht 1396 / Spring 2017

### Notes

- **The satirical cluster (the richest etymology in the preface).** Sinai mocks the
  pretentious artist with three vivid, deliberately crude images that the machine
  sanded into abstractions ("self-inflation, arrogance, the cultivation of sycophants"):
  - `باد به غبغب انداختن` — literally *to throw wind into one's dewlap/double-chin*.
    `غبغب` is the throat-pouch under the chin — and the puffed throat of a **strutting
    pigeon**. It means to swagger, to puff oneself up. Keep the bird: "puffs out his
    jowls."
  - `تفرعن` (the text's `تقرعن` is a typo) — *acting like Pharaoh*, from `فرعون`
    (Fer'own). Not mere "arrogance" but megalomaniac, despotic self-importance: "plays
    the pharaoh."
  - `نوچه‌پروری` — `نوچه` is a tough's apprentice / hanger-on / yes-man (an underworld,
    *luti* flavor) + `پروری` "rearing" (`پروردن` "to nurture"). "Breeds a retinue of
    yes-men."
  - And later, `حقنه می‌کنند` — `حقنه` literally is *an enema / a forced injection*. The
    pretenders don't just "force upon others"; they **force-feed / cram down the
    throat** what no one understands. `آب و تاب` ("water and luster") = florid pomp →
    "with much pomp." These are meant to be deflating and a little vulgar; the English
    should keep the sting.

- **`ذوق‌زده` → "thrilled."** `ذوق` (zauq, Arabic "taste, relish, aesthetic sense") +
  `زده` ("struck") = struck-with-delight, giddy with pleasure. "Elated" is fine;
  "thrilled" keeps the giddiness. `از سرِ رفاقت` = *out of comradeship* — `رفاقت`
  (`رفیق` "companion") is buddy-ish, warmer and more informal than `دوستی` "friendship."

- **`رندی` badly served by "wit."** This is the key term in the Hafez sentence. `رند` /
  `رندی` is the **Hafezian libertine-sage**: the wine-loving, hypocrisy-piercing,
  antinomian free spirit — *roguish wisdom*, not cleverness. Since Hafez is named in the
  same breath (`رندی` is *his* signature virtue), "wit" is a real loss. "Roguish grace"
  or "rendi (the libertine-sage spirit)" is closer. `جنس` = "stuff, substance" (Arabic
  *jins*, genus) → "the very stuff of poetic being"; `هدیه کرد` = "gifted / bestowed."

- **`غبطه` is not ordinary envy.** Sinai's closing confession uses `غبطه` (ghebṭa) — the
  *admiring, benign* envy that wishes the same good for oneself **without** wishing to
  deprive the other. Classical ethics opposes it to `حسد` (ḥasad, malicious envy).
  "Quiet envy" already intuits this nicely; making it explicit — "an admiring envy" —
  honors the distinction. `جوشش` ("welling, effervescence," from `جوشیدن` "to boil/gush")
  echoes the earlier *the poetic mind wells up* (`می‌جوشد`): a spring/fountain image.
  `اهالی هنر` = *the people of art*, "art's own people."

- **`همدل و همزبان و هم‌آواز`.** Render the triad: *of one heart, one tongue, one voice*.
  The machine's "sympathy, in voice, in unison" loses the chant.

- **The laugh/weep quatrain.** `عاقلان` is *the rational / sensible ones* — with an
  ironic edge: the "sensible" people look at this laughing-weeping man and diagnose him
  ("he's an artist!" = he's mad). The chiasmus (laughing-I-weep / weeping-I-laugh) is
  preserved.

- **The dialect folk-song is uncertain — flag it.** `جنگلا پُر تَمشکه!` and the
  *دوتا کفتر* quatrain are in a rural northern register (Gilaki-ish), not standard
  Persian — which is precisely Sinai's point about Jafari's "local, regional" voice.
  `تمشک` is properly *raspberry / wild bramble-berry* (blackberry is usually `شاه‌توت`);
  rendering it folksy ("brambleberries," "the woods are full o'…") signals the register.
  In the quatrain, `شفق` is the **red glow of dawn/dusk** ("dawn-glow flooded red"), and
  `سایه‌بون` is a *sunshade/arbor*. Several words (`دِ تثار`, `سه کو`) are genuinely
  unclear; the reading above is a reasonable gloss, not a certainty. If the original print
  has diacritics, they'd settle it.

- **`اصیل` = "rooted."** `اصیل` (Arabic *aṣīl*, from *aṣl* "root, origin") is "authentic"
  *in the sense of rooted, of true origin* — which is why it pairs so well against
  `امروزی` ("of today"): *rooted yet of-the-moment*.

---

## Section 3 — Bajlan Farrokhi's Introduction

### Reworked translation

> Master Mohammad Ebrahim Jafari — the great image-maker and painter — has poems composed
> shoulder to shoulder with his growth in pictorial composition, poems that shied away
> from ever being set down on the page. In the end, though, the insistence of his
> kindred companion and wise wife, Lady Maryam… and of close friends, brought this first
> volume to print. In painting, Jafari fixes fast the subjective data of life's moments;
> in his poems, he is the spokesman of those moments — and so it is that many of his
> verses stand cheek by jowl with his paintings, and at times are one and the same.
>
> Read aloud, the short poems of this collection are like the rhythm of a brushstroke
> bringing a work into being; their richness, at first encounter, recalls the
> astonishing single couplets of the classical Persian poets, and at times the profound
> Japanese haiku. In poetry as in painting he follows no one but his own self.
> Painter-poets are keen-eyed and without peer in their work — in other lands too one
> can name geniuses like Wang Wei, the Chinese painter and poet (637–740 AD),³ and
> Michelangelo, the Italian sculptor, painter, and poet.
>
> From Jafari:
>
> > I
> > am silent
> > so that the moon… may speak with you…
>
> — as if the moon has come from one side to the poet's aid, to become one with him and
> say, with fellow-feeling, what he leaves unspoken: that silence and night are brimming
> with the unsaid.
>
> And this poem by Wang Wei, in Persian rendering:
>
> > Alone, I play the oud in the far reed-grove —
> > under my breath I hum a tune.
> > In the endless reeds there is no one.
> > The moon, and its shining rays.
>
> And this poem by Bashō (1644–1694 AD), from the Persian of Shamlou and Pashaei:
>
> > Clouds
> > give a moment's rest
> > to the moon-gazers.
>
> And this poem by Jafari, which is an astonishing painting:
>
> > For fifty years now
> > this turtledove
> > has perched on a snow-laden branch.
>
> — in which time finds its way to timelessness, and the turtledove to eternity.
>
> And again, this poem of Jafari's:
>
> > When I weep in memory of you, my tears are blue…
> > I love you a sky's love —
> > for love is blue, and so is the sky.
>
> And this poem — a grievous memorial to the Rudbar earthquake of 1369 (1990):
>
> > On the night of the earthquake…
> > the moon, in the eye of the firefly,
> > became a rain of moonlight… and…
> > poured down on the rubble.
> > The firefly hadn't the strength to hear
> > the most sorrowful chorus
> > from a people who
> > had never sung so of one heart.
> > Until… the last breath…
>
> — a grievous tableau, a painful dirge, until… the last breath….
>
> Jafari's long poems, like his short poems and his astonishing paintings, are
> fold-within-fold. His poetry is not uniform; like that of many enduring poets, it
> changes over time — and you can track the change by the dates of the poems, from the
> romantic to the verse of the day — shifting in both form and content. For the essence
> of Jafari, image-maker and poet, is not static: it is forever in the act of becoming:
>
> > On the back roads —
> > blue, gray, black —
> > a peasant with his long staff.
> > White, black.
> > His donkey, I mean —
> > under a donkey-load of rain-beaten thorns.
> > Black, black…
> >
> > His fortune, I mean —
> > which has grown like a shadow at his feet.
>
> — a tableau of a peasant in a blue robe and gray trousers, with a black-and-white pack
> donkey bearing rain-beaten thorns to kindle the firewood of others' hearths and ovens:
> a symbol of village poverty, and…
>
> And the tableau-poem of the waterfall:
>
> > I am that blithe and drunken waterfall
> > who for years
> > wept on the warm sands of your body,
> > madly,
> > so that I might die at your skirt —
> > I fled the snare of my own white snows.
>
> In it the sun's rays fall on the body of the waterfall, the many-colored droplets like
> lightning, like an arrow of the gaze, and the waves of the waterfall's breast are white
> as the moon — and in its ardor to become one, it spans peak to sea. Reaching the sea,
> it longs to return to the distant valleys and the summit — a cycle that voices the wish
> to return to the beginning. This is a poem written some sixty years ago, and it stands
> level with the verse of the poets of that age, if not beyond it, in the very same style
> and idiom. It bespeaks a soul forever a poet and perpetually awake — the sense of
> sinking into nature, of becoming one with the waterfall, the wish to sink into the
> endless sea, and again the wish to return to the peak.
>
> Jafari's love poems in this collection are not few, for many of these showings rise
> from a soul forever in love — and at their highest, this is no erotic love but a love
> for the human and for all beings:
>
> > I love you —
> > this surmise,
> > O ancient, everlasting anthem,
> > this thing kneaded by the angels of heaven,
> > this certainty,
> > this oldest song of the earth —
> > like the color of cloud,
> > like the smell of clay,
> > like the taste of tears,
> > like the sleep of mountains, it is everlasting…
>
> And here and there in this collection, again, you see the great image-maker longing to
> turn inward — to raise from his own soul a peerless tableau, and make his composing and
> his renderings one and the same:
>
> > Would that I were a ruined tower on a far road,
> > so that on rainy nights
> > the rain-damp pigeons, beneath the roof of my veranda,
> > would lean on one leg and sleep.
> > …
> > At the foot of the veranda, beside the burning fire,
> > two grief-laden night-wanderers
> > told each other the tale of all that had befallen them.
>
> For Jafari, in art, his whole world is a window wrought by hand and a powerful throat —
> and in this aged fortress he holds many unspoken words, in the sound-kinship and the
> embodiment of his words, and in the rainbow of his colors and compositions.
>
> Let us leave the reader to the reading of this collection's poems, and be like Hokusai,
> whose wish was to distill all his works into a single point — and nothing more.
>
> — Bajlan Farrokhi (M.H.), Ordibehesht 1396 / Spring 2017

### Notes

- **Block 1 corrections.** "sculptor" → "image-maker" (see cross-cutting #1). `تکامل` =
  *maturation/evolution* (Arabic *takāmul*, from *kamāl* "perfection") → "growth."
  `از به دفتر نشستن دوری جسته` = literally *shunned sitting in a ledger* → "shied away
  from being set down on the page." And the `هم‑` triad for Maryam — `همدم همدل و همسر`
  = *breath-sharer, heart-sharer, head-sharer* = "kindred companion and wise wife"
  (at minimum keep "companion" + "wife"; ideally the kinship chime). `ابرام` =
  *insistence* (Arabic), not "warmth" — keep "insistence." `پهلو می‌زند` = *vies with,
  comes shoulder to shoulder with* → "stand cheek by jowl with" (a touch more than
  "alongside"). Note `سوبژکتیو` is Farrokhi's own European loanword ("subjective") — he
  writes as a trained critic; keep it.

- **"so that the moon may speak."** In the "I / am silent" poem, `تا` reads better as
  *so that* (purpose) than "until" (time): he silences himself **so the moon can speak**.
  Farrokhi's own gloss confirms it ("the moon comes to the poet's aid… to say what is
  unspoken"). Also note `خاموش` means both *silent* and *extinguished* (as of a
  quenched lamp) — he dims himself so the moon may shine/speak. `سرشار` = *brimming,
  overflowing* → "brimming with the unsaid."

- **The two borrowed poems are translations-of-translations.** Wang Wei's piece is his
  famous "Bamboo Grove" (竹里館); the Persian has shifted the *zither* to `عود` (oud) and
  the *bamboo* to `نیزار` (reed-grove, since `نی` = reed/cane). Translating the Persian
  faithfully — as done — is right for this book, but a note that the chain is
  Chinese → Persian → English would be honest. Bashō's is the *tsukimi* (moon-viewing)
  haiku "clouds now and then give a soul rest from moon-viewing"; `نظارگان ماه` =
  *the moon-gazers* (`نظاره` "beholding"). The source's **Wang Wei dates (637–740) are
  off** — he lived c. 699–761; left as the author wrote it, flagged here (footnote ③).

- **`آبی` = "blue," literally "water-colored."** In the tears poem there's a buried
  resonance: `آبی` (blue) is `آب` ("water") + `ی` — so *my tears [water] are blue
  [water-hued]*, and the chain runs water → blue → tears → sky → heavenly love.
  `آسمانی دوست دارم` is *I love you sky-ly / with a celestial love* — `آسمانی` =
  "heavenly, sky-like" (also the word for non-erotic, celestial love); "I love you a
  sky's love" keeps the strangeness.

- **The earthquake poem.** Two glow-words hinge it: `کرم شبتاب` (the firefly, literally
  *night-glow-worm*) and `مهتاب` (*moon-glow*) share `تاب` ("glow") — the moon caught in
  the firefly's eye. `آوار` is specifically *the rubble of a collapsed building* — exact
  for an earthquake. `یکدل` = *of one heart*; "had never sung so of one heart" is more
  poignant (and more literal) than "so unanimously" — these are the dying, singing as
  one. `توان نداشت` = *hadn't the strength* → "hadn't the strength to hear." `غم‌آوا` =
  *grief-voice, a dirge*.

- **The peasant poem — the `خر / خروار / خار` sound-cluster.** The machine's "cartload"
  erases a pun: `خروار` (*kharvār*) is literally a **donkey-load** (`خر` donkey + `بار`
  load — also an old unit of weight, ~300 kg). So the *donkey* (`خر`) carries a
  *donkey-load* (`خروار`) of *thorns* (`خار`) — three near-homophones in a row. "A
  donkey-load of rain-beaten thorns" recovers it. `بخت` = *fortune, lot, fate* (more than
  "luck"); `روییده است` = *has sprouted/grown* (the §1 plant-verb again). In Farrokhi's
  gloss, `جامه` = *robe/garment* (not "shirt") and `تنور` = *tandoor* (the clay
  bread-oven); `نماد` = "symbol."

- **The waterfall poem — fix line 1, and the `دام / دامن` echo.** The machine misparses
  the opening as "That waterfall — I am its joy, its intoxication." The Persian is
  first-person identification: *I am that `سرخوش` and `مست` waterfall* — `سرخوش` =
  "blithe, merry, mellow-tipsy" (`سر` head + `خوش` happy = light-headed), `مست` =
  "drunk." This matches Farrokhi's gloss about *becoming one with* the waterfall. Then
  `تا که بمیرم به دامنت` — `دامن` is *skirt / lap*, **and** the *foot/skirt of a mountain*
  — perfect for a waterfall dying at the mountain's base. And `از دامِ برف‌های سپیدم` —
  `دام` is *snare/trap*: the near-pun `دام`/`دامن` (snare inside lap) is surely deliberate.
  "Fled the snare of my own white snows" = escaped the frozen snowpack it was trapped in.

- **`در شدن` and `هوشیار/مست`.** Keep "in the act of becoming" (`در شدن`). Note a quiet
  irony: the waterfall is `مست` (drunk) and `سرخوش`, yet Farrokhi calls the soul
  `هوشیار` — "awake / **sober** / vigilant" (`هوش` "wits" + `یار`). Drunk water, sober
  soul. `درنوردیدن` = *to span, to roll up [distance]* → "spans peak to sea." `سبک و سیاق`
  = *style and idiom* (`سبک`, charmingly, comes from "casting molten metal" — a *cast*,
  hence a "style").

- **The love poem — `گمان` vs. `یقین`.** The poet calls his love both `این گمان` and
  `این یقین`. `گمان` is *surmise / conjecture / fancy* (it can even mean doubt) — its
  whole point is to sit in paradox against `یقین` (*certainty*, Arabic *yaqīn*). "This
  intuition" softens it and breaks the pair; "this surmise… this certainty" keeps the
  tension. `سرشته` = *kneaded / molded* (`سرشتن` "to knead dough, to mould"; `سرشت` =
  "innate nature") — a clay-creation image, not "woven." And `بوی خاک` — *the smell of
  clay/earth* — **is the book's title phrase** (*بوی خاک و آواز پرندگان*, "the smell of
  clay and birdsong"); rendering it "smell of clay" (not "soil") lets the title ring
  inside the poem. `باشندگان` = *beings / existents* (`بودن` "to be") — slightly wider
  than "living things": *all that is*.

- **Block 8/9 corrections.** `صورتگر` → "image-maker" again. `در خود شدن` = *becoming
  inward, turning into oneself* → "longing to turn inward" (not "to become himself").
  `تابلوی بی‌بدیل` = "a peerless tableau"; `پردازش` = *elaboration/rendering/finishing*
  (`پرداختن` "to polish, attend to"). The closing sentence is genuinely dense:
  `تجانس آوایی` = *sound-kinship / assonance* (`تجانس`, Arabic *tajānus* "congeneity,"
  the same root behind the rhetorical term *jinās*); `تجسم` = *embodiment / making
  corporeal* (`جسم` "body") — **not** "precision"; `قلعهٔ پیر` = "this aged fortress"
  (`پیر` also carries "elder / Sufi master"); `رنگین‌کمان` = "rainbow" (literally
  *colored-bow*). `خلاصه کردن` = *to distill* (`خلاصه`, Arabic *khulāṣa*, "the purified
  extract") → "distill into a single point." `و بس` = "and nothing more."

- **Tower poem = `old-news.poem`.** This is the collection's *آخرین خبر*. `ایوان` =
  *iwan / veranda* (the vaulted Persian porch); `شبگرد` = *night-wanderer / night-
  roamer* (also "night-watchman"); `سرگذشت` = *the tale of what befell one, one's
  life-story*. Note the paired `نم‌آلوده` / `غم‌آلوده` ("damp-tainted" / "grief-tainted")
  — same `‑آلوده` ending, an echo worth keeping. See cross-cutting #7 about reconciling
  the two English versions.

---

## Section 4 — Coda: *From Jafari*

### Reworked translation

> *(Persian source corrupt — see note. Only the legible lines can be rendered honestly:)*
>
> > Tonight I painted the bruise-blue voice of my song.
> > …
> > if only it would rain…
> > …the bird's song makes [it] richer in color… full.
>
> — Mohammad Ebrahim Jafari

### Notes

- **This section should not be "retranslated" — it should be re-sourced.** The HTML
  already flags it ("source text garbled in scanning — retranslation needed"), and that
  is exactly right: the **Persian itself is corrupt OCR**, not difficult Persian. Several
  "words" are not Persian at all but scanning artifacts — `کارپوری`, `گاتهام‌ها`
  (literally reads "Gothams"), `کانفی`, `کامنگل`, `زانی` — and the syntax dissolves. No
  faithful translation is possible from this text; any English (including the current
  pass) is necessarily invention. The right move is to recover the lines from the
  original printed book, then translate.

- **What *is* legible** is worth keeping for its own sake:
  - `امشب صدای کبود ترانم را نقاشی کردم` = *Tonight I painted the bruise-blue voice of my
    song.* `کبود` is not plain "dark blue" — it's the **livid blue-black of a bruise**.
    And the line is pure synesthesia: he *paints* a *sound* a *color* — a fitting opening
    from a painter-poet. "Dark blue of my song" undersells `کبود`; "bruise-blue voice"
    keeps both the color and the cross-sense.
  - `کاش باران ببارد` = *if only it would rain* — clean and legible.
  - `آواز پرنده … رنگ‌تر می‌کند … پُر` = *the bird's song makes [it] more colorful…
    full* — legible in outline (and a quiet echo of the book's title, *birdsong*).

- **Recommendation:** until the source is recovered, present only the legible lines (or
  keep the whole thing visibly marked as provisional, as it is now). Better a short
  honest fragment than a confident translation of scanner noise.

---

## Summary of recommended changes

| # | Where | Change | Reason |
|---|-------|--------|--------|
| 1 | §3 b1, b5, b8 | "sculptor" → **image-maker / painter** | `صورتگر` = image-maker; sculptor is `پیکرتراش` |
| 2 | §1 | "Mad Willow" → **weeping willow** | `بید مجنون` *is* the weeping willow; keeps the pun |
| 3 | §2 | restore the **pigeon/pharaoh/yes-men/force-feed** images | `باد به غبغب`, `تفرعن`, `نوچه`, `حقنه` — flattened satire |
| 4 | §2 | "wit" → **roguish grace / rendi** | `رندی` is the Hafezian libertine-sage virtue |
| 5 | §2 | "envy" → **admiring envy** | `غبطه` (benign) ≠ `حسد` (malicious) |
| 6 | §3 | waterfall: "I am its joy" → **"I am that blithe, drunken waterfall"** | misparse; first-person identification |
| 7 | §3 | "cartload" → **donkey-load** | `خروار` pun with `خر`/`خار` |
| 8 | §3 | "intuition" → **surmise** | `گمان` must pair against `یقین` (certainty) |
| 9 | §3 | "woven" → **kneaded/molded**; "soil" → **clay** | `سرشته` = kneaded; `خاک` = the title word |
| 10 | §1 | "That which breathes" → **Whoever breathes** | `آن که` = a person |
| 11 | all | consistent **Ebrahim**, **ardor** (`شوق`), **becoming** (`شدن`), **tableau** (`تابلو`), `هم‑` triads | recurring motifs |
| 12 | §4 | **re-source, don't retranslate** | Persian is corrupt OCR |

---

¹ Wisława Szymborska, Polish poet, Nobel laureate (1923–2012).
² Archibald MacLeish, American poet and Librarian of Congress (1892–1982); the line is his *Ars Poetica*.
³ Dates as given in the source; the historical Wang Wei lived c. 699–761.

# بوی کاهگل و آواز پرنده — The Smell of Adobe and Birdsong

A bilingual Persian/English poetry collection by **Mohammad Ebrahim Jafari**,
rendered as a single-page website and served via GitHub Pages.

## How the site works

Every `.poem` file in `poems/` (and every preface section in `preface/`) is read by
`build_collection.py` and compiled into `index.html`. GitHub Actions rebuilds and commits
`index.html` automatically whenever you push a change to a `.poem` file, a preface section,
an ornament or `build_collection.py`.

Live at https://jafari.bbben.org/ (the `CNAME` file; the github.io address redirects there).

## How to add or edit a poem

1. Create or edit a `.poem` file inside `poems/`.
2. Commit and push to `main`.
3. The workflow runs, regenerates `index.html`, and commits it back.
4. The GitHub Pages site updates within seconds.

## .poem file format

A `.poem` file is a `===meta===` section of flat TOML (the fields in `schema.toml`), then
text sections: `===persian===`, the three English layers (`===machine===`, `===lantern===`,
`===translation===`) and `===footnotes===`. The full format, and who writes which layer, is in
[`docs/FORMATS.md`](docs/FORMATS.md) and [`CLAUDE.md`](CLAUDE.md).

## Local preview

```bash
python build_collection.py poems/
# opens index.html in any browser
```

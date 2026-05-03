# بوی کاهگل و آواز پرنده — The Smell of Adobe and Birdsong

A bilingual Persian/English poetry collection by **Mohammad Ebrahim Jafari**,
rendered as a single-page website and served via GitHub Pages.

## How the site works

Every `.poem` file in `poems/` is read by `build_collection.py` and compiled
into `index.html`. GitHub Actions rebuilds and commits `index.html` automatically
whenever you push a change to any `.poem` file or to `build_collection.py`.

## How to add or edit a poem

1. Create or edit a `.poem` file inside `poems/`.
2. Commit and push to `main`.
3. The workflow runs, regenerates `index.html`, and commits it back.
4. The GitHub Pages site updates within seconds.

## .poem file format

```
id: kebab-case-identifier
persian_title: عنوان فارسی
english_title: English Title
date_written: Autumn 1989
date_translated: 4-8-2026
page_number: 12

===persian===
متن شعر فارسی
سطر به سطر

===translation===
English translation
line by line

===footnotes===
Optional translator's notes. Leave the section blank (or omit it)
if there are no notes for this poem.
```

All fields before the first `===` marker are key/value pairs separated by `:`.
The three section markers (`===persian===`, `===translation===`, `===footnotes===`)
delimit the body content. A blank `===footnotes===` section is fine — the notes
block simply won't appear in the rendered HTML.

## Local preview

```bash
python build_collection.py poems/
# opens index.html in any browser
```

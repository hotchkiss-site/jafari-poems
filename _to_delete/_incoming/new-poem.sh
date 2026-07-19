#!/usr/bin/env bash
# Scaffold a new poem: creates poems/{id}.poem (self-contained: ===meta=== + text sections)
# Run from the repo root: ./new-poem.sh

set -euo pipefail

POEMS_DIR="poems"

mkdir -p "$POEMS_DIR"

echo ""
echo "New poem — press Enter to leave a field blank."
echo "---"

# --- Required: ID ---
while true; do
  read -rp "Poem ID (slug, e.g. silent-river): " id
  [[ -n "$id" ]] && break
  echo "  ID is required."
done

if [[ -f "$POEMS_DIR/$id.poem" ]]; then
  echo "Error: poem '$id' already exists." >&2
  exit 1
fi

# --- Optional fields ---
read -rp "English title:          " english_title
read -rp "Persian title:          " persian_title
read -rp "Date written:           " date_written
read -rp "Page number:            " page_number
read -rp "Persian page number:    " persian_page_number
read -rp "Source (journal / app): " source
read -rp "Tags (comma-separated): " tags_raw

# Build TOML tags array from comma-separated input
tags_toml="[]"
if [[ -n "$tags_raw" ]]; then
  IFS=',' read -ra tag_arr <<< "$tags_raw"
  quoted=()
  for t in "${tag_arr[@]}"; do
    t="$(echo "$t" | xargs)"   # trim surrounding whitespace
    [[ -n "$t" ]] && quoted+=("\"$t\"")
  done
  if [[ ${#quoted[@]} -gt 0 ]]; then
    tags_toml="[$(IFS=', '; echo "${quoted[*]}")]"
  fi
fi

# --- Write the self-contained poem file ---
cat > "$POEMS_DIR/$id.poem" << TOML
===meta===

id                  = "$id"
english_title       = "$english_title"
persian_title       = "$persian_title"
date_written        = "$date_written"
date_translated     = ""
page_number         = "$page_number"
persian_page_number = "$persian_page_number"
source              = "$source"
tags                = $tags_toml
notes               = ""
TOML

cat >> "$POEMS_DIR/$id.poem" << 'POEM'

===persian===


===machine===


===translation===


===footnotes===
POEM

echo ""
echo "Created:"
echo "  $POEMS_DIR/$id.poem"
echo ""

# Open in editor if EDITOR is set
if [[ -n "${EDITOR:-}" ]]; then
  "$EDITOR" "$POEMS_DIR/$id.poem"
fi

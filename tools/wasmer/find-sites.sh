#!/usr/bin/env bash
# Find Wasmer Edge site folders on this computer (read-only: it changes nothing).
# Usage: bash tools/wasmer/find-sites.sh [folder-to-search]   (default: your home folder)
set -u
root="${1:-$HOME}"
echo "Searching $root for Wasmer projects (app.yaml / wasmer.toml)..."
find "$root" -maxdepth 6 \( -name node_modules -o -name .git -o -name .cache -o -name .local -o -name snap \) -prune -o \
     \( -name app.yaml -o -name wasmer.toml \) -print 2>/dev/null |
  xargs -r -n1 dirname | sort -u | while read -r dir; do
    echo
    echo "== $dir"
    [ -f "$dir/app.yaml" ] && grep -E '^(name|owner|app_id|kind):' "$dir/app.yaml" | sed 's/^/   /'
    if grep -rIlq -i 'inonda' "$dir" --include='*.html' --include='*.yaml' --include='*.toml' 2>/dev/null; then
      echo "   mentions 'inonda': yes"
    fi
    if git -C "$dir" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
      echo "   git: $(git -C "$dir" status --short | wc -l) uncommitted change(s)"
    fi
  done
echo
echo "Done. To map folders to domains: wasmer app list && wasmer app get constapo/<app-name>"

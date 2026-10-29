#!/usr/bin/env bash
# Installs the graphify CLI (needed by the graphify skill) if it is missing.
# Never fails the session: any error is ignored.
export PATH="$HOME/.local/bin:$PATH"
command -v graphify >/dev/null 2>&1 && exit 0
if ! command -v uv >/dev/null 2>&1; then
  if command -v pipx >/dev/null 2>&1; then pipx install graphifyy >/dev/null 2>&1; exit 0; fi
  python3 -m pip install --user -q uv >/dev/null 2>&1 || exit 0
fi
uv tool install graphifyy >/dev/null 2>&1 || true
exit 0

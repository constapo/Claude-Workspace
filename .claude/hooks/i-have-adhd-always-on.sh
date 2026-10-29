#!/usr/bin/env bash
# SessionStart hook: turns on the i-have-adhd output style for every session.
# Adapted from github.com/ayghri/i-have-adhd hooks/always-on.sh (MIT), minus
# the opt-in flag file: committing this hook is the opt-in.

set -euo pipefail

case "$0" in
  */*) SCRIPT_DIR="$(cd "${0%/*}" && pwd)" ;;
  *) SCRIPT_DIR="$(pwd)" ;;
esac
skill_md="$(cd "${SCRIPT_DIR}/.." && pwd)/skills/i-have-adhd/SKILL.md"
[ -r "$skill_md" ] || exit 0

# Drop the YAML frontmatter (first --- ... --- block).
body="$(awk 'NR==1 && /^---[[:space:]]*$/ {fm=1; next} fm && /^---[[:space:]]*$/ {fm=0; next} !fm' "$skill_md")"

escape_for_json() {
  local s="$1"
  s="${s//\\/\\\\}"
  s="${s//\"/\\\"}"
  s="${s//$'\n'/\\n}"
  s="${s//$'\r'/\\r}"
  s="${s//$'\t'/\\t}"
  printf '%s' "$s"
}

intro='ADHD MODE ACTIVE (always-on). The ruleset below applies to every response. "stop adhd mode" turns it off for this session; remove the i-have-adhd hook from .claude/settings.json to turn always-on off for good.'
context="$(escape_for_json "${intro}"$'\n\n'"${body}")"

printf '{\n  "hookSpecificOutput": {\n    "hookEventName": "SessionStart",\n    "additionalContext": "%s"\n  }\n}\n' "$context"

#!/usr/bin/env bash
# SessionStart hook: injects the using-superpowers skill into context.
# Adapted from github.com/obra/superpowers hooks/session-start (MIT).

set -euo pipefail

case "$0" in
  */*) SCRIPT_DIR="$(cd "${0%/*}" && pwd)" ;;
  *) SCRIPT_DIR="$(pwd)" ;;
esac
CLAUDE_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

skill_md="${CLAUDE_DIR}/skills/using-superpowers/SKILL.md"
if [ -r "$skill_md" ]; then
  content="$(<"$skill_md")"
else
  content="Error reading using-superpowers skill"
fi

escape_for_json() {
  local s="$1"
  s="${s//\\/\\\\}"
  s="${s//\"/\\\"}"
  s="${s//$'\n'/\\n}"
  s="${s//$'\r'/\\r}"
  s="${s//$'\t'/\\t}"
  printf '%s' "$s"
}

escaped=$(escape_for_json "$content")
context="<EXTREMELY_IMPORTANT>\nYou have superpowers.\n\n**Below is the full content of your 'using-superpowers' skill - your introduction to using skills. For all other skills, use the 'Skill' tool:**\n\n${escaped}\n</EXTREMELY_IMPORTANT>"

printf '{\n  "hookSpecificOutput": {\n    "hookEventName": "SessionStart",\n    "additionalContext": "%s"\n  }\n}\n' "$context"

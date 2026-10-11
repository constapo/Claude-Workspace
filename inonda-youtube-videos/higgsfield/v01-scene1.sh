#!/usr/bin/env bash
# Video 1, scene 1 (Hook, 0:00-0:25): fast cuts of the damaged bathroom, then a flash of the finished result.
# Four 5s 16:9 shots, sharing one look so they cut together. Run from the repo root once HF_KEY is set
# and api.higgsfield.ai is allowed. Each shot spends Higgsfield credits.
set -euo pipefail
cd "$(dirname "$0")/../.."

LOOK="Photorealistic, handheld documentary style, natural daylight from a small frosted window, \
slightly desaturated warm Mediterranean tones, shallow depth of field, no people, no on-screen text, \
no logos. Older apartment bathroom in Cyprus with beige 1990s ceramic tiles."

python3 tools/higgsfield/hf.py check

python3 tools/higgsfield/hf.py agent "Make a 5 second 16:9 video. Slow push-in close-up on a cracked, \
chipped wall tile beside a shower, grout stained dark, a fine crack running across the glaze. $LOOK" \
  --answer "Use the brief as written; pick the best photoreal video model."

python3 tools/higgsfield/hf.py agent "Make a 5 second 16:9 video. Camera tilts up slowly from the tiled \
wall to a bathroom ceiling corner with a brown damp stain, peeling paint and black mould spots. $LOOK" \
  --answer "Use the brief as written; pick the best photoreal video model."

python3 tools/higgsfield/hf.py agent "Make a 5 second 16:9 video. Static overhead shot of an old shower \
tray: murky water pooling and draining very slowly around a corroded drain grate. $LOOK" \
  --answer "Use the brief as written; pick the best photoreal video model."

python3 tools/higgsfield/hf.py agent "Make a 5 second 16:9 video. Quick reveal: smooth dolly-in on the \
same bathroom fully renovated - large light-grey porcelain tiles, walk-in glass shower, floating vanity, \
warm LED mirror light, spotless and bright. Photorealistic, natural daylight, crisp and clean, no people, \
no on-screen text, no logos." \
  --answer "Use the brief as written; pick the best photoreal video model."

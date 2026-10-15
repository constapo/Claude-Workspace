---
name: video-visual-check
description: Claude's "eyes" for video work — turns clips, renders and web pages into labelled contact sheets and screenshots that Claude opens with the Read tool and actually looks at. Use to check every shot matches its narration line, to vet stock candidates (logos, watermarks, on-screen text, faces, cartoon look), to verify burned-in Greek subtitles are present and readable, and to look at stock/licence web pages. Use before showing any video to the owner.
---

# Visual check (Claude's eyes)

Never say a shot "matches" or a render "looks right" without opening the images. Tool:
`tools/video/visual_check.py` (FFmpeg + Pillow + pre-installed Chromium; free, local).

## Commands

```bash
# Every subtitle cue: frame from the middle of the cue, labelled with time + text
python3 tools/video/visual_check.py cues  build/v01.mp4 build/v01.gr.srt -o build/qa/cues
# A frame every N seconds (catches black/frozen frames and jump cuts)
python3 tools/video/visual_check.py every build/v01.mp4 --step 2 -o build/qa/every
# Start/middle/end of every candidate clip in a folder
python3 tools/video/visual_check.py clips stock/clips -o build/qa/clips
# Screenshot a web page (only hosts the network policy allows; if its CSS/CDN host is
# blocked the page shows unstyled but the text is still readable)
python3 tools/video/visual_check.py web https://pixabay.com/videos/... -o build/qa/page.png
```

Each command prints the sheet paths (12 tiles per page). Open each one with **Read** and look.

## What to check on every sheet

1. **Shot = line.** The picture shows exactly the work the subtitle/narration names at that
   moment (CLAUDE.md video rule 1). Tiling line → someone laying tiles, not a finished room.
2. **Realistic only.** Real camera footage. Reject drawings, cartoons, 3D renders, flat
   illustrations, slideshows (rule 2).
3. **Clean frame.** No logos, watermarks, on-screen text, brand names or recognisable faces.
   Never the owner's face.
4. **Greek subtitles** visible on every tile of a render, bottom, readable, not cut off (rule 3).
5. **Technical.** No black, frozen, stretched or letterboxed frames; consistent colour.

Write the result per cue as a table (time · line · what the frame shows · pass/fail · fix) in
`production/vNN/qa.md`, fix every fail, re-run, and only then show the video to the owner.
Sheets and frames are build output: keep them under the git-ignored `build/` folder.

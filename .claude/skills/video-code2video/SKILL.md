---
name: video-code2video
description: Make animated explainer scenes (cross-sections, step diagrams, labelled layers, timelines) as code with Manim, using the Code2Video method (planner → coder → critic) run for FREE — Claude plans, writes and critiques the Manim code; nothing calls a paid API. Use only for scenes where the owner has explicitly allowed a diagram, because CLAUDE.md video rule 2 otherwise requires real footage.
---

# Code2Video, free edition (Manim)

Method from [Code2Video](https://github.com/showlab/Code2Video) (Show Lab, NUS, MIT licence,
arXiv 2510.01174): a **Planner** writes the scene outline, a **Coder** writes executable Manim
code and fixes errors, a **Critic** looks at rendered frames and fixes layout. The original
calls paid Claude/Gemini APIs; here Claude Code does all three roles itself, so it is free.
No code from that repo is used; this is an original write-up of the method.

## Rule check first

CLAUDE.md video rule 2: realistic footage only, **never** drawings, diagrams or illustrations.
So a Manim scene goes into a video **only** when the owner has said yes to a diagram for that
specific line (log it in `memory/requests.md`). Without that, use real footage.

## Setup (once per container, free)

```bash
apt-get install -y libpango1.0-dev            # Pango for text rendering
uv venv ~/.venvs/manim && VIRTUAL_ENV=~/.venvs/manim uv pip install manim
~/.venvs/manim/bin/python -c "import manim; print(manim.__version__)"
```
(System pip fails to build `srt` on Python 3.13; the uv venv avoids it.) No LaTeX needed: use
`Text(..., font="DejaVu Sans")`, which renders Greek correctly.

## 1. Planner (write it down before code)

For the narration line(s): duration to fill (from `build/tts/durations.json`), the one idea to
show, the elements (shapes, labels in Greek), and a beat list with times, e.g.
`0–0.3 s title · 0.3–3.5 s layers appear one by one · 4.7 s membrane fades · 5.7–8 s water path`.
Keep one idea per scene, 6–15 s, max ~5 labels, no paragraphs on screen.

## 2. Coder

- File: `production/vNN/gfx/<name>.py`, one `Scene` class, docstring with the render command.
- 1920×1080, dark neutral background, real material colours, `DejaVu Sans`, labels ≥ 24 px.
- Keep everything inside x ∈ [−6.5, 6.5], y ∈ [−3.6, 3.6]; leave the bottom ~15 % free for the
  burned-in Greek subtitles.
- Render:
  `~/.venvs/manim/bin/manim -qh --format mp4 -o <name>.mp4 --media_dir production/vNN/build/gfx gfx/<name>.py <Scene>`
- On an error: read the traceback, fix, re-render (the Coder's debug loop).

## 3. Critic (look at it)

```bash
python3 tools/video/visual_check.py every production/vNN/build/gfx/videos/<name>/1080p60/<name>.mp4 --step 1.5 -o production/vNN/build/qa/<name>
```
Open the sheet with Read and check: nothing cut off at the edges, no overlaps (labels vs
arrows vs shapes), no empty first frame, text readable, the idea matches the narration line,
nothing sits in the subtitle area. Fix and re-render until clean (usually 1–2 rounds).

## 4. Into the edit

Use the rendered MP4 like any clip in `edl.json` (`"clip"` path relative to `build/`), so
`build_video.py` times it to the voice and burns the Greek subtitles over it.

Example: `production/v01/gfx/waterproof_layers.py` (line 7.5–7.7 cross-section: wall →
membrane → adhesive → tile, then the water path without a membrane). Tested 2026-10-15.

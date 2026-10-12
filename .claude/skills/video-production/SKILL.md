---
name: video-production
description: Start here for ANY video project — YouTube videos, Shorts/Reels, ads, explainers, B-roll, AI-generated clips, edits of real footage. Lays out the full pipeline (idea → script → shot list → assets → edit → captions → sound → thumbnail/packaging → publish), says which video-* skill to use at each step, which connected tools exist, and enforces the owner's paid-generation rule. Use when the user says "make a video", "video project", "edit this", "generate a clip", "turn this script into a video", or anything video-related.
---

# Video production (router)

This repo makes videos (first project: the 20 Inonda YouTube videos in
`inonda-youtube-videos/`). This skill is the map; the step skills hold the detail.

## Rule zero: credits

Anything that spends credits (Higgsfield, Artlist, Krea, Kling, vidIQ, ElevenLabs, Runway,
Veo, RunComfy, fal.ai…) follows the **Paid AI generation** rules in `/CLAUDE.md`:
plan free → price it → explicit approval for *this* batch → ONE test clip → wait → batch.
Never retry a paid call blindly, never auto-open results. Free local work (FFmpeg, Remotion,
Whisper, writing scripts and shot lists) needs no approval.

## The crew

You are the director. Real work goes to the crew of subagents in `.claude/agents/`
(researcher, scriptwriter, shot-planner, editor, sound, captioner, packager, QA reviewer,
plus the paid `higgsfield` / `artlist` generators). The roles and the step-by-step
playbook are in [CREW.md](CREW.md). Every free and paid source, tool, model and plugin
skill they can use is in [SOURCES.md](SOURCES.md).

## The pipeline

| # | Step | Output | Skill |
|---|---|---|---|
| 1 | Brief & intake | goal, audience, platform, length, aspect, language(s), deadline | this skill (questions below) |
| 2 | Script | narration + on-screen text, timed (≈150 spoken words/min EN, ≈130 GR) | `video-youtube-packaging` (hook & structure) |
| 3 | Shot list | every shot tagged AI / FILM / GFX / REUSE, with prompt or filming note | `video-ai-generation` |
| 4 | Price & approve | total = clips × cost, one test clip | `video-ai-generation` |
| 5 | Assets | generated clips, filmed footage, stock, voiceover, music | `video-ai-generation`, `video-voiceover-music` |
| 6 | Assembly edit | rough cut → fine cut | `video-ffmpeg-editing` (fast, deterministic) or `video-remotion` (code-driven, overlays, templates) |
| 7 | Captions | SRT/ASS, burned-in or sidecar, EN + GR | `video-captions-transcription` |
| 8 | Sound | voice at −14 LUFS-ish master, music ducked, SFX | `video-voiceover-music` |
| 9 | Versions | 16:9 master, 9:16 Shorts, 1:1 | `video-repurposing-shorts` |
| 10 | Packaging | title, thumbnail, description, chapters, tags | `video-youtube-packaging` |
| 11 | QA & deliver | checklist below, then report file paths (never auto-play) | this skill |

## Intake questions (ask once, reuse answers)

1. Goal & platform (YouTube long-form, Shorts, Reels, TikTok, ad, website)?
2. Length and aspect ratio (16:9 1920×1080 · 9:16 1080×1920 · 1:1 1080×1080)?
3. Language(s) of voice and captions?
4. What exists already: script, real footage, photos, logo, brand colours/fonts, music?
5. Which shots are proof of real work (real past jobs, real clients, testimonials)? Those need
   real footage. Everything else may use AI actors and fictional example jobs, labelled as AI.
6. Budget / which paid service, if any?

## Which tool for what (connected in this account — check they actually load in the session)

| Need | Tool | Notes |
|---|---|---|
| Photoreal AI clips | Higgsfield agent (`.claude/agents/higgsfield.md`), Artlist agent (`.claude/agents/artlist.md`), Krea MCP, Kling skill, vidIQ `generate_broll`/`generate_video` | paid — rule zero |
| Voiceover | ElevenLabs MCP `creative_generate_speech`, vidIQ `voiceover_generate` | paid |
| Music | Artlist (licensed library), ElevenLabs flows, vidIQ `generate_music` | check licence for YouTube |
| Cutting, joining, reframing, loudness, subtitles burn-in | FFmpeg (installed locally) | free |
| Overlays, lower thirds, animated captions, templates | Remotion (`npx create-video@latest`) | free for individuals/small teams; check remotion.dev/license |
| Transcription | Whisper (local, free) or ElevenLabs `creative_transcribe_audio` | |
| Thumbnails | Canva MCP, Adobe Express MCP, vidIQ `generate_thumbnail` + `score_thumbnail` | |
| Titles/keywords/SEO | vidIQ `keyword_research`, `score_title`, `generate_titles`, `generate_video_chapters` | |

## Folder layout per video project

```
<project>/
  script.md          # narration + on-screen text
  shot-list.md       # AI / FILM / GFX / REUSE per shot, with prompts
  assets/raw/        # filmed footage (never committed if large – keep out of git)
  assets/ai/         # generated clips, named V01-03_take1.mp4
  assets/audio/      # voiceover.wav, music.mp3, sfx/
  edit/              # EDL (cuts.csv), concat lists, Remotion project
  out/               # renders: master_16x9.mp4, short_9x16.mp4, captions.srt
```

Large media does not belong in git. Commit scripts, shot lists, EDLs and prompts only.

## QA checklist before calling a video "done"

- [ ] Plays start to end; duration matches plan (`ffprobe`).
- [ ] No black frames or frozen frames at cut points (`blackdetect`, `freezedetect` — see `video-ffmpeg-editing`).
- [ ] Audio: no clipping, integrated loudness ≈ −14 LUFS (YouTube), true peak ≤ −1 dBTP.
- [ ] Captions in sync, no line > 42 chars, Greek characters render.
- [ ] Every AI clip passed the reject list in `inonda-youtube-videos/shot-list.md`.
- [ ] AI shots that could be mistaken for a real job carry an "illustration" label.
- [ ] Placeholders like `[ADD REAL PRICE]` are gone.
- [ ] Report output paths; don't open them on the owner's machine.

## Sources

The step skills are original write-ups for this repo, distilled from these open-source
(MIT) skill collections plus vendor docs. The full list, with install commands, is in
[CATALOG.md](CATALOG.md).

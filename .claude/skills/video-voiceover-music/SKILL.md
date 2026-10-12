---
name: video-voiceover-music
description: Voiceover, music and sound for videos — writing narration for the ear, generating voice with ElevenLabs (connected MCP) or vidIQ, picking/licensing music (Artlist), sound effects, mixing with ducking, and loudness targets (LUFS) per platform. Use when a video needs narration, a voice, background music, SFX, or an audio mix/master.
---

# Voiceover, music & sound

Voice and music generation spend credits: follow the credit rule in `/CLAUDE.md`. That means
pricing it, getting approval, and making one test line before the full narration.

## Narration that sounds natural

- Write for the ear: short sentences, one idea each, contractions, no bracketed asides.
- Pace: ~150 words/min English, ~130 Greek. A 60 s section ≈ 150 words.
- Spell out what must be read a specific way (numbers, "€2,500" → "two thousand five hundred euros", acronyms).
- Mark pauses with line breaks or `<break time="0.6s"/>` (ElevenLabs supports SSML-style breaks).
- Generate **per section**, not the whole script in one go, so a mistake costs one paragraph.

## ElevenLabs (connected MCP)

1. `creative_list_voices` → pick a voice that fits (warm, trustworthy, local accent if available). Say which one you picked.
2. Make **one test line** (≈ 10 s) → owner approves the voice.
3. Generate section by section, with the same `flow_id` for the whole video so everything stays on one canvas.
4. Poll `creative_get_flow_run_status`. Never re-call a generation to "retry".
5. Greek: use a multilingual model and test pronunciation of place names (Λεμεσός, Πάφος) and trade terms.

Other options: vidIQ `voiceover_generate` (paid), or the owner records it themselves (best for trust, free).

## Music

- Licence first: use a library that clears YouTube Content ID (Artlist, YouTube Audio Library, Epidemic). Keep the licence/track ID in `assets/audio/LICENCES.md`.
- Choose by function: under-narration beds should be low-energy, sparse, and free of vocals.
- Cut music to the edit: start at a phrase, end on a downbeat or fade 2–3 s.
- AI music (ElevenLabs/vidIQ) is paid. Check that the terms allow commercial YouTube use.

## Mixing levels (rule of thumb)

| Element | Level relative to voice |
|---|---|
| Voice | reference (peaks ≈ −6 dBFS before master) |
| Music under voice | −18 to −24 dB below voice (duck it, see `video-ffmpeg-editing` §7) |
| Music with no voice | up to −6 dB below voice level |
| SFX | short, felt rather than noticed |

Clean the voice first: high-pass ~80 Hz, gentle de-noise (`afftdn`), light compression.
```bash
ffmpeg -i vo_raw.wav -af "highpass=f=80,afftdn=nf=-25,acompressor=threshold=-18dB:ratio=3:attack=5:release=100" vo_clean.wav
```

## Loudness targets (master)

| Destination | Integrated | True peak |
|---|---|---|
| YouTube / Shorts / Reels / TikTok | −14 LUFS | ≤ −1 dBTP |
| Podcasts | −16 LUFS (stereo) | ≤ −1 dBTP |
| Broadcast (EBU R128) | −23 LUFS | ≤ −1 dBTP |

Measure: `ffmpeg -i out.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -12`
Normalise: `loudnorm=I=-14:TP=-1:LRA=11` (`video-ffmpeg-editing` §7).

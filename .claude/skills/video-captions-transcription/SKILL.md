---
name: video-captions-transcription
description: Transcribe speech and make captions/subtitles for videos — Whisper (local, free) or ElevenLabs transcription, word-level timestamps, SRT/VTT/ASS files, caption style rules, Greek + English, translating subtitles, burned-in vs sidecar, TikTok-style word highlighting, and using the transcript to pick clean cut points. Use when a video needs captions, a transcript, subtitles in another language, or transcript-driven editing.
---

# Captions & transcription

## Get a transcript

Extract clean audio first: `ffmpeg -i in.mp4 -vn -ac 1 -ar 16000 -c:a pcm_s16le audio16k.wav`

| Option | Cost | Notes |
|---|---|---|
| `openai-whisper` (Python) | free, local, slow on CPU | `pip install -U openai-whisper` (needs ffmpeg) |
| `faster-whisper` (Python) | free, local, 4× faster | good default on CPU |
| `whisper.cpp` | free, local, fastest | build from github.com/ggml-org/whisper.cpp |
| ElevenLabs `creative_transcribe_audio` (connected MCP) | paid credits | apply the credit rule |

Model size: `small` for drafts, `medium`/`large-v3` for Greek or noisy audio. Always
pass the language (`--language el` or `en`). Auto-detect gets mixed Greek/English wrong.

```bash
whisper audio16k.wav --model medium --language en --output_format all --word_timestamps True --output_dir edit/
# → edit/audio16k.srt / .vtt / .json (word-level in json)
```

```python
# faster-whisper, word-level JSON
from faster_whisper import WhisperModel
m = WhisperModel("medium", compute_type="int8")
segs, _ = m.transcribe("audio16k.wav", language="el", word_timestamps=True, vad_filter=True)
for s in segs:
    for w in s.words: print(f"{w.start:.2f}\t{w.end:.2f}\t{w.word}")
```

When a script exists (narration for the Inonda videos), **align to the script** rather than
trusting Whisper's words: keep the script text and take only the timings from Whisper.

## Caption rules (readable on phones)

- ≤ 42 characters per line, ≤ 2 lines (Shorts: 1 line, 3–5 words).
- Each caption on screen 1–7 s; never flash one for under 0.8 s.
- Break at phrase boundaries, never between article and noun ("the | roof").
- Reading speed ≤ 17 characters/second (EN), ≤ 15 for Greek.
- Numbers and prices exactly as the script says them; check placeholders are filled.
- Safe area: keep captions above the bottom 15% (YouTube controls, Shorts UI).
- Greek: use a font with Greek glyphs (DejaVu Sans, Noto Sans, Inter). Check with `fc-list :lang=el`.

## File formats

- **SRT**: universal, upload to YouTube per language (`en.srt`, `el.srt`).
- **VTT**: web players.
- **ASS**: styled burn-in (fonts, colours, box, position, karaoke `\k` tags).

Minimal SRT:
```
1
00:00:00,000 --> 00:00:02,400
Is your bathroom stuck in the 1990s?
```

## Translation (EN ↔ GR)

Translate caption by caption and keep the timings. Then re-check line length (Greek runs
~15–20% longer, so split long lines). Have a native speaker review anything customer-facing.

## Burned-in vs sidecar

- YouTube long-form: **sidecar** SRTs (searchable, toggleable, multi-language).
- Shorts/Reels/TikTok: **burned-in**. Most people watch muted.
- Burn-in command: see `video-ffmpeg-editing` §8. Animated word-highlight captions: `video-remotion`.

## Transcript-driven editing (from BenAI video-repurposing, MIT)

- Clip boundaries come from **word timestamps**, not guesses.
- Whisper times run ~200–700 ms early. Add an audio buffer after the last word, or it gets clipped.
- Punctuation tokens have timestamps but aren't spoken. Never end a clip on them.
- Cut only where a thought ends and there's a breath (check `silencedetect`).
- Never open a clip with "But / And / So / It / This / I think". Start on a complete, explicit statement.

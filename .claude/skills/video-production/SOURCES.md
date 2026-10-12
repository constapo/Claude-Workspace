# Sources & co-workers for video making

Everything the crew can draw on, from free to paid. Licences change, so **re-check the
licence on the item's own page before using it** and record it in the project's
`SOURCES.md` / `LICENCES.md`. Researched 2026-10-12. Most third-party summaries disagree
on details, so the site's own terms win.

## 1. Free footage & photos

| Source | What | Licence (summary, verify) | Access |
|---|---|---|---|
| Pexels | video + photo | Pexels License: free commercial use, no attribution, no reselling as-is | API, free key → `PEXELS_API_KEY` |
| Pixabay | video, photo, music, SFX | Pixabay Content License: free commercial use, no attribution, restrictions on standalone resale; some music can trigger Content ID | API, free key → `PIXABAY_API_KEY` |
| Wikimedia Commons | video, photo, audio | per file: CC0 / CC BY / CC BY-SA / public domain. Attribution usually required | API, no key |
| Openverse | CC images + audio search across Flickr, museums, etc. | per item CC licence | API, no key |
| Internet Archive | archival video/audio | per item, often public domain | no key |
| NASA, EU audiovisual service | space / EU footage | mostly public domain or free with credit | web |
| Coverr, Mixkit, Videvo | short B-roll | site licences, and some items are restricted. Check each one | web |

Search helper: `python3 tools/video/stock_search.py {wikimedia|openverse|pexels|pixabay} "query"`.

## 2. Free music & sound effects

| Source | Notes |
|---|---|
| YouTube Audio Library (Studio → Audio library) | free for YouTube videos; some tracks need attribution; limits outside YouTube |
| Pixabay Music / SFX | free, no attribution. Keep the licence certificate, because Content ID claims happen |
| Freesound | per file CC0 / CC BY / CC BY-NC. Filter for **CC0** to avoid attribution; avoid NC for business videos |
| Free Music Archive, Incompetech | CC licences, mostly attribution required |
| Mixkit SFX | free licence. Check each item |

## 3. Fonts, icons, graphics

Google Fonts (OFL), **Noto Sans / Inter with Greek subset** for GR captions, Material
Symbols, Lucide icons, unDraw illustrations, Openverse for CC images.

## 4. Free open-source tools (the crew's workbench)

| Job | Tool | Status here |
|---|---|---|
| Cut/join/encode/QA | **FFmpeg / ffprobe** | installed |
| Code-driven video, templates, captions | **Remotion** (`npx create-video@latest`) | needs `npm i` per project |
| Maths/diagram animation | Manim, Motion Canvas | pip / npm |
| Transcription | faster-whisper, openai-whisper, whisper.cpp, WhisperX (word alignment) | `pip install faster-whisper` |
| Silence/jump-cut removal | auto-editor | `pip install auto-editor` |
| Scene detection | PySceneDetect | `pip install scenedetect` |
| Stem separation (remove music from voice) | Demucs | pip, heavy |
| Upscale / frame interpolation | Real-ESRGAN, RIFE | GPU |
| Background removal (stills) | rembg | pip |
| Full editors (owner's machine) | DaVinci Resolve (free), Kdenlive, Shotcut, Blender | desktop |
| Downloads | yt-dlp, **only for content you own or are licensed to use** | pip |

## 5. Open-weights AI models (free to run, need a strong GPU, not this container)

- **Video:** Wan 2.x (strong, permissive licence), LTX-2.3 (fast, audio + video in one pass), CogVideoX (Apache-2.0, small GPUs), HunyuanVideo (very heavy; community licence limits some commercial use), Mochi 1, SkyReels V2.
- **Voice (TTS):** Piper (light, fast), Kokoro, F5-TTS. Check the model licence. Some voice-clone models are non-commercial.
- **Music:** Stable Audio Open, MusicGen. Weights are often non-commercial, so check before using on a business channel.
- Usually run through ComfyUI or diffusers on a rented GPU (RunPod, Vast.ai). That costs money, so the credit rule applies to GPU rental too.

## 6. Paid co-workers (credit rule applies to every call)

| Service | Good for | How it's wired here |
|---|---|---|
| Higgsfield | photoreal AI clips | `higgsfield` agent + `tools/higgsfield/hf.py` (needs `HF_KEY`, host allowed) |
| Artlist | licensed stock, music, AI clips | `artlist` agent via the Artlist connector |
| Kling | AI clips, camera control | `kling-ai:*` plugin skills |
| Krea | images/video/upscale | Krea MCP |
| ElevenLabs | voice, voice design, transcription | ElevenLabs MCP |
| vidIQ | keywords, title/thumbnail scoring, B-roll, voiceover, chapters | vidIQ MCP (check which calls cost credits) |
| Canva / Adobe Express / Figma | thumbnails, end screens, social variants | MCPs |
| Veo / Runway / Seedance / Hailuo / RunComfy / fal.ai | other generators | not connected. Add a connector or key first |

## 7. Plugin skills already on this account (extra co-workers)

Try before installing anything new. Most call paid services:
`kling-ai:kling-ai-generate-video`, `kling-ai-prompt-generator:kling-ai`,
`ai-video-editor:video-editing` / `video-generation`, `openclip:caption-video` /
`clip-video` / `repurpose-clips`, `openclips:openclips-edit` / `-clips` / `-video-ads`,
`blitzreels:blitzreels-editing` / `-clipping` / `-generation`, `muapi:generate-video` /
`image-to-video`, `arcads:*` (ads, cinematic, image-to-motion), `naksha:video-script` /
`gen-video` / `motion-design`, `cineflo:build-shot-list` / `script-breakdown` /
`prep-call-sheet` / `plan-shoot-days` (real filming days), `audiopod:audiopod-stems` /
`-transcribe` / `-audio-cleanup`, `canva:resize-for-social-media`,
`adobe-for-creativity:adobe-edit-quick-cut` / `adobe-resize-photos-and-videos`,
`content-intelligence:thumbnails`, `cloudinary:cloudinary-transformations`.
They only work in sessions where the plugin's server connects. Several failed to connect
in the 2026-10-12 session because of the network policy.

## 8. Network access needed in this cloud environment

These hosts were blocked on 2026-10-12. The owner can add them under the environment's
network settings → Allowed domains:
`commons.wikimedia.org`, `upload.wikimedia.org`, `api.openverse.org`, `api.pexels.com`,
`videos.pexels.com`, `images.pexels.com`, `pixabay.com`, `cdn.pixabay.com`, `archive.org`,
`freesound.org`, `api.higgsfield.ai`. Docs: https://code.claude.com/docs/en/cloud-environments#network-access

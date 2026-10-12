---
name: video-ai-generation
description: Plan, prompt, price and quality-check AI-generated video clips (text-to-video, image-to-video, extend) on any service — Higgsfield, Artlist, Kling, Veo, Seedance, Wan, Hailuo, Runway, Krea, vidIQ. Covers model choice, the shot-prompt formula, photorealism, character/style consistency, cost estimates and the reject list. Use before ANY paid video generation, when writing a shot list, or when a generated clip looks fake.
---

# AI video generation

## Gate (from `/CLAUDE.md`, never skip)

1. Write the shot list / prompts as text and show them. Nothing is generated yet.
2. Price it: clips × seconds × rate. Use the service's free estimate when it has one, and say plainly when there isn't one.
3. Get explicit approval for **this** batch in **this** conversation.
4. Generate **one** test clip, check it against the reject list, show it, wait for approval.
5. On failure or timeout: check the job status. Never resubmit blindly.
6. Report paths/links only, never auto-open.

## Choose the approach per shot (cheapest that works)

| Shot need | Approach |
|---|---|
| Proof of real work: a specific real job, real client, testimonial, real before/after | **FILM** it (real footage or records) |
| People at work, presenters, homeowners, example jobs | **Photoreal AI actors / fictional example job** that look like real camera footage and match the narration exactly, labelled "AI-generated". Never the likeness of a real person |
| Real people you film (owner, staff, clients) | **FILM** with signed written consent; otherwise blur or use an AI actor |
| Text, icons, checklists, end screens | **GFX** in Remotion/editor (free) |
| Generic B-roll that exists in stock libraries | **Stock** (Artlist, Pexels, Pixabay), usually cheaper and more realistic |
| Generic B-roll with no stock match | **Text-to-video** |
| Exact composition, product or location you have a photo of | **Image-to-video** from a real photo (more realistic than from an AI still) |
| Longer continuous shot | Generate 5 s, then **extend** (Veo extend), or cut between two clips |

## Model cheat-sheet (late 2026, vendor claims, verify on the service)

| Model | Strong at | Weak at |
|---|---|---|
| Veo 3.1 (Google) | photoreal physics, object permanence, native audio, extend | cost |
| Kling 3.0 (Pro/4K) | deliberate camera moves, subject consistency over 5–10 s, multi-shot | lip-sync, >10 s |
| Seedance v2 Pro | cinematic, multi-reference (images/video/audio refs) | overkill for simple shots |
| Wan 2.7 | open weights, lip-sync to a given audio file | in-pass audio |
| Hailuo 2.3 Pro | lifelike motion of real people and products | stylised content |
| Dreamina 3.0 | illustrated/painterly | photoreal |

For this repo's realism standard, use the most photoreal tier. Never "fast", "draft" or
"turbo" tiers for final shots. Fast tiers are fine only for a cheap composition test, and
only if the owner approves that.

## The shot-prompt formula

Describe a **shot**, not a picture. One subject, one action, one camera move.

```
[SHOT & CAMERA]  medium close-up, 35mm lens, slow handheld push-in
[SUBJECT]        a worker's gloved hands
[ACTION]         press a notched trowel through grey tile adhesive on a bathroom wall
[SETTING]        small Cyprus bathroom, white render, 1990s ceramic tiles, window daylight
[LOOK]           handheld documentary, warm slightly desaturated, shallow depth of field
[AUDIO]          (only if the model makes audio) scrape of trowel, distant traffic
[REALISM GUARD]  append the guard from inonda-youtube-videos/shot-list.md
```

Rules that keep clips realistic:
- **Motion verbs beat adjectives.** "presses", "drips", "peels back" > "beautiful", "stunning".
- **Use real camera language**: lens (24/35/50/85mm), real light (window, overcast, low sun), real moves (static tripod, slow push-in, pan left, handheld). One move per clip.
- **Avoid faces and hands in fast motion.** Aggressive moves on hands or faces cause warping.
- **No text in the frame.** Models garble letters. Add text later as GFX.
- **Lived-in detail**: dust, scuffs, uneven grout, clutter at the frame edge.
- **Don't pack events.** No prop changes, outfit changes or cuts inside one generation.
- **5 seconds by default.** Longer clips drift and cost more.
- Negative prompt / avoid list when supported: CGI, 3D render, cartoon, oversaturated, glow, slow-motion, warped hands, extra fingers, melting, garbled text, watermark.

## Consistency across shots

- Lock a **style line** and append it verbatim to every prompt in a video. The Inonda one is in `shot-list.md`.
- Keep the same aspect ratio, resolution, model and seed family per video.
- For a recurring subject, generate or photograph one **reference image** and use image-to-video or reference inputs (Kling elements, Seedance refs). Avoid re-describing the subject from scratch.
- Heavy option: train a LoRA / use IPAdapter+FaceID (ComfyUI). Only for a recurring character, and never for a real person without consent.

## Image-to-video tips

- Start from a sharp, well-lit real photo at the target aspect ratio.
- Prompt only the **motion**: "camera slowly pushes in; dust drifts in the window light; no other motion".
- Say what must stay still ("the tiles do not move").

## Pricing template (show before asking)

```
Batch: V01 test clip
Clips: 1 × 5 s, 16:9, 1080p, model <name> (<tier>)
Rate:  <credits per second or per clip> (source: <free estimate / price page / unknown>)
Total: <n> credits ≈ <€/$ if known>. Balance: <n>
Approve this one clip? (yes/no)
```

## Reject list (check every clip before showing it as usable)

Wrong finger counts, tools merging with hands, morphing or melting objects, liquids flowing
unnaturally, garbled text or logos, plastic/CGI surfaces, impossible light, warped walls or
tiles, warped or melting faces, any face resembling a real person, and visible watermarks. A rejected clip is
reported with the reason and is **not** regenerated without approval.

Quick local check: pull frames and look at them before calling a clip good:
```bash
ffmpeg -v error -i clip.mp4 -vf "fps=2,scale=640:-2,tile=5x2" -frames:v 1 contact.jpg
```

## Naming

`V<video>-<shot>_<model>_take<n>.mp4`, e.g. `V01-03_kling3pro_take1.mp4`. Record the
prompt, model, seed, cost and verdict next to the shot in `shot-list.md`.

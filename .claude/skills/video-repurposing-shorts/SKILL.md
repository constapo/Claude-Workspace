---
name: video-repurposing-shorts
description: Turn a long video into YouTube Shorts, Instagram Reels, TikToks, teasers and highlight clips — picking hooks from the transcript, sentence-aligned cuts, vertical reframing, burned-in captions, length and platform specs. Use when the user wants shorts, reels, clips, a teaser/trailer, or a vertical version of any video.
---

# Repurposing into Shorts / Reels / TikTok

Based on BenAI `video-repurposing` and ECC `video-editing` (MIT), adapted for this repo.

## Platform specs (check before export)

| Platform | Aspect / size | Length | Notes |
|---|---|---|---|
| YouTube Shorts | 9:16, 1080×1920 | up to 3 min (≤ 60 s performs most reliably) | link to the long video via "related video" |
| Instagram Reels | 9:16, 1080×1920 | up to 3 min (15–60 s typical) | keep text out of the bottom 20% and right edge |
| TikTok | 9:16, 1080×1920 | up to 10 min | first 1–2 s decide the swipe |
| Facebook / LinkedIn feed | 1:1 or 4:5 | 30–90 s | captions mandatory |

Specs change. Confirm current limits on the platform before a batch.

## Workflow

1. **Intake**: which long video, which platforms, how many clips, burn captions (yes by default), reveal the ending or keep curiosity.
2. **Transcript** with word timestamps (`video-captions-transcription`).
3. **Find candidates**: hooks, bold claims, surprising numbers, before/after reveals, common mistakes, questions viewers ask. Score each one: hook strength, standalone sense, payoff.
4. **Propose an edit plan** with exact timestamps and the first and last words of each clip. Get approval before rendering.
5. **Cut** (`video-ffmpeg-editing` §2), **reframe** (§5), **caption** (burn-in), **loudness** (§7).
6. **Review copy** at low resolution for approval → final export (§12).

## Hook & ending rules (critical)

- The first second must make sense on its own: a statement, a striking visual, or a question.
- Never open with "But / And / So / Now / It / This / They / I think / Basically".
- End on a resolved thought: a takeaway, a punchline, or a call to action. Never trail off.
- Every cut sits at a natural pause, never mid-word. Check with `silencedetect`.
- Hard cuts, no fades (fades read as template-ware on feeds).

## Making it work vertically

- Centre crop when the subject is central. Shift the crop x when it isn't. Use blurred background fill when the whole frame matters (before/after shots).
- For AI B-roll destined for Shorts, generate **natively in 9:16** rather than cropping. Price it as a separate clip.
- Big captions (1 line, 3–5 words, centre-lower third). Highlight one keyword in the brand colour.
- Add a 1–2 word title card in the first 2 s only if the visual hook is weak.

## Inonda specifics

- Each of the 20 long videos → 3–5 Shorts: the hook, the top mistake, the price/time reveal, the before/after.
- Greek and English versions: same cut, different caption file. Voiceover only if it was recorded in both languages.
- Shorts end screen: "Full video on the channel" + phone/WhatsApp (fill the real number, never leave the placeholder).

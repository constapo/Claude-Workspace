---
name: video-youtube-packaging
description: Script structure and packaging for YouTube — hook and retention structure, titles, thumbnails, descriptions, chapters, tags, end screens, and using vidIQ (connected) for keyword research and title/thumbnail scoring. Use when writing or tightening a video script, choosing a title or thumbnail, or preparing a video for upload.
---

# YouTube scripting & packaging

Adapted from the BenAI YouTube chain (ideation → brief → outline → scripting → packaging →
thumbnail → chapters → description, MIT) and made generic for this repo.

## Package first, then script

Decide the **title + thumbnail idea before writing the script**. If the package isn't
clickable, the video won't be watched however good it is.

## Script structure that holds viewers

1. **Hook (0–15 s)**: show the result or the problem and state the promise. No "Hi guys, welcome back".
2. **Stakes (15–45 s)**: why it matters (cost of doing it wrong, risk, money).
3. **Body**: 3–5 sections, each opening with a mini-hook. Put a pattern change (new visual, graphic, location) every 20–40 s.
4. **Payoff**: the reveal (before/after, final price, finished job).
5. **CTA (last 10–20 s)**: one action only (call/WhatsApp, or watch the next video). End screen for 5–20 s.

Write narration and on-screen text in two columns, or tag `[GFX]`, `[B-ROLL V01-03]`, `[FILM]`.

## Titles

- ≤ 60 characters, front-load the keyword, promise a specific outcome or curiosity gap.
- Patterns: "X mistakes that…", "How much does X cost in <place> (real numbers)", "Before & after: …", "Don't do X until you watch this".
- Write 10 options, then shortlist 3. vidIQ `vidiq_score_title` and `vidiq_keyword_research` (connected; check whether each call costs credits before using it).

## Thumbnails

- 1280×720 (16:9), < 2 MB, readable at phone size: one subject, one emotion or contrast, ≤ 4 words.
- Before/after split works for renovation. Real photos beat AI (trust); label anything AI as an illustration.
- Make 2–3 variants (Canva MCP, Adobe Express MCP, or `npx remotion still`) and use YouTube's "Test & compare".
- vidIQ `vidiq_score_thumbnail` / `vidiq_generate_thumbnail` are paid, so apply the credit rule.

## Description

```
<1–2 sentence summary with main keyword>
📞 <real phone/WhatsApp> · 🌐 <site>

Chapters
00:00 <hook>
00:42 <section>
...

<3–5 lines of extra context, service area, keywords naturally>
#hashtag1 #hashtag2 #hashtag3
```
Chapters: the first must be `00:00`, at least 3 chapters, each ≥ 10 s. Build them from the
transcript timestamps (vidIQ `vidiq_generate_video_chapters` can draft them).

## Tags & metadata

- 5–15 tags: exact keyword, variants, location ("Limassol", "Cyprus"), Greek spellings.
- Upload SRT captions for EN and GR (`video-captions-transcription`).
- Set the language, category, and "altered or synthetic content" disclosure when realistic AI footage is used (YouTube requires it).

## Pre-upload checklist

- [ ] Title ≤ 60 chars, thumbnail readable on a phone
- [ ] Description with chapters, contact details filled (no `[ADD …]` placeholders)
- [ ] Captions uploaded (EN + GR)
- [ ] End screen + cards set
- [ ] AI-content disclosure set where needed
- [ ] Publish time chosen (vidIQ best-time data, if available)

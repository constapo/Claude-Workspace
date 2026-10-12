---
name: video-remotion
description: Build videos as code with Remotion (React) — project setup, compositions, sequences, timing, overlays, lower thirds, animated titles, word-highlight captions, charts, templates reused across a video series, and rendering MP4s. Use for motion graphics, GFX shots, branded templates, kinetic captions, or any edit that should be repeatable across many videos (e.g. 20 Inonda episodes).
---

# Remotion (video as code)

Remotion renders React components frame by frame to MP4. It's free for individuals and small
companies; bigger companies need a licence (check remotion.dev/license before commercial
scale). Rendering is local, so it spends no AI credits.

**Official skills**: inside a Remotion project, run `npx remotion skills add` to install
Remotion's own agent skills (best-practices, captions, render, studio…). Prefer them for API
detail. This skill covers the workflow and the house rules.

## Setup

```bash
npx create-video@latest inonda-gfx      # pick "Blank" or "Hello World" (TypeScript)
cd inonda-gfx && npm i
npx remotion studio                     # preview in browser (don't auto-open on the owner's machine)
npx remotion render src/index.ts MyComp out/mycomp.mp4
```
Media goes in `public/` (no spaces in filenames) and is referenced with `staticFile("x.mp4")`.
Source video must be H.264 with `-movflags +faststart` (see `video-ffmpeg-editing`), or the studio crawls.

## Core concepts

```tsx
// src/Root.tsx — register every composition
import { Composition } from "remotion";
import { Episode } from "./Episode";
export const Root = () => (
  <Composition id="Episode01" component={Episode} durationInFrames={30 * 60}
    fps={30} width={1920} height={1080} defaultProps={{ title: "Bathroom renovation" }} />
);
```

```tsx
// src/Episode.tsx
import { AbsoluteFill, Sequence, OffthreadVideo, Audio, staticFile,
         useCurrentFrame, interpolate, spring, useVideoConfig } from "remotion";

export const Episode: React.FC<{ title: string }> = ({ title }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const pop = spring({ frame, fps, config: { damping: 200 } });
  return (
    <AbsoluteFill style={{ backgroundColor: "#0A0A14" }}>
      <Sequence from={0} durationInFrames={150} premountFor={60}>
        <OffthreadVideo src={staticFile("V01-01.mp4")} />
      </Sequence>
      <Sequence from={20} durationInFrames={100}>
        <AbsoluteFill style={{ justifyContent: "flex-end", padding: 80 }}>
          <div style={{ transform: `scale(${pop})`, opacity: interpolate(frame, [20, 30], [0, 1], { extrapolateRight: "clamp" }),
                        fontSize: 64, color: "white", fontFamily: "Inter" }}>{title}</div>
        </AbsoluteFill>
      </Sequence>
      <Audio src={staticFile("voiceover.wav")} />
    </AbsoluteFill>
  );
};
```

- Time is frames: `seconds × fps`. Keep `fps` = 30 for all Inonda output.
- `useCurrentFrame()` inside a `<Sequence>` restarts at 0.
- Use `<OffthreadVideo>` for rendering accuracy, `premountFor` to avoid blank first frames.
- Animate only with `interpolate`/`spring` driven by the frame. **Never** use CSS transitions, `setTimeout`, or `Math.random()` without a seed, because renders must be deterministic.
- Fonts: `@remotion/google-fonts/Inter` (has Greek subset: load `subsets: ["greek"]`).

## House rules (from BenAI video-repurposing + ECC video-editing, MIT)

- One `CONFIG` block at the top of each composition: clip list with `startMs`/`endMs` and the spoken words as comments. It should be the only place anyone edits.
- **Hard cuts by default**: plain consecutive `<Sequence>`s. Use crossfades only for trailers, and only when asked.
- Brand kit in one file (`src/brand.ts`): colours, fonts, caption style. Never pure `#000`.
- Template once, reuse 20×: drive each episode with `defaultProps` / `--props=episode01.json`.
- Run QA (duration, black/freeze detection, loudness) before showing a preview. Render the final only on approval.

## Word-highlight captions

Install `@remotion/captions`. Build a `Caption[]` (`{text, startMs, endMs}`) from Whisper word
JSON (see `video-captions-transcription`), group with `createTikTokStyleCaptions({ captions,
combineTokensWithinMilliseconds: 1200 })`, render each page in a `<Sequence>`, and colour the
token whose `fromMs ≤ currentMs < toMs`.

## Rendering

```bash
npx remotion render src/index.ts Episode01 out/ep01_16x9.mp4 --codec h264 --crf 18
npx remotion render src/index.ts Episode01 out/ep01.mp4 --props=props/ep01.json
npx remotion still src/index.ts Thumbnail out/thumb.png --frame=0      # thumbnails from code
```
Vertical version: register a second composition at 1080×1920 that reuses the same scenes.

## Alternatives

- **Manim** (Python) for maths/diagram explainers (ECC `manim-video`).
- **Motion Canvas** for code-driven explainer animation.
- Plain FFmpeg `drawtext` for one static label (much faster to set up).

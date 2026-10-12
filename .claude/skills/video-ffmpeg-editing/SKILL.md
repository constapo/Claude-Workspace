---
name: video-ffmpeg-editing
description: Edit video locally and for free with FFmpeg/ffprobe — inspect, cut, trim, join, proxy, reframe 16:9↔9:16↔1:1, crossfade, overlay logos/text, mix and duck music, normalise loudness, burn subtitles, detect silence/scenes/black/frozen frames, extract stills, and export YouTube/Shorts presets. Use for any deterministic edit of footage or AI clips, assembling a rough cut from an edit list, or QA of a render.
---

# FFmpeg editing

FFmpeg is installed in this environment (`ffmpeg -version`). It's free and needs no approval.
Plan the edit as an **edit decision list** first (`edit/cuts.csv`: `start,end,label`), then run commands.
Never overwrite source files. Write to `out/` or `edit/`.

## 1. Inspect first

```bash
ffprobe -v error -show_entries format=duration:stream=codec_name,width,height,r_frame_rate,sample_rate,channels -of compact in.mp4
```
- AV1 or VP9 source (YouTube downloads) → transcode to H.264 before editing in Remotion.
- Different fps/resolution across clips → normalise before concat (section 3).

## 2. Cut

```bash
# Fast, no re-encode (cuts snap to keyframes — may be off by up to ~2 s)
ffmpeg -ss 00:01:05 -to 00:01:20 -i in.mp4 -c copy cut.mp4
# Frame-accurate (re-encode)
ffmpeg -ss 65.4 -to 80.2 -i in.mp4 -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 192k cut.mp4
# Batch from edit list
while IFS=, read -r s e label; do
  ffmpeg -nostdin -v error -ss "$s" -to "$e" -i raw.mp4 -c:v libx264 -crf 18 -c:a aac "edit/${label}.mp4"
done < edit/cuts.csv
```
`-nostdin` is required inside `while read` loops, or ffmpeg eats the list.

## 3. Join

```bash
# Same codec/size/fps → lossless concat
for f in edit/seg_*.mp4; do echo "file '$PWD/$f'"; done > edit/list.txt
ffmpeg -f concat -safe 0 -i edit/list.txt -c copy out/assembled.mp4

# Mixed sources (AI clips from different models) → normalise each first
ffmpeg -i in.mp4 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30,format=yuv420p" \
  -c:v libx264 -crf 18 -c:a aac -ar 48000 -ac 2 norm.mp4
# Clips with no audio track: add silence so concat doesn't break
ffmpeg -i silent.mp4 -f lavfi -i anullsrc=r=48000:cl=stereo -shortest -c:v copy -c:a aac with_audio.mp4
```

## 4. Transitions

Hard cuts are the default (they read as confident). For a crossfade between two normalised clips:
```bash
# A is 5 s long; 0.5 s fade starting at 4.5 s
ffmpeg -i a.mp4 -i b.mp4 -filter_complex \
 "[0:v][1:v]xfade=transition=fade:duration=0.5:offset=4.5[v];[0:a][1:a]acrossfade=d=0.5[a]" \
 -map "[v]" -map "[a]" -c:v libx264 -crf 18 xfade.mp4
```
Fade in/out at the start and end: `-vf "fade=t=in:st=0:d=0.5,fade=t=out:st=9.5:d=0.5" -af "afade=t=in:d=0.5,afade=t=out:st=9.5:d=0.5"`.

## 5. Reframe for other platforms

```bash
# 16:9 → 9:16 centre crop (Shorts/Reels/TikTok)
ffmpeg -i in.mp4 -vf "crop=ih*9/16:ih,scale=1080:1920" -c:a copy vertical.mp4
# 16:9 → 9:16 with blurred background (keeps the whole frame)
ffmpeg -i in.mp4 -filter_complex \
 "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20[bg];[0:v]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2" \
 -c:a copy vertical_blur.mp4
# 16:9 → 1:1
ffmpeg -i in.mp4 -vf "crop=ih:ih,scale=1080:1080" -c:a copy square.mp4
```
Off-centre subject: change crop x, e.g. `crop=ih*9/16:ih:x=iw*0.6-ih*9/32:y=0`.

## 6. Overlays

```bash
# Logo top-right, 40 px margin, 288 px wide (15% of 1920)
ffmpeg -i in.mp4 -i logo.png -filter_complex "[1:v]scale=288:-1[l];[0:v][l]overlay=W-w-40:40" -c:a copy logo.mp4
# Simple text label (e.g. the "Illustration" tag on AI shots), shown 0–5 s
ffmpeg -i in.mp4 -vf "drawtext=text='Illustration':fontcolor=white:fontsize=36:box=1:boxcolor=black@0.5:boxborderw=12:x=40:y=h-th-40:enable='between(t,0,5)'" -c:a copy labelled.mp4
```
Use `fontfile=/path/font.ttf` for Greek text if the default font lacks the glyphs (`fc-list :lang=el`).
Anything fancier (animated lower thirds, kinetic text) belongs in Remotion.

## 7. Audio

```bash
# Music under voice, auto-ducked when voice speaks
ffmpeg -i voice.wav -i music.mp3 -filter_complex \
 "[1:a]volume=0.5[m];[m][0:a]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[duck];[0:a][duck]amix=inputs=2:duration=first:normalize=0[a]" \
 -map "[a]" -c:a pcm_s16le mix.wav
# Put the mix on the picture
ffmpeg -i picture.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest with_mix.mp4
# Loudness normalise to YouTube-ish target (two-pass is more accurate; single pass shown)
ffmpeg -i in.mp4 -af loudnorm=I=-14:TP=-1:LRA=11 -c:v copy -c:a aac -b:a 192k loud.mp4
# Measure loudness only
ffmpeg -i in.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -12
# Extract audio for transcription (16 kHz mono WAV)
ffmpeg -i in.mp4 -vn -ac 1 -ar 16000 -c:a pcm_s16le audio16k.wav
```

## 8. Subtitles

```bash
# Burn in (style via ASS force_style)
ffmpeg -i in.mp4 -vf "subtitles=captions.srt:force_style='FontName=DejaVu Sans,FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H80000000,BorderStyle=3,Outline=2,MarginV=60'" -c:a copy subbed.mp4
# Soft subtitles (toggleable), EN + GR tracks
ffmpeg -i in.mp4 -i en.srt -i el.srt -map 0 -map 1 -map 2 -c copy -c:s mov_text \
  -metadata:s:s:0 language=eng -metadata:s:s:1 language=ell soft.mp4
```
For YouTube, upload `.srt` files separately rather than burning them in, except on Shorts.

## 9. Detection (auto-cut & QA)

```bash
ffmpeg -i in.mp4 -af silencedetect=noise=-30dB:d=0.6 -f null - 2>&1 | grep -E 'silence_(start|end)'
ffmpeg -i in.mp4 -vf "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -o 'pts_time:[0-9.]*'
ffmpeg -i in.mp4 -vf blackdetect=d=0.2:pix_th=0.10 -an -f null - 2>&1 | grep blackdetect
ffmpeg -i in.mp4 -vf freezedetect=n=-60dB:d=1 -an -f null - 2>&1 | grep freeze
```

## 10. Stills, contact sheets, GIF

```bash
ffmpeg -ss 12.5 -i in.mp4 -frames:v 1 -q:v 2 still.jpg              # thumbnail candidate
ffmpeg -i in.mp4 -vf "fps=1/10,scale=480:-2,tile=4x3" -frames:v 1 sheet.jpg   # overview
ffmpeg -i in.mp4 -vf "fps=12,scale=480:-2:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse" -t 4 clip.gif
```

## 11. Speed, stabilise, colour

```bash
ffmpeg -i in.mp4 -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" fast2x.mp4
ffmpeg -i in.mp4 -vf vidstabdetect -f null - && ffmpeg -i in.mp4 -vf vidstabtransform=smoothing=20 stab.mp4  # needs vidstab build
ffmpeg -i in.mp4 -vf "eq=contrast=1.05:saturation=0.9,colortemperature=temperature=5800" -c:a copy graded.mp4
```
Matching AI clips from different models: a light shared grade (same `eq` on every clip) helps them sit together.

## 12. Export presets

```bash
# YouTube master 1080p30
ffmpeg -i in.mp4 -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -ar 48000 -movflags +faststart out/master_16x9.mp4
# Shorts/Reels 1080x1920, ≤ 60 s for Shorts
ffmpeg -i vertical.mp4 -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart out/short_9x16.mp4
# Small review copy to share for approval
ffmpeg -i in.mp4 -vf scale=960:-2 -c:v libx264 -crf 28 -preset veryfast -c:a aac -b:a 96k out/review.mp4
```
Always `-pix_fmt yuv420p` (plays everywhere) and `-movflags +faststart` (streams immediately).

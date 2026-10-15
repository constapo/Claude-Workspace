#!/usr/bin/env python3
"""Assemble video 01: one shot per narration line (edl.json), English Kokoro voice,
Greek subtitles burned in for the whole video, 1920x1080 30 fps, loudness -14 LUFS.

Inputs : lines.json, edl.json, build/tts/*.wav, build/stock/*.mp4 (from branch stock-media-v01)
Outputs: build/v01.mp4, build/v01.gr.srt, build/v01.en.srt
edl.json: {"<line id>": {"clip": "<file in build/stock>", "in": <seconds into the clip>}, ...}
"""
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, "build")
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
GAP, LONG_GAP = 0.35, 0.9          # pause after a line; longer after a section / a <break>
LONG_AFTER = {"1.4", "1.8", "2.9", "3.11", "4.9", "5.5", "6.8", "7.1", "7.8", "7.11", "8.9", "9.5", "10.8", "11.5"}
TAIL = 2.0                          # picture held after the last line


def run(*cmd):
    subprocess.run(cmd, check=True)


def dur(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                                 "default=nw=1:nk=1", path], capture_output=True, text=True).stdout)


def ts(t):
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s % 1) * 1000)) % 1000:03d}"


def split_cue(text, a, b, limit=84):
    """Split a long subtitle into readable parts, timed by length."""
    parts, cur = [], ""
    for chunk in [c for c in text.replace(", ", ",| ").replace(". ", ".| ").split("| ")]:
        if cur and len(cur) + len(chunk) > limit:
            parts.append(cur.strip())
            cur = ""
        cur += chunk + " "
    parts.append(cur.strip())
    total, t, out = sum(len(p) for p in parts), a, []
    for p in parts:
        e = t + (b - a) * len(p) / total
        out.append((t, e, p))
        t = e
    return out


def wrap2(text, width=48):
    """Two lines at most, broken near the middle."""
    if len(text) <= width:
        return text
    words, best = text.split(), None
    for i in range(1, len(words)):
        l1, l2 = " ".join(words[:i]), " ".join(words[i:])
        score = max(len(l1), len(l2))
        if best is None or score < best[0]:
            best = (score, l1 + "\n" + l2)
    return best[1]


def main():
    lines = json.load(open(os.path.join(HERE, "lines.json"), encoding="utf-8"))
    edl = json.load(open(os.path.join(HERE, "edl.json"), encoding="utf-8"))
    seg_dir = os.path.join(B, "seg")
    os.makedirs(seg_dir, exist_ok=True)

    # 1. Timeline from the voice
    t, timeline = 0.0, []
    for i, ln in enumerate(lines):
        d = dur(os.path.join(B, "tts", ln["id"] + ".wav"))
        gap = LONG_GAP if ln["id"] in LONG_AFTER else GAP
        slot = d + gap + (TAIL if i == len(lines) - 1 else 0)
        timeline.append(dict(ln, start=t, speech=d, slot=slot, gap=gap))
        t += slot

    # 2. Voice track: lines + silences, then loudness to -14 LUFS
    alist = os.path.join(B, "audio_list.txt")
    with open(alist, "w") as f:
        for i, x in enumerate(timeline):
            sil = os.path.join(seg_dir, f"sil_{i:03d}.wav")
            run("ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
                "-t", f"{x['slot'] - x['speech']:.3f}", sil)
            f.write(f"file '{os.path.join(B, 'tts', x['id'] + '.wav')}'\nfile '{sil}'\n")
    raw = os.path.join(B, "voice_raw.wav")
    run("ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", alist, "-c", "pcm_s16le", raw)
    voice = os.path.join(B, "voice.m4a")
    run("ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af",
        "highpass=f=70,loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-ac", "2", "-c:a", "aac", "-b:a", "192k", voice)

    # 3. Picture: one segment per line, cut from the chosen clip (slowed if the clip is short)
    vlist = os.path.join(B, "video_list.txt")
    with open(vlist, "w") as f:
        for i, x in enumerate(timeline):
            e = edl[x["id"]]
            clip = os.path.join(B, "stock", e["clip"])
            avail = dur(clip) - e.get("in", 0)
            speed = min(1.0, avail / x["slot"])          # <1 = slow motion to fill the slot
            seg = os.path.join(seg_dir, f"v_{i:03d}.mp4")
            vf = (f"setpts=PTS/{max(speed, 0.5):.4f},scale=1920:1080:force_original_aspect_ratio=increase,"
                  f"crop=1920:1080,fps=30,format=yuv420p")
            loop = ["-stream_loop", "-1"] if speed < 0.5 else []
            run("ffmpeg", "-y", "-loglevel", "error", *loop, "-ss", str(e.get("in", 0)), "-i", clip, "-t",
                f"{x['slot']:.3f}", "-an", "-vf", vf, "-c:v", "libx264", "-preset", "fast", "-crf", "18", seg)
            f.write(f"file '{seg}'\n")
    picture = os.path.join(B, "picture.mp4")
    run("ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", vlist, "-c", "copy", picture)

    # 4. Subtitles (Greek burned in; English sidecar)
    for lang in ("gr", "en"):
        n, out = 1, []
        for x in timeline:
            for a, b, txt in split_cue(x[lang], x["start"], x["start"] + x["speech"] + min(x["gap"], 0.3)):
                out.append(f"{n}\n{ts(a)} --> {ts(b)}\n{wrap2(txt)}\n")
                n += 1
        open(os.path.join(B, f"v01.{lang}.srt"), "w", encoding="utf-8").write("\n".join(out))

    style = ("FontName=DejaVu Sans,FontSize=20,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
             "BackColour=&H80000000,BorderStyle=1,Outline=2.2,Shadow=1,Alignment=2,MarginV=38")
    srt = os.path.join(B, "v01.gr.srt").replace(":", r"\:")
    run("ffmpeg", "-y", "-loglevel", "error", "-i", picture, "-i", voice, "-map", "0:v", "-map", "1:a",
        "-vf", f"subtitles='{srt}':fontsdir={FONT_DIR}:force_style='{style}'",
        "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-profile:v", "high", "-pix_fmt", "yuv420p",
        "-c:a", "copy", "-movflags", "+faststart", "-shortest", os.path.join(B, "v01.mp4"))
    json.dump(timeline, open(os.path.join(B, "timeline.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("done", round(t, 1), "s")


if __name__ == "__main__":
    main()

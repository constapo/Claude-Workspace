#!/usr/bin/env python3
"""Build a free explainer video: presenter photo + section titles + burned captions + narration.

Usage: build_explainer.py <sections.json> <presenter.jpg> <out_dir> [--title "Video title"]
sections.json comes from the TTS step: [{"title","text","wav","dur"}, ...]
"""
import json, os, re, subprocess, sys, textwrap

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
BG, ACCENT = "0x0A0A14", "0xB8E0B0"


def run(cmd):
    subprocess.run(cmd, check=True)


def esc(t):
    return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’").replace("%", "\\%")


def ts(t):
    h, m = int(t // 3600), int(t % 3600 // 60)
    s = t % 60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int((s % 1) * 1000):03d}"


def captions(text, dur, offset):
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    chunks = []
    for s in sents:  # split long sentences at commas so each caption is <= ~84 chars
        while len(s) > 84:
            cut = s.rfind(", ", 0, 84)
            cut = cut + 1 if cut > 20 else s.rfind(" ", 0, 84)
            chunks.append(s[:cut].strip()); s = s[cut:].strip()
        chunks.append(s)
    total = sum(len(c) for c in chunks) or 1
    t, out = offset, []
    for c in chunks:
        d = dur * len(c) / total
        out.append((t, t + d, "\n".join(textwrap.wrap(c, 42))))
        t += d
    return out


def main():
    sec_file, photo, out = sys.argv[1], sys.argv[2], sys.argv[3]
    title = sys.argv[sys.argv.index("--title") + 1] if "--title" in sys.argv else ""
    os.makedirs(out, exist_ok=True)
    secs = json.load(open(sec_file))
    parts, srt, t0 = [], [], 0.0
    for n, s in enumerate(secs):
        d = s["dur"] + 0.6
        frames = int(d * 30)
        seg = f"{out}/seg{n:02d}.mp4"
        vf = (
            f"[1:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,boxblur=30,eq=brightness=-0.25[bg];"
            f"[1:v]crop=iw:ih*0.84:0:0,eq=contrast=1.12:brightness=-0.04:saturation=1.1,scale=-2:760,"
            f"zoompan=z='min(zoom+0.0004,1.12)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=1426x760:fps=30[p];"
            f"[bg][p]overlay=70:110[v1];"
            f"[v1]drawbox=x=1540:y=110:w=330:h=760:color={BG}@0.85:t=fill,"
            f"drawtext=fontfile={FONTB}:text='{esc(s['title'])}':fontcolor={ACCENT}:fontsize=40:x=70:y=40,"
            f""+"".join(f"drawtext=fontfile={FONT}:text='{esc(l)}':fontcolor=white:fontsize=26:x=1560:y={140+i*36}," for i,l in enumerate(textwrap.wrap(title,18)))+f""
            f"drawtext=fontfile={FONT}:text='INONDA LTD':fontcolor={ACCENT}:fontsize=34:x=1560:y=820,"
            f"drawtext=fontfile={FONT}:text='AI voice':fontcolor=white@0.7:fontsize=22:x=1560:y=760[v]"
        )
        run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c={BG}:s=1920x1080:r=30:d={d}",
             "-loop", "1", "-i", photo, "-i", s["wav"], "-filter_complex", vf,
             "-map", "[v]", "-map", "2:a", "-t", f"{d}", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
             "-pix_fmt", "yuv420p", "-c:a", "aac", "-ar", "48000", "-ac", "2", "-af", "apad", seg])
        srt += captions(s["text"], s["dur"], t0 + 0.3)
        parts.append(seg); t0 += d
        print(f"segment {n+1}/{len(secs)} done ({d:.1f}s)", flush=True)
    with open(f"{out}/captions_en.srt", "w") as f:
        for i, (a, b, c) in enumerate(srt, 1):
            f.write(f"{i}\n{ts(a)} --> {ts(b)}\n{c}\n\n")
    with open(f"{out}/list.txt", "w") as f:
        f.writelines(f"file '{os.path.abspath(p)}'\n" for p in parts)
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{out}/list.txt", "-c", "copy", f"{out}/joined.mp4"])
    style = "FontName=DejaVu Sans,FontSize=12,PrimaryColour=&H00FFFFFF,BackColour=&H99000000,BorderStyle=4,Outline=0,MarginV=14"
    run(["ffmpeg", "-v", "error", "-y", "-i", f"{out}/joined.mp4", "-vf", f"subtitles={out}/captions_en.srt:force_style='{style}'",
         "-af", "loudnorm=I=-14:TP=-1:LRA=11", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", f"{out}/final.mp4"])
    print("final:", f"{out}/final.mp4")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Visual check ("eyes") for video work. Makes labelled contact sheets that Claude can open
with the Read tool and look at, so every shot can be checked against its narration line.

  # One frame per subtitle cue (middle of the cue), labelled with time + subtitle text
  python3 tools/video/visual_check.py cues  RENDER.mp4 SUBS.srt   -o qa/cues
  # One frame every N seconds
  python3 tools/video/visual_check.py every RENDER.mp4 --step 2   -o qa/every
  # Start / middle / end frame of every clip in a folder (stock candidates)
  python3 tools/video/visual_check.py clips stock/clips/          -o qa/clips
  # Screenshot a web page (licence page, stock page, YouTube studio preview...)
  python3 tools/video/visual_check.py web https://example.com     -o qa/page.png

Sheets are written as OUT-01.png, OUT-02.png ... (12 tiles per page). Free and local:
FFmpeg, Pillow and the pre-installed Chromium only.
"""
import argparse
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
TILE_W, TILE_H, LABEL_H, COLS, PER_PAGE = 480, 270, 64, 3, 12


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=nw=1:nk=1", path], capture_output=True, text=True).stdout
    return float(out.strip() or 0)


def grab(path, t, dst):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{max(t, 0):.3f}", "-i", path,
                    "-frames:v", "1", "-vf", f"scale={TILE_W}:{TILE_H}:force_original_aspect_ratio=decrease,"
                    f"pad={TILE_W}:{TILE_H}:(ow-iw)/2:(oh-ih)/2", dst])
    return os.path.exists(dst)


def fmt(t):
    return f"{int(t // 60)}:{t % 60:05.2f}"


def wrap(draw, text, font, width):
    lines, line = [], ""
    for word in text.split():
        test = (line + " " + word).strip()
        if draw.textlength(test, font=font) <= width:
            line = test
        else:
            lines.append(line)
            line = word
    lines.append(line)
    return lines[:3]


def write_sheets(tiles, out):
    """tiles: list of (image_path, label)."""
    font = ImageFont.truetype(FONT, 15)
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    pages = []
    for p in range(0, len(tiles), PER_PAGE):
        chunk = tiles[p:p + PER_PAGE]
        rows = (len(chunk) + COLS - 1) // COLS
        sheet = Image.new("RGB", (COLS * TILE_W, rows * (TILE_H + LABEL_H)), "white")
        draw = ImageDraw.Draw(sheet)
        for i, (img, label) in enumerate(chunk):
            x, y = (i % COLS) * TILE_W, (i // COLS) * (TILE_H + LABEL_H)
            if img and os.path.exists(img):
                sheet.paste(Image.open(img), (x, y))
            for j, line in enumerate(wrap(draw, label, font, TILE_W - 10)):
                draw.text((x + 5, y + TILE_H + 3 + j * 19), line, fill="black", font=font)
        name = f"{out}-{p // PER_PAGE + 1:02d}.png"
        sheet.save(name)
        pages.append(name)
    print("\n".join(pages))


def parse_srt(path):
    cues = []
    for block in re.split(r"\n\s*\n", open(path, encoding="utf-8").read().strip()):
        m = re.search(r"(\d+):(\d+):(\d+)[,.](\d+)\s*-->\s*(\d+):(\d+):(\d+)[,.](\d+)", block)
        if not m:
            continue
        g = [int(x) for x in m.groups()]
        a = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000
        b = g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000
        text = " ".join(block[m.end():].strip().splitlines())
        cues.append((a, b, re.sub(r"<[^>]+>|\{[^}]+\}", "", text)))
    return cues


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("cues"); c.add_argument("video"); c.add_argument("srt")
    e = sub.add_parser("every"); e.add_argument("video"); e.add_argument("--step", type=float, default=2.0)
    k = sub.add_parser("clips"); k.add_argument("folder")
    w = sub.add_parser("web"); w.add_argument("url"); w.add_argument("--size", default="1366,900")
    for s in (c, e, k, w):
        s.add_argument("-o", "--out", required=True)
    a = ap.parse_args()

    if a.cmd == "web":
        chrome = shutil.which("chromium") or "/opt/pw-browsers/chromium"
        os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
        subprocess.run([chrome, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                        f"--window-size={a.size}", f"--screenshot={os.path.abspath(a.out)}", a.url], check=False)
        print(a.out if os.path.exists(a.out) else "screenshot failed (host blocked by the network policy?)")
        return

    tmp = tempfile.mkdtemp(prefix="vcheck-")
    tiles = []
    if a.cmd == "cues":
        for i, (s, t, text) in enumerate(parse_srt(a.srt)):
            f = os.path.join(tmp, f"{i:04d}.png")
            grab(a.video, (s + t) / 2, f)
            tiles.append((f, f"{fmt(s)}–{fmt(t)}  {text}"))
    elif a.cmd == "every":
        d, t, i = duration(a.video), 0.0, 0
        while t < d:
            f = os.path.join(tmp, f"{i:04d}.png")
            grab(a.video, t, f)
            tiles.append((f, fmt(t)))
            t, i = t + a.step, i + 1
    else:
        files = sorted(glob.glob(os.path.join(a.folder, "*.mp4")) + glob.glob(os.path.join(a.folder, "*.mov")))
        for n, clip in enumerate(files):
            d = duration(clip)
            for j, t in enumerate((0.3, d / 2, max(d - 0.5, 0))):
                f = os.path.join(tmp, f"{n:04d}-{j}.png")
                grab(clip, t, f)
                tiles.append((f, f"{os.path.basename(clip)}  @{fmt(t)}"))
    if not tiles:
        sys.exit("nothing to show")
    write_sheets(tiles, a.out)
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()

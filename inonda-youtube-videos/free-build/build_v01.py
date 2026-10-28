#!/usr/bin/env python3
"""Build Video 01 (bathroom renovation) for free: Pollinations.ai stills (no key, no credits)
+ slow camera moves in ffmpeg at 30 fps + the existing Emma narration.
Usage: python3 build_v01.py OUT_DIR   (re-runs reuse downloaded stills)."""
import os, subprocess, sys, urllib.parse, urllib.request, time

ROOT = os.path.dirname(os.path.abspath(__file__))
AUDIO = os.path.join(ROOT, "..", "audio", "Inonda_Video01_narration_Emma.mp3")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "out")
FPS, W, H = 30, 1920, 1080
STYLE = ("photorealistic phone photo, 35mm lens, natural daylight, real camera, realistic textures, "
         "older Cyprus apartment, no people, no faces, no text, no logos")

# (shot id, prompt, camera move) in narration order; FILM shots use stand-ins until real footage exists
SHOTS = [
 ("V01-01", "close-up of a cracked chipped beige 1990s ceramic wall tile beside a shower, grout stained dark", "in"),
 ("V01-02", "bathroom ceiling corner with brown damp stain, peeling paint and black mould spots", "up"),
 ("V01-03", "overhead view of an old shower tray with murky water around a corroded drain grate", "in"),
 ("V01-04", "renovated bathroom, large light-grey porcelain tiles, walk-in glass shower, floating vanity, warm LED mirror", "in"),
 ("V01-05", "doorway view into an old dated bathroom with beige tiles, worn fittings", "out"),
 ("V01-06", "street of white-rendered apartment blocks in Cyprus in morning sun, solar water heaters on flat roofs", "right"),
 ("V01-07", "moisture meter pressed against a stained bathroom wall", "in"),
 ("V01-08", "old galvanised pipes inside an opened bathroom wall cavity lit by a torch", "left"),
 ("V01-09", "hallway floor covered with protective sheeting, old wall tiles being removed, dust in the light", "in"),
 ("V01-10", "pressure test gauge attached to new PEX water supply pipes on a bathroom wall", "in"),
 ("V01-11", "grey waterproof membrane freshly rolled on a shower floor with reinforcing tape in the corner", "out"),
 ("V01-12", "notched trowel and tile adhesive on a wall, large tile placed, spirit level on top", "right"),
 ("V01-13", "smooth white silicone sealant bead along a shower corner", "in"),
 ("V01-14", "new chrome tap running clear water over a white basin", "in"),
 ("V01-15", "bright renovated bathroom seen from the doorway, light-grey tiles, glass shower", "left"),
 ("V01-16", "finished renovated bathroom with floating vanity and warm LED mirror, clean and bright", "out"),
]
VARIANTS = 2  # two stills per shot so no image stays on screen too long

def fetch(prompt, seed, path):
    if os.path.exists(path) and os.path.getsize(path) > 20000:
        return
    q = urllib.parse.quote(f"{prompt}, {STYLE}")
    url = f"https://image.pollinations.ai/prompt/{q}?width=1920&height=1080&nologo=true&seed={seed}"
    for attempt in range(4):  # free service, no cost to retry
        try:
            data = urllib.request.urlopen(url, timeout=180).read()
            if len(data) > 20000:
                open(path, "wb").write(data); return
        except Exception as e:
            print("retry", path, e)
        time.sleep(5 * (attempt + 1))
    raise SystemExit(f"could not fetch {path}")

def duration(path):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", path]).decode())

def clip(img, out, secs, move):
    n = int(secs * FPS)
    # crop away the service's bottom-right badge, keep 16:9, upscale, then a slow move
    zoom = {"in": f"1+0.12*on/{n}", "out": f"1.12-0.12*on/{n}"}.get(move, "1.10")
    x = {"left": f"(iw-iw/zoom)*(1-on/{n})", "right": f"(iw-iw/zoom)*on/{n}"}.get(move, "(iw-iw/zoom)/2")
    y = {"up": f"(ih-ih/zoom)*(1-on/{n})"}.get(move, "(ih-ih/zoom)/2")
    vf = (f"crop=iw*0.9375:ih*0.9375:0:0,scale=3840:2160:flags=lanczos,"
          f"zoompan=z='{zoom}':x='{x}':y='{y}':d={n}:s={W}x{H}:fps={FPS},"
          f"eq=saturation=0.92,noise=alls=4:allf=t,format=yuv420p")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", img, "-vf", vf,
                    "-frames:v", str(n), "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast",
                    "-crf", "20", out], check=True)

def card(text, out, secs):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i",
                    f"color=c=0x1d2a33:s={W}x{H}:r={FPS}:d={secs}", "-vf",
                    f"drawtext=text='{text}':fontcolor=white:fontsize=72:x=(w-tw)/2:y=(h-th)/2,"
                    f"fade=in:0:15,fade=out:st={secs-0.5}:d=0.5,format=yuv420p",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", out], check=True)

def main():
    os.makedirs(f"{OUT}/img", exist_ok=True); os.makedirs(f"{OUT}/clips", exist_ok=True)
    total = duration(AUDIO)
    end_card = 6.0
    per = (total + 1.0 - end_card) / (len(SHOTS) * VARIANTS)
    parts = []
    for i, (sid, prompt, move) in enumerate(SHOTS):
        for v in range(VARIANTS):
            img = f"{OUT}/img/{sid}_{v}.jpg"
            fetch(prompt, 100 + i * 10 + v, img)
            c = f"{OUT}/clips/{sid}_{v}.mp4"
            if not os.path.exists(c):
                clip(img, c, per, move if v == 0 else {"in": "out", "out": "in", "left": "right",
                                                        "right": "left", "up": "in"}[move])
            parts.append(c); print("ok", c, flush=True)
    endc = f"{OUT}/clips/end.mp4"
    card("Inonda  -  inonda.site  |  inonda.org  |  inonda.homes", endc, end_card)
    parts.append(endc)
    with open(f"{OUT}/list.txt", "w") as f:
        f.writelines(f"file '{p}'\n" for p in parts)
    final = f"{OUT}/Inonda_Video01_bathroom_renovation_30fps.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i",
                    f"{OUT}/list.txt", "-i", AUDIO, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "192k", "-af", "apad", "-shortest", "-movflags", "+faststart",
                    final], check=True)
    print("DONE", final, duration(final))

if __name__ == "__main__":
    main()

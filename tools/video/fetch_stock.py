#!/usr/bin/env python3
"""Fetch free stock video candidates for a shot list (meant to run in GitHub Actions,
where the network is open; the cloud session's network blocks the stock hosts).

Usage:
  python3 tools/video/fetch_stock.py inonda-youtube-videos/production/v01/stock/queries.json OUT_DIR

Sources, all free:
  - Pixabay  (needs PIXABAY_API_KEY, Pixabay Content License)
  - Pexels   (needs PEXELS_API_KEY,  Pexels License)
  - Mixkit   (no key, Mixkit Stock Video Free License)
  - Wikimedia Commons (no key, licence per file: CC0 / CC BY / CC BY-SA)

For each shot it downloads up to `per_shot` clips, trims to `max_seconds`, scales to
1920x1080 H.264, and writes a 4-frame contact sheet. OUT_DIR/manifest.json lists every
clip with its page URL, licence and author. Nothing here is paid.
"""
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (X11; Linux x86_64) Dope-video-crew/1.0 (+https://github.com/constapo/dope)"


def fetch(url, headers=None, raw=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
    except Exception as e:  # one bad source must not stop the run
        print(f"  ! {urllib.parse.urlparse(url).hostname}: {e}", file=sys.stderr)
        return None
    return data if raw else data.decode("utf-8", "replace")


def pixabay(q, n):
    key = os.environ.get("PIXABAY_API_KEY")
    if not key:
        return []
    t = fetch("https://pixabay.com/api/videos/?" + urllib.parse.urlencode(
        {"key": key, "q": q, "per_page": max(3, n), "safesearch": "true"}))
    out = []
    for r in (json.loads(t).get("hits", []) if t else []):
        v = r.get("videos", {})
        f = v.get("large") or v.get("medium") or {}
        if f.get("url"):
            out.append({"source": "pixabay", "page": r.get("pageURL"), "file": f["url"],
                        "licence": "Pixabay Content License", "author": r.get("user"), "tags": r.get("tags")})
    return out


def pexels(q, n):
    key = os.environ.get("PEXELS_API_KEY")
    if not key:
        return []
    t = fetch("https://api.pexels.com/videos/search?" + urllib.parse.urlencode({"query": q, "per_page": n}),
              {"Authorization": key})
    out = []
    for r in (json.loads(t).get("videos", []) if t else []):
        files = [f for f in r.get("video_files", []) if (f.get("width") or 0) <= 1920]
        best = max(files, key=lambda f: f.get("width") or 0, default=None)
        if best:
            out.append({"source": "pexels", "page": r.get("url"), "file": best["link"],
                        "licence": "Pexels License", "author": r.get("user", {}).get("name")})
    return out


def mixkit(q, n):
    slug = re.sub(r"[^a-z0-9]+", "-", q.lower()).strip("-")
    html = fetch(f"https://mixkit.co/free-stock-video/discover/{slug}/")
    if not html:
        return []
    out, seen = [], set()
    # Each result card links to /free-stock-video/<name>-<id>/ and previews assets.mixkit.co/videos/<id>/...
    for m in re.finditer(r'href="(/free-stock-video/[a-z0-9-]+-(\d+)/)"', html):
        page, vid = m.group(1), m.group(2)
        if vid in seen:
            continue
        seen.add(vid)
        # Only clips under the free licence may be used on the channel; "Restricted" clips are
        # personal-use only (their free file is the 720p one), so check the clip page first.
        page_html = fetch("https://mixkit.co" + page) or ""
        if "Restricted License" in page_html or "Free License" not in page_html:
            print(f"  - skip mixkit {vid}: not under the Mixkit free licence")
            continue
        out.append({"source": "mixkit", "page": "https://mixkit.co" + page,
                    "file": f"https://assets.mixkit.co/videos/{vid}/{vid}-1080.mp4",
                    "fallback": f"https://assets.mixkit.co/videos/{vid}/{vid}-720.mp4",
                    "licence": "Mixkit Stock Video Free License", "author": "Mixkit"})
        if len(out) >= n:
            break
    return out


def wikimedia(q, n):
    t = fetch("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query", "format": "json", "generator": "search", "gsrsearch": f"{q} filetype:video",
        "gsrnamespace": 6, "gsrlimit": n, "prop": "imageinfo", "iiprop": "url|extmetadata"}))
    out = []
    for p in ((json.loads(t).get("query", {}) or {}).get("pages", {}) if t else {}).values():
        ii = (p.get("imageinfo") or [{}])[0]
        md = ii.get("extmetadata", {})
        lic = md.get("LicenseShortName", {}).get("value", "")
        if ii.get("url") and re.search(r"CC0|CC BY|Public domain", lic, re.I):
            out.append({"source": "wikimedia", "page": ii.get("descriptionurl"), "file": ii["url"],
                        "licence": lic, "author": re.sub("<[^>]+>", "", md.get("Artist", {}).get("value", ""))})
    return out


def normalise(src, dst, max_s):
    vf = "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,format=yuv420p"
    r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-t", str(max_s), "-an",
                        "-vf", vf, "-c:v", "libx264", "-preset", "veryfast", "-crf", "23", dst])
    return r.returncode == 0 and os.path.getsize(dst) > 10000


def contact_sheet(clip, png):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", clip, "-vf",
                    "fps=1/4,scale=480:-2,tile=4x1", "-frames:v", "1", png])


def main():
    qfile, out_dir = sys.argv[1], sys.argv[2]
    cfg = json.load(open(qfile))
    n, max_s = cfg.get("per_shot", 4), cfg.get("max_seconds", 20)
    os.makedirs(out_dir, exist_ok=True)
    manifest, used = [], set()
    for shot in cfg["shots"]:
        sid = shot["id"]
        print(f"== {sid} {shot['line']}")
        cands = []
        for q in shot["queries"]:
            for fn in (pixabay, pexels, mixkit, wikimedia):
                cands += [dict(c, query=q) for c in fn(q, n)]
        got = 0
        for c in cands:
            if got >= n or c["page"] in used:
                continue
            raw = fetch(c["file"], raw=True) or (c.get("fallback") and fetch(c["fallback"], raw=True))
            if not raw or len(raw) < 50000:
                continue
            used.add(c["page"])
            got += 1
            name = f"{sid.replace('.', '_')}-{got}-{c['source']}"
            tmp = os.path.join(out_dir, name + ".src")
            open(tmp, "wb").write(raw)
            clip = os.path.join(out_dir, name + ".mp4")
            ok = normalise(tmp, clip, max_s)
            os.remove(tmp)
            if not ok:
                got -= 1
                continue
            contact_sheet(clip, os.path.join(out_dir, name + ".png"))
            manifest.append(dict(c, shot=sid, line=shot["line"], clip=name + ".mp4", sheet=name + ".png"))
            print(f"  + {name}  {c['page']}")
        if not got:
            print("  (no clip found)")
    json.dump(manifest, open(os.path.join(out_dir, "manifest.json"), "w"), indent=2, ensure_ascii=False)
    print(f"{len(manifest)} clips")


if __name__ == "__main__":
    main()

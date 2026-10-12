#!/usr/bin/env python3
"""Search free stock libraries for video/photo/audio and print licence info.

Usage:
  python3 tools/video/stock_search.py wikimedia "tile adhesive"   [--type video|image|audio] [-n 10]
  python3 tools/video/stock_search.py openverse "plastering wall"  [--type image|audio]
  python3 tools/video/stock_search.py pexels "bathroom renovation" [--type video|image]   # needs PEXELS_API_KEY
  python3 tools/video/stock_search.py pixabay "roof repair"        [--type video|image]   # needs PIXABAY_API_KEY

Add --json for machine-readable output. Searching is free; it downloads nothing.
Always re-check the licence on the result page before using a file.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

UA = "Dope-video-crew/1.0 (stock search; https://github.com/constapo/dope)"


def get(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"{urllib.parse.urlparse(url).hostname}: HTTP {e.code} {e.reason}")
    except urllib.error.URLError as e:
        sys.exit(f"cannot reach {urllib.parse.urlparse(url).hostname} ({e.reason}). "
                 "If this is a cloud session, add the host to Allowed domains in the environment's network settings.")


def wikimedia(q, kind, n):
    mime = {"video": "filetype:video", "image": "filetype:bitmap", "audio": "filetype:audio"}[kind]
    params = {
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": f"{q} {mime}", "gsrnamespace": 6, "gsrlimit": n,
        "prop": "imageinfo", "iiprop": "url|size|extmetadata|mime",
    }
    data = get("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params))
    out = []
    for p in (data.get("query", {}).get("pages", {}) or {}).values():
        ii = (p.get("imageinfo") or [{}])[0]
        md = ii.get("extmetadata", {})
        out.append({
            "title": p.get("title"), "page": ii.get("descriptionurl"), "file": ii.get("url"),
            "size": f'{ii.get("width")}x{ii.get("height")}', "mime": ii.get("mime"),
            "licence": md.get("LicenseShortName", {}).get("value"),
            "attribution": md.get("Artist", {}).get("value"),
        })
    return out


def openverse(q, kind, n):
    if kind == "video":
        sys.exit("openverse has images and audio only")
    data = get(f"https://api.openverse.org/v1/{kind}/?" + urllib.parse.urlencode({"q": q, "page_size": n}))
    return [{
        "title": r.get("title"), "page": r.get("foreign_landing_url"), "file": r.get("url"),
        "licence": f'{r.get("license")} {r.get("license_version") or ""}'.strip(),
        "attribution": r.get("attribution") or r.get("creator"), "source": r.get("source"),
    } for r in data.get("results", [])]


def pexels(q, kind, n):
    key = os.environ.get("PEXELS_API_KEY") or sys.exit("set PEXELS_API_KEY (free at pexels.com/api)")
    base = "https://api.pexels.com/videos/search?" if kind == "video" else "https://api.pexels.com/v1/search?"
    data = get(base + urllib.parse.urlencode({"query": q, "per_page": n}), {"Authorization": key})
    out = []
    for r in data.get("videos" if kind == "video" else "photos", []):
        if kind == "video":
            best = max(r.get("video_files", []), key=lambda f: (f.get("width") or 0), default={})
            out.append({"page": r.get("url"), "file": best.get("link"), "size": f'{best.get("width")}x{best.get("height")}',
                        "duration": r.get("duration"), "licence": "Pexels License", "attribution": r.get("user", {}).get("name")})
        else:
            out.append({"page": r.get("url"), "file": r.get("src", {}).get("original"), "size": f'{r.get("width")}x{r.get("height")}',
                        "licence": "Pexels License", "attribution": r.get("photographer")})
    return out


def pixabay(q, kind, n):
    key = os.environ.get("PIXABAY_API_KEY") or sys.exit("set PIXABAY_API_KEY (free at pixabay.com/api/docs)")
    base = "https://pixabay.com/api/videos/?" if kind == "video" else "https://pixabay.com/api/?"
    data = get(base + urllib.parse.urlencode({"key": key, "q": q, "per_page": max(3, n)}))
    out = []
    for r in data.get("hits", []):
        if kind == "video":
            v = r.get("videos", {}).get("large") or r.get("videos", {}).get("medium") or {}
            out.append({"page": r.get("pageURL"), "file": v.get("url"), "size": f'{v.get("width")}x{v.get("height")}',
                        "duration": r.get("duration"), "licence": "Pixabay Content License", "attribution": r.get("user")})
        else:
            out.append({"page": r.get("pageURL"), "file": r.get("largeImageURL"), "size": f'{r.get("imageWidth")}x{r.get("imageHeight")}',
                        "licence": "Pixabay Content License", "attribution": r.get("user")})
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", choices=["wikimedia", "openverse", "pexels", "pixabay"])
    ap.add_argument("query")
    ap.add_argument("--type", default=None, choices=["video", "image", "audio"])
    ap.add_argument("-n", type=int, default=10)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    kind = a.type or ("image" if a.source == "openverse" else "video")
    results = {"wikimedia": wikimedia, "openverse": openverse, "pexels": pexels, "pixabay": pixabay}[a.source](a.query, kind, a.n)
    if a.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return
    if not results:
        print("no results")
    for i, r in enumerate(results, 1):
        print(f"{i}. {r.get('title') or r.get('page')}")
        for k in ("page", "file", "size", "duration", "licence", "attribution"):
            if r.get(k):
                print(f"   {k}: {str(r[k])[:160]}")


if __name__ == "__main__":
    main()

# Free stock VIDEO sources for Inonda renovation videos

Researched 2026-10-15 by the research worker. Scope: real camera footage (no AI clips, no
animation) of renovation hand-work for a **monetised** YouTube channel, free only (no
purchase, no paid plan), no watermark, scriptable from a GitHub Actions runner.

**How this was checked:** the cloud session's network blocks every stock host (direct fetch
and curl both failed), so each licence was read through web search of the site's **own**
licence/help pages (pexels.com/license, help.pexels.com, pixabay.com/service/license,
pixabay.com/api/docs, mixkit.co/license + clip pages, coverr.co/license, api.coverr.co/docs,
help.videvo.net, vecteezy.com/licensing-agreement + /developers, support.videezy.com,
freenaturestock.com/license, dareful.com/about, isorepublic.com, splitshire.com,
api.dvidshub.net/docs, dvidshub.net/about/copyright, nasa.gov media guidelines). Where only
third-party summaries existed, the entry says "unverified". **Re-open the licence page from the
runner (or a browser) before the first real download, and save a copy/screenshot in the
project's `assets/stock/SOURCES.md` notes.**

Needed shots: cracked tiles, damp/mould ceiling, shower drain, tile removal/demolition,
plumbing pipes, pressure gauge, electrician wiring, waterproofing membrane/roller, tiling with
notched trowel and spacers, grouting with float, silicone gun, toilet/basin/tap install,
finished modern bathroom, Mediterranean apartment buildings.

---

## 1. Ranked table (top 6 for our needs)

| # | Source | Licence (commercial YouTube?) | Attribution | Watermark on free file | Renovation footage | Script access from GitHub Actions |
|---|---|---|---|---|---|---|
| 1 | **Pixabay** – pixabay.com/videos | Pixabay Content License: yes, commercial OK; no standalone resale/redistribution; no use of visible brands for goods/services; no misleading use of recognisable people | Not required | No | Medium: "bathroom remodeling" ~55, "plumbing" ~19, "plumber" ~2, lots of tiles/bathrooms; hand-work close-ups exist but thin per trade | **Public API, free key** (free account) → `PIXABAY_API_KEY`. 100 req / 60 s per key, cache results 24 h, "no systematic mass downloads", max 500 hits/query. Video files are direct MP4 links (may be embedded/downloaded). Already wired in `fetch_stock.py` |
| 2 | **Pexels** – pexels.com/videos | Pexels License: yes, commercial OK; no selling unaltered copies, no re-upload to stock/wallpaper sites; identifiable people not in a bad light (e.g. "suffering a medical ailment"), no implied endorsement; ToS says people/brands/buildings may need consent for commercial use | Not required (appreciated) | No | **Largest**: thousands of tile/wall-tile/bathroom/plumbing/construction clips, many 4K, good hands-only shots | **Public API, free key** → `PEXELS_API_KEY`. 200 req/h, 20 000/month, cache 24 h. **Warning: help.pexels.com (updated 2026-10-14) says new API key issuance is currently paused** (contact api@pexels.com). If the owner cannot get a key, Pexels is manual-download only. Already wired |
| 3 | **Mixkit** (Envato) – mixkit.co | Two licences per clip: **Mixkit Stock Video Free License** = commercial OK incl. YouTube; **Mixkit Restricted License** = personal projects only (free 720p file, 1080p sold via Envato). No resale/redistribution as stock | Not required | No | Small: ~264 "construction" clips, mostly sites/cranes/blueprints; little bathroom hand-work | **No key.** HTML pages + predictable files `https://assets.mixkit.co/videos/<id>/<id>-1080.mp4` (also `-720.mp4`). **Must read each clip page and reject "Restricted License"** (see §4 bug note) |
| 4 | **Coverr** – coverr.co | Coverr licence: free, commercial OK, monetised YouTube OK; no standalone resale; **no use for AI training**; trademarks in shot may need owner permission | Not required (API apps must show the source – credit "Coverr" in description) | No | Small–medium: "home renovation", "remodeling", "home repair", "building site", "hardwood floor" collections. **Mixed with labelled AI-generated clips – reject those** | **Public API, free key** (account + "add app" at coverr.co/developers) → `COVERR_API_KEY`. Demo app: 50 req/h (Production needs paid plan – not needed). `GET https://api.coverr.co/videos?query=…&urls=true`, key as `Authorization: Bearer` or `api_key=`. Pages also show **iStock** (paid) panels – ignore |
| 5 | **Wikimedia Commons** – commons.wikimedia.org | Per file: CC0 / public domain / CC BY / CC BY-SA (all commercial OK). Reject anything NC/ND or "fair use" | **Required** for CC BY / BY-SA (author + licence + link); BY-SA: our edit is arguably an adaptation → keep credits in description | No | Small: Category:Videos of construction (21 subcats, 37 files), Videos of construction workers (12), Videos of building construction (10), Videos of masonry (4), Videos of building demolition; no plumbing/tiling video categories found. Good for **Cyprus/Mediterranean building exteriors** (search "Limassol", "Larnaca", "Nicosia" + filetype:video) | **Keyless MediaWiki API**, direct `upload.wikimedia.org` file URLs (WebM/OGV, transcode with FFmpeg). Already wired (search); add category crawl (§4) |
| 6 | **Vecteezy / Videezy** – vecteezy.com/free-videos, videezy.com | **Free License**: personal and "some commercial" use **with attribution**; video productions with budgets up to US$1 000 (a no-budget YouTube video fits, but read the clause). YouTube allowed unless the clip is **Editorial Use Only**. Pro clips need paid plan | **Required**: "Free Stock Footage by Vecteezy.com" (or "Videezy.com") in the YouTube description | Free-licence files: no watermark reported; **Pro clips show watermarked previews** – skip them | Medium: civilian construction/renovation clips exist; free/Pro mixed in results | **API with Free plan: 500 downloads/month**, needs account + key (`VECTEEZY_API_KEY`), endpoint details at vecteezy.com/developers (not verified here). Otherwise manual download |

Runner-up (7): **DVIDS** (US DoD, public domain) – real US Navy Seabee footage of electrical,
plumbing, framing and finish work; free API key; but military uniforms/insignia, identifiable
service members and "no implied endorsement" rules make it a last resort for hands-only
close-ups.

### Genuinely free vs fake-free at a glance

| Genuinely free, no watermark | Attribution | Fake-free / not usable for us |
|---|---|---|
| Pixabay, Pexels, Mixkit (Free-License clips only), Coverr (real clips only), ISO Republic, Free Nature Stock | none | **Dreamstime** (paid, watermarked previews), **Videezy/Vecteezy Pro** (paid credits, watermarked previews), **Videvo Premium** (paid plan), **Mixkit Restricted** clips (personal use only), **Kaboompics video** (paid shop: once-only commercial use), **iStock/Getty/Shutterstock panels** shown inside Pexels/Pixabay/Coverr pages (paid, watermarked), **Storyblocks / Envato Elements / Artgrid** (subscriptions) |
| Wikimedia Commons (CC0/PD) | none | **SplitShire videos** – now mostly AI-generated (Kling/Veo) and "free to use with a link" → reject (realism rule) |
| Wikimedia Commons (CC BY/BY-SA), Dareful (CC BY 4.0), Videvo free clips (Videvo Attribution / CC BY 3.0), Vecteezy/Videezy Free, Freepik/Magnific free videos | simple credit line | **EU Audiovisual Service** – free only for EU information/education; commercial use unclear → reject |
| Adobe Stock **Free collection** (commercial licence, model-released, needs free Adobe ID, manual only) | none stated | Openverse – **no video at all** (images + audio only) |
| DVIDS, NASA (US government public domain) | credit unit/agency; no endorsement | Life of Vids – reported offline in 2026 (one source), redistribution capped at 10 clips/site |

---

## 2. Per-source notes

### Pixabay (rank 1)
- Licence: pixabay.com/service/license – free, no attribution, modify OK. Prohibited: selling or
  distributing the clip "Standalone" (unchanged, or only filtered/cropped/resized); using
  recognisable brands for goods/services; immoral/misleading use of recognisable people.
  An edited explainer with narration, captions and other clips is not Standalone use.
- No watermark on downloads. The website shows **sponsored iStock results** (paid) above the
  free ones; the API returns only Pixabay content.
- API: pixabay.com/api/docs – `https://pixabay.com/api/videos/?key=…&q=…&video_type=film&min_width=1280&per_page=…`.
  Rate limit 100/60 s, results must be cached 24 h, no mass downloading, ≤500 hits/query.
  Free key from a free account (owner signs up; we did not).
- Music on Pixabay can trigger Content ID; not relevant for silent B-roll.
- Good queries: `tiling`, `tiler`, `tile adhesive`, `grout`, `bathroom remodeling`, `plumbing`,
  `pipe wrench`, `electrician`, `wiring`, `silicone`, `caulking`, `mold`, `damp wall`,
  `demolition hammer`, `Cyprus apartment`, `Limassol`.

### Pexels (rank 2)
- Licence: pexels.com/license + Terms. Free, commercial, no attribution. Not allowed: selling
  unaltered copies, re-uploading to stock/wallpaper platforms, showing identifiable people in
  a bad light or with a medical ailment, political use, implying endorsement, using content as
  a trademark. Terms warn that identifiable people, logos and buildings may need consent for
  commercial use → **prefer hands-only shots; reject visible faces and brand logos.**
- API: 200 req/h, 20 000/month, free. **Key issuance paused** per help.pexels.com
  ("How do I get an API key?", updated 2026-10-14). Existing keys keep working. If no key:
  owner downloads manually from the site, and we log page URL + author.
- Library is the deepest for our list (tile, wall tile, bathroom, plumbing, construction, many 4K).

### Mixkit (rank 3)
- mixkit.co/license: Free License clips → commercial projects incl. YouTube, no attribution,
  no watermark. Restricted License clips → personal social posts only; their free file is
  720p and the 1080p is sold through Envato. Terms: no resale/redistribution as stock.
- Not every clip on a search page is Free-License. Check the clip page text.
- No API. Search page `https://mixkit.co/free-stock-video/discover/<slug>/` and category pages
  `https://mixkit.co/free-stock-video/construction/`; files at
  `https://assets.mixkit.co/videos/<id>/<id>-1080.mp4`.
- Content: construction sites, crane, blueprint, concrete; very little bathroom hand-work.

### Coverr (rank 4)
- coverr.co/license: irrevocable, worldwide, free, commercial; no attribution for free
  downloads; no training AI with the content; no competing service; brand owners' permission
  may be needed for trademarks in shot; no reselling raw clips. No watermark on free videos.
- **Library mixes human-shot and AI-generated clips (labelled).** Our realism rule: reject AI
  clips (and an AI clip would also need the "AI-generated" label). Filter on the label/tag in
  the API result and check by eye.
- API docs: api.coverr.co/docs (auth, videos, schema). Free account → create app → Demo key,
  50 req/h. `urls=true` adds file URLs (token tied to the key, no expiry). Coverr also offers an
  MCP server (`https://mcp.coverr.co/mcp`, header `x-coverr-api-key`).
- Content: home renovation, remodeling, home repair, building site, carpentry, hardwood floor.

### Wikimedia Commons (rank 5)
- Licence per file in `extmetadata.LicenseShortName`. Accept CC0, PD, CC BY, CC BY-SA. Reject
  NC/ND/fair use. Credit = author + licence + link in the YouTube description.
- Useful categories: `Category:Videos_of_construction`, `Category:Videos_of_construction_workers`,
  `Category:Videos_of_building_construction`, `Category:Videos_of_masonry`,
  `Category:Videos_of_building_demolition`, `Category:Videos_of_tools`,
  `Category:National_Institute_for_Occupational_Safety_and_Health_videos` (US gov, PD, safety
  films – people visible). Cyprus city categories for exteriors.
- Small volume; quality varies (phone video, WebM). Keyless and reliable.

### Vecteezy / Videezy (rank 6)
- Same company. Free License = attribution required ("Vecteezy" / "Videezy.com"), commercial
  use "with limitations", video/film productions with budgets ≤ US$1 000. Editorial-only clips
  cannot be used commercially. Pro clips: paid (Videezy credits ~US$19 each) and previews are
  watermarked – never use them.
- API: vecteezy.com/developers lists a **Free plan, 500 downloads/month**, key needed (account).
  Paid Pay-As-You-Go ($1/download) must never be enabled.
- Risk: free and Pro clips are mixed; script must keep only items flagged free + non-editorial.

### Videvo (not ranked)
- Owned by Freepik (now Magnific). Free clips under **Videvo Attribution License** (credit
  "<author> / www.videvo.net", no redistribution of originals) or **CC BY 3.0**. Check the
  "Usage" line: "Editorial Use Only" (red) = not for commercial use. Premium clips need a paid
  plan. No public API found → manual only. Use only if Pixabay/Pexels lack a shot.

### Freepik / Magnific videos (not ranked)
- Free videos: commercial OK, YouTube OK, **attribution always required** for free users
  ("Designed by Freepik"/author, in description or credits). Many premium clips mixed in.
  Manual download (API not checked for free video use).

### Adobe Stock – Free collection (manual only)
- Adobe help: free-collection assets (incl. videos) come with a commercial licence and meet the
  same model/property-release standards as paid assets. Needs a free Adobe ID; no API for us.
  Good fallback for a single missing shot, downloaded by the owner by hand.

### ISO Republic
- isorepublic.com: CC0, no attribution, ~130+ videos (some re-posted from Videezy/Vimeo CC0).
  Little renovation content. No API; manual.

### Free Nature Stock
- freenaturestock.com/license: CC0, commercial, no attribution, all real (not AI). Nature only –
  not useful for renovation. Manual.

### Dareful
- dareful.com: CC BY 4.0 (credit Dareful / Joel Holland), 4K, account needed; nature, aerial,
  time-lapse only. Not useful.

### Mazwai
- Now "by Videvo"; ~70 artistic clips under CC BY 3.0 or Mazwai License. No renovation. Skip.

### SplitShire
- Video pages now mostly AI-generated (labelled Kling, Veo 3.1) with "Free to use with a link
  to splitshire.com". Reject: AI footage, not real camera footage.

### Life of Vids
- "No copyright restrictions" but ≤10 videos redistributed per site; © 2018 footer; one 2026
  round-up says it went offline. No renovation. Skip.

### Vidsplay
- ~500 clips (nature/backgrounds); licence descriptions conflict (no-attribution vs credit link
  vs CC BY 3.0). Unverified – skip.

### Kaboompics
- Free licence covers **photos**. Video clips are sold in the Kaboompics Shop (paid; licence =
  one commercial project). Fake-free for video.

### Openverse
- Searches images and audio only; no video endpoint. Not usable for footage.

### Internet Archive
- Keyless `https://archive.org/advancedsearch.php?q=mediatype:movies AND licenseurl:*creativecommons*&output=json`,
  files at `https://archive.org/download/<id>/<file>`. Licence metadata is per item and often
  missing/wrong; the Archive grants no rights. Prelinger films (~60–65 % PD) are 1903–1990
  ephemeral films – wrong era and look for a modern bathroom. Not recommended.

### NASA
- Mostly not copyrighted; credit NASA; no logo use; no implied endorsement; identifiable people
  may have publicity rights. API `https://images-api.nasa.gov/search?q=…&media_type=video`
  (keyless). No renovation content – irrelevant.

### DVIDS (US Department of Defense) – runner-up
- dvidshub.net/about/copyright: public domain unless marked; credit the unit; commercial users
  should remove distinctive military markings and add a non-endorsement disclaimer.
- API `https://api.dvidshub.net/search?type=video&q=…&api_key=…` – free key via signup;
  **key is tied to the origin it was issued for**, so test that it works from a GitHub runner.
- Content: Seabee builders/electricians/utilitiesmen doing real wiring, plumbing, framing,
  concrete, tiling (photos confirmed; videos fewer). Uniforms and bases → hands-only crops only.

### EU Audiovisual Service, Pond5 Public Domain Project
- EU AV: free for EU-related information/education; commercial terms unclear → reject.
- Pond5 PD project (pond5.com/free): historic National Archives footage; wrong era. Skip.

---

## 3. Rejection rules for every candidate (apply in the script and by eye)

1. Licence must be one of: Pixabay Content License, Pexels License, Mixkit Stock Video Free
   License, Coverr License, CC0/PD, CC BY, CC BY-SA, Vecteezy Free (non-editorial).
   Reject: Mixkit Restricted, Editorial Use Only, any NC/ND, unknown.
2. Reject AI-generated clips (Coverr/SplitShire labels) – realism rule.
3. Reject visible faces of private people (no model release we can show), brand logos on
   tools/products, watermarks or burnt-in text.
4. Shot must match the narration line exactly (CLAUDE.md rule 1).
5. Record per file: source, page URL, file URL, licence name + licence URL, author,
   attribution text, resolution, duration, date checked → `assets/stock/SOURCES.md`.
6. Attribution-required clips: add the credit lines to the YouTube description.

---

## 4. How to add these to `tools/video/fetch_stock.py`

**Bug to fix first (Mixkit):** `mixkit()` takes every card from the search page and downloads
`-1080.mp4`, falling back to `-720.mp4`. Restricted-License clips have a free 720p file for
**personal use only**, so the fallback can silently fetch a clip we may not use. Fix: fetch the
clip page and keep it only if it says "Mixkit Stock Video Free License" and does not say
"Restricted License"; drop the 720p fallback for clips that fail that check.

```python
def mixkit_licence_ok(page_url):
    html = fetch(page_url) or ""
    return "Stock Video Free License" in html and "Restricted License" not in html
```

**Pixabay:** add `"video_type": "film", "min_width": 1280` to the query; cache responses for 24 h
(e.g. `actions/cache` on a `cache/pixabay/*.json` folder) to respect the API rules.

**Pexels:** unchanged; keep `best["link"]`, add `"licence_url": "https://www.pexels.com/license/"`
and the author name for the manifest. Works only if the owner already has a key (issuance paused).

**Coverr (new, needs `COVERR_API_KEY` secret):**
```python
def coverr(q, n):
    key = os.environ.get("COVERR_API_KEY")
    if not key:
        return []
    t = fetch("https://api.coverr.co/videos?" + urllib.parse.urlencode(
        {"query": q, "page_size": n, "urls": "true"}), {"Authorization": f"Bearer {key}"})
    out = []
    for r in (json.loads(t).get("hits", []) if t else []):   # field names: verify at api.coverr.co/docs/schema
        if r.get("is_ai") or "ai" in [x.lower() for x in r.get("tags", [])]:
            continue                                            # realism rule: no AI clips
        u = (r.get("urls") or {}).get("mp4_download") or (r.get("urls") or {}).get("mp4")
        if u:
            out.append({"source": "coverr", "page": f"https://coverr.co/videos/{r.get('slug', r.get('id'))}",
                        "file": u, "licence": "Coverr License", "author": "Coverr"})
    return out
```
The response field names (`hits`, `urls.mp4_download`, AI flag) were **not verified** because
the docs could not be opened from this session – read api.coverr.co/docs/videos and /schema on
the runner and adjust. Demo key = 50 req/h, so cap queries per run (e.g. ≤40).

**Wikimedia Commons:** add a category crawl next to the search:
`action=query&generator=categorymembers&gcmtitle=Category:Videos_of_construction_workers&gcmtype=file&prop=imageinfo&iiprop=url|extmetadata`
and keep the existing licence regex (CC0 | CC BY | Public domain); store the `Artist` and
`LicenseShortName` for the credit line.

**Vecteezy (optional, needs `VECTEEZY_API_KEY`, Free plan only):** read vecteezy.com/developers
for the search/download endpoints; keep only items whose licence is Free and not Editorial;
store the credit "Free Stock Footage by Vecteezy.com"; hard-stop at 500 downloads/month and
never enable Pay-As-You-Go.

**DVIDS (optional, `DVIDS_API_KEY`):** `GET https://api.dvidshub.net/search?type=video&q=<q>&api_key=<key>`,
then the Asset API for the file URL; licence "Public domain (US DoD)", credit the unit; manual
check for insignia/faces before use.

Register the new functions in the source loop:
`for fn in (pixabay, pexels, coverr, mixkit, wikimedia):`
and add the new secrets (`COVERR_API_KEY`, optional `VECTEEZY_API_KEY`, `DVIDS_API_KEY`) to the
GitHub Actions workflow `env:` block. All keys are free; the owner must create the accounts.

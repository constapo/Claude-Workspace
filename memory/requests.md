# Owner's requests – permanent log

Every request the owner makes, from any device or session, is appended here (newest at the
bottom) and committed, so every future session on this repo sees it. Standing rules are
also copied into `/CLAUDE.md`.

Format: date · what was asked · what was done / status.

## 2026-10-11

1. **Find Higgsfield, make it an agent, use its skills.** → No Higgsfield plugin/connector
   exists. Built `higgsfield` agent (`.claude/agents/higgsfield.md`) + `tools/higgsfield/hf.py`
   (official SDK, Agent API). *Blocked:* needs `HF_KEY` secret and `api.higgsfield.ai`
   allowed in the network policy.
2. **Option 2: make it generate videos.** → Done as above; untested against the live API.
3. **Make a video for Inonda scene 1.** → Not generated (no Higgsfield key). Wrote briefs:
   `inonda-youtube-videos/higgsfield/v01-scene1.sh` (4 shots, one shot per run).
4. **Connect to "artist.io", bring its AI in as an agent, clone its skills.** → artist.io
   does not exist; it is **Artlist** (artlist.io). Built `artlist` agent using the official
   Artlist MCP connector (`https://mcp.artlist.io/mcp`). Artlist has no skill files to clone.
   *Blocked:* owner must add the connector in claude.ai → Settings → Connectors.
5. **Use the artlist agent to make video 1 scene 1.** → Not generated: connector not connected.
6. **Turn the 20 Inonda scripts into AI-generated videos.** → Not generated. ElevenLabs
   (connected) refuses video on the current plan. Options given: Artlist, Higgsfield, paid
   ElevenLabs, or stills + narration.
7. **"I don't want to see wasted credits on junk videos… never again."** → Standing rule in
   `/CLAUDE.md`: plan free first, price first, explicit approval per batch, one test clip
   first, no blind retries, never open/auto-play results on the owner's computer.
8. **Write the shot list for all 20 videos.** → Done: `inonda-youtube-videos/shot-list.md`
   (189 AI clips, 72 to film for real, 39 graphics). Videos 17, 19, 20 must be filmed.
9. **Make sure generated videos look like realistic scenes.** → Standing rule: Realism
   standard in `shot-list.md` (one action per clip, most photoreal model, realism guard,
   reject list), wired into `/CLAUDE.md` and both agents.
10. **Keep in memory absolutely all my requests from both devices.** → This file, plus a
    `/CLAUDE.md` rule that every session reads it first and appends each new request.

11. **"I connected Artlist, make test clip V01-01."** → Not generated, no credits spent.
    Artlist tools were not visible in that session (connectors added mid-session only load
    in a new session). Next: in a new session, price V01-01 and ask for approval first.

12. **"Make test clip V01-01 with artlist" (repeated in the same session).** → Not generated,
    no credits spent: Artlist tools still not loaded in that session. Other paid video
    tools seen there (vidIQ, Krea) were NOT used – they need the owner's explicit choice.

13. **"Use vidIQ for V01-01, show me the price."** → Not generated. vidIQ balance 80 credits
    (refills to 150 on 2026-11-06). vidIQ gives no free estimate; cost = seconds × model rate
    × 20, rates unpublished, so a realistic 4s clip likely exceeds 80. Prompt shown; waiting
    for the owner to choose: try vidIQ anyway / wait for Artlist (recommended) / top up.

14. **"Seek as many skills as possible from the internet for future video making and
    generating."** → Researched ~30 open-source video skills (Remotion official, ECC
    video-editing/remotion/manim, erichowens FFmpeg + AI-production + voice, BenAI
    repurposing/YouTube chain, RunComfy model router, Tella). Third-party files were NOT
    copied in (unreviewed scripts would auto-load every session); instead wrote 8 original
    skills distilled from them in `.claude/skills/video-*` (production router + catalog,
    ai-generation, ffmpeg-editing, captions-transcription, remotion, repurposing-shorts,
    voiceover-music, youtube-packaging). All FFmpeg recipes tested locally. Install
    commands for the external skills are in `.claude/skills/video-production/CATALOG.md`
    – installing any of them is the owner's choice. No credits spent.

15. **"Use all sources available online as workers and co-workers in making videos, and
    harness as many skills as needed."** → Built a video crew of 8 subagents in
    `.claude/agents/video-*.md` (researcher, scriptwriter, shot-planner, editor, sound,
    captioner, packager, QA reviewer). None of them can spend credits; paid generation
    stays with the owner-approved `higgsfield`/`artlist` agents. Added
    `video-production/CREW.md` (director playbook), `video-production/SOURCES.md` (free
    footage/music/SFX/fonts, open-source tools, open models, paid co-workers, plugin
    skills) and `tools/video/stock_search.py` (Wikimedia, Openverse, Pexels, Pixabay).
    *Blocked:* this environment's network policy denies the stock hosts (wikimedia,
    openverse, pexels, pixabay…). The owner must add them under Allowed domains. Pexels and
    Pixabay also need free API keys. No credits spent.

16. **"I don't allow the 'never fake real people or jobs' rule. European privacy law means we
    should use fake people and even fake jobs for presentation and marketing."** → Rule
    replaced everywhere (CLAUDE.md rule 8, all video-* agents, video skills, shot-list.md):
    AI actors and fictional example jobs are now allowed. Kept three conditions: no likeness
    of a real person, an "AI-generated" label plus YouTube disclosure (EU AI Act transparency),
    and never present an AI scene as a real job, client, testimonial or result (EU
    unfair-commercial-practices rules). Existing FILM rows in shot-list.md were not re-tagged
    one by one.

17. **"Anything generated must look like a real person even if fake; filming real people
    needs their consent; generated jobs must look realistic and match the description over
    them."** → Added to CLAUDE.md rule 8, all video-* agents, video-ai-generation skill and
    shot-list.md: photoreal fictional AI people (reject anything doll-like/CGI/uncanny),
    signed consent for any real person filmed (kept in `<project>/consent/`, else blur),
    and every AI job shot must match its narration line. QA reviewer checks all three.

18. **"Re-tag the videos I'm still waiting for (3 days)."** → Re-tagged `shot-list.md` under the
    AI-actors rule: 43 FILM shots → AI (one fictional AI presenter for all videos, example
    finished rooms labelled "Illustration – example"). Now 232 AI / 29 FILM / 39 GFX. Still
    FILM: real case studies 17, 19, 20, real past-work montages, own reviews page, and shots
    the scripts require genuine (V08-03, V09-06, V18-13). Nothing generated yet, no credits
    spent – next step is still pricing + approval of test clip V01-01.

19. **"My face can be used in the videos."** → Recorded as the owner's consent (2026-10-12) in
    CLAUDE.md rule 8, all video-* agents and shot-list.md: the presenter in videos 01–16 and
    18 is the owner, filmed for real or as an AI likeness built from the owner's own photos.
    Waiting on the owner: choose film vs AI likeness, and (for AI) provide reference photos/video.

20. **"AI version of me. I will add pictures."** → Owner chose an AI likeness as presenter.
    Created `inonda-youtube-videos/presenter/` (README with photo/video checklist; images are
    git-ignored for privacy). Waiting on the owner's photos and a 30–60 s talking video.

21. **Owner sent 5 photos for the AI likeness ("can show me working in videos").** → Saved in
    `inonda-youtube-videos/presenter/` (git-ignored, lost when the container resets – owner keeps
    originals). Free check: 4 webcam shots (front, both ¾ sides) are usable for a first test but
    low-res (959×512), backlit by the window; the beach photo is rotated, with sunglasses and an
    older hairstyle, so it is excluded to keep the face consistent. Next: price one test still
    of the owner in workwear on a job site, then one test video clip. Nothing generated, no
    credits spent.

22. **"Keep going on making the 20 videos." / "I don't want to pay any agents or co-workers."**
    → New standing rule (CLAUDE.md): free tools only. Cancelled the $0.12 ElevenLabs test-image
    proposal; nothing was generated or charged. Checked this container: no GPU (4 CPU, 15 GB),
    so free local AI video and an AI likeness of the owner are not possible here; Hugging Face
    (free voice models) and the stock hosts are blocked by the network policy. Free route:
    owner films/records on phone, free stock (needs Allowed domains), FFmpeg/Remotion graphics.

23. **"Find sources online, do what you wish – I don't care how the AI me looks. I want results
    as generated videos."** → Built a free pipeline and rendered the first real video:
    `inonda-youtube-videos/production/v01/build/render/final.mp4` (6:04, 1080p, −14.6 LUFS, EN
    burned captions + `captions_en.srt`). Free voice: Kokoro TTS (open model from GitHub,
    male voice "am_michael", labelled "AI voice"). Picture: owner photo (cropped) + section
    titles. Builder: `tools/video/build_explainer.py`. Price/duration sentence left out and
    WhatsApp line points to the description until the owner fills the placeholders. Media is
    git-ignored (container is temporary). Crew also wrote `production/v01/shot-plan.md` and
    `narration.md` (EN + GR). Next free steps: talking-head animation of the owner photo
    (SadTalker, CPU), Greek version, videos 02–20.

24. **"Talking about bathroom, must show bathroom, not my face" / "what the heck is this junk" /
    "the job talked about must be shown, subtitles in Greek all the time, bathroom must look
    realistic not drawn, stop all junk now."** → Stopped. The photo-slideshow render and the
    flat animated drawings were rejected as junk; nothing more rendered. New standing rules in
    CLAUDE.md: picture shows the exact job narrated, realistic footage only (no drawings or
    photo slideshows), Greek subtitles always, sample before long renders. Realistic free
    footage needs the stock sites allowed in the network settings (still blocked).

25. **"Restart from zero on making videos."** → Fresh plan under the current rules (free only,
    realistic footage showing the narrated job, Greek subtitles always, sample first). Checked
    again: Pexels, Pixabay, Wikimedia and archive.org are still blocked in this environment, so
    no realistic footage can be fetched yet. Waiting on the owner to allow those domains and
    open a new session.

26. **"Make them one by one – I must see each before you do the next."** → Standing rule 5 in
    CLAUDE.md video content rules: one video at a time, owner sees it, then the next.

27. **"Use https://pixabay.com/users/constapo-58008077/ to get access to inspirational
    materials."** → Owner has a free Pixabay account. Tried it: pixabay.com and cdn.pixabay.com
    are still blocked here (curl and web fetch both fail). Needs: owner's free Pixabay API key
    (pixabay.com/api/docs while logged in) saved as secret `PIXABAY_API_KEY`, plus
    `pixabay.com` and `cdn.pixabay.com` in Allowed domains, then a new session.
    `tools/video/stock_search.py pixabay` already uses that key.

28. **Owner shared the Pixabay API key in chat.** → Not written to the repo. Kept only in this
    session's scratchpad. Search test still fails: pixabay.com blocked by the network policy.
    Owner should save it as the `PIXABAY_API_KEY` environment secret (so new sessions have it)
    and allow pixabay.com + cdn.pixabay.com, then start a new session.

29. **"Make Inonda video 01 (bathroom renovation, old to new) from Pixabay footage; pixabay.com +
    cdn.pixabay.com allowed and PIXABAY_API_KEY added."** → Stopped at step 1 (access check), nothing
    built. In this session (2026-10-12) `stock_search.py pixabay` failed: `PIXABAY_API_KEY` is not
    in the environment, and the network proxy still answers 403 to pixabay.com and cdn.pixabay.com
    (policy denial). The settings change has not reached this container. Next: owner checks the
    environment settings (Allowed domains: `pixabay.com`, `cdn.pixabay.com`; environment variable
    `PIXABAY_API_KEY`), saves, and starts a NEW session; then rerun the same request.

30. **Same request again (video 01 from Pixabay, "now allowed + key set").** → Re-checked in a new
    session (2026-10-12): still blocked at step 1, nothing built. `echo ${PIXABAY_API_KEY:+key-set}`
    prints nothing (no Pixabay variable of any name in the container), and the proxy still
    answers `CONNECT 403` for both pixabay.com and cdn.pixabay.com. So the saved settings are
    not reaching new sessions. Owner should open the environment this session runs in (cloud
    environment menu in the title bar → Edit) and confirm the change is saved on THAT environment:
    Network access → Allowed domains has `pixabay.com` and `cdn.pixabay.com` (keep "Allow package
    managers" ticked), and Environment variables has `PIXABAY_API_KEY=<key>`. Then start a new
    session on that environment.

## Open items waiting on the owner
- Artlist connected by the owner (2026-10-11) – start a NEW session so its tools load, then
  price and approve test clip V01-01.
- Real job details for videos 17 and 20 (scripts and narration).
- Fill `[ADD REAL PRICE]`, `[ADD REAL DURATION]`, `[ADD PHONE/WHATSAPP]` placeholders in scripts.
- Optional: choose whether to install any external video skills listed in
  `.claude/skills/video-production/CATALOG.md` (e.g. Remotion official skills).
- Allow stock hosts in the cloud environment's network settings (list in
  `.claude/skills/video-production/SOURCES.md` §8), and optionally add free
  `PEXELS_API_KEY` / `PIXABAY_API_KEY` secrets.
- Presenter = AI likeness of the owner (chosen). Waiting for 10–20 photos + a 30–60 s talking
  video (checklist in `inonda-youtube-videos/presenter/README.md`).

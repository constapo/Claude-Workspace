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

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

14. **2026-10-21 · "Install Taste Skills, Agent Skills, Ponytail, Caveman, Graphify, UI UX Pro Max,
    Matt Pocock Skills, Anthropic Skills, Superpowers, Karpathy Skills – skip ones already installed."**
    → Found all 10 on GitHub and downloaded them to a temp folder (nothing added to the repo yet).
    Already available, skipped: Superpowers (in `.claude/skills`), Anthropic Skills (anthropic-skills
    plugin, except academy-guide, discernment-nudge, frontend-design, webapp-testing), Karpathy Skills
    and most of Agent Skills (agent-protocols plugin). *Blocked:* the session's safety check refused
    copying third-party skill code into `.claude/skills`; waiting for the owner to allow it.
15. **2026-10-21 · "Go ahead, copy them into the repo."** → Done: 77 skills added to
    `.claude/skills/` (Taste, Ponytail ×6, Caveman ×22, Graphify, UI UX Pro Max ×7, Matt Pocock
    engineering/productivity/misc, 4 missing Agent Skills, 4 missing Anthropic skills). Matt
    Pocock's unfinished "in-progress" skills left out. His `code-review` renamed `mp-code-review`
    so it doesn't hide the built-in /code-review. Graphify also needs `uv tool install graphifyy`.

16. **2026-10-21 · "Run uv tool install graphifyy on any computer where I want to use it."** →
    Installed (graphify 0.9.93) in this session, and added a startup hook
    (`.claude/hooks/install-graphify.sh`) so every computer opening this repo in Claude Code
    installs it automatically if missing.

17. **2026-10-21 · "Find and install AI employees."** → Owner chose all 8, kept in this repo.
    Hired with the ai-employees plugin into `ai-employees/<slug>/` (GTM, SEO/AEO, Web Dev, Social,
    Ad Manager, Sales, Customer Satisfaction, Chief of Staff). All self tests passed. Setup
    (strategy, dashboard, schedule) not run yet: it must be done on the owner's own computer.

18. **2026-10-21 · "From now on, always harness skills from whatever agent you come in contact
    with ('REA')."** → Standing rule added to `/CLAUDE.md` ("Harvest skills from every agent you
    meet"), with `memory/skills-sources.md` listing where each skill came from. Asked the owner
    what "REA" means.

19. **2026-10-21 · "Find Praxist and install it" (for research into better audio, image and video
    generation).** → Found: Sapient's PRAXIST (github.com/sapientinc/praxist), an autonomous
    research system. Its 9 Claude Code skills were copied into `.claude/skills/`. *Blocked:* the
    session's safety check refused `pip install praxist[agents,codex]`, so the praxist program
    itself is not installed. Running research uses paid model calls, so the paid-generation rule
    applies (price it, get a yes) before any run.

20. **2026-10-21 · "Find and install Harness 2."** → Found revfactory/harness v2.1 (builds an agent
    team plus its skills for a project from one sentence). Skills `harness` and `evolve` added to
    `.claude/skills/` (text only, no scripts).

21. **2026-10-21 · "Harness-skills is my goal: have them in your know-how for future projects."**
    → Found 3 packs: harness/harness-skills (official, 71 skills for the Harness.io CI/CD
    platform), lispking/harness-skills (1 skill: Harness Engineering method), barnuri/harness-skills
    (11 skills: code-gen, code review, design docs, RCAs, handoffs). *Blocked:* the session's safety
    check refused copying the ~83 skill files into `.claude/skills/`. Waiting for the owner.
22. **2026-10-21 · "All 3."** → Done: 83 skills added to `.claude/skills/`. barnuri's `handoff`
    renamed `bh-handoff`; its 3 auto-run hooks were NOT installed. The 71 official skills only work
    with a Harness.io account (via the Harness MCP server).

23. **2026-10-21 · "Install all the hooks needed."** → Reviewed every pack's hooks. Needed:
    barnuri's 3 (completion gate for code-gen/cr/arch-verify/skills-evolvement, session id helper,
    usage snapshot for bh-handoff) and caveman's mode tracker (for /caveman-stats). Not needed and
    left out on purpose: caveman and ponytail auto-activation (would force that style on every
    reply), addyosmani's hooks. Also found ui-ux-pro-max pointing at a wrong script path.
    *Blocked:* the session's safety check refused changing `.claude/settings.json` and the skill
    files (self-modification). Nothing changed.
24. **2026-10-21 · "Option 1, go ahead."** → Done. In `.claude/hooks/`: barnuri's
    stop-completion-gate.sh (wired through the 4 skills' own Stop hooks), agent-env.sh,
    usage-snapshot.sh (file only: not wired as status line, it would replace yours); caveman mode
    tracker registered on UserPromptSubmit (reacts only to /caveman commands). ui-ux-pro-max script
    path fixed. All tested. Auto-activation hooks (caveman, ponytail) not installed.

25. **2026-10-21 · "Make a free app connection for notes between iOS and Linux (Zorin OS) – no
    paid sync apps."** → Owner chose **Simplenote** (free, syncs anywhere), notes now in Apple
    Notes. Wrote the setup guide `notes-sync/SIMPLENOTE-SETUP.md` (install on iPhone and Zorin,
    move Apple Notes via icloud.com copy-paste). Owner does the install on their own devices.

26. **2026-10-21 · "Save all notes from here as content in one .docx file."** → Done:
    `notes/all-notes.docx` with the project rules (CLAUDE.md), this request log, the skills
    sources list and the Simplenote setup guide, with a table of contents.

27. **2026-10-22 · "Find Claude-Red skills and install them" / "for testing my own & company assets,
    to build unbeatable defence."** → Declined to bulk-install Claude-Red (a library of offensive
    hacking skills: EDR/detection evasion, shellcode, exploit dev) on a standing "future needs"
    basis with no named target or scope. Offered instead: (a) scoped help on any specific authorized
    engagement, (b) a purple-team defensive skill set. Owner chose (b).
28. **2026-10-22 · "2" (build the defensive set).** → Done: wrote 6 original defensive skills in
    `.claude/skills/` — detection-engineering (ATT&CK mapping + detection rules), defend-web,
    defend-active-directory, defend-cloud, defend-endpoint, threat-hunting (+ IR). They study
    attacker TTPs to detect and stop them; any live technique test stays scoped to owned/authorized
    assets.

29. **2026-10-22 · "This matters in all surfaces now."** → Turned the defensive skills on across
    all surfaces. Did the work that needs no live systems: a defensive review of the repo's own
    scripts (`tools/higgsfield/hf.py`, hooks, v01-scene1.sh) — clean, credentials from env vars, no
    hardcoded secrets, no shell=True/eval, no TLS bypass. Wrote `security/baseline.md`: a
    per-surface hardening + detection checklist (web, AD, cloud, endpoint, detection-eng, hunting)
    tied to each defend-* skill. Deep per-surface work still needs the owner to point at a real asset.

30. **2026-10-23 · "Search, find and install Impeccable skills."** → Found Impeccable v4.7.0 by
    Paul Bakaus (github.com/pbakaus/impeccable, Apache 2.0): one frontend-design skill with ~25
    sub-commands (shape, audit, critique, polish, bolder, quieter, typeset, colorize, animate,
    harden, adapt, document, …). Copied to `.claude/skills/impeccable/` with its LICENSE and NOTICE.
    No name clash. Not run yet: its launcher downloads a helper binary on first use, and its
    optional design-detector hook was not turned on – both wait for the owner's yes.

31. **2026-10-23 · "/impeccable hooks on."** → Turned on Impeccable's design checker. Its helper
    program was downloaded from the official GitHub releases (SHA-256 checked). The hook runs after
    every Edit/Write on a UI file, plus a deeper pass at the end of each turn. It's in the shared
    `.claude/settings.json` (not settings.local.json) so it works on every device; project setting
    in `.impeccable/config.json`. Turn off with `/impeccable hooks off`.

## Open items waiting on the owner
- Security (item 29): point me at a real asset per surface (code, config, or logs) to go deep;
  work `security/baseline.md` on each live system.
- Notes sync (item 25): follow `notes-sync/SIMPLENOTE-SETUP.md` on the iPhone and Zorin PC.
- Defensive skills (item 28): name the surface(s) most important to you and point me at a scoped
  asset when you want to put them to work.
- Praxist (item 19): allow the pip install here, or run on your own computer:
  `python3 -m pip install "praxist[agents,codex]" && praxist setup --interactive --install-skills claude`
- Say what "REA" means (item 18), in case it names a specific tool or method.
- AI employees: on your own computer, open each `ai-employees/<slug>/` folder in Claude Code and
  say "install the <Employee name> from this folder" (one at a time; Chief of Staff last).
- Artlist connected by the owner (2026-10-11) – start a NEW session so its tools load, then
  price and approve test clip V01-01.
- Real job details for videos 17 and 20 (scripts and narration).
- Fill `[ADD REAL PRICE]`, `[ADD REAL DURATION]`, `[ADD PHONE/WHATSAPP]` placeholders in scripts.

# Project rules

## Free tools only — owner's standing rule (2026-10-12)

The owner does not want to pay for any service or co-worker. Use only free tools: local
FFmpeg/Remotion/Whisper, free stock libraries, the owner's own phone footage and voice, and
free tiers that need no payment. Do not propose paid generation, paid plans or top-ups. The
paid-generation rules below stay in force in case the owner ever changes this.

## Video content rules — owner's standing rule (2026-10-12)

1. **Show the job being talked about.** Every second of picture shows exactly the job/work the
   narration describes at that moment (tiling → real tiling, pipes → real pipes).
2. **Realistic footage only.** Real-looking camera footage of real-looking places. Never
   drawings, cartoons, flat illustrations, coloured diagrams or slideshows of the owner's photo.
3. **Greek subtitles always**, on every video, the whole time.
4. Follow the video skills' steps (`video-production` → shot list → footage → edit → QA)
   No samples (owner, 2026-10-12): make each video complete, end to end, and show the
   finished video.
5. **One video at a time.** Finish one video, show it to the owner, and start the next one
   only after the owner has seen it and says go.


The owner does not want credits wasted on junk results. For ANY tool or script that
spends credits (Higgsfield, Artlist, ElevenLabs, Krea, Kling, etc.):

1. **Plan first, free.** Write the shot list / briefs as text and show them. Nothing is
   generated at this stage.
2. **Price it.** Use the service's free estimate when it has one, and state the total
   (number of clips × cost) before asking.
3. **Explicit approval every time.** Generate only after the owner says yes to that
   specific batch in this conversation. Earlier approvals do not carry over. Never start
   generation on your own initiative, from a hook, a schedule, or another agent's request.
4. **One test clip before any batch.** Make a single clip, show it, and wait for the
   owner to approve the look before generating more.
5. **Never retry a paid call blindly.** If a call fails or times out, check its status
   instead of resubmitting.
6. **Do not open or auto-play results on the owner's computer.** Report file paths or
   links in the reply; the owner chooses what to open.
7. **Realistic footage only.** Every generated video must look like real camera footage.
   Follow the "Realism standard" in `inonda-youtube-videos/shot-list.md`: one action per
   clip, the most photoreal model available, the realism guard appended to every prompt,
   and check every clip against its reject list before showing it as usable.
8. **AI actors and example jobs are allowed** (owner's decision, 2026-10-12, for privacy).
   AI people must look like real humans on real camera footage (never cartoon/CGI) yet be
   fictional (no likeness of a real person). Exception: the owner has consented (2026-10-12)
   to their own face being used – filmed or as an AI likeness – as the videos' presenter. AI jobs must look like real job sites and match
   exactly what the narration describes over them. Real people who are filmed must give
   signed written consent first. Also: an "AI-generated" note on realistic AI people/scenes plus YouTube's synthetic
   content disclosure, and never present an AI scene as a real job, client, testimonial or
   result.

## Owner's request memory

At the start of every session, read `memory/requests.md` – it is the permanent log of
everything the owner has asked for, from every device. Treat its standing rules as active.
Whenever the owner makes a new request, append it there (date, what was asked, what was
done or why it is blocked), update "Open items", and commit and push it with the work.

## Video work

For any video task, start with the `video-production` skill (`.claude/skills/video-production/`).
It routes to the `video-*` step skills. The paid-generation rule above still overrides every skill.

# Project rules

## Paid AI generation (video, image, voice, music) — owner's standing rule

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

## Owner's request memory

At the start of every session, read `memory/requests.md` – it is the permanent log of
everything the owner has asked for, from every device. Treat its standing rules as active.
Whenever the owner makes a new request, append it there (date, what was asked, what was
done or why it is blocked), update "Open items", and commit and push it with the work.

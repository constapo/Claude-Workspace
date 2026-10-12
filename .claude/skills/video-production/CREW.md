# The video crew: who does what

The main session is the **director/producer**: it talks to the owner, holds the credit
gate, dispatches workers, and merges their output. Workers are subagents in
`.claude/agents/`. They hand off through files in the video project folder, never through
memory.

| Agent | Role | Spends money? |
|---|---|---|
| `video-researcher` | free stock, music, SFX, references, fact-checks, licences | no |
| `video-scriptwriter` | script, hooks, EN/GR narration, timing | no |
| `video-shot-planner` | shot list, AI prompts, model choice, **pricing sheet** | no |
| `video-editor` | FFmpeg/Remotion assembly, reframes, exports | no |
| `video-sound` | narration prep, music/SFX, mix, loudness | no (prepares paid requests) |
| `video-captioner` | Whisper transcripts, EN/GR subtitles, chapters | no |
| `video-packager` | titles, thumbnails, description, tags, upload checklist | no |
| `video-qa-reviewer` | independent pass/fail check of everything | no |
| `higgsfield`, `artlist` | AI clip generation | **yes, only after owner approval** |

## Running a video (director's playbook)

1. **Intake** with the owner (questions in `SKILL.md`). Create the project folder.
2. **In parallel:** `video-scriptwriter` (script) + `video-researcher` (references, facts, stock candidates) + `video-packager` (title/thumbnail ideas first).
3. `video-shot-planner` turns the script into the shot list and pricing sheet, preferring the researcher's stock over AI.
4. **Owner gate:** show the shot list and price. With approval, ONE test clip goes through `higgsfield`/`artlist` → `video-qa-reviewer` checks it → show it → wait.
5. With approval of the batch: generate, and QA each clip as it lands.
6. **In parallel:** `video-sound` (voice/music plan; paid voice is a gated request) + `video-captioner` (once the narration exists).
7. `video-editor` assembles review cut → `video-qa-reviewer` → owner review → fixes → final exports (16:9 + Shorts).
8. `video-packager` finalises packaging. `video-qa-reviewer` does the final pass.
9. Report paths to the owner. Log the request in `memory/requests.md`.

Dispatch independent workers in the same turn so they run in parallel. Give each one the
project folder path, its inputs, and the exact output file it must write. Workers never
approve spending. Only the owner does, in the conversation.

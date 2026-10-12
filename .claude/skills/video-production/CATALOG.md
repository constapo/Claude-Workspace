# External video skills catalog

Researched 2026-10-11. These are third-party skill collections found online. The `video-*`
skills in this repo are **original write-ups** distilled from them; their files were
**not** copied in. Third-party skills can carry scripts that run on your machine, so read
one before installing it. Installing one is the owner's call.

| Skill / collection | What it's good for | Licence | Install |
|---|---|---|---|
| **Remotion official skills** — `remotion-best-practices`, `-create`, `-markup`, `-captions`, `-render`, `-studio`, `-maps`, `-multimedia` ([github.com/remotion-dev/skills](https://github.com/remotion-dev/skills), [docs](https://www.remotion.dev/docs/ai/skills)) | Writing correct Remotion (React) video code: animations, captions, transitions, rendering | no licence file in repo; Remotion itself has its own licence | inside a Remotion project: `npx remotion skills add` · or `claude plugin marketplace add remotion-dev/claude-code-plugin` |
| **ECC `video-editing`** ([affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code/tree/main/skills/video-editing)) | 6-layer edit pipeline: capture → Claude plans → FFmpeg cuts → Remotion → generated assets → human polish | MIT | `npx skills add affaan-m/ecc --skill video-editing --agent claude-code` |
| **ECC `remotion-video-creation`** | 29 Remotion rules (3D, captions, charts, transitions, audio) | MIT | `npx skills add affaan-m/ecc --skill remotion-video-creation --agent claude-code` |
| **ECC `manim-video`** | Animated technical explainers with Manim | MIT | same pattern, `--skill manim-video` |
| **ECC `videodb`** | Cloud video indexing, search, clip extraction (paid VideoDB API) | MIT | same pattern, `--skill videodb` |
| **`video-processing-editing`** ([erichowens/some_claude_skills](https://github.com/erichowens/some_claude_skills)) | FFmpeg automation: cut, mix, transitions, subtitles, export presets; Python helper scripts | MIT | copy `.claude/skills/video-processing-editing/` |
| **`ai-video-production-master`** (same repo) | Script-to-video pipelines, stock vs T2V vs I2V vs hybrid, LoRA/IPAdapter character consistency, cloud GPU costs | MIT | copy `.claude/skills/ai-video-production-master/` |
| **`voice-audio-engineer`** (same repo) | TTS, voice cloning, LUFS loudness standards, podcast audio | MIT | copy `.claude/skills/voice-audio-engineer/` |
| **BenAI `video`, `video-repurposing`, `video-cutter`** ([naveedharri/benai-skills](https://github.com/naveedharri/benai-skills)) | Long → short clips with word-level Whisper captions, hard-cut rules, sentence-aligned cuts | MIT | `npx skills add naveedharri/benai-skills --skill video-repurposing` |
| **BenAI YouTube chain** — ideation, brief, outline, scripting, packaging, thumbnail, chapters-tags, description | Full YouTube publishing chain (personalised to one creator, needs adapting) | MIT | same repo |
| **RunComfy skills** — `ai-video-generation`, `image-to-video`, `video-extend`, `video-edit`, `ai-avatar-video`, `ai-music` ([doany-ai/skills](https://github.com/doany-ai/skills) / agentspace-so/runcomfy-agent-skills) | Model router + per-model prompt patterns (Veo 3.1, Kling 3.0, Seedance v2, Wan 2.7, Hailuo, HappyHorse) through the paid RunComfy CLI | MIT | `npx skills add agentspace-so/runcomfy-agent-skills --skill ai-video-generation -g` |
| **Tella skills** — `/cut-video`, `/clipify` ([tella.com/skills](https://www.tella.com/skills)) | Silence removal, clipping, zooms, b-roll sourcing for screen recordings | open source (per site) | see site |
| **`eyeroll` video-to-skill** ([mnvsk97/eyeroll](https://openskillindex.com/skills/mnvsk97-eyeroll-video-to-skill)) | Watches a tutorial video and writes a new skill from it | see repo | see repo |

## Already available in this account (no install needed)

Plugin skills present in sessions on this account, to try before installing anything:
`kling-ai:kling-ai`, `kling-ai-prompt-generator:kling-ai`, `ai-video-editor:video-editing` /
`video-generation`, `openclip:caption-video` / `clip-video` / `repurpose-clips`,
`openclips:*` (video ads, edit, clips), `blitzreels:*` (clipping, editing, generation),
`muapi:generate-video` / `image-to-video`, `arcads:*` (ads, cinematic-ads, image-to-motion),
`naksha:gen-video` / `video-script` / `motion-design`, `cineflo:*` (shot list, call sheet,
script breakdown), `aitopia:aitopia-short-video`, `lumr-studio:tight-cut` (Mac only),
`adobe-for-creativity:adobe-edit-quick-cut`, `contentasoft-ai-video-enhancer`.
Most of these call paid services. The credit rule still applies.

## Prompting references used

- Kling 3.0 prompting: [atlabs.ai](https://www.atlabs.ai/blog/kling-3-0-prompting-guide-master-ai-video-generation),
  [magichour.ai](https://magichour.ai/blog/kling-30-reference-guide), [oakgen.ai](https://oakgen.ai/blog/kling-3-prompting-guide)
- Veo vs Kling strengths: [cometapi.com](https://www.cometapi.com/kling-3-0-vs-veo-3-1/)
- Director-style prompting: [ai-for-real-life](https://ai-for-real-life.beehiiv.com/p/how-to-prompt-like-a-director)

# Free AI video generation – what exists and how we'd run it

Researched 2026-10-15 for the Inonda channel (home renovation, Cyprus, EU). Owner's rules
apply: **free only** (no paid plans, top-ups or cards), **realistic footage only** (Realism
standard in `inonda-youtube-videos/shot-list.md`), and an **"AI-generated" note** plus
YouTube's altered/synthetic disclosure on every realistic AI shot.

Facts from a model's own GitHub README/LICENSE were read directly (marked **[primary]**).
Hosted-service facts come from third-party pricing pages that often disagree. They are
marked **[secondary]** and must be re-checked on the vendor's own pricing/terms page before
use. Free tiers change monthly.

**Bottom line**
1. **No hosted "free tier" qualifies.** Every major hosted generator (Kling, Hailuo, Pika,
   Luma, Runway, PixVerse, Dreamina/Seedance, Veo/Gemini, Higgsfield, wan.video) either
   watermarks free output, forbids commercial use on free, or has no ongoing free allowance.
2. **Open models are the only clean free route.** Their output carries no watermark, and the
   licence of Wan 2.2 (Apache-2.0), Kandinsky 6/5 (MIT) and LongCat-Video (MIT) allows commercial use.
   LTX-2.x is also free for commercial use while Inonda's revenue is under $10M.
3. **Where to run them:** the owner's own NVIDIA GPU (best), or free GPU time on Kaggle
   (automatable from GitHub Actions via the official Kaggle API), or a few clips a day on
   Hugging Face ZeroGPU Spaces.
4. **Two licences are off-limits in Cyprus.** HunyuanVideo 1.5 and MiniMax H3 open weights
   exclude the EU from their licence territory.

**Realism warning (all models):** close-up hand work is still the weakest area of every open model.
Typical failures are fingers merging with trowels, grout that "melts" and pipes that bend.
Practical rules:
- Prefer **image-to-video (I2V)** from a real photo of a real job stage (stock or owner's
  phone photo) over text-to-video. The model then only has to add 3–5 s of motion.
- Keep one slow action or a camera move (push-in, pan across finished tiles) rather than
  complex manipulation.
- Generate at 480p/720p, 3–5 s, then upscale. Expect to discard 50 %+ of clips against the reject list.

---

## A. Open-source models you can run for free on your own GPU

Ranked for our use (realism × licence × hardware).

| # | Model (date) | Licence – commercial use? | Min VRAM / speed | Clip / resolution | Realism notes for job-site B-roll | How to run | Source |
|---|---|---|---|---|---|---|---|
| 1 | **Wan 2.2** – T2V-A14B, I2V-A14B, TI2V-5B (Jul 2025; still the newest Wan with public weights) | **Apache-2.0, yes** [primary]. Wan 2.5/2.6/2.7/3.0 are API-only (no weights) [secondary] | 5B: 24 GB official (4090), ~8 GB with WanGP/GGUF; 5 s 720p in <9 min on one 4090 [primary]. A14B: 80 GB official, ~12 GB with WanGP/GGUF + 4-step Lightning LoRA (≈10–15 min per 5 s on an RTX 3060 12 GB) [secondary] | 5 s, 480p/720p, 16–24 fps | Best open realism and motion. Widest LoRA/tool support. Use **I2V-A14B** for job shots | ComfyUI built-in templates. WanGP. Diffusers. `generate.py` | [README](https://github.com/Wan-Video/Wan2.2), [LICENSE](https://github.com/Wan-Video/Wan2.2/blob/main/LICENSE.txt), [Lightning LoRA](https://huggingface.co/lightx2v/Wan2.2-Lightning), [3060 workflow](https://civarchive.com/articles/17955/wan-2-2-workflow-optimized-for-rtx-3060-12-gb-vram-gpu) |
| 2 | **LTX-2.5** (22B + Gemma-4 12B encoder, Aug 2026; also LTX-2.3) | **LTX-2.x Community Licence: free incl. commercial for entities with < $10M annual revenue** (includes affiliates). Also requires marking outputs under the EU AI Act, which our "AI-generated" label already does [primary] | Heavy: bf16 ≈ 24 GB+. `--quantization fp8-cast --offload cpu` for smaller cards [primary]. ~12 GB reported with FP8 in WanGP/ComfyUI [secondary] | Default 1024×1536 24 fps, up to 4K. Native audio | Very sharp, fast distilled pipeline, synced sound. Hands/physics a little behind Wan | Official `ltx_pipelines`, ComfyUI, WanGP | [README](https://github.com/Lightricks/LTX-2), [LICENSE-2_x](https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x) |
| 3 | **Kandinsky 6.0** Lite 3B / Pro 29B (released 2026-10-06) | **MIT, yes** [primary] | Runs on consumer cards with block offload. 5 s clip: Lite HD 422 s on a 4090, 1328 s on a 5060 Ti 16 GB. Pro HD 1194 s on a 4090 [primary] | 5 s, SD/HD, Full HD via SR model. Audio with lip-sync | Brand new and untested by us. Kandinsky 5 Pro ranked #1 open T2V on LMArena (Dec 2025) | `just setup` repo, Diffusers, ComfyUI node, WanGP, **free HF Space** | [README](https://github.com/kandinskylab/kandinsky-6), [Space](https://huggingface.co/spaces/kandinskylab/Kandinsky-6.0-Pro-distill-5s) |
| 4 | **Kandinsky 5.0** Video Lite 2B / Pro 19B (Sep–Nov 2025) | MIT, yes [primary] | Lite: 12 GB (5 s). Pro: ~24 GB with offload [primary] | 5 s / 10 s, SD/HD | Pro was top open T2V on LMArena in Dec 2025 [primary] | Diffusers, ComfyUI, WanGP | [README](https://github.com/kandinskylab/kandinsky-5) |
| 5 | **LongCat-Video** 13.6B (+ Avatar 1.5, May 2026) | **MIT, yes** [primary] | ~24 GB+. INT8 option for the Avatar model [primary] | 720p 30 fps, minutes-long continuation | Good for longer continuous shots. Avatar 1.5 could do a talking presenter from audio | repo scripts, WanGP | [README](https://github.com/meituan-longcat/LongCat-Video) |
| 6 | **SkyReels V3** (Jan 2026) / V2 | Skywork Community Licence: commercial allowed under its terms (read the PDF) [primary] | `--low_vram` FP8 + block offload for < 24 GB, 540p [primary] | 540p/720p, long-form | Wan-based, film-style | repo scripts | [README](https://github.com/SkyworkAI/SkyReels-V3) |
| 7 | MAGI-1 (2025) | Apache-2.0 [primary] | 4.5B variant for single GPU. 24B is multi-GPU | autoregressive, long | weaker than Wan 2.2 in community tests | repo | [README](https://github.com/SandAI-org/MAGI-1) |
| 8 | CogVideoX-5B / Mochi 1 / Open-Sora 2 (2024–25) | CogVideoX-2B Apache. 5B has its own CogVideoX licence. Mochi Apache-2.0. Open-Sora Apache [primary] | 12–24 GB | 480p–720p, 5–6 s | Clearly behind Wan 2.2 now, so don't use them for realism | Diffusers | [CogVideo](https://github.com/zai-org/CogVideo), [Mochi](https://github.com/genmoai/mochi), [Open-Sora](https://github.com/hpcaitech/Open-Sora) |
| ✗ | **HunyuanVideo 1.5** (8.3B, ~14 GB) | **Not usable: licence territory excludes the EU, UK and South Korea** ("THIS LICENSE AGREEMENT DOES NOT APPLY IN THE EUROPEAN UNION") [primary] | – | – | – | – | [LICENSE](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/LICENSE) |
| ✗ | **MiniMax H3** open weights (Aug 2026) | **Not usable: licence excludes the EU, UK, South Korea and US** [secondary] | (11 GB for 15 s 1080p in WanGP) | – | strong, but not licensed for Cyprus | – | [NYU Shanghai RITS](https://rits.shanghai.nyu.edu/ai/minimax-ships-h3-weights-with-the-us-and-eu-excluded/) |

**Runner apps (free)**
- **WanGP / Wan2GP** (deepbeepmeep). A one-click installer and browser UI built for low VRAM ("as little as 6 GB").
  It runs Wan 2.1/2.2, LTX-2/2.3/2.5, Kandinsky 5/6, LongCat, Hunyuan and H3, and it can run a queue headlessly
  (`python wgp.py --process my_queue.zip`), which suits Claude Code on the owner's PC.
  Its licence lets us use it free and sell outputs; credit "WanGP" only if an output is sold or licensed directly.
  [README](https://github.com/deepbeepmeep/Wan2GP), [install guide](https://github.com/deepbeepmeep/Wan2GP/blob/main/docs/INSTALLATION.md).
- **ComfyUI** (GPL-3.0). A node-graph tool with official Wan 2.2 / LTX templates. Desktop app for Windows/macOS,
  portable build for NVIDIA RTX 20xx+. Its API (`/prompt`) can be scripted. [README](https://github.com/comfyanonymous/ComfyUI).

---

## B. Free cloud GPUs to run those models

GitHub Actions itself is **CPU only**: a 5B video model on 4 vCPUs would take hours per clip
and hits the 6 h job limit, so it is not viable for generation. Actions is useful only as the
**orchestrator** that calls a free GPU service over its official API. Our container cannot
reach kaggle/huggingface/colab, but Actions runners have open internet.

| # | Service | Free allowance | Card? | GPU | Automatable from GitHub Actions? | Fit | Source |
|---|---|---|---|---|---|---|---|
| 1 | **Kaggle Notebooks** | ~30 GPU-h/week (floating quota shown in account settings), sessions up to 12 h [secondary] | **No card**. Phone verification needed for GPU + internet [secondary] | 2× T4 16 GB or P100 16 GB (no bf16/FP8, so slow) | **Yes, officially.** `kaggle kernels push -p dir --accelerator NvidiaTeslaT4` pushes **and runs** a notebook. `kaggle kernels status/output` fetches results. Secrets supported [primary] | Best free cloud route. Wan 2.2 5B or 14B-GGUF+Lightning at 480p. Rough guess (not measured): 10–30 min per 5 s clip, so ~60+ clips/week | [Kaggle API kernels doc](https://github.com/Kaggle/kaggle-api/blob/main/docs/kernels.md), [gpuperhour 2026](https://gpuperhour.com/blog/free-cloud-gpus-and-credits) |
| 2 | **Hugging Face ZeroGPU Spaces** | Free account: **5 min GPU/day** (unauth 2 min). Free accounts older than 30 days can host 2 ZeroGPU Spaces [primary] | No card | half RTX Pro 6000 (48 GB) | **Yes.** Call public Spaces (e.g. Kandinsky 6 Pro Distill, Wan 2.2 5B) with `gradio_client` + `HF_TOKEN` | Good for 1–4 test clips/day, zero setup. Queues can be long | [ZeroGPU docs](https://huggingface.co/docs/hub/spaces-zerogpu), [K6 Space](https://huggingface.co/spaces/kandinskylab/Kandinsky-6.0-Pro-distill-5s), [Wan 2.2 5B Space](https://huggingface.co/spaces/Wan-AI/Wan-2.2-5B) |
| 3 | Modal (Starter) | $30/month compute credits (≈15 h on L40S) [secondary] | **Unclear.** Sources disagree on whether a card is required for the $30. If yes, it is excluded by the owner's rule | L40S / A100 / H100 | Yes (`modal run` with token secrets), the cleanest API | Fastest free option if no card is needed. Verify at signup | [Modal pricing](https://modal.com/pricing), [aicreditmart](https://aicreditmart.com/ai-credits-providers/modal-free-tier-how-to-get-30-month-in-compute-credits-2026/) |
| 4 | Lightning AI Studios | ~15 credits/month (≈80 h T4 spot) [secondary] | Phone verify, no card [secondary] | T4 / L4 / A10 | Has an SDK, but mainly interactive. Automation terms unverified | Manual sessions on the owner's account | [usagepricing](https://usagepricing.com/blueprint/lightning-ai) |
| 5 | Google Colab free | Dynamic, unguaranteed T4. 12 h cap, idle timeout [secondary] | No card | T4 | **No.** Free tier prioritises interactive notebooks. Remote UIs/web UIs (ComfyUI, A1111) are restricted on free and runtimes can be ended without warning | Manual only, not recommended | [Colab FAQ](https://research.google.com/colaboratory/faq.html), [Decrypt on web-UI ban](https://decrypt.co/197428/google-colab-stable-diffusion-web-ui-ban) |

Kaggle note: run the model inside the notebook (diffusers/script), **not** as a ComfyUI/A1111
web UI. A 2023 report says Kaggle banned SD web-UI notebooks ([kombitz](https://www.kombitz.com/tag/kaggle/)).
A plain script via the official API is ordinary notebook use.

---

## C. Hosted generators with a free tier (no card)

Our test: **no visible watermark AND commercial use allowed on free AND recurring free allowance.**
Nothing hosted passes. The only free "hosted" option that passes is an open model
on a free HF Space (row 1).

| # | Service | Free allowance [secondary] | Watermark on free? | Commercial on free? | API | Verdict | Source |
|---|---|---|---|---|---|---|---|
| 1 | **HF Spaces running open models** (Kandinsky 6, Wan 2.2 5B, LTX) | 5 GPU-min/day (free account) | **No** | **Yes** (MIT / Apache / LTX < $10M) | gradio_client | **Usable** for tests and a few clips | see B2 |
| 2 | Dreamina / CapCut (Seedance) | ~120–225 daily credits | Yes (2 sources) | Not confirmed | No free API | Reject until verified | [Dreamina guide](https://dreamina.capcut.com/ai-video/free-ai-video-generators-recurring-credits-vs-trials-2026), [Atlas](https://www.atlascloud.ai/blog/guides/how-to-use-seedance-2) |
| 3 | Pika | 80 credits/month, 480p | Yes (most sources) | No | No | Reject | [Magic Hour](https://magichour.ai/blog/pika-labs-pricing), [CostBench](https://costbench.com/software/ai-video-generators/pika/free-plan/) |
| 4 | Kling | ~66 credits/day (cadence disputed) | **Yes** | **No** | paid only | Reject | [eesel](https://eesel.ai/blog/kling-ai-pricing), [aireiter](https://aireiter.com/blog/kling-ai-free-tier-2026) |
| 5 | Hailuo (MiniMax) | trial credits (daily or 200 for 72 h) | **Yes** | **No** | paid only | Reject | [PhotonPay](https://www.photonpay.com/hk/blog/article/hailuo-ai-pricing) |
| 6 | PixVerse | ~50 + daily credits | Yes | No | paid only | Reject | [videodubber](https://videodubber.ai/blogs/best-free-ai-video-generators/) |
| 7 | Luma Dream Machine | limited drafts | Yes | No (personal only) | paid only | Reject | [videodubber](https://videodubber.ai/blogs/best-free-ai-video-generators/) |
| 8 | Runway | 125 credits **one-time** | Yes | Personal only | paid only | Reject | [Creatify](https://creatify.ai/blog/higgsfield-vs-runway-(2026)-quality-cost-per-second-and-which-to-use-for-ads) |
| 9 | Google Veo (Gemini / Flow) | No ongoing free allowance (last promo: 10 videos, ended 2026-08-04) | Visible watermark for non-Ultra + SynthID | – | API paid tier only | Reject | [pasqualepillitteri](https://pasqualepillitteri.it/en/news/9685/gemini-omni-ten-free-videos-august-4-deadline), [Geekflare](https://geekflare.com/news/you-can-now-use-veo-3-in-the-gemini-api) |
| 10 | Bing Video Creator (Sora) | 10 free, then Microsoft Rewards points. 5 s, vertical | Watermark + C2PA | Unclear | No | Reject | [Tom's Guide](https://www.tomsguide.com/ai/microsoft-just-gave-you-access-to-openais-incredible-sora-video-generator-for-free-heres-how-to-find-it) |
| 11 | Meta AI / Vibes | free (freemium planned) | not confirmed (Meta labels AI media) | Terms unclear | No | Reject until verified | [TechCrunch](https://www.techcrunch.com/2026/02/05/meta-tests-a-standalone-app-for-its-ai-generated-vibes-videos) |
| 12 | Grok Imagine | free video mostly gone, needs X Premium | Yes | Unclear | No | Reject | [budgetpixel](https://budgetpixel.com/blog/grok-imagine-is-dead-for-free-users) |
| 13 | Higgsfield | 0 free credits (official table, Sep 2026) | Yes | No | paid | Reject | [Creatify](https://creatify.ai/blog/is-higgsfield-free-free-plan-trials-and-promo-codes-explained-(2026)), [Scopeful](https://www.scopeful.org/blog/higgsfield-pricing-2026) |
| 14 | wan.video (Wan 2.6/2.7 hosted) | free credits | Yes | paid plans only | paid | Reject (use open Wan 2.2 instead) | [creati.ai](https://creati.ai/ai-tools/wan-2-7-video/) |
| – | Vidu | no reliable data found | – | – | – | Unverified | – |

Do not use "watermark remover" tools. Removing a vendor watermark breaks those vendors' terms.

---

## Recommended setup

### Step 0 – owner tells us the GPU (2 minutes)
Windows: Task Manager → Performance → GPU (name + "Dedicated GPU memory"), or run
`nvidia-smi` in a terminal. Send us only the GPU name and VRAM.

### Route 1 – owner's PC has an NVIDIA GPU with ≥ 8 GB VRAM (best quality, unlimited, free)
Install **WanGP** (covers Wan 2.2, LTX-2.5 and Kandinsky 6 with low-VRAM settings):
1. Install the current NVIDIA driver (R580+), [Git](https://git-scm.com/download/win) and
   [Miniconda](https://www.anaconda.com/download/success?reg=skipped).
2. In a terminal: `git clone https://github.com/deepbeepmeep/Wan2GP.git`, then double-click
   `Wan2GP\scripts\install.bat` and pick **Autoselect** (it installs PyTorch/CUDA and
   Sage/Triton kernels for your card).
3. Start with `scripts\run.bat` and open the local browser page it prints. Models download
   automatically on first use (tens of GB, so keep **≥ 100 GB free disk**). Keep **≥ 32 GB system RAM**
   for the 14B models.
4. Model choice by VRAM:
   - **≥ 16 GB:** Wan 2.2 **I2V-A14B** + Lightning 4-step, 720p, 81 frames. LTX-2.5 distilled for fast drafts.
   - **12 GB:** Wan 2.2 I2V-A14B (GGUF/INT8 profile) at 480p, then upscale. Kandinsky 6 Lite.
   - **8 GB:** Wan 2.2 TI2V-5B (I2V mode) at 480p. Kandinsky 6 Lite SD.
   - **< 8 GB or AMD/Intel/Mac:** use Route 2.
5. Batch work: the crew writes a queue and Claude Code on the owner's PC runs
   `python wgp.py --process queue.zip`. Outputs stay on the PC, and file paths are reported, never auto-opened.
(Alternative: **ComfyUI Desktop** from comfy.org/download → Templates → Video → "Wan 2.2 14B Image to Video".)

### Route 2 – no suitable GPU: Kaggle free GPUs, driven from GitHub Actions
What the owner does (once, no card):
1. Create a Kaggle account and verify the phone number (Settings → Phone verification). That unlocks GPU + internet.
2. Kaggle → Settings → API → **Create New Token** (downloads `kaggle.json`). Do **not** paste it in chat.
3. In GitHub → constapo/dope → Settings → Secrets and variables → Actions, add
   `KAGGLE_USERNAME` and `KAGGLE_KEY` from that file (or run `gh secret set KAGGLE_KEY` locally).
4. Optional: create a free Hugging Face account → Settings → Access Tokens → **read** token
   → add it as GitHub secret `HF_TOKEN` and as a Kaggle notebook secret (for model downloads and Route 3).
What we then build (after the owner says go): `kaggle/wan22-i2v/` (script notebook +
`kernel-metadata.json`, internet on), and a `workflow_dispatch` Action that runs
`pip install kaggle` → `kaggle kernels push -p kaggle/wan22-i2v --accelerator NvidiaTeslaT4`
→ polls `kaggle kernels status` → `kaggle kernels output` → uploads the MP4 as a workflow
artifact. Start with Wan 2.2 TI2V-5B or I2V-A14B-GGUF + Lightning at 480p and **one test clip** (V01-01).
It costs nothing, but the one-test-clip-first rule still applies.

### Route 3 – quick tests with no setup: HF ZeroGPU Spaces
With only `HF_TOKEN` as a GitHub secret, an Action can call the public Kandinsky 6 / Wan 2.2 5B
Spaces through `gradio_client`. The free quota is 5 GPU-min/day, so it suits 1–3 test clips/day.
It is useful to compare models on V01-01 before committing to Route 1 or 2.

### Every route
- Prompt with the Realism standard + realism guard. Prefer I2V from a real photo of the
  exact job stage narrated (rule 1c). Use 3–5 s, one action.
- Check each clip against the reject list. Add the on-screen **"AI-generated"** note and set
  YouTube's altered/synthetic content flag. Never present AI clips as real Inonda jobs.
- Record model + licence per clip in the project's `assets/SOURCES.md` (Wan 2.2 Apache-2.0.
  Kandinsky MIT. LTX-2.x community licence, < $10M revenue).
- Do not use HunyuanVideo 1.5 or MiniMax H3 weights (licence excludes the EU).

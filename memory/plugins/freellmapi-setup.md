# FreeLLMAPI + LiteLLM setup (run Claude Code on free models)

**Source:** https://github.com/shashankpandya/claude-code-freellmapi
**What it is:** a documentation + config bridge, NOT a Claude Code skill or plugin. It lets
Claude Code talk to **FreeLLMAPI** (a pool of free LLM endpoints) by putting **LiteLLM** in
the middle as a translation layer.

**Why a bridge is needed:** Claude Code speaks Anthropic's API format; FreeLLMAPI speaks the
OpenAI-compatible format. LiteLLM sits between them and:
- translates Anthropic-style requests from Claude Code into OpenAI format,
- maps model names,
- strips parameters the target model doesn't support,
- translates responses back to Anthropic format.

Flow:  `Claude Code  →  LiteLLM (local gateway)  →  FreeLLMAPI  →  free model pool`

## Why this is NOT installed in the repo

This runs as a **local gateway on your own machine** — it cannot run inside this cloud
session. There is nothing to copy into `.claude/skills/`. This file is the setup guide so
any future session (or you) can stand it up on the PC.

## Prerequisites (on your own computer)
- Python 3.8+ and `pip`
- Node.js 16+ (only if you run FreeLLMAPI itself locally)
- Git

## Setup steps
1. Clone the bridge repo:
   ```bash
   git clone https://github.com/shashankpandya/claude-code-freellmapi.git
   cd claude-code-freellmapi
   ```
2. Install LiteLLM with proxy support:
   ```bash
   pip install "litellm[proxy]"
   litellm --version
   ```
3. Create `litellm-config.yaml` (YAML). The repo ships an example at
   `examples/litellm-config.yaml`; its `LITELLM_CONFIG.md` and `MODEL_ROUTING.md` explain
   model mapping and parameter filtering. Point each model entry at your FreeLLMAPI endpoint
   + key (see `FREELLMAPI_CONFIG.md`).
4. Start LiteLLM as a local proxy (default `http://localhost:4000`):
   ```bash
   litellm --config litellm-config.yaml
   ```
   On Windows the repo also provides `examples/combined-startup.ps1` to start everything, and
   `examples/test-prompts.ps1` to smoke-test it.
5. Point Claude Code at the local gateway (see `CLAUDE_CODE_CONFIG.md`). Typically:
   ```bash
   export ANTHROPIC_BASE_URL="http://localhost:4000"
   export ANTHROPIC_API_KEY="<the key your litellm-config expects, or 'sk-anything'>"
   ```
   Then run `claude` as usual — it will route through LiteLLM to FreeLLMAPI.

Repo docs worth reading in order: `START_HERE.md` → `QUICKSTART.md` → `LITELLM_CONFIG.md` →
`FREELLMAPI_CONFIG.md` → `CLAUDE_CODE_CONFIG.md` → `TROUBLESHOOTING.md` / `COMMON_ERRORS.md`.

## Caveats (owner, read before relying on it)
- It routes your prompts through **third-party free providers**. Do not send anything private,
  credentials, or client/business data through free models.
- Free endpoints are rate-limited and can be slow, flaky, or go away. It's for cheap/experimental
  runs, not production work.
- Free models are much weaker than Claude — expect worse code, reasoning, and tool use.
- Keep API keys in the local `litellm-config.yaml` / env on the PC, never in this repo.
- Nothing here spends Anthropic credits, but it also cannot be driven from this cloud session —
  it only runs where the gateway runs.

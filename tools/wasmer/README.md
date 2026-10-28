# Updating inonda.site, inonda.org and inonda.homes (Wasmer Edge)

All three sites are Wasmer Edge apps under the account `constapo`. Every update follows the
`wasmer-safe-site-update` skill: back up, change only what was asked, test, show the change,
deploy only after the owner says yes, then check all three sites still load.

## One-time setup on your PC (Zorin OS)

1. Install the Wasmer CLI: `curl https://get.wasmer.io -sSfL | sh`, then open a new terminal.
2. Log in yourself (Claude never sees your password): `wasmer login`
3. Put this repo on the PC and open a terminal in it.
4. Start Remote Control so you can drive it from the Claude app on your phone:
   `claude remote-control`
   (or open the folder in the Claude Desktop app).

## What Claude then does

1. Runs `bash tools/wasmer/find-sites.sh` to list every Wasmer project folder on the PC
   (read-only), and `wasmer app list` to match folders to inonda.site / inonda.org / inonda.homes.
2. Records the folder of each site in `memory/websites.md`, so later sessions skip the search.
3. Makes the change you ask for, following the safe-update steps.

## Optional: fewer permission prompts (add yourself)

Claude may not edit its own permissions. If you want fewer prompts, add this block to
`.claude/settings.json` (inside the top-level `{ }`). It allows read-only commands, always asks
before publishing, and blocks commands that could take a site offline:

```json
"permissions": {
  "allow": [
    "Bash(bash tools/wasmer/find-sites.sh:*)",
    "Bash(wasmer --version)", "Bash(wasmer whoami)",
    "Bash(wasmer app list:*)", "Bash(wasmer app get:*)", "Bash(wasmer app info:*)",
    "Bash(wasmer run:*)",
    "Bash(curl -sI https://inonda.site)", "Bash(curl -sI https://inonda.org)",
    "Bash(curl -sI https://inonda.homes)"
  ],
  "ask": ["Bash(wasmer deploy:*)", "Bash(wasmer login:*)"],
  "deny": [
    "Bash(wasmer app create:*)", "Bash(wasmer app delete:*)",
    "Bash(wasmer app remove:*)", "Bash(wasmer domain:*)"
  ]
}
```

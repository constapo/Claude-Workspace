# Security baseline — all surfaces

A starting checklist for hardening and detection across every surface, with the skill that
does the deep work on each. Work it per real system: point the matching `defend-*` skill at
an actual asset (code, config, or logs) and it produces findings and detection rules.

Rule that governs all of this: everything here runs against assets you own or are explicitly
authorized to test. Studying attacker techniques is for detecting and stopping them.

## 0. Telemetry first (nothing below works without it)
Detection needs data. Before anything else, confirm each surface is actually logging:
- Endpoints: Sysmon (Windows) or auditd/eBPF (Linux), PowerShell script-block logging, EDR.
- Identity/AD: domain-controller security logs (4768/4769/4624/4625/4728…), Entra sign-in logs.
- Cloud: CloudTrail / Azure Activity / GCP Audit, delivered to a store you control.
- Web: app, WAF, and proxy/access logs with the authenticated identity on each request.
A surface with no telemetry is the first finding — fix the blind spot before writing rules.

## 1. Web & APIs → `defend-web`
- [ ] Authorization enforced server-side on every object, by identity (no trust in client ids/roles)
- [ ] Parameterized queries everywhere; untrusted input never concatenated into an interpreter
- [ ] Strong password hashing, MFA, rate-limit + lockout, secure session tokens
- [ ] Outbound allow-list + metadata/link-local blocked (SSRF)
- [ ] Dependencies pinned and scanned (SCA); hardened headers (CSP, HSTS); no debug in prod
- [ ] Detections: auth brute-force/spray, access-control violations, injection metacharacters

## 2. Identity / Active Directory → `defend-active-directory`
- [ ] Tier-0 accounts never log on to workstations/servers
- [ ] No standing Domain Admin; just-in-time elevation; shadow-admin audit
- [ ] LAPS, Credential Guard, gMSA for service accounts, no unconstrained delegation
- [ ] SMB signing, LDAP channel binding, NTLM reduced, MFA on privileged/remote access
- [ ] Detections: Kerberoasting (4769 RC4), DCSync by non-DC, pass-the-hash, new privileged members

## 3. Cloud (AWS/Azure/GCP) → `defend-cloud`
- [ ] MFA on all humans; no long-lived keys (short-lived roles/workload identity); rotate+vault
- [ ] Least-privilege IAM; no wildcard admin; privilege-escalation paths reviewed
- [ ] No public storage/services by default; IMDSv2 / metadata protection on
- [ ] Guardrails: SCPs/org policies, config rules, drift detection
- [ ] Detections: key use from new origin, IAM policy changes, public exposure, logging tampering

## 4. Endpoints & servers → `defend-endpoint`
- [ ] Prompt patching; local admin removed; application control / allow-listing
- [ ] Egress filtering + DNS logging; EDR tamper-protected
- [ ] Detections: Office/browser spawning shells, new service/task/autorun, log clear (1102),
      beaconing and DNS tunnelling

## 5. Standing practice → `detection-engineering` + `threat-hunting`
- [ ] Every technique that matters is mapped to MITRE ATT&CK with a detection in a `detections/` backlog
- [ ] Each detection has false-positive tuning and a response step
- [ ] Regular hypothesis-driven hunts for what the rules miss; findings become new rules
- [ ] An incident-response playbook exists (scope → contain → eradicate → recover → write-up)

## Repo self-check (done 2026-10-22)
This repo's own scripts were reviewed: `tools/higgsfield/hf.py`, the hook scripts, and
`inonda-youtube-videos/higgsfield/v01-scene1.sh`. Credentials come from environment variables,
with no hardcoded secrets, no `shell=True`/`eval`/`os.system`, and no TLS verification disabled.
Clean. Re-run this review whenever those scripts change.

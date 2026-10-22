---
name: defend-web
description: Harden and monitor web applications and APIs against the common attack classes (injection, broken access control, auth flaws, SSRF, deserialization, misconfiguration, dependency and supply-chain risk). Use when reviewing your own web app or API for these weaknesses, writing detections for web attacks, building WAF/input-validation/authz controls, or mapping OWASP Top 10 to defences. Defensive: it finds and fixes weaknesses in systems you own or are authorized to test, and writes detections — it is not a tool for attacking third-party sites.
---

# Defending web applications

Work the OWASP Top 10 as a checklist of what to prevent, detect, and test on your own app.

## By attack class — prevent, then detect

- **Broken access control (IDOR, privilege escalation).** Prevent: enforce authorization
  server-side on every object by the authenticated identity, never trust a client-supplied
  id or role. Detect: alert on a user accessing object ids outside their own range, or
  403-storms that turn into a 200.
- **Injection (SQL, NoSQL, command, LDAP).** Prevent: parameterized queries / prepared
  statements, allow-list input, never concatenate untrusted input into an interpreter.
  Detect: WAF and app logs for interpreter metacharacters in fields that should never carry
  them; DB errors spiking.
- **Authentication flaws.** Prevent: strong hashing (argon2/bcrypt), MFA, rate limiting and
  lockout, secure session tokens, no credentials in URLs. Detect: brute force (T1110) — many
  failures then a success, impossible-travel logins, password-spray (one password across
  many accounts).
- **SSRF.** Prevent: allow-list outbound destinations, block link-local/metadata ranges,
  resolve-and-pin DNS. Detect: app making requests to internal/metadata IPs.
- **Insecure deserialization / dependency risk.** Prevent: avoid deserializing untrusted
  data; pin and scan dependencies (SCA), verify integrity. Detect: SCA alerts, unexpected
  child processes from the app runtime.
- **Security misconfiguration.** Prevent: hardened headers (CSP, HSTS), no debug in prod,
  least-privilege service accounts, secrets in a vault not code. Detect: config drift scans.

## Method

1. Read the app's real routes, auth model, and data access — work from the code, not guesses.
2. For each endpoint, check the relevant classes above against what the code actually does.
3. Report findings most-severe first, each with the concrete fix in this codebase's style.
4. For each class, add the detection (log source + rule) via the detection-engineering skill.
5. Verify fixes against your own running instance only (see webapp-testing), never a third
   party's.

Pairs with: detection-engineering (rules), defend-endpoint and defend-cloud (where the app
runs), and the repo's existing security scanners.

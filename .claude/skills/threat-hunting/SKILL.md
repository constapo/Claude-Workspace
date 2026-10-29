---
name: threat-hunting
description: Proactively hunt for signs of compromise in your own environment and run incident response when something is found. Use for hypothesis-driven hunts across logs/EDR/cloud-audit data, triaging an alert, scoping an incident, or building a response playbook. Complements detection-engineering (which writes the standing rules); hunting looks for what the rules missed. Defensive: it searches data from systems you own or are authorized to monitor — not a tool for attacking others.
---

# Threat hunting & incident response

Detections are standing tripwires. Hunting is the active search for an attacker who didn't
trip one, driven by a hypothesis rather than an alert.

## Hunting loop

1. **Hypothesis.** Start from a technique or an assumption: "if an attacker had a foothold,
   there would be beaconing to a new domain", "a Kerberoastable service account would have
   been requested with RC4". Base it on ATT&CK and what your environment is exposed to.
2. **Data.** Identify the telemetry that would show it (see the defend-* skills for which
   source records which technique). No data → that is itself a finding: a blind spot.
3. **Search.** Query for the behaviour's invariant, then reduce to anomalies against a
   baseline (new, rare, out-of-pattern by host/account/time/volume).
4. **Triage.** For each hit decide benign / suspicious / malicious, with the evidence. Pivot
   on anything malicious to find the full scope (same host, same account, same C2).
5. **Turn findings into detections.** Anything worth hunting twice becomes a standing rule
   via detection-engineering. The hunt feeds the backlog.

## If you find an active intrusion — response

Follow a calm playbook, not reflex:

1. **Scope before you act.** Identify every affected host, account and credential. Acting on
   one and missing the rest tips the attacker off and loses the others.
2. **Contain.** Isolate hosts, disable/rotate compromised credentials and keys, block C2.
   Preserve evidence (memory, disk, logs) before wiping if the incident may matter later.
3. **Eradicate & recover.** Remove persistence, patch the entry vector, restore from known-
   good, re-image where trust can't be established.
4. **Post-incident.** Write it up — timeline, root cause, what detection would have caught it
   earlier — and add that detection. Use the repo's `rca` skill for the report.

## Principles

- Hunt the invariant, pivot on identity, and always baseline.
- A blind spot (missing telemetry) is a finding, not a dead end.
- Every hunt either finds something or becomes a new detection — never wasted.
- Only ever query and act on systems you own or are authorized to monitor.

Pairs with: detection-engineering, defend-web / defend-active-directory / defend-cloud /
defend-endpoint, and `rca` for the write-up.

---
name: detection-engineering
description: Core purple-team skill — turn an attacker technique into a reliable defence. Use when the user wants to understand how an attack class works in order to detect, alert on, and mitigate it on their own systems, map activity to MITRE ATT&CK, write detection rules (Sigma/EDR/SIEM queries), reduce false positives, or build a detection backlog. Pair with defend-web, defend-active-directory, defend-cloud, defend-endpoint, and threat-hunting for surface-specific work. Defensive only: it studies attacker TTPs to beat them, never to carry them out — any live testing of a technique needs a specific authorized, scoped engagement.
---

# Detection engineering

The point of knowing an attack is to make it loud and cheap to catch. Every technique
leaves evidence somewhere: a log line, a process tree, a network flow, an auth event.
Detection engineering is the discipline of turning that evidence into a reliable alert.

## The loop

For any attacker technique the user names:

1. **Understand the mechanism, at the level defence needs.** How does the technique
   actually work, what does it touch, and what must be true for it to succeed? Explain it
   plainly — enough to defend, without writing a runnable weapon.
2. **Map it to MITRE ATT&CK.** Give the tactic and technique ID (e.g. T1110 Brute Force,
   T1048 Exfiltration Over Alternative Protocol). This anchors the detection to a shared
   language and lets the user track coverage.
3. **Find the telemetry.** Name the exact data source that records it: Windows Security
   event IDs, Sysmon, EDR process/network events, cloud audit logs (CloudTrail, Azure
   Activity, GCP Audit), web/proxy logs, auth logs, DNS. If the telemetry isn't being
   collected, that gap is the first finding.
4. **Write the detection.** Produce a concrete rule — a Sigma rule, a SIEM query (KQL,
   SPL, Elastic), or an EDR query. Make the logic match the technique's invariant (the
   thing the attacker can't avoid doing), not a single tool's string.
5. **Estimate false positives and tune.** Say what legitimate activity looks the same,
   and how to scope it out (asset, account, time, baseline). A noisy rule gets muted and
   is worse than none.
6. **Add the mitigation.** Detection catches it after; a control stops it before. Give the
   hardening change too (config, policy, segmentation, least privilege).
7. **Record coverage.** Log the technique ID, data source, rule, FP notes and mitigation
   so the user builds a living detection backlog and can see their ATT&CK coverage map.

## Principles

- **Detect the invariant, not the signature.** Tool names and payload strings change;
  the underlying behaviour (a service account authenticating from a workstation, a process
  spawning a shell, mass reads of a data store) is far more stable. Alert on the latter.
- **Layer: prevent, detect, respond.** No single rule is unbeatable. Aim for defence in
  depth where evasion of one layer trips another.
- **Baseline first.** You can't spot anomalous without knowing normal. Many detections are
  "this, but from somewhere/someone/at a time it has never happened before".
- **Every detection needs a response.** An alert nobody can action is noise. Pair each with
  a triage step and, where safe, an automated containment.
- **Test on your own assets only.** To validate a detection you may need to reproduce the
  technique. Do that solely against systems the user owns or is explicitly authorized to
  test, as a scoped exercise — never as a standing capability and never against third
  parties.

## Output

A detection-engineering answer gives: the technique explained for defence, its ATT&CK ID,
the telemetry to collect, a ready detection rule, false-positive tuning, and the preventive
control. Offer to append it to a `detections/` backlog in the repo so coverage accumulates.

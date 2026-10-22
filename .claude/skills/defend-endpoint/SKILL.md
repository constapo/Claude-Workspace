---
name: defend-endpoint
description: Harden and monitor endpoints and servers (Windows, Linux, macOS) against common attacker techniques — initial execution, persistence, privilege escalation, defense evasion, and command-and-control. Use when hardening your own hosts, configuring EDR/logging, writing process-tree and network detections, or mapping host techniques to MITRE ATT&CK defences. Defensive: it secures hosts you own or administer and writes detections — not a tool for attacking others' machines.
---

# Defending endpoints

Most host intrusions show up as an unusual process tree, a new persistence entry, or a
beacon. Collect the right telemetry and these become obvious.

## Telemetry to collect first

Without data there are no detections. Ensure: Sysmon (Windows) or auditd/eBPF (Linux) for
process, network and file events; EDR if available; PowerShell script-block and module
logging; command-line auditing. Missing telemetry is the first finding.

## By tactic — prevent and detect

- **Execution (T1059).** Prevent: application control / allow-listing, block script hosts
  for users who don't need them, macro controls. Detect: Office or a browser spawning a
  shell/script interpreter; encoded command lines.
- **Persistence (T1547, T1053, T1543).** Prevent: restrict who can create services and
  scheduled tasks. Detect: new service (7045), new scheduled task, new autorun/registry run
  key, new cron/systemd unit, new launch agent.
- **Privilege escalation (T1068, T1548).** Prevent: patch promptly, remove local admin,
  UAC enforced, sudo tightly scoped. Detect: token manipulation, unusual setuid execution,
  a process suddenly running as SYSTEM/root.
- **Defense evasion (T1562, T1070).** Prevent: protect/ tamper-guard the EDR and log
  pipeline. Detect: security services stopped, event log cleared (1102), Sysmon unloaded —
  treat tampering as high severity.
- **Command & control (T1071, T1572).** Prevent: egress filtering, DNS logging, proxy.
  Detect: beaconing (regular small outbound at fixed intervals), long connections to new
  domains, DNS tunnelling (high-entropy subdomains, large TXT volume).

## Method

1. Confirm what telemetry the host actually produces; flag gaps.
2. Review hardening (patching, local admin, app control, egress) against what's in place.
3. Report findings most-severe first with the concrete change.
4. For each technique add the detection (Sysmon/auditd/EDR rule) via detection-engineering.
5. Reproduce a technique to test a rule only on your own hosts or an authorized, scoped lab.

Pairs with: detection-engineering, defend-active-directory, threat-hunting.

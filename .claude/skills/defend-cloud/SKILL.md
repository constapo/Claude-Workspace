---
name: defend-cloud
description: Harden and monitor cloud environments (AWS, Azure, GCP) against common attacker techniques — identity and key abuse, privilege escalation through IAM, public exposure of storage and services, metadata/SSRF, persistence, and data exfiltration. Use when reviewing your own cloud account for misconfiguration, writing detections from cloud audit logs, tightening IAM, or mapping cloud attacks to MITRE ATT&CK defences. Defensive: it secures accounts you own or administer and writes detections — not a tool for attacking others' tenants.
---

# Defending cloud environments

Cloud compromise is overwhelmingly identity, keys, and misconfiguration — not kernel
exploits. Defence is least privilege, no public exposure by default, and reading the audit
log well.

## Core controls (prevent)

- **Identity first.** MFA on all humans, no long-lived access keys (use short-lived
  roles / workload identity), rotate and vault any key that must exist. Remove unused
  principals and keys.
- **Least-privilege IAM.** No wildcard `*` actions/resources on broad principals. Watch
  for privilege-escalation paths (a role that can edit its own or others' policies,
  pass-role to a more privileged role). Review these explicitly — they are the cloud
  equivalent of a shadow admin.
- **No public by default.** Block public S3/blob/GCS unless deliberate; restrict security
  groups/NSGs; private endpoints over public where possible.
- **Protect the metadata service.** Enforce IMDSv2 (AWS) / equivalent, so an app-layer SSRF
  can't mint credentials.
- **Guardrails.** Organization policies / SCPs, config rules, and drift detection so a
  misconfiguration is caught automatically.

## By technique — detect (from the audit log)

- **Credential/key abuse (T1078).** Detect: API calls from new IPs/regions/ASNs for a
  principal, use of a key outside its normal pattern, console login without MFA.
- **IAM privilege escalation (T1098).** Detect: `PutUserPolicy`, `AttachRolePolicy`,
  `CreateAccessKey`, `UpdateAssumeRolePolicy` by unexpected principals.
- **Public exposure / exfiltration (T1530, T1537).** Detect: bucket ACL/policy made public,
  snapshots/AMIs shared to external accounts, large or unusual data reads/egress.
- **Persistence (T1136).** Detect: new users/roles, new identity providers, new access keys
  on existing users.
- **Defense evasion.** Detect: CloudTrail/Activity-log/Audit-log stopped, deleted, or its
  delivery changed — treat logging tampering as high severity.

## Method

1. Enumerate identities, keys, public exposure and risky IAM in the account (read-only).
2. Report findings most-severe first with the exact fix (policy/config change).
3. For each technique add the detection (audit-log query/rule) via detection-engineering.
4. Test only against accounts you own or are authorized, as a scoped exercise.

The AWS MCP tools in this environment can read account state (read-only) when you need live
data. Pairs with: detection-engineering, defend-web (app running in cloud), threat-hunting.

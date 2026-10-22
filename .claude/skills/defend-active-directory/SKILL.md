---
name: defend-active-directory
description: Harden and monitor Active Directory and identity infrastructure against common attacker techniques (credential theft, Kerberoasting, pass-the-hash/ticket, DCSync, privilege escalation, lateral movement, persistence). Use when hardening your own AD/Entra environment, writing detections for identity attacks, reviewing tiering and privileged access, or mapping these techniques to MITRE ATT&CK defences. Defensive: it secures directories you own or administer and writes detections — not a tool for attacking others' environments.
---

# Defending Active Directory & identity

AD compromise is usually identity abuse, not an exploit. Defence is tiering, least
privilege, and watching authentication closely.

## Core controls (prevent)

- **Tiered admin model.** Tier 0 (domain controllers, AD admins) accounts never log on to
  workstations or servers. This single control defeats most lateral-movement-to-DA paths.
- **Least privilege.** Remove standing Domain Admin membership; use just-in-time elevation.
  Audit nested group membership and shadow admins.
- **Protect credentials.** Credential Guard, LAPS for local admin passwords, disable
  unconstrained delegation, strong service-account passwords (or gMSA) to blunt Kerberoasting.
- **Harden authentication.** Enforce SMB signing and LDAP channel binding, disable NTLM where
  possible, require MFA on privileged and remote access.

## By technique — detect

Map each to ATT&CK and the telemetry that catches it:

- **Kerberoasting (T1558.003).** Detect: event 4769 (TGS request) with RC4 encryption for
  service accounts, especially many SPNs requested fast by one account.
- **Pass-the-hash / pass-the-ticket (T1550).** Detect: logon type 9, anomalous NTLM auth,
  tickets used from hosts the account never uses.
- **DCSync (T1003.006).** Detect: replication (directory service access, GUID
  1131f6aa-…) requested by a principal that is not a DC.
- **Golden/silver ticket.** Detect: TGTs with anomalous lifetimes, mismatched account
  domains, auth with no prior 4768.
- **Lateral movement / persistence.** Detect: new service installs (7045), scheduled tasks,
  WMI/PSRemoting from workstations, new privileged group membership (4728/4732/4756).

## Method

1. Review the tiering model, privileged group membership, delegation settings, and auth
   protocols actually in place.
2. Report gaps most-severe first with the concrete remediation.
3. For each technique add the detection (event source + rule) via detection-engineering.
4. Validate detections only in your own lab or an authorized, scoped exercise.

Pairs with: detection-engineering, defend-endpoint, defend-cloud (for Entra/hybrid),
threat-hunting.

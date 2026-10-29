# Notes sync: iPhone ↔ Zorin OS with Simplenote (free)

Simplenote is free on both devices and syncs automatically over the internet through your
free Simplenote account. It holds text only: no images or attachments.

## 1. iPhone
1. App Store → install **Simplenote** (by Automattic).
2. Open it → **Sign up** with your email → create a password. This free account is what syncs.
3. Optional: Settings → **Passcode** to lock the app.

## 2. Zorin OS
Use either method:

- **Software store:** open *Software* → search **Simplenote** → Install.
- **Terminal:** `sudo snap install simplenote`

Open Simplenote → **Log in** with the same email and password as on the iPhone.
Type a note on one device and it should appear on the other within a few seconds.

No install at all: **app.simplenote.com** works in Firefox or Chrome on Zorin.

## 3. Moving notes over from Apple Notes
Apple Notes has no bulk export and no Linux app. The easiest route is copy and paste on the PC,
where you have a keyboard:

1. On Zorin, open **icloud.com** in the browser → sign in with your Apple ID → **Notes**.
2. Open Simplenote next to it.
3. For each note: open it in iCloud → `Ctrl+A`, `Ctrl+C` → in Simplenote press `Ctrl+Shift+I`
   (new note) or click **+** → `Ctrl+V`.

What changes on the way:
- Images, drawings, scans and attachments do not come across (text only).
- Folders become **tags**: type a tag at the bottom of a note, e.g. `work`, `shopping`.
- Checklists paste as plain text. To make them tickable again, use `- [ ] item` lines.
- Locked Apple notes must be unlocked in iCloud before you can copy them.

If you have a few notes, doing it on the iPhone is fine too: open the note → select all → Copy
→ paste into a new Simplenote note.

## 4. Everyday use
- The first line of a note is its title.
- **Pin** important notes to keep them at the top.
- Turn on **Markdown** per note (note's ⋯ menu) for headings, bold and lists.
- You can edit offline; changes sync when you're back online.
- Every note keeps a **history** (⋯ → History), so you can restore an older version.

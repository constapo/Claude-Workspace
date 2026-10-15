# Video 01 – YouTube upload texts

**Full Bathroom Renovation in Cyprus: Old to New, Step by Step**

- Sources: `scripts/v01.md` (packaging section), `production/v01/narration.md` (§1–§11),
  `production/v01/lines.json` (final spoken English + Greek subtitles).
- Status: text only. Nothing uploaded or published, no credits spent. vidIQ was not used
  (not available in this session); titles were not scored.
- The final narration has **no price and no duration** (lines 10.4 and 10.5 were removed), so the
  description has none either. Do not add any number that is not a real Inonda figure.
- Picture = free stock footage that illustrates each step. It is **not an Inonda job**. The texts
  below say so and never call it "our bathroom", "this job" or a client's home.
- Voice = synthetic (TTS) English voice. Subtitles = Greek, burned in for the whole video.

## Placeholders – fill before upload

| Placeholder | Who fills it | Notes |
|---|---|---|
| `[ADD WHATSAPP NUMBER]` | **Owner** | The narration says "the number is in the description". Write it with country code, e.g. +357 … (format only). Appears in EN and GR descriptions and in the wa.me link. In the link use digits only, no `+`, no spaces (e.g. `https://wa.me/357XXXXXXXX`). |
| `[ADD WEBSITE OR DELETE LINE]` | Owner | Optional. If Inonda has no website/Facebook page yet, delete the whole line. |
| `{t:§1}` … `{t:§11}` | Main session | Section start times from `build/timeline.json`, format `M:SS`. `{t:§1}` **must be `0:00`**. |
| `{STOCK CREDITS}` | Main session | One line per clip from `stock/SOURCES.md` (title, author, site, licence, URL). |
| `{VOICE CREDIT}` | Main session | Confirm the TTS engine/voice actually used in the final build (current `make_voice.py`: Kokoro TTS, voice `am_michael`). |

---

## 1. Titles (≤ 60 characters, keyword first)

| # | Title | Chars | Note |
|---|---|---|---|
| **A – recommended** | **Bathroom Renovation in Cyprus: Old to New, Step by Step** | 55 | Script's working title with "Full" dropped so it fits comfortably; keyword "bathroom renovation Cyprus" first; promise matches the video exactly. |
| B | Bathroom Renovation in Cyprus: The Step Nobody Sees | 51 | Curiosity gap from the hook (waterproofing). Good for a later A/B "Test & compare". |
| C | Bathroom Renovation Step by Step: 6 Stages (Cyprus Guide) | 57 | Plain how-to; the video has exactly 6 numbered steps. |

Full working title "Full Bathroom Renovation in Cyprus: Old to New, Step by Step" is exactly 60 characters and is also allowed if the owner prefers it.

**Greek title (Studio → Languages → add Greek translation):**
Ανακαίνιση Μπάνιου στην Κύπρο: Από Παλιό σε Καινούργιο (54 chars)
Alternative: Ανακαίνιση Μπάνιου στην Κύπρο: Βήμα προς Βήμα (45 chars)

Do not use titles or thumbnails that suggest a real Inonda before/after (e.g. "We transformed this bathroom") – the footage is stock.

---

## 2. Description – English (default language)

Paste everything between the lines. Replace the placeholders first.

---

Planning a bathroom renovation in Cyprus? This guide walks you through a full bathroom renovation from old to new, step by step: survey and planning, strip-out, plumbing and electrics, waterproofing (the step nobody sees), tiling, and fixtures and finishing – plus what to ask before anyone picks up a hammer.

💬 WhatsApp Inonda Ltd: [ADD WHATSAPP NUMBER]
👉 Message us: https://wa.me/[ADD WHATSAPP NUMBER]
🌐 [ADD WEBSITE OR DELETE LINE]

Chapters
{t:§1} Cracked tiles, damp ceiling, slow drain
{t:§2} Who we are
{t:§3} Step 1: Survey and plan
{t:§4} Step 2: Strip-out
{t:§5} Quick pause
{t:§6} Step 3: Plumbing and electrics
{t:§7} Step 4: Waterproofing, the step nobody sees
{t:§8} Step 5: Tiling
{t:§9} Step 6: Fixtures and finish
{t:§10} Cost and time: why we quote in person
{t:§11} Wrap-up and how to contact us

Every bathroom is different. Cost and time depend on the size, the tiles, the fixtures and what is found behind the walls, so we don't guess on camera. We visit, listen to what you want, and give you a clear written quote, so you know what is included before work begins.

Inonda Ltd repairs, renovates and maintains homes and apartments across Cyprus: bathrooms, kitchens, damp treatment, painting, roofing and waterproofing. Have a bathroom, kitchen, damp wall or leaking terrace in mind? Send us a WhatsApp message and we'll talk it through.

Next video: turning an old Cyprus apartment into a modern rental. Subscribe so you don't miss it.

About this video
• Footage: illustrative stock footage, not an Inonda job. It shows the type of work described in each step, not a real Inonda project, client or result.
• Narration: AI-generated (synthetic) English voice.
• Subtitles: Greek.

Credits
{STOCK CREDITS}
Voice: {VOICE CREDIT}

#BathroomRenovation #Cyprus #Inonda

---

## 3. Description – Greek (Studio → Languages → Greek → Description)

---

Σκέφτεστε ανακαίνιση μπάνιου στην Κύπρο; Σε αυτόν τον οδηγό σας δείχνουμε βήμα βήμα μια πλήρη ανακαίνιση μπάνιου, από παλιό σε καινούργιο: αυτοψία και σχεδιασμός, ξήλωμα, υδραυλικά και ηλεκτρικά, στεγανοποίηση (το βήμα που δεν φαίνεται), πλακάκια, είδη υγιεινής και φινίρισμα – και τι να ρωτήσετε πριν πιάσει κανείς σφυρί.

💬 WhatsApp Inonda Ltd: [ADD WHATSAPP NUMBER]
👉 Στείλτε μας μήνυμα: https://wa.me/[ADD WHATSAPP NUMBER]
🌐 [ADD WEBSITE OR DELETE LINE]

Κεφάλαια
{t:§1} Σπασμένα πλακάκια, υγρασία, ντους που δεν αδειάζει
{t:§2} Ποιοι είμαστε
{t:§3} Βήμα 1: Αυτοψία και σχεδιασμός
{t:§4} Βήμα 2: Ξήλωμα
{t:§5} Μικρή παύση
{t:§6} Βήμα 3: Υδραυλικά και ηλεκτρικά
{t:§7} Βήμα 4: Στεγανοποίηση, το βήμα που δεν φαίνεται
{t:§8} Βήμα 5: Πλακάκια
{t:§9} Βήμα 6: Είδη υγιεινής και φινίρισμα
{t:§10} Κόστος και χρόνος: γιατί δίνουμε προσφορά επί τόπου
{t:§11} Κλείσιμο και επικοινωνία

Κάθε μπάνιο είναι διαφορετικό. Το κόστος και ο χρόνος εξαρτώνται από το μέγεθος, τα πλακάκια, τα είδη που θα διαλέξετε και από το τι θα βρεθεί πίσω από τους τοίχους, γι' αυτό δεν μαντεύουμε μπροστά στην κάμερα. Ερχόμαστε στον χώρο, ακούμε τι θέλετε και σας δίνουμε καθαρή γραπτή προσφορά, για να ξέρετε τι περιλαμβάνεται πριν ξεκινήσουμε.

Η Inonda Ltd κάνει επισκευές, ανακαινίσεις και συντήρηση σε σπίτια και διαμερίσματα σε όλη την Κύπρο: μπάνια, κουζίνες, αντιμετώπιση υγρασίας, βαψίματα, στέγες και στεγανοποιήσεις. Σκέφτεστε ένα μπάνιο, μια κουζίνα, έναν τοίχο με υγρασία ή μια ταράτσα που μπάζει νερά; Στείλτε μας μήνυμα στο WhatsApp και θα τα συζητήσουμε.

Επόμενο βίντεο: ένα παλιό διαμέρισμα στην Κύπρο γίνεται σύγχρονο διαμέρισμα για ενοικίαση. Κάντε εγγραφή για να μην το χάσετε.

Σχετικά με το βίντεο
• Πλάνα: ενδεικτικά πλάνα από ελεύθερες βιβλιοθήκες (stock), όχι δουλειά της Inonda. Δείχνουν το είδος της εργασίας σε κάθε βήμα, όχι πραγματικό έργο, πελάτη ή αποτέλεσμα της Inonda.
• Αφήγηση: συνθετική φωνή (AI) στα αγγλικά.
• Υπότιτλοι: ελληνικά.

Credits / Πηγές
{STOCK CREDITS}
Φωνή: {VOICE CREDIT}

#ΑνακαίνισηΜπάνιου #Κύπρος #Inonda

---

Note on chapters: YouTube reads chapters from the description in the viewer's language, so keep one chapter block per language version (as above). Do not paste both language blocks into the same description, or the second chapter list will be ignored/confusing. Rules: first time `0:00`, at least 3 chapters, each ≥ 10 s, times in ascending order (all 11 sections are ≥ 10 s in the narration plan; re-check against `build/timeline.json`). If §5 "Quick pause" is cut in the edit, delete its chapter line.

---

## 4. Tags (Studio → Tags, ≤ 500 characters total)

English:
bathroom renovation Cyprus, bathroom renovation step by step, full bathroom renovation, bathroom remodel, bathroom waterproofing, shower waterproofing, bathroom tiling, home renovation Cyprus, Inonda

Greek:
ανακαίνιση μπάνιου, ανακαίνιση μπάνιου Κύπρος, στεγανοποίηση μπάνιου, πλακάκια μπάνιου, ανακαίνιση σπιτιού Κύπρος

Locations:
Cyprus, Κύπρος, Limassol, Λεμεσός, Nicosia, Λευκωσία, Larnaca, Λάρνακα, Paphos, Πάφος

(The video names no city, so the cities are only tags for search; add or remove to match where Inonda actually works.)

---

## 5. Altered or synthetic content disclosure

Studio → Upload → Details → "Altered content" ("Does this content contain altered or synthetic media…?").

- **What is synthetic in this video:** the English narration is a text-to-speech (AI) voice. It is a generic voice, not a clone or imitation of any real person.
- **What is not synthetic:** the picture is real camera stock footage (not AI-generated), used as illustration; the Greek subtitles are a translation of the script.
- **Recommendation: answer "Yes".** YouTube's mandatory cases are realistic content a viewer could mistake for real (a real person appearing to say or do something, altered real events, realistic invented scenes); a generic TTS narrator is a borderline case, but the owner's rule (CLAUDE.md, EU AI Act transparency) is to disclose AI-generated audio, and ticking "Yes" costs nothing. The description also states "Narration: AI-generated (synthetic) English voice". (YouTube Help could not be opened from this environment to re-check the current wording; check the Studio text at upload.)
- **Separately and always:** the stock-footage disclaimer in the description ("illustrative stock footage, not an Inonda job"). If any AI-generated picture is ever added to this video, the "Yes" answer becomes mandatory and those shots need the on-screen "AI-generated" label.

---

## 6. Upload checklist (owner – nothing here is done automatically)

Before upload
- [ ] `[ADD WHATSAPP NUMBER]` filled in **both** descriptions and both wa.me links; link tested on a phone
- [ ] `[ADD WEBSITE OR DELETE LINE]` filled or the line deleted
- [ ] `{t:§1}`…`{t:§11}` replaced with real times (first = `0:00`), `{STOCK CREDITS}` and `{VOICE CREDIT}` filled
- [ ] No `[ADD …]` or `{…}` left anywhere (search the text before pasting)
- [ ] Every stock clip's licence allows commercial use on YouTube; attribution given where required (Wikimedia CC BY / CC BY-SA)
- [ ] Final video watched once in full: Greek subtitles on screen the whole time; no stock watermark; no shot that looks like a specific Inonda job
- [ ] Thumbnail 1280×720, < 2 MB, readable on a phone; real stock frame or own photo; no "our job" before/after claim (script ideas: "OLD TO NEW", "WHAT'S BEHIND THE WALL?", "DON'T SKIP THIS STEP")

In YouTube Studio
- [ ] Title: option A (or B/C); Greek title + Greek description added under Languages
- [ ] Description (EN) pasted; tags pasted
- [ ] Video language: English. Caption tracks: Greek (`el`) SRT uploaded (in addition to the burned-in subtitles), English SRT optional
- [ ] Category: Howto & Style. Audience: "No, it's not made for kids". Paid promotion: No
- [ ] Altered content: **Yes** (synthetic voice) – see section 5
- [ ] Video location: Cyprus
- [ ] End screen (last 5–20 s of §11): subscribe element + "next video" placeholder until video 02 exists
- [ ] Visibility: Unlisted first, owner checks the watch page on a phone, then Public

Open questions for the owner
- WhatsApp number (required) and website/social link (optional).
- §5 says the next video is "old apartment to modern rental" (video 02 is not made yet); keep the "Next video" line in the description or remove it until video 02 is published.

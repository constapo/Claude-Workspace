#!/usr/bin/env python3
"""Build lines.json (id, English for the voice, Greek for the subtitles) from narration.md.

Changes from narration.md, made for the owner's standing rules:
- 10.4 / 10.5 dropped: price and duration are not confirmed; never invent them.
- 11.5: no phone number on screen or in the voice; it says the number is in the description.
- 5.3: "in two weeks" not confirmed -> "soon".
- "Inonda" respelled for the TTS only, so it is pronounced ee-NON-da.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "narration.md"), encoding="utf-8").read()
en_part, gr_part = src.split("# ΕΛΛΗΝΙΚΗ ΑΦΗΓΗΣΗ")


def rows(text):
    out = {}
    for m in re.finditer(r"^\| (\d+\.\d+) \| (.+?) \|", text, re.M):
        t = re.sub(r"<break[^>]*>|`\[CONFIRM[^`]*`|\*\*", "", m.group(2)).strip()
        out.setdefault(m.group(1), re.sub(r"\s+", " ", t))
    return out


en, gr = rows(en_part.split("### Pronunciation notes")[0]), rows(gr_part.split("### Native-speaker")[0])
DROP = {"10.4", "10.5"}
EN_FIX = {
    "5.3": "Soon we're covering how to turn an old Cyprus apartment into a modern rental.",
    "11.5": "Message us on WhatsApp. The number is in the description, or use the link there, and we'll talk it through.",
}
GR_FIX = {
    "5.3": "Σύντομα θα δούμε πώς ένα παλιό διαμέρισμα στην Κύπρο γίνεται σύγχρονο διαμέρισμα για ενοικίαση.",
    "11.5": "Στείλτε μας μήνυμα στο WhatsApp. Ο αριθμός είναι στην περιγραφή, ή πατήστε τον σύνδεσμο εκεί, και θα τα συζητήσουμε.",
}
key = lambda i: tuple(int(x) for x in i.split("."))
lines = []
for i in sorted(en, key=key):
    if i in DROP:
        continue
    e, g = EN_FIX.get(i, en[i]), GR_FIX.get(i, gr.get(i))
    assert g, f"no Greek for {i}"
    assert "[ADD" not in e and "ΠΡΟΣΘΕΣΤΕ" not in g, i
    lines.append({"id": i, "en": e, "tts": e.replace("Inonda", "Ee-non-da"), "gr": g})
json.dump(lines, open(os.path.join(HERE, "lines.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(lines), "lines")

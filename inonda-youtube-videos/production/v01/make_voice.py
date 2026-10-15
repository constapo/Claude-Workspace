#!/usr/bin/env python3
"""Voice every line of lines.json with free local Kokoro TTS -> build/tts/<id>.wav + build/tts/durations.json.
Model files: ~/.cache/kokoro/kokoro-v1.0.onnx and voices-v1.0.bin (github.com/thewh1teagle/kokoro-onnx, model-files-v1.0).
"""
import json
import os
import sys

import soundfile as sf
from kokoro_onnx import Kokoro

HERE = os.path.dirname(os.path.abspath(__file__))
VOICE = sys.argv[1] if len(sys.argv) > 1 else "am_michael"
M = os.path.expanduser("~/.cache/kokoro")
out = os.path.join(HERE, "build", "tts")
os.makedirs(out, exist_ok=True)
k = Kokoro(f"{M}/kokoro-v1.0.onnx", f"{M}/voices-v1.0.bin")
durs = {}
for line in json.load(open(os.path.join(HERE, "lines.json"), encoding="utf-8")):
    wav = os.path.join(out, line["id"] + ".wav")
    samples, sr = k.create(line["tts"], voice=VOICE, speed=0.97, lang="en-us")
    sf.write(wav, samples, sr)
    durs[line["id"]] = round(len(samples) / sr, 3)
    print(line["id"], durs[line["id"]], flush=True)
json.dump(durs, open(os.path.join(out, "durations.json"), "w"), indent=1)
print("total", round(sum(durs.values()), 1), "s")

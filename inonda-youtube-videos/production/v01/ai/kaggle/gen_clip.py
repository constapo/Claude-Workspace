#!/usr/bin/env python3
"""Runs INSIDE a Kaggle notebook session (free GPU, internet on). Generates one short clip per
prompt in prompts.json with the open Wan text-to-video models (Apache-2.0, no watermark,
commercial use allowed) and writes MP4s + log.json to /kaggle/working.

Tries Wan 2.2 TI2V-5B first (better realism); falls back to Wan 2.1 T2V-1.3B if it does not fit
or fails on the GPU Kaggle gives us. Free: no paid service is called.
"""
import json
import os
import subprocess
import sys
import time
import traceback

subprocess.run([sys.executable, "-m", "pip", "install", "-q", "-U", "diffusers>=0.35", "transformers",
                "accelerate", "ftfy", "imageio", "imageio-ffmpeg"], check=True)

import torch  # noqa: E402
from diffusers import AutoencoderKLWan, WanPipeline  # noqa: E402
from diffusers.utils import export_to_video  # noqa: E402

GUARD = (" Shot on a real camera, natural imperfect lighting, realistic physics and textures, "
         "real-world scale, subtle handheld movement.")
NEGATIVE = ("CGI, 3D render, cartoon, illustration, painting, oversaturated colours, glowing light, "
            "slow-motion, warped hands, extra fingers, melting objects, garbled text, watermark, logo, "
            "subtitles, blurry, low quality, static frame")
OUT = "/kaggle/working"
HERE = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else "."

MODELS = [
    # (repo, height, width, frames, fps, steps, guidance)
    ("Wan-AI/Wan2.2-TI2V-5B-Diffusers", 704, 1280, 81, 24, 40, 5.0),
    ("Wan-AI/Wan2.1-T2V-1.3B-Diffusers", 480, 832, 81, 16, 40, 5.0),
]


def find_prompts():
    for root in (HERE, "/kaggle/input", "/kaggle/src", "."):
        for dp, _, files in os.walk(root):
            if "prompts.json" in files:
                return json.load(open(os.path.join(dp, "prompts.json")))
    raise SystemExit("prompts.json not found")


def load(repo):
    vae = AutoencoderKLWan.from_pretrained(repo, subfolder="vae", torch_dtype=torch.float32)
    pipe = WanPipeline.from_pretrained(repo, vae=vae, torch_dtype=torch.float16)
    pipe.enable_model_cpu_offload()
    if hasattr(pipe.vae, "enable_tiling"):
        pipe.vae.enable_tiling()
    return pipe


def main():
    cfg = find_prompts()
    log = {"gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "none",
           "vram_gb": round(torch.cuda.get_device_properties(0).total_memory / 2**30, 1)
           if torch.cuda.is_available() else 0, "clips": []}
    print(log, flush=True)
    for repo, h, w, n, fps, steps, cfg_scale in MODELS:
        try:
            t0 = time.time()
            pipe = load(repo)
            for clip in cfg["clips"]:
                t1 = time.time()
                frames = pipe(prompt=clip["prompt"] + GUARD, negative_prompt=NEGATIVE, height=h, width=w,
                              num_frames=n, num_inference_steps=steps, guidance_scale=cfg_scale,
                              generator=torch.Generator("cpu").manual_seed(42)).frames[0]
                name = f"{clip['id']}-{repo.split('/')[1]}.mp4"
                export_to_video(frames, os.path.join(OUT, name), fps=fps)
                log["clips"].append({"id": clip["id"], "file": name, "model": repo, "size": f"{w}x{h}",
                                     "seconds": round(n / fps, 1), "gen_minutes": round((time.time() - t1) / 60, 1),
                                     "prompt": clip["prompt"] + GUARD, "negative": NEGATIVE, "seed": 42})
                print(log["clips"][-1], flush=True)
            log["model_used"] = repo
            log["load_minutes"] = round((time.time() - t0) / 60, 1)
            break
        except Exception as e:  # out of memory / unsupported dtype -> next, smaller model
            log.setdefault("errors", []).append({"model": repo, "error": repr(e)[:500]})
            traceback.print_exc()
            torch.cuda.empty_cache()
    json.dump(log, open(os.path.join(OUT, "log.json"), "w"), indent=2)
    if not log["clips"]:
        raise SystemExit("no clip generated")


if __name__ == "__main__":
    main()

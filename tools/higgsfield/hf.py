#!/usr/bin/env python3
"""Higgsfield video generation CLI, used by the `higgsfield` agent.

Credentials: set HF_KEY="key-id:key-secret" (or HF_API_KEY + HF_API_SECRET).
Get them at https://cloud.higgsfield.ai/.

Commands:
  check                                  verify credentials and API reachability
  agent  "<brief>" [--image PATH] ...    run a Higgsfield Agent API turn (it picks the model)
  generate MODEL_ID --args JSON          call one model directly (e.g. a known video model id)
  upload PATH                            upload an image/video, print its URL
  status REQUEST_ID | result REQUEST_ID  inspect a direct-generation request

Every generated asset is downloaded to media/higgsfield/<timestamp>-<slug>/ with a
run.json recording the prompt, model and source URLs.
"""

import argparse
import datetime as dt
import json
import mimetypes
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

try:
    import httpx
    import higgsfield_client
    from higgsfield_client import SyncClient
except ImportError:
    sys.exit("Missing dependency: pip install -r tools/higgsfield/requirements.txt")

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_ROOT = REPO_ROOT / "media" / "higgsfield"
MEDIA_EXT = re.compile(r"\.(mp4|mov|webm|gif|png|jpe?g|webp|mp3|wav)$", re.I)


def has_credentials() -> bool:
    return bool(os.getenv("HF_KEY") or (os.getenv("HF_API_KEY") and os.getenv("HF_API_SECRET")))


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:40] or "run"


def new_run_dir(label: str) -> Path:
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    path = OUT_ROOT / f"{stamp}-{slugify(label)}"
    path.mkdir(parents=True, exist_ok=True)
    return path


def collect_urls(obj) -> list:
    """Find every http(s) URL in a nested result payload."""
    found = []
    if isinstance(obj, str):
        if obj.startswith(("http://", "https://")):
            found.append(obj)
    elif isinstance(obj, dict):
        for value in obj.values():
            found.extend(collect_urls(value))
    elif isinstance(obj, (list, tuple)):
        for value in obj:
            found.extend(collect_urls(value))
    return list(dict.fromkeys(found))


def download(urls, run_dir: Path) -> list:
    saved = []
    for i, url in enumerate(urls, 1):
        name = Path(urlparse(url).path).name or f"asset-{i}"
        if not MEDIA_EXT.search(name):
            name = f"asset-{i}{Path(name).suffix or ''}"
        target = run_dir / f"{i:02d}-{name}"
        try:
            with httpx.stream("GET", url, follow_redirects=True, timeout=300) as resp:
                resp.raise_for_status()
                if target.suffix == "":
                    ext = mimetypes.guess_extension(resp.headers.get("content-type", "").split(";")[0]) or ""
                    target = target.with_suffix(ext)
                with open(target, "wb") as fh:
                    for chunk in resp.iter_bytes():
                        fh.write(chunk)
            saved.append(str(target.relative_to(REPO_ROOT)))
        except httpx.HTTPError as exc:
            print(f"warning: could not download {url}: {exc}", file=sys.stderr)
    return saved


def write_record(run_dir: Path, record: dict) -> None:
    (run_dir / "run.json").write_text(json.dumps(record, indent=2, default=str))


def cmd_check(_args) -> int:
    if not has_credentials():
        print("FAIL: no credentials. Set HF_KEY (or HF_API_KEY + HF_API_SECRET).")
        return 1
    try:
        httpx.get("https://api.higgsfield.ai", timeout=15)
    except httpx.HTTPError as exc:
        print(f"FAIL: cannot reach api.higgsfield.ai ({exc}). Allow the host in the network policy.")
        return 1
    print("OK: credentials set and api.higgsfield.ai reachable.")
    return 0


def cmd_agent(args) -> int:
    client = SyncClient()
    message = args.brief
    for path in args.image or []:
        ext = Path(path).suffix.lstrip(".").lower() or "jpeg"
        url = client.agents.media.upload(Path(path).read_bytes(), extension=ext, type="image")
        message += f"\nReference image: {url}"
    if args.session:
        session_id = args.session
    else:
        session_id = client.agents.sessions.create().session_id
    print(f"session: {session_id}", file=sys.stderr)

    answer = args.answer
    result = client.agents.sessions.run(
        session_id,
        message,
        on_question=(lambda _q: answer) if answer else None,
        timeout=args.timeout,
    )
    run_dir = new_run_dir(args.brief)
    saved = download(result.asset_urls, run_dir)
    record = {
        "mode": "agent",
        "session_id": session_id,
        "brief": message,
        "status": result.status,
        "agent_text": result.text,
        "asset_urls": result.asset_urls,
        "files": saved,
    }
    write_record(run_dir, record)
    print(json.dumps(record, indent=2))
    return 0 if result.status == "completed" else 2


def cmd_generate(args) -> int:
    arguments = json.loads(args.args)
    result = higgsfield_client.subscribe(
        args.model,
        arguments=arguments,
        on_enqueue=lambda rid: print(f"request: {rid}", file=sys.stderr),
        on_queue_update=lambda st: print(f"status: {st}", file=sys.stderr),
    )
    urls = collect_urls(result)
    run_dir = new_run_dir(arguments.get("prompt", args.model))
    saved = download(urls, run_dir)
    record = {"mode": "generate", "model": args.model, "arguments": arguments,
              "result": result, "files": saved}
    write_record(run_dir, record)
    print(json.dumps(record, indent=2, default=str))
    return 0


def cmd_upload(args) -> int:
    print(higgsfield_client.upload_file(args.path))
    return 0


def cmd_status(args) -> int:
    print(higgsfield_client.status(request_id=args.request_id))
    return 0


def cmd_result(args) -> int:
    print(json.dumps(higgsfield_client.result(request_id=args.request_id), indent=2, default=str))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("check").set_defaults(func=cmd_check)

    p = sub.add_parser("agent", help="run a Higgsfield Agent API turn")
    p.add_argument("brief", help="full creative brief, including 'make a video' and specs")
    p.add_argument("--image", action="append", help="reference image to upload (repeatable)")
    p.add_argument("--session", help="continue an existing session id")
    p.add_argument("--answer", help="auto-answer any clarifying question the agent asks")
    p.add_argument("--timeout", type=int, default=1800, help="seconds to wait (default 1800)")
    p.set_defaults(func=cmd_agent)

    p = sub.add_parser("generate", help="call one model directly")
    p.add_argument("model", help="Higgsfield model id, e.g. bytedance/seedream/v4/text-to-image")
    p.add_argument("--args", required=True, help="JSON arguments for the model")
    p.set_defaults(func=cmd_generate)

    p = sub.add_parser("upload")
    p.add_argument("path")
    p.set_defaults(func=cmd_upload)

    for name, func in (("status", cmd_status), ("result", cmd_result)):
        p = sub.add_parser(name)
        p.add_argument("request_id")
        p.set_defaults(func=func)

    args = parser.parse_args()
    if args.command != "check" and not has_credentials():
        sys.exit("Higgsfield credentials missing: set HF_KEY or HF_API_KEY + HF_API_SECRET.")
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

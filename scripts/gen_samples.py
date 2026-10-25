#!/usr/bin/env python3
"""Generate live engine samples for the Olai site.

Runs the pure-Rust alai-engine over a fixed bilingual prompt set and writes
data/samples.json. Executed on GitHub Actions during every deploy.
"""
import json
import subprocess
import sys
import time
from datetime import datetime, timezone

model, tok_dir, out_path = sys.argv[1], sys.argv[2], sys.argv[3]

PROMPTS = [
    ("The three primary colors are", 32),
    ("The capital of France is", 32),
    ("7 times 8 is", 32),
    ("Once upon a time in a small Indian village", 40),
    ("வணக்கம்", 24),
    ("Water boils when", 24),
]

samples = []
for prompt, max_new in PROMPTS:
    t0 = time.time()
    r = subprocess.run(
        ["target/release/alai", "run", "--model", model, "--dir", tok_dir,
         "--prompt", prompt, "--max-new", str(max_new), "--temp", "0.3", "--seed", "7"],
        capture_output=True, text=True, timeout=600,
    )
    secs = time.time() - t0
    lines = [ln for ln in r.stdout.strip().splitlines() if ln.strip()]
    reply = []
    for ln in lines:
        if ln.startswith("["):
            break
        if "ready —" in ln:
            continue
        reply.append(ln)
    samples.append({
        "prompt": prompt,
        "reply": "\n".join(reply).strip() or ("(empty)" if r.returncode == 0 else f"(engine error: {r.stderr[-200:]})"),
        "max_new": max_new,
        "secs": round(secs, 2),
    })
    print(f"  ✓ {prompt!r} -> {len(reply)} lines in {secs:.1f}s", file=sys.stderr)

doc = {
    "model": "Olai-350M (LFM2.5 anchor ⊕ python-math LoRA ⊕ SmolLM2-360M assimilated)",
    "engine": "alai-engine — pure Rust, zero ML framework",
    "runner": "GitHub Actions ubuntu-latest",
    "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "sampler": "temp=0.3, seed=7, greedy-safe",
    "samples": samples,
}
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=1)
print(f"wrote {out_path} with {len(samples)} samples", file=sys.stderr)

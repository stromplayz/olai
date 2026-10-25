# NOTICE — model ancestry & licenses

Olai (ஓலை) model artifacts are **merge derivatives** of open-source checkpoints.
No training was performed; all weights originate from the sources below.

## Olai-350M (flagship, release `v0.2.0`)

| Source | Used for | License | Link |
|---|---|---|---|
| LiquidAI **LFM2.5-350M** | anchor weights (all tensors), tokenizer | LFM Open License v1.0 | https://huggingface.co/LiquidAI/LFM2.5-350M |
| hauser458b **python-lora** (merged: `python-math`) | task-delta donor (TIES λ=0.4) | LFM Open License v1.0 (LoRA on LFM2.5) | https://huggingface.co/hauser458b/python-lora |
| HuggingFaceTB **SmolLM2-360M-Instruct** | FFN subspace donor (approx-SVD rank-32, λ=0.05, 48 tensors) | Apache-2.0 | https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct |

## Research harvests (knowledge packs only, no shipped weights)

| Source | Status | License |
|---|---|---|
| LiquidAI LFM2-350M-Math, LFM2-350M-ENJP-MT | REA-fingerprinted; **excluded from merges** (cross-basin deltas 3.4× weight scale) | LFM Open License v1.0 |
| deepseek-ai DeepSeek-R1-Distill-Qwen-1.5B | 6 FFN tensors harvested via HTTP range requests; experimental assimilation only (not shipped) | MIT |
| google gemma-3-1b-it | **NOT used** — access request not approved (HTTP 403) | Gemma Terms of Use |
| Qwen Qwen2.5-0.5B-Instruct | config-level reference for the qwen2 family fingerprint | Apache-2.0 |

## Code

- This website and all Olai crates: MIT.
- Reference inspiration: https://github.com/morluto/rea (REA = "Reverse Engineer
  Anything" for binaries; our REA = "Recursive Extraction & Assimilation" for weights).

## License compliance notes

- LFM Open License v1.0: commercial use permitted below US$10M revenue; attribution
  preserved here. Merge derivatives are permitted as "Models" under the license.
- Apache-2.0 (SmolLM2): redistribution with license & notice preserved.
- The `.olai` pack contains quantized (I4_SYM) derivatives of the above tensors;
  provenance is recoverable from the merge recipe in the core repo (deterministic,
  seeded, SHA-256-verified inputs).

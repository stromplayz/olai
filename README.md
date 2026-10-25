# ஓலை Olai — The Palm-Leaf Intelligence

**India's edge AI, merged — not trained.** Two thousand years ago Tamil scholars
packed libraries onto dried *olai* palm leaves: compressed, portable, durable.
Olai does the same for edge AI — a 354.5M-parameter model assembled from the
already-trained weights of open-source giants, packed in the `.olai` format
(3.76× smaller than safetensors, binary directory parsed in 62 µs).

**This public repo is the website & lab. The model core lives in the private
[`olai-core`](https://github.com/stromplayz/olai-core) repo; every deploy of
this site pulls the flagship pack from its releases using an encrypted
`OLAI_PAT` Actions secret — the token never touches site code.**

## What you can do here

- **[The Lab](lab.html)** — run the real `.olai` parser (Rust → WebAssembly)
  against the genuine first megabyte of Olai-350M: CRC verification, binary
  directory walk, full 148-tensor inventory with quantization mix.
- **Live engine samples** — every deploy re-builds `alai-engine` from source on
  GitHub's runners and generates fresh completions (English + Tamil).
- **The story & benchmarks** — [index.html](index.html).

## The stack (all free, zero GPUs)

| Piece | Crate | What it does |
|---|---|---|
| `.olai` format | `olai` | 4096-aligned packets, 64-byte fixed-stride binary directory (FNV-1a hash lookup), native I4_SYM/I8_SYM quantization, per-packet CRC32 |
| REA | `rea` | Reverse-engineers any safetensors checkpoint into role-tagged knowledge packs; harvests tensors from any HF model via HTTP range requests; assimilates cross-architecture subspaces via approx-SVD projection |
| sangam | `sangam` | Same-basin merges: Soup, SLERP, TIES, DARE, DARE-TIES, Model Stock |
| engine | `alai-engine` | Pure-Rust LFM2 hybrid runtime (10 conv + 6 gated-attention blocks), no ML framework, no KV-cache history |
| browser | `olai-wasm` | The format reader compiled to a 30 KB wasm module with a C ABI |

## Merge recipe (Olai-350M flagship)

```
LFM2.5-350M (anchor, LFM Open License v1.0)
  ⊕ python-math LoRA donor          — TIES, density 0.9, λ 0.4   (same basin)
  ⊕ SmolLM2-360M FFN subspaces      — approx-SVD rank-32, λ 0.05 (cross-architecture)
  → pack → .olai (188.6 MB, 3.76× smaller)
```

Every input is SHA-256-verified against Hugging Face LFS oids; every merge step
is gated by live evals. We explicitly **rejected** cross-basin donors after
measuring their deltas at 3.4× weight scale (see the story section).

## Licenses & attribution

See [NOTICE.md](NOTICE.md). Site code: MIT. Merged weights are derivatives of
their upstream licenses, attribution preserved.

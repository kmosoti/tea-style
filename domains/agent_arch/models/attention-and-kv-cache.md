# Attention and KV Cache

## Purpose
Explain what attention does during inference and why KV cache is a first-order performance concern.

## Core claim
Attention enables token-to-token dependency modeling, but naive long-context inference grows expensive; KV cache shifts repeated work from recompute to memory.

## Definitions
- **Attention**: mechanism that computes weighted interactions between token representations.
- **K/V tensors**: cached key and value projections from prior tokens.
- **Prefill**: first pass over prompt tokens to build initial cache.
- **Decode step**: generation of one new token using existing cache.

## Mechanics
During autoregressive inference:
1. Prompt tokens run through layers (prefill).
2. Each layer produces key/value tensors per token.
3. Tensors are stored in KV cache.
4. For each new token, model reuses cached keys/values instead of recomputing old token projections.

Without cache, cost repeatedly includes prior context processing. With cache, decode work focuses on the new token plus attention over cached state.

## Why long context increases cost
Longer context increases:
- memory required for cached K/V tensors
- attention operations over larger token history
- bandwidth pressure moving cache through device memory

So long context affects both latency and memory headroom.

## Latency implications
- Prefill latency scales with prompt length.
- Decode latency scales with model size and active context window.
- KV cache reduces redundant compute and usually improves token throughput.

## Memory implications
KV cache consumes substantial VRAM/RAM for long contexts and larger batch sizes. Throughput tuning often becomes a memory-allocation problem before raw compute is saturated.

## Patterns
- Separate prefill and decode metrics when profiling.
- Use context limits and batching policies aligned with memory budgets.
- Evaluate cache strategy as part of serving design, not as an afterthought.

## Anti-patterns
- Reporting only average latency without prompt-length breakdown.
- Increasing max context without measuring memory impact.

## Examples
- A service can meet SLOs by capping max context and reserving memory for KV cache rather than only increasing GPU count.

## Related pages
- `transformer-inference-pipeline.md`
- `taxonomy.md`
- `../projects/local-model-lab.md`

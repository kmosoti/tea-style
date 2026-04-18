# Transformer Inference Pipeline

## Purpose
Explain the transformer inference path in practical engineering terms.

## Core claim
Inference is a staged pipeline from text normalization to token sampling; understanding each stage makes latency and quality tradeoffs explicit.

## Definitions
- **Tokenization**: mapping text into token IDs.
- **Logits**: unnormalized scores over vocabulary for the next token.
- **Sampling**: policy for selecting the next token from logits.

## Pipeline walkthrough
1. **Tokenization**
   - Input text is segmented into token IDs.
   - Token count, not character count, governs compute cost.
2. **Embedding lookup**
   - Each token ID maps to a vector in model space.
3. **Positional information**
   - Positional encoding/rotation injects order so identical tokens at different positions are distinguishable.
4. **Attention blocks**
   - Each layer computes context-aware representations by weighting prior tokens.
5. **MLP blocks**
   - Feed-forward layers transform representations and add non-linear capacity.
6. **Final projection to logits**
   - Hidden state at the last position projects to vocabulary scores.
7. **Sampling/decoding**
   - Sampling policy (e.g., temperature/top-p/greedy) chooses next token.
8. **Loop**
   - Chosen token is appended; process repeats until stop criteria.

## Why next-token prediction can still look like reasoning
The model is not executing symbolic proof steps by default. It is producing high-probability continuations conditioned on learned patterns. Structured prompts, tool use, and verification loops can make this behavior appear reasoned because they constrain continuation space.

## Patterns
- Measure and optimize per-stage bottlenecks (tokenization overhead, attention cost, sampling strategy).
- Keep decoding policy explicit in evaluations.

## Anti-patterns
- Treating inference as a single opaque step.
- Comparing model outputs without controlling sampling parameters.

## Examples
- In latency-sensitive endpoints, using smaller output limits and controlled sampling can reduce tail latency without changing model weights.

## Related pages
- `attention-and-kv-cache.md`
- `taxonomy.md`
- `../projects/local-model-lab.md`

# Model and System Taxonomy

## Purpose
Define the core model and system distinctions used in this repository.

## Core claim
Clear taxonomy prevents design mistakes caused by mixing model class, serving pattern, and agent behavior.

## Definitions
- **LLM**: model that maps token context to next-token probabilities.
- **Agent**: system that uses one or more models plus tools, memory, and control logic to complete tasks.
- **Dense model**: model where all parameters are active per token.
- **MoE model**: model where routing activates a subset of experts per token.

## LLM vs agent
- An LLM is a model component.
- An agent is an architecture that may include LLM(s), retrieval, tools, planning policy, and verification loops.

Treating an LLM as an agent hides system responsibilities such as state management and tool safety.

## Encoder/decoder classes
- **Encoder-only**: optimized for representation tasks (classification, embedding-style understanding).
- **Decoder-only**: optimized for autoregressive generation.
- **Encoder-decoder**: separate encode/decode stages; common in translation and sequence transduction workloads.

## Dense vs MoE
- **Dense**: simpler serving profile, predictable activation cost.
- **MoE**: lower per-token active compute at similar parameter scale, but adds routing complexity and load-balancing concerns.

## Multimodal vs text-only
- **Text-only**: token input/output limited to text channels.
- **Multimodal**: combines text with one or more non-text modalities (image, audio, video).

Multimodal capability is a model/property distinction, not an agent property by itself.

## Generator vs embedding model vs reranker
- **Generator**: produces sequences (responses, completions, structured drafts).
- **Embedding model**: maps content to vectors for retrieval and clustering.
- **Reranker**: scores query-document pairs to reorder candidate context.

In retrieval systems, embedding models retrieve candidates; rerankers improve ordering before generation.

## Patterns
- Separate model-role language from system-role language.
- Document serving and evaluation criteria per model role.

## Anti-patterns
- Calling any tool-using app an “agent” without architecture definition.
- Mixing embedding and generation benchmarks as if they were equivalent.

## Examples
- A local Q&A assistant can use:
  - embedding model for retrieval,
  - reranker for candidate ordering,
  - decoder-only generator for final answer.

## Related pages
- `transformer-inference-pipeline.md`
- `attention-and-kv-cache.md`
- `../projects/local-model-lab.md`

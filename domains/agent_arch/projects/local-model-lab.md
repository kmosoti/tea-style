# Local Model Lab

## Purpose
Provide a repeatable project for learning local model hosting, retrieval integration, and output quality controls.

## Core claim
A staged lab with explicit comparison criteria builds practical model engineering skill faster than ad hoc experimentation.

## Definitions
- **Baseline**: single local generator with no retrieval or tool loop.
- **RAG variant**: generator augmented with retrieval context.
- **Verifier variant**: retrieval + tools + output checking pass.

## Lab phases
### Phase 1: Bare model baseline
- Stand up one local decoder-only model.
- Run a fixed prompt set.
- Record latency, output quality notes, and failure patterns.

### Phase 2: Retrieval-enhanced variant
- Add embedding-based retrieval over a small local corpus.
- Inject top-k context into prompts.
- Compare answer grounding, hallucination rate, and latency versus baseline.

### Phase 3: Retrieval + tools + verifier variant
- Add one or more tools (e.g., calculator/search over local corpus metadata).
- Add a verifier pass (rule-based or model-based) that checks response support.
- Compare reliability gains and added cost/latency.

## Comparison criteria
Track for each phase:
- setup complexity
- median and tail latency
- quality against a small evaluation set
- hallucination/error categories
- operational stability (resource usage, failure modes)

## Expected artifacts
- short runbook for setup
- prompt/eval set used for comparison
- results table across phases
- concise retrospective on tradeoffs and recommended default configuration

## Patterns
- Keep model and evaluation set fixed while changing one major variable per phase.
- Record evidence in a consistent table format.

## Anti-patterns
- Changing model, prompts, and retrieval settings at once.
- Declaring improvement without measured comparison.

## Related pages
- `../models/taxonomy.md`
- `../models/transformer-inference-pipeline.md`
- `../models/attention-and-kv-cache.md`

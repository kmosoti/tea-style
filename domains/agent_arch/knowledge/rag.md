# RAG

Retrieval-augmented generation is a pattern for supplying external knowledge at runtime.

## Use when
- the model needs private, current, or large external knowledge
- direct tool calls are too coarse
- retrieval can improve answer grounding

## Do not assume
A vector database is not automatically required. Sometimes direct search, exact lookup, or curated context injection is enough.

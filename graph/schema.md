# TEA Doctrine Graph Schema

## Purpose
Define the generated graph model consumed by `tea-kb`.

## Core claim
The graph is a directed labeled property graph derived from authored Markdown/frontmatter.

## Node shape
```json
{
  "id": "note:evidence:systems-should-tell-on-themselves",
  "type": "note",
  "title": "Systems Should Tell on Themselves",
  "domain": "repo-wide",
  "status": "active",
  "concepts": ["evidence", "operability"],
  "path": "kb/notes/evidence/systems-should-tell-on-themselves.md",
  "source_hash": "..."
}
```

## Edge shape
```json
{
  "source": "note:evidence:systems-should-tell-on-themselves",
  "target": "note:state:observable-state",
  "type": "supports",
  "origin": "manual",
  "reason": "Both reduce operator guessing by exposing state."
}
```

## Chunk shape
```json
{
  "chunk_id": "chunk:note:evidence:systems-should-tell-on-themselves:core-claim",
  "node_id": "note:evidence:systems-should-tell-on-themselves",
  "path": "kb/notes/evidence/systems-should-tell-on-themselves.md",
  "heading": "Core claim",
  "text": "Good systems reduce guessing by exposing state...",
  "concepts": ["evidence", "operability"],
  "domain": "repo-wide",
  "node_type": "note",
  "outbound_edges": ["doctrine:repo:systems-should-tell-on-themselves"],
  "source_hash": "..."
}
```

## Related pages
- [docs/standards/graph-knowledge-base-standard.md](../docs/standards/graph-knowledge-base-standard.md)
- [docs/standards/generated-artifact-standard.md](../docs/standards/generated-artifact-standard.md)

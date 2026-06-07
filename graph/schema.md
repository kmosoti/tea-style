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
  "created": "2026-06-07",
  "updated": "2026-06-07",
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
  "created": "2026-06-07",
  "updated": "2026-06-07",
  "outbound_edges": ["doctrine:repo:systems-should-tell-on-themselves"],
  "source_hash": "..."
}
```

## Timeline event shape
```json
{
  "date": "2026-06-07",
  "event_type": "created",
  "node_id": "note:evidence:systems-should-tell-on-themselves",
  "node_type": "note",
  "title": "Systems Should Tell on Themselves",
  "domain": "repo-wide",
  "path": "kb/notes/evidence/systems-should-tell-on-themselves.md",
  "concepts": ["evidence", "operability"]
}
```

Timeline events are derived from source frontmatter. `created` emits a `created` event.
`updated` emits an `updated` event when it differs from `created`.

## Related pages
- [docs/standards/graph-knowledge-base-standard.md](../docs/standards/graph-knowledge-base-standard.md)
- [docs/standards/generated-artifact-standard.md](../docs/standards/generated-artifact-standard.md)

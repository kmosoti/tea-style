"""Generated graph artifact exporters."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from tea_kb.domain.enums import NodeType
from tea_kb.domain.models import KnowledgeEdge, KnowledgeGraph, KnowledgeNode
from tea_kb.graph.timeline import timeline_events
from tea_kb.io.artifact_writer import Artifact


def graph_jsonl_artifacts(graph: KnowledgeGraph) -> list[Artifact]:
    return [
        Artifact(Path("graph/generated/nodes.jsonl"), _nodes_jsonl(graph)),
        Artifact(Path("graph/generated/edges.jsonl"), _edges_jsonl(graph)),
        Artifact(Path("graph/generated/chunks.jsonl"), _chunks_jsonl(graph)),
        Artifact(Path("graph/generated/concepts.jsonl"), _concepts_jsonl(graph)),
        Artifact(Path("graph/generated/timeline.jsonl"), _timeline_jsonl(graph)),
    ]


def _nodes_jsonl(graph: KnowledgeGraph) -> str:
    records = [
        _node_record(node) for node in sorted(graph.nodes.values(), key=lambda item: item.id)
    ]
    return _jsonl(records)


def _edges_jsonl(graph: KnowledgeGraph) -> str:
    records = [
        {
            "source": str(edge.source),
            "target": str(edge.target),
            "type": edge.edge_type.value,
            "origin": edge.origin,
            "reason": edge.reason,
        }
        for edge in sorted(graph.edges, key=_edge_sort_key)
    ]
    return _jsonl(records)


def _chunks_jsonl(graph: KnowledgeGraph) -> str:
    records = [
        {
            "chunk_id": str(chunk.id),
            "node_id": str(chunk.node_id),
            "path": chunk.path.as_posix(),
            "heading": chunk.heading,
            "text": chunk.text,
            "concepts": [str(concept) for concept in chunk.concepts],
            "domain": chunk.domain,
            "node_type": chunk.node_type.value,
            "outbound_edges": [str(edge) for edge in chunk.outbound_edges],
            "source_hash": chunk.source_hash,
            "created": _date_value(chunk.created),
            "updated": _date_value(chunk.updated),
        }
        for chunk in graph.chunks
    ]
    return _jsonl(records)


def _concepts_jsonl(graph: KnowledgeGraph) -> str:
    records = [
        {
            "id": str(node.id),
            "name": node.title,
            "aliases": list(node.aliases),
            "status": node.status,
            "path": node.path.as_posix(),
            "created": _date_value(node.created),
            "updated": _date_value(node.updated),
        }
        for node in sorted(graph.nodes.values(), key=lambda item: item.id)
        if node.node_type == NodeType.CONCEPT
    ]
    return _jsonl(records)


def _timeline_jsonl(graph: KnowledgeGraph) -> str:
    records = [
        {
            "date": event.date.isoformat(),
            "event_type": event.event_type,
            "node_id": str(event.node_id),
            "node_type": event.node_type.value,
            "title": event.title,
            "domain": event.domain,
            "path": event.path.as_posix(),
            "concepts": [str(concept) for concept in event.concepts],
        }
        for event in timeline_events(graph)
    ]
    return _jsonl(records)


def _node_record(node: KnowledgeNode) -> dict[str, object]:
    return {
        "id": str(node.id),
        "type": node.node_type.value,
        "title": node.title,
        "domain": node.domain,
        "status": node.status,
        "concepts": [str(concept) for concept in node.concepts],
        "path": node.path.as_posix(),
        "source_hash": node.source_hash,
        "summary": node.summary,
        "created": _date_value(node.created),
        "updated": _date_value(node.updated),
    }


def _edge_sort_key(edge: KnowledgeEdge) -> tuple[str, str, str]:
    return (str(edge.source), edge.edge_type.value, str(edge.target))


def _jsonl(records: list[dict[str, object]]) -> str:
    return "".join(
        json.dumps(record, sort_keys=True, ensure_ascii=False) + "\n" for record in records
    )


def _date_value(value: date | None) -> str | None:
    return value.isoformat() if value is not None else None

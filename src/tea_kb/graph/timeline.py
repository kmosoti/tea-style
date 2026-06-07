"""Timeline views derived from graph node dates."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from tea_kb.domain.enums import NodeType
from tea_kb.domain.ids import ConceptId, NodeId
from tea_kb.domain.models import KnowledgeGraph, KnowledgeNode


@dataclass(frozen=True, slots=True)
class TimelineEvent:
    date: date
    event_type: str
    node_id: NodeId
    title: str
    node_type: NodeType
    domain: str
    path: Path
    concepts: tuple[ConceptId, ...]


def timeline_events(graph: KnowledgeGraph) -> tuple[TimelineEvent, ...]:
    events: list[TimelineEvent] = []
    for node in graph.nodes.values():
        if node.created is not None:
            events.append(_event_for_node(node, node.created, "created"))
        if node.updated is not None and node.updated != node.created:
            events.append(_event_for_node(node, node.updated, "updated"))
    return tuple(
        sorted(events, key=lambda item: (item.date.isoformat(), item.event_type, item.node_id))
    )


def major_concepts(graph: KnowledgeGraph, limit: int = 6) -> tuple[tuple[ConceptId, int], ...]:
    counts: Counter[ConceptId] = Counter(
        concept for node in graph.nodes.values() for concept in node.concepts
    )
    ranked = sorted(counts.items(), key=lambda item: (-item[1], str(item[0])))
    return tuple((concept, count) for concept, count in ranked[:limit] if count > 0)


def events_for_concept(
    events: tuple[TimelineEvent, ...], concept: ConceptId
) -> tuple[TimelineEvent, ...]:
    return tuple(event for event in events if concept in event.concepts)


def _event_for_node(node: KnowledgeNode, event_date: date, event_type: str) -> TimelineEvent:
    return TimelineEvent(
        date=event_date,
        event_type=event_type,
        node_id=node.id,
        title=node.title,
        node_type=node.node_type,
        domain=node.domain,
        path=node.path,
        concepts=node.concepts,
    )

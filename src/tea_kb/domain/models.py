"""Internal graph models."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from tea_kb.domain.enums import EdgeType, NodeType
from tea_kb.domain.ids import ChunkId, ConceptId, NodeId


@dataclass(frozen=True, slots=True)
class KnowledgeNode:
    id: NodeId
    title: str
    node_type: NodeType
    domain: str
    status: str
    concepts: tuple[ConceptId, ...]
    path: Path
    source_hash: str
    summary: str | None = None
    aliases: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class KnowledgeEdge:
    source: NodeId
    target: NodeId
    edge_type: EdgeType
    origin: str
    reason: str | None = None


@dataclass(frozen=True, slots=True)
class KnowledgeChunk:
    id: ChunkId
    node_id: NodeId
    path: Path
    heading: str
    text: str
    concepts: tuple[ConceptId, ...]
    domain: str
    node_type: NodeType
    outbound_edges: tuple[NodeId, ...]
    source_hash: str


@dataclass(frozen=True, slots=True)
class KnowledgeGraph:
    nodes: dict[NodeId, KnowledgeNode]
    edges: tuple[KnowledgeEdge, ...]
    chunks: tuple[KnowledgeChunk, ...]
    duplicate_ids: tuple[NodeId, ...] = ()
    source_paths: tuple[Path, ...] = ()
    section_names_by_node: dict[NodeId, tuple[str, ...]] = field(default_factory=dict)

    def outbound_edges(self, node_id: NodeId) -> tuple[KnowledgeEdge, ...]:
        return tuple(edge for edge in self.edges if edge.source == node_id)

    def inbound_edges(self, node_id: NodeId) -> tuple[KnowledgeEdge, ...]:
        return tuple(edge for edge in self.edges if edge.target == node_id)

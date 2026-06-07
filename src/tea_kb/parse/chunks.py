"""Chunk extraction."""

from __future__ import annotations

from pathlib import Path

from tea_kb.domain.enums import NodeType
from tea_kb.domain.ids import ChunkId, ConceptId, NodeId, slugify
from tea_kb.domain.models import KnowledgeChunk
from tea_kb.parse.sections import MarkdownSection


def build_chunks(
    *,
    node_id: NodeId,
    path: Path,
    sections: tuple[MarkdownSection, ...],
    concepts: tuple[ConceptId, ...],
    domain: str,
    node_type: NodeType,
    outbound_edges: tuple[NodeId, ...],
    source_hash: str,
) -> tuple[KnowledgeChunk, ...]:
    chunks: list[KnowledgeChunk] = []
    for section in sections:
        if section.level != 2 or not section.text:
            continue
        chunk_id = ChunkId(f"chunk:{node_id}:{slugify(section.heading)}")
        chunks.append(
            KnowledgeChunk(
                id=chunk_id,
                node_id=node_id,
                path=path,
                heading=section.heading,
                text=section.text,
                concepts=concepts,
                domain=domain,
                node_type=node_type,
                outbound_edges=outbound_edges,
                source_hash=source_hash,
            )
        )
    return tuple(chunks)

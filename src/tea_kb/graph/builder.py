"""Build the doctrine graph from Markdown source."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path

from tea_kb.boundary.frontmatter import ParsedDocument, parse_markdown_document
from tea_kb.domain.enums import EdgeType
from tea_kb.domain.ids import NodeId
from tea_kb.domain.models import KnowledgeEdge, KnowledgeGraph, KnowledgeNode
from tea_kb.errors import FrontmatterError
from tea_kb.io.markdown_reader import FileSystemMarkdownReader
from tea_kb.parse.chunks import build_chunks
from tea_kb.parse.sections import extract_sections, section_names
from tea_kb.reports.diagnostics import Diagnostic, Severity


@dataclass(frozen=True, slots=True)
class BuildResult:
    graph: KnowledgeGraph
    diagnostics: tuple[Diagnostic, ...]


def build_graph(root: Path) -> BuildResult:
    reader = FileSystemMarkdownReader()
    nodes: dict[NodeId, KnowledgeNode] = {}
    edges: list[KnowledgeEdge] = []
    chunks = []
    diagnostics: list[Diagnostic] = []
    duplicate_ids: list[NodeId] = []
    parsed_docs: list[ParsedDocument] = []
    source_paths: list[Path] = []
    edge_targets_by_source: dict[NodeId, list[NodeId]] = {}
    section_names_by_node: dict[NodeId, tuple[str, ...]] = {}

    for absolute_path, text in reader.read(root):
        relative = absolute_path.resolve().relative_to(root.resolve())
        source_paths.append(relative)
        try:
            parsed = parse_markdown_document(relative, text)
        except FrontmatterError as exc:
            diagnostics.append(
                Diagnostic(
                    severity=Severity.ERROR,
                    code="frontmatter-invalid",
                    message=str(exc),
                    path=relative.as_posix(),
                )
            )
            continue

        parsed_docs.append(parsed)
        source_hash = _source_hash(text)
        node = parsed.to_node(source_hash)
        if node.id in nodes:
            duplicate_ids.append(node.id)
            diagnostics.append(
                Diagnostic(
                    severity=Severity.ERROR,
                    code="duplicate-id",
                    message=f"duplicate node id: {node.id}",
                    path=relative.as_posix(),
                    node_id=str(node.id),
                )
            )
            continue
        nodes[node.id] = node
        section_names_by_node[node.id] = section_names(parsed.content)

        outbound_targets: list[NodeId] = []
        for edge_type, targets in parsed.metadata.edges.items():
            for target in targets:
                target_id = NodeId(target)
                outbound_targets.append(target_id)
                edges.append(
                    KnowledgeEdge(
                        source=node.id,
                        target=target_id,
                        edge_type=EdgeType(edge_type),
                        origin=parsed.metadata.origin.review.value,
                    )
                )
        edge_targets_by_source[node.id] = outbound_targets

    for parsed in parsed_docs:
        node = nodes.get(NodeId(parsed.metadata.id))
        if node is None:
            continue
        sections = extract_sections(parsed.content)
        chunks.extend(
            build_chunks(
                node_id=node.id,
                path=node.path,
                sections=sections,
                concepts=node.concepts,
                domain=node.domain,
                node_type=node.node_type,
                outbound_edges=tuple(edge_targets_by_source.get(node.id, [])),
                source_hash=node.source_hash,
                created=node.created,
                updated=node.updated,
            )
        )

    graph = KnowledgeGraph(
        nodes=nodes,
        edges=tuple(sorted(edges, key=lambda item: (item.source, item.edge_type, item.target))),
        chunks=tuple(sorted(chunks, key=lambda item: item.id)),
        duplicate_ids=tuple(duplicate_ids),
        source_paths=tuple(sorted(source_paths, key=lambda item: item.as_posix())),
        section_names_by_node=section_names_by_node,
    )
    return BuildResult(graph=graph, diagnostics=tuple(diagnostics))


def _source_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

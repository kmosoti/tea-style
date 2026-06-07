"""Graph validation."""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

import networkx as nx

from tea_kb.domain.enums import EdgeType, NodeType
from tea_kb.domain.ids import concept_id_for, is_valid_id
from tea_kb.domain.models import KnowledgeGraph
from tea_kb.graph.algorithms import to_networkx
from tea_kb.graph.builder import BuildResult
from tea_kb.reports.diagnostics import Diagnostic, Severity, ValidationReport

MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
NOTE_REQUIRED_SECTIONS = {"Core claim", "Why it matters", "Use this when", "Failure smell"}


def validate_build_result(result: BuildResult, root: Path) -> ValidationReport:
    diagnostics = list(result.diagnostics)
    graph = result.graph
    diagnostics.extend(_validate_ids(graph))
    diagnostics.extend(_validate_edge_targets(graph))
    diagnostics.extend(_validate_acyclic_edges(graph, EdgeType.DEPENDS_ON))
    diagnostics.extend(_validate_acyclic_edges(graph, EdgeType.SUPERSEDES))
    diagnostics.extend(_validate_markdown_links(graph, root))
    diagnostics.extend(_validate_orphans(graph))
    diagnostics.extend(_validate_dense_links(graph))
    diagnostics.extend(_validate_related_to_overuse(graph))
    diagnostics.extend(_validate_concept_notes(graph))
    diagnostics.extend(_validate_note_sections(graph))
    diagnostics.extend(_validate_proposed_edges(graph))
    return ValidationReport(tuple(diagnostics))


def _validate_ids(graph: KnowledgeGraph) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    for node in graph.nodes.values():
        if not is_valid_id(str(node.id)):
            diagnostics.append(
                Diagnostic(
                    severity=Severity.ERROR,
                    code="invalid-id",
                    message=f"invalid node id: {node.id}",
                    path=node.path.as_posix(),
                    node_id=str(node.id),
                )
            )
    return diagnostics


def _validate_edge_targets(graph: KnowledgeGraph) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    for edge in graph.edges:
        if edge.target not in graph.nodes:
            diagnostics.append(
                Diagnostic(
                    severity=Severity.ERROR,
                    code="invalid-edge-target",
                    message=f"{edge.source} -> {edge.target} target does not exist",
                    node_id=str(edge.source),
                )
            )
    return diagnostics


def _validate_acyclic_edges(graph: KnowledgeGraph, edge_type: EdgeType) -> list[Diagnostic]:
    nx_graph = nx.DiGraph()
    for edge in graph.edges:
        if edge.edge_type == edge_type:
            nx_graph.add_edge(str(edge.source), str(edge.target))
    try:
        cycle = nx.find_cycle(nx_graph)
    except nx.NetworkXNoCycle:
        return []
    return [
        Diagnostic(
            severity=Severity.ERROR,
            code=f"{edge_type.value}-cycle",
            message=f"{edge_type.value} cycle detected: {cycle}",
        )
    ]


def _validate_markdown_links(graph: KnowledgeGraph, root: Path) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    for relative in graph.source_paths:
        path = root / relative
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_PATTERN.finditer(text):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            if not resolved.exists():
                diagnostics.append(
                    Diagnostic(
                        severity=Severity.ERROR,
                        code="broken-markdown-link",
                        message=f"broken Markdown link: {target}",
                        path=relative.as_posix(),
                    )
                )
    return diagnostics


def _validate_orphans(graph: KnowledgeGraph) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    for node in graph.nodes.values():
        if node.node_type != NodeType.NOTE or node.status != "active":
            continue
        if not graph.inbound_edges(node.id) and not graph.outbound_edges(node.id):
            diagnostics.append(
                Diagnostic(
                    severity=Severity.WARNING,
                    code="orphan-active-note",
                    message=f"active note has no graph edges: {node.id}",
                    path=node.path.as_posix(),
                    node_id=str(node.id),
                )
            )
    return diagnostics


def _validate_dense_links(graph: KnowledgeGraph, threshold: int = 20) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    nx_graph = to_networkx(graph)
    for node_id in sorted(nx_graph.nodes):
        degree = nx_graph.in_degree(node_id) + nx_graph.out_degree(node_id)
        if degree > threshold:
            diagnostics.append(
                Diagnostic(
                    severity=Severity.WARNING,
                    code="dense-links",
                    message=f"{node_id} has {degree} total edges",
                    node_id=node_id,
                )
            )
    return diagnostics


def _validate_related_to_overuse(graph: KnowledgeGraph, threshold: int = 5) -> list[Diagnostic]:
    counts: defaultdict[str, int] = defaultdict(int)
    for edge in graph.edges:
        if edge.edge_type == EdgeType.RELATED_TO:
            counts[str(edge.source)] += 1
    return [
        Diagnostic(
            severity=Severity.WARNING,
            code="related-to-overuse",
            message=f"{node_id} uses related_to {count} times",
            node_id=node_id,
        )
        for node_id, count in sorted(counts.items())
        if count > threshold
    ]


def _validate_concept_notes(graph: KnowledgeGraph) -> list[Diagnostic]:
    concept_nodes = {
        str(node.id) for node in graph.nodes.values() if node.node_type == NodeType.CONCEPT
    }
    concept_checked_types = {NodeType.NOTE, NodeType.EXAMPLE, NodeType.ANTIPATTERN}
    used = sorted(
        {
            str(concept_id_for(str(concept)))
            for node in graph.nodes.values()
            if node.node_type in concept_checked_types
            for concept in node.concepts
        }
    )
    return [
        Diagnostic(
            severity=Severity.WARNING,
            code="missing-concept-note",
            message=f"concept appears but has no concept note: {concept_id}",
            node_id=concept_id,
        )
        for concept_id in used
        if concept_id not in concept_nodes
    ]


def _validate_note_sections(graph: KnowledgeGraph) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    for node in graph.nodes.values():
        if node.node_type != NodeType.NOTE:
            continue
        section_names = set(graph.section_names_by_node.get(node.id, ()))
        missing = sorted(NOTE_REQUIRED_SECTIONS - section_names)
        for section in missing:
            diagnostics.append(
                Diagnostic(
                    severity=Severity.WARNING,
                    code="missing-note-section",
                    message=f"{node.id} missing section: {section}",
                    path=node.path.as_posix(),
                    node_id=str(node.id),
                )
            )
    return diagnostics


def _validate_proposed_edges(graph: KnowledgeGraph) -> list[Diagnostic]:
    counts = Counter(str(edge.source) for edge in graph.edges if edge.origin == "proposed")
    return [
        Diagnostic(
            severity=Severity.WARNING,
            code="agent-proposed-edges",
            message=f"{node_id} has {count} proposed edge(s) requiring review",
            node_id=node_id,
        )
        for node_id, count in sorted(counts.items())
    ]

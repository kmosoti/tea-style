"""Markdown report rendering."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

from tea_kb.domain.enums import NodeType
from tea_kb.domain.ids import concept_id_for
from tea_kb.domain.models import KnowledgeGraph
from tea_kb.graph.timeline import events_for_concept, major_concepts, timeline_events
from tea_kb.io.artifact_writer import Artifact
from tea_kb.reports.diagnostics import ValidationReport


def report_artifacts(graph: KnowledgeGraph, report: ValidationReport) -> list[Artifact]:
    return [
        Artifact(Path("graph/generated/reports/health.md"), render_health_report(graph, report)),
        Artifact(Path("graph/generated/reports/orphan-notes.md"), render_orphan_notes(graph)),
        Artifact(Path("graph/generated/reports/dense-links.md"), render_dense_links(graph)),
        Artifact(
            Path("graph/generated/reports/duplicate-concepts.md"), render_duplicate_concepts(graph)
        ),
        Artifact(Path("graph/generated/reports/proposed-edges.md"), render_proposed_edges(graph)),
        Artifact(Path("graph/generated/reports/timeline.md"), render_timeline_report(graph)),
    ]


def render_health_report(graph: KnowledgeGraph, report: ValidationReport) -> str:
    type_counts = Counter(node.node_type.value for node in graph.nodes.values())
    degree_rows = _highest_degree_rows(graph)
    warning_lines = [f"- `{item.code}`: {item.message}" for item in report.warnings[:25]] or [
        "- None"
    ]
    return "\n".join(
        [
            "# TEA Graph Health",
            "",
            "## Summary",
            "",
            f"- Nodes: {len(graph.nodes)}",
            f"- Edges: {len(graph.edges)}",
            f"- Chunks: {len(graph.chunks)}",
            f"- Notes: {type_counts.get(NodeType.NOTE.value, 0)}",
            f"- Concepts: {type_counts.get(NodeType.CONCEPT.value, 0)}",
            f"- Antipatterns: {type_counts.get(NodeType.ANTIPATTERN.value, 0)}",
            f"- Errors: {len(report.errors)}",
            f"- Warnings: {len(report.warnings)}",
            "",
            "## Highest-degree nodes",
            "",
            "| Node | Inbound | Outbound |",
            "|---|---:|---:|",
            *degree_rows,
            "",
            "## Warnings",
            "",
            *warning_lines,
            "",
        ]
    )


def render_orphan_notes(graph: KnowledgeGraph) -> str:
    orphans = [
        node
        for node in graph.nodes.values()
        if node.node_type == NodeType.NOTE
        and node.status == "active"
        and not graph.inbound_edges(node.id)
        and not graph.outbound_edges(node.id)
    ]
    lines = ["# Orphan Notes", ""]
    if not orphans:
        lines.append("No orphan active notes detected.")
    else:
        lines.extend(
            f"- `{node.id}` - {node.path.as_posix()}"
            for node in sorted(orphans, key=lambda item: item.id)
        )
    lines.append("")
    return "\n".join(lines)


def render_dense_links(graph: KnowledgeGraph, threshold: int = 12) -> str:
    rows: list[str] = []
    for node in sorted(graph.nodes.values(), key=lambda item: item.id):
        inbound = len(graph.inbound_edges(node.id))
        outbound = len(graph.outbound_edges(node.id))
        if inbound + outbound > threshold:
            rows.append(f"| `{node.id}` | {inbound} | {outbound} |")
    lines = ["# Dense Links", "", "| Node | Inbound | Outbound |", "|---|---:|---:|"]
    lines.extend(rows or ["| None | 0 | 0 |"])
    lines.append("")
    return "\n".join(lines)


def render_duplicate_concepts(graph: KnowledgeGraph) -> str:
    concept_nodes = {
        str(node.id) for node in graph.nodes.values() if node.node_type == NodeType.CONCEPT
    }
    used = sorted(
        {
            str(concept_id_for(str(concept)))
            for node in graph.nodes.values()
            for concept in node.concepts
        }
    )
    missing = [concept for concept in used if concept not in concept_nodes]
    alias_index: defaultdict[str, list[str]] = defaultdict(list)
    for node in graph.nodes.values():
        if node.node_type == NodeType.CONCEPT:
            for alias in node.aliases:
                alias_index[alias.lower()].append(str(node.id))
    duplicate_aliases = {alias: ids for alias, ids in alias_index.items() if len(ids) > 1}

    lines = ["# Duplicate Concepts", ""]
    if duplicate_aliases:
        lines.extend(
            f"- `{alias}` appears in {', '.join(ids)}"
            for alias, ids in sorted(duplicate_aliases.items())
        )
    else:
        lines.append("No duplicate concept aliases detected.")
    lines.extend(["", "## Concepts without concept notes", ""])
    lines.extend(
        (f"- `{concept}`" for concept in missing),
    )
    if not missing:
        lines.append("- None")
    lines.append("")
    return "\n".join(lines)


def render_proposed_edges(graph: KnowledgeGraph) -> str:
    proposed = [edge for edge in graph.edges if edge.origin == "proposed"]
    lines = ["# Proposed Edges", ""]
    if not proposed:
        lines.append("No proposed edges detected.")
    else:
        lines.extend(
            f"- `{edge.source}` --{edge.edge_type.value}--> `{edge.target}`"
            for edge in sorted(
                proposed, key=lambda item: (item.source, item.edge_type, item.target)
            )
        )
    lines.append("")
    return "\n".join(lines)


def render_timeline_report(graph: KnowledgeGraph) -> str:
    events = timeline_events(graph)
    created = sum(1 for event in events if event.event_type == "created")
    updated = sum(1 for event in events if event.event_type == "updated")
    rows_by_date: defaultdict[str, list[str]] = defaultdict(list)
    for event in events:
        rows_by_date[event.date.isoformat()].append(str(event.node_id))

    lines = [
        "# Knowledge Timeline",
        "",
        "## Summary",
        "",
        f"- Timeline events: {len(events)}",
        f"- Created events: {created}",
        f"- Updated events: {updated}",
        f"- Dated nodes: {sum(1 for node in graph.nodes.values() if node.created or node.updated)}",
        "",
        "## Overall Growth",
        "",
        "| Date | Events | Nodes |",
        "|---|---:|---|",
    ]
    if rows_by_date:
        for date_value, node_ids in sorted(rows_by_date.items()):
            visible_nodes = ", ".join(f"`{node_id}`" for node_id in node_ids[:8])
            suffix = " ..." if len(node_ids) > 8 else ""
            lines.append(f"| {date_value} | {len(node_ids)} | {visible_nodes}{suffix} |")
    else:
        lines.append("| None | 0 | None |")

    lines.extend(["", "## Major Concept Timelines", ""])
    for concept, count in major_concepts(graph):
        concept_events = events_for_concept(events, concept)
        lines.extend(
            [
                f"### {concept}",
                "",
                f"{count} node(s) carry this concept.",
                "",
                "| Date | Event | Node | Type | Path |",
                "|---|---|---|---|---|",
            ]
        )
        for event in concept_events[:20]:
            lines.append(
                "| "
                f"{event.date.isoformat()} | "
                f"{event.event_type} | "
                f"`{event.node_id}` | "
                f"{event.node_type.value} | "
                f"{event.path.as_posix()} |"
            )
        if not concept_events:
            lines.append("| None | None | None | None | None |")
        lines.append("")
    return "\n".join(lines)


def _highest_degree_rows(graph: KnowledgeGraph, limit: int = 10) -> list[str]:
    rows: list[tuple[str, int, int]] = []
    for node in graph.nodes.values():
        inbound = len(graph.inbound_edges(node.id))
        outbound = len(graph.outbound_edges(node.id))
        rows.append((str(node.id), inbound, outbound))
    rows.sort(key=lambda item: (item[1] + item[2], item[0]), reverse=True)
    return [
        f"| `{node_id}` | {inbound} | {outbound} |" for node_id, inbound, outbound in rows[:limit]
    ]

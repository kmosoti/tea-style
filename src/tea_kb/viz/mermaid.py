"""Mermaid export helpers."""

from __future__ import annotations

from tea_kb.domain.models import KnowledgeGraph
from tea_kb.graph.algorithms import shortest_path


def render_path_mermaid(graph: KnowledgeGraph, source: str, target: str) -> str:
    path = shortest_path(graph, source, target)
    if not path:
        return "flowchart LR\n  missing[No path found]\n"
    lines = ["flowchart LR"]
    for index, node_id in enumerate(path):
        lines.append(f'  n{index}["{node_id}"]')
    for index in range(len(path) - 1):
        lines.append(f"  n{index} --> n{index + 1}")
    return "\n".join(lines) + "\n"

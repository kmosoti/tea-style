"""Graph algorithms."""

from __future__ import annotations

import networkx as nx

from tea_kb.domain.models import KnowledgeGraph


def to_networkx(graph: KnowledgeGraph) -> nx.DiGraph:
    nx_graph = nx.DiGraph()
    for node in graph.nodes.values():
        nx_graph.add_node(
            str(node.id),
            title=node.title,
            type=node.node_type.value,
            domain=node.domain,
            path=node.path.as_posix(),
        )
    for edge in graph.edges:
        nx_graph.add_edge(str(edge.source), str(edge.target), type=edge.edge_type.value)
    return nx_graph


def shortest_path(graph: KnowledgeGraph, source: str, target: str) -> list[str] | None:
    nx_graph = to_networkx(graph)
    try:
        return list(nx.shortest_path(nx_graph, source=source, target=target))
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        return None

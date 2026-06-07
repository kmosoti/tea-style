"""Deterministic HTML graph visualization.

The module name is kept for the planned PyVis integration boundary. The generated
artifact is intentionally deterministic for build --check.
"""

from __future__ import annotations

from html import escape
from pathlib import Path

from tea_kb.domain.models import KnowledgeGraph
from tea_kb.io.artifact_writer import Artifact


def overview_artifact(graph: KnowledgeGraph) -> Artifact:
    return Artifact(
        Path("graph/generated/visualizations/overview.html"), render_overview_html(graph)
    )


def render_overview_html(graph: KnowledgeGraph) -> str:
    node_rows = "\n".join(
        "<tr>"
        f"<td><code>{escape(str(node.id))}</code></td>"
        f"<td>{escape(node.node_type.value)}</td>"
        f"<td>{escape(node.domain)}</td>"
        f"<td><a href='../../../{escape(node.path.as_posix())}'>{escape(node.title)}</a></td>"
        "</tr>"
        for node in sorted(graph.nodes.values(), key=lambda item: item.id)
    )
    edge_rows = "\n".join(
        "<tr>"
        f"<td><code>{escape(str(edge.source))}</code></td>"
        f"<td>{escape(edge.edge_type.value)}</td>"
        f"<td><code>{escape(str(edge.target))}</code></td>"
        f"<td>{escape(edge.origin)}</td>"
        "</tr>"
        for edge in sorted(graph.edges, key=lambda item: (item.source, item.edge_type, item.target))
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>TEA Graph Overview</title>
  <style>
    :root {{
      color-scheme: light dark;
      --bg: #ffffff;
      --ink: #172033;
      --muted: #57606a;
      --line: #d0d7de;
      --head: #f6f8fa;
      --link: #0969da;
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{
        --bg: #0b1220;
        --ink: #e5edf7;
        --muted: #9aa8bd;
        --line: #334155;
        --head: #111827;
        --link: #60a5fa;
      }}
    }}
    body {{
      background: var(--bg);
      color: var(--ink);
      font-family: system-ui, sans-serif;
      margin: 2rem;
      line-height: 1.4;
    }}
    table {{ border-collapse: collapse; width: 100%; margin: 1rem 0 2rem; }}
    th, td {{ border: 1px solid var(--line); padding: 0.4rem 0.5rem; text-align: left; }}
    th {{ background: var(--head); }}
    code {{ white-space: nowrap; }}
    a {{ color: var(--link); }}
  </style>
</head>
<body>
  <h1>TEA Graph Overview</h1>
  <p>Nodes: {len(graph.nodes)}. Edges: {len(graph.edges)}. Chunks: {len(graph.chunks)}.</p>
  <h2>Nodes</h2>
  <table>
    <thead><tr><th>ID</th><th>Type</th><th>Domain</th><th>Source</th></tr></thead>
    <tbody>
{node_rows}
    </tbody>
  </table>
  <h2>Edges</h2>
  <table>
    <thead><tr><th>Source</th><th>Type</th><th>Target</th><th>Origin</th></tr></thead>
    <tbody>
{edge_rows}
    </tbody>
  </table>
</body>
</html>
"""

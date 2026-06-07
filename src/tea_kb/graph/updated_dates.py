"""Git-backed updated-date validation."""

from __future__ import annotations

import subprocess
from datetime import date
from pathlib import Path

from tea_kb.domain.models import KnowledgeGraph
from tea_kb.reports.diagnostics import Diagnostic, Severity


def validate_updated_dates_since(
    graph: KnowledgeGraph, root: Path, base_ref: str
) -> tuple[Diagnostic, ...]:
    changed = _changed_source_paths(graph, root, base_ref)
    diagnostics: list[Diagnostic] = []
    nodes_by_path = {node.path.as_posix(): node for node in graph.nodes.values()}
    for path in changed:
        node = nodes_by_path.get(path.as_posix())
        if node is None:
            continue
        latest_change = _latest_change_date(root, base_ref, path)
        if latest_change is None:
            continue
        if node.updated is None or node.updated < latest_change:
            diagnostics.append(
                Diagnostic(
                    severity=Severity.WARNING,
                    code="stale-updated-date",
                    message=(
                        f"{node.id} changed since {base_ref} but updated date "
                        f"{node.updated} is before {latest_change}"
                    ),
                    path=node.path.as_posix(),
                    node_id=str(node.id),
                )
            )
    return tuple(diagnostics)


def _changed_source_paths(graph: KnowledgeGraph, root: Path, base_ref: str) -> tuple[Path, ...]:
    source_paths = {path.as_posix() for path in graph.source_paths}
    completed = subprocess.run(
        ["git", "diff", "--name-only", base_ref, "HEAD", "--", *sorted(source_paths)],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    paths = [
        Path(line.strip()) for line in completed.stdout.splitlines() if line.strip() in source_paths
    ]
    return tuple(sorted(paths, key=lambda item: item.as_posix()))


def _latest_change_date(root: Path, base_ref: str, path: Path) -> date | None:
    completed = subprocess.run(
        ["git", "log", "--format=%cs", f"{base_ref}..HEAD", "--", path.as_posix()],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    for line in completed.stdout.splitlines():
        if line.strip():
            return date.fromisoformat(line.strip())
    return None

"""tea-kb command line interface."""

from __future__ import annotations

import json
import shutil
from datetime import date
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from tea_kb.boundary.config import GENERATED_DIR
from tea_kb.domain.ids import slugify
from tea_kb.graph.algorithms import shortest_path
from tea_kb.io.artifact_writer import ArtifactWriter
from tea_kb.lifecycle import all_artifacts, load_and_validate, report_only_artifacts
from tea_kb.reports.diagnostics import Severity, ValidationReport
from tea_kb.viz.mermaid import render_path_mermaid
from tea_kb.viz.pyvis_export import overview_artifact
from tea_kb.viz.svg import (
    repo_system_svg_artifacts,
    research_support_svg_artifacts,
    svg_visualization_artifacts,
    timeline_overview_svg_artifacts,
)

app = typer.Typer(no_args_is_help=True)
new_app = typer.Typer(no_args_is_help=True)
app.add_typer(new_app, name="new")
console = Console()


def _root(path: Path) -> Path:
    return path.resolve()


def _print_report(report: ValidationReport) -> None:
    for diagnostic in report.diagnostics:
        style = "red" if diagnostic.severity == Severity.ERROR else "yellow"
        location = f" {diagnostic.path}" if diagnostic.path else ""
        label = f"[{style}]{diagnostic.severity.value.upper()}[/{style}]"
        console.print(f"{label} {diagnostic.code}: {diagnostic.message}{location}")
    if not report.diagnostics:
        console.print("No diagnostics.")


def _exit_for_report(report: ValidationReport, *, strict: bool = False) -> None:
    if report.errors or (strict and report.warnings):
        raise typer.Exit(1)


@app.command()
def init(root: Path = typer.Option(Path("."), "--root", help="Repository root.")) -> None:
    """Create expected graph source and output directories."""
    repo = _root(root)
    for path in (
        "docs/maps",
        "docs/standards",
        "kb/notes",
        "kb/concepts",
        "kb/antipatterns",
        "kb/examples",
        "graph/generated/reports",
        "graph/generated/visualizations",
    ):
        (repo / path).mkdir(parents=True, exist_ok=True)
    console.print("Initialized tea-kb directories.")


@app.command()
def validate(
    root: Path = typer.Option(Path("."), "--root", help="Repository root."),
    strict: bool = typer.Option(False, "--strict", help="Treat warnings as failures."),
    output_format: str = typer.Option("text", "--format", help="text or json."),
) -> None:
    """Validate source files and graph consistency."""
    _, report = load_and_validate(_root(root))
    if output_format == "json":
        payload = [
            {
                "severity": item.severity.value,
                "code": item.code,
                "message": item.message,
                "path": item.path,
                "node_id": item.node_id,
            }
            for item in report.diagnostics
        ]
        console.print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        _print_report(report)
        summary = (
            f"Validation complete: {len(report.errors)} error(s), "
            f"{len(report.warnings)} warning(s)."
        )
        console.print(summary)
    _exit_for_report(report, strict=strict)


@app.command()
def build(
    root: Path = typer.Option(Path("."), "--root", help="Repository root."),
    check: bool = typer.Option(False, "--check", help="Fail if generated artifacts are stale."),
    clean: bool = typer.Option(False, "--clean", help="Remove generated artifacts before writing."),
) -> None:
    """Build generated graph artifacts."""
    repo = _root(root)
    result, report = load_and_validate(repo)
    _exit_for_report(report)
    artifacts = all_artifacts(result, report)
    writer = ArtifactWriter(repo)
    if check:
        writer.check(artifacts, managed_root=GENERATED_DIR)
        console.print("Generated artifacts are current.")
        return
    if clean and (repo / GENERATED_DIR).exists():
        shutil.rmtree(repo / GENERATED_DIR)
    elif not clean:
        pruned = writer.prune_unexpected(artifacts, GENERATED_DIR)
        if pruned:
            console.print(f"Pruned {len(pruned)} stale generated artifact(s).")
    writer.write(artifacts)
    console.print(f"Wrote {len(artifacts)} generated artifact(s).")


@app.command()
def report(
    root: Path = typer.Option(Path("."), "--root", help="Repository root."),
    section: str = typer.Option(
        "all", "--section", help="all, health, orphans, dense, duplicate, proposed."
    ),
    open_report: bool = typer.Option(False, "--open", help="Print report paths after writing."),
) -> None:
    """Write human-readable Markdown reports."""
    repo = _root(root)
    result, validation = load_and_validate(repo)
    _exit_for_report(validation)
    artifacts = report_only_artifacts(result, validation)
    if section != "all":
        aliases = {
            "health": "health.md",
            "orphans": "orphan-notes.md",
            "dense": "dense-links.md",
            "duplicate": "duplicate-concepts.md",
            "proposed": "proposed-edges.md",
        }
        suffix = aliases.get(section)
        if suffix is None:
            console.print(f"Unknown report section: {section}")
            raise typer.Exit(2)
        artifacts = [artifact for artifact in artifacts if artifact.path.name == suffix]
    ArtifactWriter(repo).write(artifacts)
    console.print(f"Wrote {len(artifacts)} report artifact(s).")
    if open_report:
        for artifact in artifacts:
            console.print((repo / artifact.path).as_posix())


@app.command()
def viz(
    view: str = typer.Argument("overview", help="overview or path."),
    source: str | None = typer.Argument(None, help="Source node for path view."),
    target: str | None = typer.Argument(None, help="Target node for path view."),
    root: Path = typer.Option(Path("."), "--root", help="Repository root."),
) -> None:
    """Create or render graph visualizations."""
    repo = _root(root)
    result, validation = load_and_validate(repo)
    _exit_for_report(validation)
    if view == "overview":
        ArtifactWriter(repo).write([overview_artifact(result.graph)])
        console.print("Wrote graph/generated/visualizations/overview.html")
        return
    if view == "timeline":
        ArtifactWriter(repo).write(timeline_overview_svg_artifacts(result.graph))
        console.print("Wrote timeline overview light/dark SVGs.")
        return
    if view == "system":
        ArtifactWriter(repo).write(repo_system_svg_artifacts(result.graph))
        console.print("Wrote repository system light/dark SVGs.")
        return
    if view == "research":
        ArtifactWriter(repo).write(research_support_svg_artifacts(result.graph))
        console.print("Wrote research support light/dark SVGs.")
        return
    if view == "all":
        artifacts = [overview_artifact(result.graph), *svg_visualization_artifacts(result.graph)]
        writer = ArtifactWriter(repo)
        writer.prune_unexpected(artifacts, GENERATED_DIR / "visualizations")
        writer.write(artifacts)
        console.print(f"Wrote {len(artifacts)} visualization artifact(s).")
        return
    if view == "path" and source and target:
        console.print(render_path_mermaid(result.graph, source, target))
        return
    console.print(
        "Supported views: overview, timeline, system, research, all, path <source> <target>"
    )
    raise typer.Exit(2)


@app.command()
def inspect(
    node_id: str, root: Path = typer.Option(Path("."), "--root", help="Repository root.")
) -> None:
    """Show one node, metadata, edges, chunks, and source path."""
    result, validation = load_and_validate(_root(root))
    _exit_for_report(validation)
    node = result.graph.nodes.get(node_id)  # type: ignore[arg-type]
    if node is None:
        console.print(f"Unknown node: {node_id}")
        raise typer.Exit(1)
    console.print(f"[bold]{node.title}[/bold]")
    console.print(f"ID: {node.id}")
    console.print(f"Type: {node.node_type.value}")
    console.print(f"Domain: {node.domain}")
    console.print(f"Status: {node.status}")
    console.print(f"Path: {node.path.as_posix()}")
    console.print("Inbound:")
    for edge in result.graph.inbound_edges(node.id):
        console.print(f"- {edge.source} --{edge.edge_type.value}--> {edge.target}")
    console.print("Outbound:")
    for edge in result.graph.outbound_edges(node.id):
        console.print(f"- {edge.source} --{edge.edge_type.value}--> {edge.target}")


@app.command()
def neighbors(
    node_id: str, root: Path = typer.Option(Path("."), "--root", help="Repository root.")
) -> None:
    """Show inbound and outbound neighbors for a node."""
    result, validation = load_and_validate(_root(root))
    _exit_for_report(validation)
    graph = result.graph
    if node_id not in graph.nodes:
        console.print(f"Unknown node: {node_id}")
        raise typer.Exit(1)
    table = Table("Direction", "Edge", "Neighbor")
    for edge in graph.inbound_edges(node_id):  # type: ignore[arg-type]
        table.add_row("in", edge.edge_type.value, str(edge.source))
    for edge in graph.outbound_edges(node_id):  # type: ignore[arg-type]
        table.add_row("out", edge.edge_type.value, str(edge.target))
    console.print(table)


@app.command(name="path")
def path_command(
    source: str,
    target: str,
    root: Path = typer.Option(Path("."), "--root", help="Repository root."),
) -> None:
    """Show the shortest directed path between two nodes."""
    result, validation = load_and_validate(_root(root))
    _exit_for_report(validation)
    path = shortest_path(result.graph, source, target)
    if not path:
        console.print("No path found.")
        raise typer.Exit(1)
    for index, node_id in enumerate(path, start=1):
        console.print(f"{index}. {node_id}")


@app.command()
def export(
    root: Path = typer.Option(Path("."), "--root", help="Repository root."),
    check: bool = typer.Option(False, "--check", help="Fail if generated artifacts are stale."),
) -> None:
    """Export generated graph artifacts."""
    build(root=root, check=check, clean=False)


@app.command()
def brew(
    root: Path = typer.Option(Path("."), "--root", help="Repository root."),
    check: bool = typer.Option(False, "--check", help="Fail if generated artifacts are stale."),
) -> None:
    """Alias for build."""
    build(root=root, check=check, clean=False)


@app.command()
def taste(root: Path = typer.Option(Path("."), "--root", help="Repository root.")) -> None:
    """Alias for report."""
    report(root=root, section="all", open_report=False)


@app.command(name="map")
def map_command(
    view: str = typer.Argument("overview"),
    source: str | None = typer.Argument(None),
    target: str | None = typer.Argument(None),
    root: Path = typer.Option(Path("."), "--root", help="Repository root."),
) -> None:
    """Alias for viz."""
    viz(view=view, source=source, target=target, root=root)


@new_app.command()
def note(
    title: str,
    domain: str,
    category: str,
    root: Path = typer.Option(Path("."), "--root", help="Repository root."),
) -> None:
    """Create a note template."""
    _write_template(
        root=_root(root),
        path=Path("kb/notes") / category / f"{slugify(title)}.md",
        node_id=f"note:{category}:{slugify(title)}",
        title=title,
        node_type="note",
        domain=domain,
    )


@new_app.command()
def concept(
    title: str, root: Path = typer.Option(Path("."), "--root", help="Repository root.")
) -> None:
    """Create a concept template."""
    _write_template(
        root=_root(root),
        path=Path("kb/concepts") / f"{slugify(title)}.md",
        node_id=f"concept:{slugify(title)}",
        title=title,
        node_type="concept",
        domain="repo-wide",
    )


@new_app.command()
def antipattern(
    title: str,
    root: Path = typer.Option(Path("."), "--root", help="Repository root."),
) -> None:
    """Create an antipattern template."""
    _write_template(
        root=_root(root),
        path=Path("kb/antipatterns") / f"{slugify(title)}.md",
        node_id=f"antipattern:{slugify(title)}",
        title=title,
        node_type="antipattern",
        domain="repo-wide",
    )


def _write_template(
    root: Path, path: Path, node_id: str, title: str, node_type: str, domain: str
) -> None:
    target = root / path
    if target.exists():
        console.print(f"Refusing to overwrite existing file: {path.as_posix()}")
        raise typer.Exit(1)
    target.parent.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    content = f"""---
id: {node_id}
title: {title}
type: {node_type}
domain: {domain}
status: active
created: {today}
updated: {today}
summary: >
  TODO
concepts: []
edges: {{}}
origin:
  author: human
  review: manual
---

# {title}

## Core claim
TODO

## Why it matters
TODO

## Use this when
TODO

## Failure smell
TODO
"""
    target.write_text(content, encoding="utf-8", newline="\n")
    console.print(f"Wrote {path.as_posix()}")

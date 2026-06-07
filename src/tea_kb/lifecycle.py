"""High-level lifecycle orchestration."""

from __future__ import annotations

from pathlib import Path

from tea_kb.graph.builder import BuildResult, build_graph
from tea_kb.graph.exporters import graph_jsonl_artifacts
from tea_kb.graph.validators import validate_build_result
from tea_kb.io.artifact_writer import Artifact
from tea_kb.reports.diagnostics import ValidationReport
from tea_kb.reports.markdown_report import report_artifacts
from tea_kb.reports.site_index import site_index_artifact
from tea_kb.viz.pyvis_export import overview_artifact
from tea_kb.viz.svg import svg_visualization_artifacts


def load_and_validate(root: Path) -> tuple[BuildResult, ValidationReport]:
    result = build_graph(root)
    report = validate_build_result(result, root)
    return result, report


def all_artifacts(result: BuildResult, report: ValidationReport) -> list[Artifact]:
    graph = result.graph
    return [
        *graph_jsonl_artifacts(graph),
        *report_artifacts(graph, report),
        site_index_artifact(graph),
        overview_artifact(graph),
        *svg_visualization_artifacts(graph),
    ]


def report_only_artifacts(result: BuildResult, report: ValidationReport) -> list[Artifact]:
    return report_artifacts(result.graph, report)

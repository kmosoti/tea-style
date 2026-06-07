"""Boundary protocols."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path
from typing import Protocol

from tea_kb.domain.models import KnowledgeGraph
from tea_kb.reports.diagnostics import ValidationReport


class MarkdownReader(Protocol):
    def read(self, root: Path) -> Iterable[tuple[Path, str]]: ...


class GraphExporter(Protocol):
    def export(self, graph: KnowledgeGraph, output_dir: Path) -> None: ...


class GraphValidator(Protocol):
    def validate(self, graph: KnowledgeGraph) -> ValidationReport: ...

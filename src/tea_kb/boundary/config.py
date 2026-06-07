"""Repository configuration defaults."""

from __future__ import annotations

from pathlib import Path

GRAPH_SOURCE_GLOBS: tuple[str, ...] = (
    "kb/**/*.md",
    "docs/doctrines/*.md",
    "docs/standards/*.md",
    "docs/maps/*.md",
    "docs/decisions/[0-9]*.md",
)

GENERATED_DIR = Path("graph/generated")

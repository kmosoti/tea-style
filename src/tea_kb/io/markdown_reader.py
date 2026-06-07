"""Markdown source discovery."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from tea_kb.boundary.config import GRAPH_SOURCE_GLOBS


class FileSystemMarkdownReader:
    def __init__(self, patterns: tuple[str, ...] = GRAPH_SOURCE_GLOBS) -> None:
        self._patterns = patterns

    def paths(self, root: Path) -> tuple[Path, ...]:
        seen: set[Path] = set()
        paths: list[Path] = []
        for pattern in self._patterns:
            for path in root.glob(pattern):
                if path.name == "README.md":
                    continue
                if path.is_file() and path not in seen:
                    seen.add(path)
                    paths.append(path)
        return tuple(sorted(paths, key=lambda item: item.as_posix()))

    def read(self, root: Path) -> Iterable[tuple[Path, str]]:
        for path in self.paths(root):
            yield path, path.read_text(encoding="utf-8")

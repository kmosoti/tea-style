"""Path helpers."""

from __future__ import annotations

from pathlib import Path


def repo_root_from(path: Path | None = None) -> Path:
    root = path or Path.cwd()
    return root.resolve()


def relative_path(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()

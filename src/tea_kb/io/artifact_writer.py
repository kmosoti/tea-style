"""Generated artifact writer."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from tea_kb.errors import BuildCheckFailed


@dataclass(frozen=True, slots=True)
class Artifact:
    path: Path
    content: str


class ArtifactWriter:
    def __init__(self, root: Path) -> None:
        self._root = root

    def write(self, artifacts: list[Artifact]) -> None:
        for artifact in artifacts:
            target = self._root / artifact.path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(artifact.content, encoding="utf-8", newline="\n")

    def check(self, artifacts: list[Artifact], managed_root: Path | None = None) -> None:
        stale: list[str] = []
        for artifact in artifacts:
            target = self._root / artifact.path
            current = target.read_text(encoding="utf-8") if target.exists() else None
            if current != artifact.content:
                stale.append(artifact.path.as_posix())
        if managed_root is not None:
            stale.extend(path.as_posix() for path in self.unexpected_paths(artifacts, managed_root))
        if stale:
            joined = ", ".join(stale)
            raise BuildCheckFailed(f"generated artifacts are stale: {joined}")

    def prune_unexpected(self, artifacts: list[Artifact], managed_root: Path) -> tuple[Path, ...]:
        unexpected = self.unexpected_paths(artifacts, managed_root)
        managed_base = (self._root / managed_root).resolve()
        root = self._root.resolve()
        if not managed_base.is_relative_to(root):
            raise BuildCheckFailed(f"managed root is outside repository root: {managed_root}")
        for relative in unexpected:
            target = (self._root / relative).resolve()
            if not target.is_relative_to(managed_base):
                raise BuildCheckFailed(f"refusing to prune outside managed root: {relative}")
            target.unlink()
        return unexpected

    def unexpected_paths(self, artifacts: list[Artifact], managed_root: Path) -> tuple[Path, ...]:
        expected = {artifact.path for artifact in artifacts}
        base = self._root / managed_root
        if not base.exists():
            return ()
        root = self._root.resolve()
        if not base.resolve().is_relative_to(root):
            raise BuildCheckFailed(f"managed root is outside repository root: {managed_root}")
        paths: list[Path] = []
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            relative = path.resolve().relative_to(root)
            if relative not in expected:
                paths.append(relative)
        return tuple(sorted(paths, key=lambda item: item.as_posix()))

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

    def check(self, artifacts: list[Artifact]) -> None:
        stale: list[str] = []
        for artifact in artifacts:
            target = self._root / artifact.path
            current = target.read_text(encoding="utf-8") if target.exists() else None
            if current != artifact.content:
                stale.append(artifact.path.as_posix())
        if stale:
            joined = ", ".join(stale)
            raise BuildCheckFailed(f"generated artifacts are stale: {joined}")

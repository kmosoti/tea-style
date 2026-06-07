from pathlib import Path

import pytest

from tea_kb.errors import BuildCheckFailed
from tea_kb.io.artifact_writer import Artifact, ArtifactWriter


def test_check_fails_on_unexpected_managed_artifact(tmp_path: Path) -> None:
    writer = ArtifactWriter(tmp_path)
    expected = Artifact(Path("graph/generated/nodes.jsonl"), "{}\n")
    writer.write([expected])
    stale = tmp_path / "graph/generated/visualizations/old.svg"
    stale.parent.mkdir(parents=True)
    stale.write_text("<svg />\n", encoding="utf-8")

    with pytest.raises(BuildCheckFailed, match="old.svg"):
        writer.check([expected], managed_root=Path("graph/generated"))


def test_prune_unexpected_removes_only_unmanaged_artifacts(tmp_path: Path) -> None:
    writer = ArtifactWriter(tmp_path)
    expected = Artifact(Path("graph/generated/nodes.jsonl"), "{}\n")
    writer.write([expected])
    stale = tmp_path / "graph/generated/visualizations/old.svg"
    stale.parent.mkdir(parents=True)
    stale.write_text("<svg />\n", encoding="utf-8")

    pruned = writer.prune_unexpected([expected], Path("graph/generated"))

    assert pruned == (Path("graph/generated/visualizations/old.svg"),)
    assert (tmp_path / expected.path).exists()
    assert not stale.exists()

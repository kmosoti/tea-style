from pathlib import Path

from tea_kb.graph.builder import build_graph
from tea_kb.graph.exporters import graph_jsonl_artifacts
from tea_kb.graph.validators import validate_build_result


def test_build_and_validate_fixture_graph(tmp_path: Path) -> None:
    concept = tmp_path / "kb/concepts/evidence.md"
    concept.parent.mkdir(parents=True)
    concept.write_text(
        """---
id: concept:evidence
title: Evidence
type: concept
domain: test
status: active
created: 2026-06-07
updated: 2026-06-07
concepts:
  - evidence
edges: {}
origin:
  author: human
  review: manual
---

# Evidence

## Definition
Proof.
""",
        encoding="utf-8",
    )
    note = tmp_path / "kb/notes/evidence/valid-note.md"
    note.parent.mkdir(parents=True)
    note.write_text(
        Path("tests/fixtures/valid_note.md").read_text(encoding="utf-8"), encoding="utf-8"
    )

    result = build_graph(tmp_path)
    report = validate_build_result(result, tmp_path)

    assert report.is_valid
    assert len(result.graph.nodes) == 2
    assert len(result.graph.chunks) >= 4


def test_jsonl_export_is_stable(tmp_path: Path) -> None:
    concept = tmp_path / "kb/concepts/evidence.md"
    concept.parent.mkdir(parents=True)
    concept.write_text(
        """---
id: concept:evidence
title: Evidence
type: concept
domain: test
status: active
created: 2026-06-07
updated: 2026-06-07
concepts:
  - evidence
edges: {}
origin:
  author: human
  review: manual
---

# Evidence

## Definition
Proof.
""",
        encoding="utf-8",
    )

    result = build_graph(tmp_path)
    artifacts = graph_jsonl_artifacts(result.graph)

    assert artifacts[0].path.as_posix() == "graph/generated/nodes.jsonl"
    assert '"id": "concept:evidence"' in artifacts[0].content
    assert artifacts[-1].path.as_posix() == "graph/generated/timeline.jsonl"
    assert '"event_type": "created"' in artifacts[-1].content

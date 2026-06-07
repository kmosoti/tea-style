from pathlib import Path

import pytest

from tea_kb.boundary.frontmatter import parse_markdown_document
from tea_kb.errors import FrontmatterError


def test_parse_valid_frontmatter() -> None:
    text = Path("tests/fixtures/valid_note.md").read_text(encoding="utf-8")
    parsed = parse_markdown_document(Path("tests/fixtures/valid_note.md"), text)

    assert parsed.metadata.id == "note:test:valid-note"
    assert parsed.metadata.type == "note"
    assert parsed.metadata.edges


def test_missing_frontmatter_raises() -> None:
    text = Path("tests/fixtures/invalid_note.md").read_text(encoding="utf-8")

    with pytest.raises(FrontmatterError):
        parse_markdown_document(Path("tests/fixtures/invalid_note.md"), text)

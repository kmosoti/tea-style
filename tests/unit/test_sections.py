from tea_kb.parse.sections import extract_sections


def test_extract_sections() -> None:
    sections = extract_sections("# Title\n\n## Core claim\nText\n\n## Why it matters\nMore")

    assert [section.heading for section in sections] == ["Title", "Core claim", "Why it matters"]
    assert sections[1].text == "Text"

"""Markdown section extraction."""

from __future__ import annotations

from dataclasses import dataclass

from markdown_it import MarkdownIt


@dataclass(frozen=True, slots=True)
class MarkdownSection:
    heading: str
    level: int
    text: str


def extract_sections(markdown: str) -> tuple[MarkdownSection, ...]:
    MarkdownIt("commonmark").parse(markdown)
    sections: list[MarkdownSection] = []
    current_heading: str | None = None
    current_level = 0
    current_lines: list[str] = []

    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            marker, _, title = stripped.partition(" ")
            if marker and set(marker) == {"#"} and title:
                if current_heading is not None:
                    sections.append(
                        MarkdownSection(
                            heading=current_heading,
                            level=current_level,
                            text="\n".join(current_lines).strip(),
                        )
                    )
                current_heading = title.strip()
                current_level = len(marker)
                current_lines = []
                continue
        if current_heading is not None:
            current_lines.append(line)

    if current_heading is not None:
        sections.append(
            MarkdownSection(
                heading=current_heading,
                level=current_level,
                text="\n".join(current_lines).strip(),
            )
        )

    return tuple(sections)


def section_names(markdown: str) -> tuple[str, ...]:
    return tuple(section.heading for section in extract_sections(markdown))

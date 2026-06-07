"""Frontmatter date updates."""

from __future__ import annotations

from datetime import date
from pathlib import Path


def update_updated_date(path: Path, updated: date) -> bool:
    text = path.read_text(encoding="utf-8")
    next_text = update_updated_date_text(text, updated)
    if next_text == text:
        return False
    path.write_text(next_text, encoding="utf-8", newline="\n")
    return True


def update_updated_date_text(text: str, updated: date) -> str:
    if not text.startswith("---"):
        raise ValueError("missing YAML frontmatter")

    body = text[3:]
    frontmatter, separator, content = body.partition("---")
    if not separator:
        raise ValueError("missing closing YAML frontmatter marker")

    lines = frontmatter.splitlines()
    updated_line = f"updated: {updated.isoformat()}"
    has_updated = any(line.startswith("updated:") for line in lines)
    insert_prefix = "created:" if any(line.startswith("created:") for line in lines) else "status:"
    rendered: list[str] = []
    inserted = False
    for line in lines:
        if line.startswith("updated:"):
            rendered.append(updated_line)
            inserted = True
            continue
        rendered.append(line)
        if not has_updated and not inserted and line.startswith(insert_prefix):
            rendered.append(updated_line)
            inserted = True

    if not inserted:
        rendered.append(updated_line)

    next_frontmatter = "\n".join(rendered).strip("\n")
    return f"---\n{next_frontmatter}\n---{content}"

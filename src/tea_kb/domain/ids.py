"""Typed ID helpers."""

from __future__ import annotations

import re
from typing import NewType

NodeId = NewType("NodeId", str)
EdgeId = NewType("EdgeId", str)
ChunkId = NewType("ChunkId", str)
ConceptId = NewType("ConceptId", str)

ID_PATTERN = re.compile(r"^[a-z][a-z0-9-]*(?::[a-z0-9][a-z0-9-]*){1,}$")
SLUG_PATTERN = re.compile(r"[^a-z0-9]+")


def is_valid_id(value: str) -> bool:
    return bool(ID_PATTERN.fullmatch(value))


def slugify(value: str) -> str:
    slug = SLUG_PATTERN.sub("-", value.lower()).strip("-")
    return slug or "untitled"


def concept_id_for(value: str) -> NodeId:
    if value.startswith("concept:"):
        return NodeId(value)
    return NodeId(f"concept:{slugify(value)}")

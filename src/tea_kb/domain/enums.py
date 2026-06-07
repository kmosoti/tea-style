"""Graph enums."""

from __future__ import annotations

from enum import StrEnum


class NodeType(StrEnum):
    NOTE = "note"
    DOCTRINE = "doctrine"
    CONCEPT = "concept"
    ANTIPATTERN = "antipattern"
    DECISION = "decision"
    EXAMPLE = "example"
    STANDARD = "standard"
    MAP = "map"


class EdgeType(StrEnum):
    SUPPORTS = "supports"
    REFINES = "refines"
    DEPENDS_ON = "depends_on"
    CONTRADICTS = "contradicts"
    APPLIES_TO = "applies_to"
    EXEMPLIFIES = "exemplifies"
    SUPERSEDES = "supersedes"
    RELATED_TO = "related_to"


class ReviewStatus(StrEnum):
    MANUAL = "manual"
    PROPOSED = "proposed"
    REVIEWED = "reviewed"


class AuthorType(StrEnum):
    HUMAN = "human"
    AGENT = "agent"

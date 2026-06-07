"""Markdown frontmatter boundary models."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import frontmatter  # type: ignore[import-untyped]
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from tea_kb.domain.enums import AuthorType, EdgeType, NodeType, ReviewStatus
from tea_kb.domain.ids import ConceptId, NodeId
from tea_kb.domain.models import KnowledgeNode
from tea_kb.errors import FrontmatterError


class OriginModel(BaseModel):
    author: AuthorType = AuthorType.HUMAN
    review: ReviewStatus = ReviewStatus.MANUAL


class FrontmatterModel(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    type: NodeType
    domain: str = Field(min_length=1)
    status: str = "active"
    summary: str | None = None
    concepts: list[str] = Field(default_factory=list)
    applies_when: list[str] = Field(default_factory=list)
    edges: dict[EdgeType, list[str]] = Field(default_factory=dict)
    aliases: list[str] = Field(default_factory=list)
    origin: OriginModel = Field(default_factory=OriginModel)


@dataclass(frozen=True, slots=True)
class ParsedDocument:
    path: Path
    metadata: FrontmatterModel
    content: str
    raw: str

    def to_node(self, source_hash: str) -> KnowledgeNode:
        return KnowledgeNode(
            id=NodeId(self.metadata.id),
            title=self.metadata.title,
            node_type=self.metadata.type,
            domain=self.metadata.domain,
            status=self.metadata.status,
            concepts=tuple(ConceptId(concept) for concept in self.metadata.concepts),
            path=self.path,
            source_hash=source_hash,
            summary=self.metadata.summary,
            aliases=tuple(self.metadata.aliases),
        )


def parse_markdown_document(path: Path, text: str) -> ParsedDocument:
    if not text.lstrip().startswith("---"):
        raise FrontmatterError(f"{path}: missing YAML frontmatter")

    try:
        post = frontmatter.loads(text)
        metadata = _normalize_metadata(dict(post.metadata))
        model = FrontmatterModel.model_validate(metadata)
    except ValidationError as exc:
        raise FrontmatterError(f"{path}: invalid frontmatter: {exc}") from exc
    except Exception as exc:
        raise FrontmatterError(f"{path}: invalid YAML frontmatter: {exc}") from exc

    return ParsedDocument(path=path, metadata=model, content=post.content, raw=text)


def _normalize_metadata(metadata: dict[str, Any]) -> dict[str, Any]:
    edges = metadata.get("edges")
    if isinstance(edges, dict):
        metadata["edges"] = {str(key): list(value or []) for key, value in edges.items()}
    return metadata

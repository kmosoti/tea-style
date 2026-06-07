"""Tool-specific errors."""

from __future__ import annotations


class TeaKbError(Exception):
    """Base error for tea-kb."""


class FrontmatterError(TeaKbError):
    """Raised when Markdown frontmatter is missing or invalid."""


class BuildCheckFailed(TeaKbError):
    """Raised when generated artifacts are stale."""

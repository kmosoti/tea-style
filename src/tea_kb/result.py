"""Small result helpers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Result:
    ok: bool
    message: str = ""

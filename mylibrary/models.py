"""Domain models for the library."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class Book:
    """A single book held by the library."""

    title: str
    author: str
    available: bool = True

    def __post_init__(self) -> None:
        self.title = self.title.strip()
        self.author = self.author.strip()
        if not self.title:
            raise ValueError("Book title must not be empty")
        if not self.author:
            raise ValueError("Book author must not be empty")

    def __str__(self) -> str:
        status = "available" if self.available else "borrowed"
        return f"{self.title} by {self.author} ({status})"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Book:
        return cls(
            title=data["title"],
            author=data["author"],
            available=data.get("available", True),
        )

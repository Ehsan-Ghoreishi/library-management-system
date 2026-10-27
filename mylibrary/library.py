"""Core library logic, independent of any user interface."""

from __future__ import annotations

from collections.abc import Iterator

from mylibrary.exceptions import BookNotFoundError, DuplicateBookError
from mylibrary.models import Book


def _normalize(title: str) -> str:
    return title.strip().casefold()


class Library:
    """An in-memory collection of books keyed by case-insensitive title."""

    def __init__(self) -> None:
        self._books: dict[str, Book] = {}

    def __len__(self) -> int:
        return len(self._books)

    def __iter__(self) -> Iterator[Book]:
        return iter(self._books.values())

    def __contains__(self, title: object) -> bool:
        return isinstance(title, str) and _normalize(title) in self._books

    @property
    def books(self) -> list[Book]:
        return list(self._books.values())

    def add_book(self, title: str, author: str) -> Book:
        book = Book(title, author)
        key = _normalize(book.title)
        if key in self._books:
            raise DuplicateBookError(book.title)
        self._books[key] = book
        return book

    def get_book(self, title: str) -> Book:
        try:
            return self._books[_normalize(title)]
        except KeyError:
            raise BookNotFoundError(title) from None

    def remove_book(self, title: str) -> Book:
        book = self.get_book(title)
        del self._books[_normalize(title)]
        return book

    def search(self, query: str) -> list[Book]:
        """Return books whose title or author contains ``query``."""
        needle = query.strip().casefold()
        if not needle:
            return []
        return [
            book
            for book in self._books.values()
            if needle in book.title.casefold() or needle in book.author.casefold()
        ]

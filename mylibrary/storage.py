"""Load and save a Library as JSON."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

from mylibrary.library import Library
from mylibrary.models import Book

FORMAT_VERSION = 1


def save(library: Library, path: str | Path) -> None:
    """Write the library to ``path`` atomically."""
    path = Path(path)
    payload = {
        "version": FORMAT_VERSION,
        "books": [book.to_dict() for book in library],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        os.replace(tmp_name, path)
    except BaseException:
        os.unlink(tmp_name)
        raise


def load(path: str | Path) -> Library:
    """Read a library from ``path``; a missing file yields an empty library."""
    path = Path(path)
    library = Library()
    if not path.exists():
        return library
    with path.open(encoding="utf-8") as fh:
        payload = json.load(fh)
    for data in payload.get("books", []):
        book = Book.from_dict(data)
        library.add_book(book.title, book.author)
        if not book.available:
            library.borrow_book(book.title)
    return library

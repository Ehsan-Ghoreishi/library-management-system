"""A simple library management system."""

from mylibrary.exceptions import (
    BookNotBorrowedError,
    BookNotFoundError,
    BookUnavailableError,
    DuplicateBookError,
    LibraryError,
)
from mylibrary.library import Library
from mylibrary.models import Book

__version__ = "2.0.0"

__all__ = [
    "Book",
    "BookNotBorrowedError",
    "BookNotFoundError",
    "BookUnavailableError",
    "DuplicateBookError",
    "Library",
    "LibraryError",
    "__version__",
]

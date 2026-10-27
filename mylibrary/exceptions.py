"""Exceptions raised by the library."""


class LibraryError(Exception):
    """Base class for all library errors."""


class BookNotFoundError(LibraryError):
    """Raised when a requested book is not in the library."""

    def __init__(self, title: str) -> None:
        super().__init__(f"'{title}' was not found")
        self.title = title


class DuplicateBookError(LibraryError):
    """Raised when adding a book whose title already exists."""

    def __init__(self, title: str) -> None:
        super().__init__(f"'{title}' is already in the library")
        self.title = title


class BookUnavailableError(LibraryError):
    """Raised when borrowing a book that is already borrowed."""

    def __init__(self, title: str) -> None:
        super().__init__(f"'{title}' is already borrowed")
        self.title = title


class BookNotBorrowedError(LibraryError):
    """Raised when returning a book that was not borrowed."""

    def __init__(self, title: str) -> None:
        super().__init__(f"'{title}' was not borrowed")
        self.title = title

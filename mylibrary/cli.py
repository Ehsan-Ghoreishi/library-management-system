"""Interactive command-line interface for the library."""

from __future__ import annotations

import argparse
from collections.abc import Callable, Iterable
from pathlib import Path

from mylibrary import __version__, storage
from mylibrary.exceptions import LibraryError
from mylibrary.library import Library
from mylibrary.models import Book

DEFAULT_DATA_FILE = Path("library.json")

MENU = """
--- Library Menu ---
1. Add book
2. Remove book
3. Search books
4. Show books
5. Borrow book
6. Return book
7. Exit"""


def _print_books(books: Iterable[Book], empty_message: str) -> None:
    books = list(books)
    if not books:
        print(empty_message)
        return
    for book in books:
        print(f"  - {book}")


def _add(library: Library, prompt: Callable[[str], str]) -> bool:
    book = library.add_book(prompt("Book title: "), prompt("Author: "))
    print(f"'{book.title}' was added")
    return True


def _remove(library: Library, prompt: Callable[[str], str]) -> bool:
    book = library.remove_book(prompt("Title to remove: "))
    print(f"'{book.title}' was removed")
    return True


def _search(library: Library, prompt: Callable[[str], str]) -> bool:
    _print_books(library.search(prompt("Search (title or author): ")), "No matching books")
    return False


def _show(library: Library, prompt: Callable[[str], str]) -> bool:
    _print_books(library, "The library is empty")
    return False


def _borrow(library: Library, prompt: Callable[[str], str]) -> bool:
    book = library.borrow_book(prompt("Title to borrow: "))
    print(f"You borrowed '{book.title}'")
    return True


def _return(library: Library, prompt: Callable[[str], str]) -> bool:
    book = library.return_book(prompt("Title to return: "))
    print(f"'{book.title}' was returned")
    return True


# Each action returns True when it modified the library and it must be saved.
ACTIONS: dict[str, Callable[[Library, Callable[[str], str]], bool]] = {
    "1": _add,
    "2": _remove,
    "3": _search,
    "4": _show,
    "5": _borrow,
    "6": _return,
}
EXIT_CHOICE = "7"


def run(data_file: Path, prompt: Callable[[str], str] = input) -> None:
    library = storage.load(data_file)

    while True:
        print(MENU)
        try:
            choice = prompt("Choose an option: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            choice = EXIT_CHOICE

        if choice == EXIT_CHOICE:
            print("Goodbye!")
            return

        action = ACTIONS.get(choice)
        if action is None:
            print("Invalid choice, try again")
            continue

        try:
            if action(library, prompt):
                storage.save(library, data_file)
        except (LibraryError, ValueError) as exc:
            print(f"Error: {exc}")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="mylibrary", description="A simple library manager.")
    parser.add_argument(
        "-f",
        "--file",
        type=Path,
        default=DEFAULT_DATA_FILE,
        help=f"JSON file to store books in (default: {DEFAULT_DATA_FILE})",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args(argv)
    run(args.file)

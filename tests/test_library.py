import pytest

from mylibrary import (
    BookNotBorrowedError,
    BookNotFoundError,
    BookUnavailableError,
    DuplicateBookError,
    Library,
)


def test_new_library_is_empty():
    lib = Library()
    assert len(lib) == 0
    assert lib.books == []


def test_add_book(library):
    book = library.add_book("Neuromancer", "William Gibson")
    assert book.title == "Neuromancer"
    assert "Neuromancer" in library
    assert len(library) == 3


def test_add_duplicate_is_case_insensitive(library):
    with pytest.raises(DuplicateBookError):
        library.add_book("  dune ", "Someone Else")
    assert len(library) == 2


def test_get_book_is_case_insensitive(library):
    assert library.get_book("the hobbit").author == "J.R.R. Tolkien"


def test_get_missing_book_raises(library):
    with pytest.raises(BookNotFoundError):
        library.get_book("Missing")


def test_remove_book(library):
    removed = library.remove_book("DUNE")
    assert removed.title == "Dune"
    assert "Dune" not in library
    assert len(library) == 1


def test_remove_missing_book_raises(library):
    with pytest.raises(BookNotFoundError):
        library.remove_book("Missing")


def test_iteration_preserves_insertion_order(library):
    assert [b.title for b in library] == ["Dune", "The Hobbit"]


@pytest.mark.parametrize(
    "query, expected",
    [
        ("dune", ["Dune"]),
        ("TOLKIEN", ["The Hobbit"]),
        ("e", ["Dune", "The Hobbit"]),
        ("nothing", []),
        ("   ", []),
    ],
)
def test_search(library, query, expected):
    assert [b.title for b in library.search(query)] == expected


def test_contains_ignores_non_strings(library):
    assert 42 not in library


def test_borrow_and_return(library):
    assert not library.borrow_book("dune").available
    assert library.return_book("Dune").available


def test_borrow_unavailable_raises(library):
    library.borrow_book("Dune")
    with pytest.raises(BookUnavailableError):
        library.borrow_book("Dune")


def test_return_not_borrowed_raises(library):
    with pytest.raises(BookNotBorrowedError):
        library.return_book("Dune")


def test_borrow_missing_raises(library):
    with pytest.raises(BookNotFoundError):
        library.borrow_book("Missing")

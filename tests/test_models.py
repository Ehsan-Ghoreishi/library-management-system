import pytest

from mylibrary import Book


def test_strips_whitespace():
    book = Book("  Dune ", " Frank Herbert ")
    assert book.title == "Dune"
    assert book.author == "Frank Herbert"


@pytest.mark.parametrize("title, author", [("", "Someone"), ("   ", "Someone"), ("Title", "")])
def test_rejects_empty_fields(title, author):
    with pytest.raises(ValueError):
        Book(title, author)


def test_str_shows_availability():
    book = Book("Dune", "Frank Herbert")
    assert str(book) == "Dune by Frank Herbert (available)"
    book.available = False
    assert str(book) == "Dune by Frank Herbert (borrowed)"


def test_dict_round_trip():
    book = Book("Dune", "Frank Herbert", available=False)
    assert Book.from_dict(book.to_dict()) == book


def test_from_dict_defaults_to_available():
    assert Book.from_dict({"title": "Dune", "author": "Frank Herbert"}).available

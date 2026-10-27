import pytest

from mylibrary import Library


@pytest.fixture
def library():
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    lib.add_book("The Hobbit", "J.R.R. Tolkien")
    return lib

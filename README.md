# Library Management System

[![CI](https://github.com/Ehsan-Ghoreishi/library-management-system/actions/workflows/ci.yml/badge.svg)](https://github.com/Ehsan-Ghoreishi/library-management-system/actions/workflows/ci.yml)

A command-line library management system written in Python, packaged as an installable module with a clean separation between domain logic, persistence and the user interface.

## Features

- Add, remove, borrow and return books
- Case-insensitive title lookup with duplicate protection
- Substring search across titles and authors
- Persistent storage in a JSON file (atomic writes, Unicode-safe)
- Interactive menu, available as `mylibrary`, `python -m mylibrary` or `python main.py`
- Usable as a library from your own Python code
- Fully tested (pytest), linted (ruff) and checked by CI on Python 3.9–3.13

## Project Structure

```
library-management-system/
├── mylibrary/
│   ├── __init__.py      # Public API and version
│   ├── __main__.py      # python -m mylibrary
│   ├── cli.py           # Interactive menu and argument parsing
│   ├── exceptions.py    # LibraryError hierarchy
│   ├── library.py       # Library: core collection logic
│   ├── models.py        # Book dataclass
│   └── storage.py       # JSON load/save
├── tests/               # pytest suite
├── .github/workflows/   # CI pipeline
├── main.py              # Convenience entry point
└── pyproject.toml
```

## Installation

Requires Python 3.9 or newer.

```bash
git clone https://github.com/Ehsan-Ghoreishi/library-management-system.git
cd library-management-system
pip install .
```

## Usage

```bash
mylibrary                     # stores books in ./library.json
mylibrary --file ~/books.json # use a different data file
mylibrary --version
```

```
--- Library Menu ---
1. Add book
2. Remove book
3. Search books
4. Show books
5. Borrow book
6. Return book
7. Exit
```

Every change is saved to the data file right away.

### As a Python library

```python
from mylibrary import Library, BookUnavailableError
from mylibrary import storage

lib = Library()
lib.add_book("Dune", "Frank Herbert")
lib.borrow_book("dune")  # titles are case-insensitive

try:
    lib.borrow_book("Dune")
except BookUnavailableError as exc:
    print(exc)  # 'Dune' is already borrowed

for book in lib.search("herbert"):
    print(book)  # Dune by Frank Herbert (borrowed)

storage.save(lib, "library.json")
lib = storage.load("library.json")
```

All errors derive from `mylibrary.LibraryError`.

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

pytest --cov=mylibrary   # run tests with coverage
ruff check .             # lint
ruff format .            # format
```

## Author

Ehsan Ghoreishi

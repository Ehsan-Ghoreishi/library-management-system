# Library Management System

A simple command-line library management system built with Python using Object-Oriented Programming (OOP). This project is structured as an installable Python package.

## Features

- Add a book with title and author
- Remove a book by title
- Search for a book by title
- Display all books in the library
- Interactive command-line menu

## Project Structure

library-management-system/

├── mylibrary/

│   ├── init.py

│   └── library.py

├── main.py

├── setup.py

└── README.md

## Installation

Clone the repository and install the package locally:

```bash
git clone https://github.com/Ehsan-Ghoreishi/library-management-system.git
cd library-management-system
pip install .
```

## Usage

Run the program:

```bash
python main.py
```

You will see an interactive menu:

--- Library Menu ---

1. Add book
2. Remove book
3. Search book
4. Show books
5. Exit

You can also import and use the library in your own code:

```python
from mylibrary.library import Library

lib = Library()
lib.add_book("Dune", "Herbert")
lib.show_books()
```

## Technologies

- Python 3
- Object-Oriented Programming (OOP)
- Python packaging (setuptools)

## Author

Ehsan Ghoreishi


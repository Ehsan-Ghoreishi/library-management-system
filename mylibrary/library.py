class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {"title": title, "author": author}
        self.books.append(book)
        print(f"The book {title} was added")

    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                return f"'{title}' was removed"
        return f"'{title}' was not found"

    def search_book(self, title):
        for book in self.books:
            if book["title"] == title:
                return f"'{title}' is in the library."
        return f"'{title}' is NOT in the library."

    def show_books(self):
        if not self.books:
            print("The library is empty")
            return
        for book in self.books:
            print(f"{book['title']} by {book['author']}")
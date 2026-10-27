from mylibrary.exceptions import LibraryError
from mylibrary.library import Library


def main():
    my_library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search book")
        print("4. Show books")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                title = input("Book title: ")
                author = input("Author: ")
                book = my_library.add_book(title, author)
                print(f"'{book.title}' was added")
            elif choice == "2":
                title = input("Title to remove: ")
                book = my_library.remove_book(title)
                print(f"'{book.title}' was removed")
            elif choice == "3":
                query = input("Search (title or author): ")
                results = my_library.search(query)
                if not results:
                    print("No matching books")
                for book in results:
                    print(book)
            elif choice == "4":
                if not len(my_library):
                    print("The library is empty")
                for book in my_library:
                    print(book)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again")
        except (LibraryError, ValueError) as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()

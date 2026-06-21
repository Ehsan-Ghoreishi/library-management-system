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

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Book title: ")
            author = input("Author: ")
            my_library.add_book(title, author)
        elif choice == "2":
            title = input("Title to remove: ")
            print(my_library.remove_book(title))
        elif choice == "3":
            title = input("Title to search: ")
            print(my_library.search_book(title))
        elif choice == "4":
            my_library.show_books()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again")


if __name__ == "__main__":
    main()
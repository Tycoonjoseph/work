def main():
    book = load_data()
    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. Remove a book")
        print("3. Search for books")
        print("4. List all books")
        print("5. Mark a book as read")
        print("6. Show reading progress")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            new_book = add_books()
            book.append(new_book)
            save_data(book)
        elif choice == "2":
            remove_books(book)
            save_data(book)
        elif choice == "3":
            search_books(book)
        elif choice == "4":
            list_books(book)
        elif choice == "5":
            mark_as_read(book)
            save_data(book)
        elif choice == "6":
            show_reading_progress(book)
        elif choice == "7":
            exit_program()
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
# add a new book
def add_books():
    title = str(input("Enter the book title: ")).capitalize().strip()
    author = str(input("enter the book author: ")).capitalize().strip()
    year = int(input("Enter the publication year: "))
    isbn = str(input("Enter the ISBN number: ")).strip()
    book = {
        "title": title,
        "author": author,
        "year": year,
        "isbn": isbn
    }
    return book
# remove a book by title
def remove_books(book):
    title = str(input("Enter the book title to remove: ")).capitalize().strip()
    for b in book:
        if b["title"] == title:
            book.remove(b)
            print(f"{title} has been removed.")
            return
    print(f"{title} not found in the library.")
# search for books(by title or author)
def search_books(book):
    search_term = str(input("Enter the book title or author to search: ")).capitalize().strip()
    found_books = []
    for b in book:
        if search_term in b["title"] or search_term in b["author"]:
            found_books.append(b)
    if found_books:
        print("Books found:")
        for b in found_books:
            print(f"{b['title']} by {b['author']} ({b['year']}) - ISBN: {b['isbn']}")
    else:
        print("No books found matching the search term.")
# lsit all books sorted by title 
def list_books(book):
    sorted_books = sorted(book, key=lambda x: x["title"])
    print("Books in the library:")
    for b in sorted_books:
        print(f"{b['title']} by {b['author']} ({b['year']}) - ISBN: {b['isbn']}")
# mark a book as read
def mark_as_read(book):
    title = str(input("Enter the book title to mark as read: ")).capitalize().strip()
    for b in book:
        if b["title"] == title:
            b["read"] = True
            print(f"{title} has been marked as read.")
            return
    print(f"{title} not found in the library.")
# show reading progrss(example 2 of 10 books read)
def show_reading_progress(book):
    total_books = len(book)
    read_books = sum(1 for b in book if b.get("read"))
    print(f"Reading progress: {read_books} of {total_books} books read.")
# save data to a file and load it automatically on start
import json
def save_data(book):
    with open("library_data.json", "w") as f:
        json.dump(book, f)
def load_data():
    try:
        with open("library_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
#exit the program
def exit_program():
    print("Exiting the program. Goodbye!")
    exit()
if __name__ == "__main__":
    main()
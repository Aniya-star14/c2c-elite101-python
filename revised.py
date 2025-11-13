from datetime import datetime, timedelta

# -------- Starter Data (from library_books.py) --------
library_books = [
    {
        "id": "B1",
        "title": "The Lightning Thief",
        "author": "Rick Riordan",
        "genre": "Fantasy",
        "available": True,
        "due_date": None,
        "checkouts": 2
    },
    {
        "id": "B2",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Historical",
        "available": False,
        "due_date": "2025-11-01",
        "checkouts": 5
    },
    {
        "id": "B3",
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "Science Fiction",
        "available": True,
        "due_date": None,
        "checkouts": 3
    }
]

# -------- Level 5: OOP Refactor --------
class Book:
    def __init__(self, id, title, author, genre, available=True, due_date=None, checkouts=0):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        # Convert string due_date to datetime if necessary
        if isinstance(due_date, str):
            self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        else:
            self.due_date = due_date
        self.checkouts = checkouts

    def checkout(self):
        """Mark book as checked out if available."""
        if self.available:
            self.available = False
            self.due_date = datetime.now() + timedelta(weeks=2)
            self.checkouts += 1
            return f"'{self.title}' checked out successfully! Due on {self.due_date.strftime('%Y-%m-%d')}."
        else:
            return f"'{self.title}' is already checked out."

    def return_book(self):
        """Mark book as returned and clear due date."""
        if not self.available:
            self.available = True
            self.due_date = None
            return f"'{self.title}' has been returned."
        else:
            return f"'{self.title}' was not checked out."

    def is_overdue(self):
        """Check if the book is overdue."""
        return (not self.available) and self.due_date and self.due_date < datetime.now()

    def __str__(self):
        status = "Available" if self.available else f"Checked out (Due {self.due_date.strftime('%Y-%m-%d')})"
        return f"{self.id}: '{self.title}' by {self.author} — {status}"


# -------- Library Management System --------
class Library:
    def __init__(self, books_data):
        self.books = [Book(**b) for b in books_data]

    # Level 1: View available books
    def list_available_books(self):
        print("\nAvailable Books:")
        available = [b for b in self.books if b.available]
        if not available:
            print("No books currently available.")
        else:
            for b in available:
                print(f"ID: {b.id} | Title: '{b.title}' | Author: {b.author}")
        print()

    # Level 2: Search by author or genre
    def search_books(self, characteristic, value):
        characteristic = characteristic.lower()
        value = value.lower()
        results = []
        for b in self.books:
            if characteristic == "author" and value in b.author.lower():
                results.append(b)
            elif characteristic == "genre" and value in b.genre.lower():
                results.append(b)
        return results

    # Level 3: Checkout
    def checkout_book(self, book_id):
        for b in self.books:
            if b.id.lower() == book_id.lower():
                print(b.checkout())
                return
        print("Book ID not found.")

    # Level 4: Return + Overdue
    def return_book(self, book_id):
        for b in self.books:
            if b.id.lower() == book_id.lower():
                print(b.return_book())
                return
        print("Book ID not found.")

    def view_overdue_books(self):
        print("\nOverdue Books:")
        overdue_books = [b for b in self.books if b.is_overdue()]
        if not overdue_books:
            print("No overdue books.")
        else:
            for b in overdue_books:
                print(f"{b.id}: '{b.title}' by {b.author} (Due {b.due_date.strftime('%Y-%m-%d')})")
        print()

    # Bonus: View top 3 most checked-out books
    def view_top_books(self):
        print("\nTop 3 Most Checked-Out Books:")
        top_books = sorted(self.books, key=lambda x: x.checkouts, reverse=True)[:3]
        for b in top_books:
            print(f"{b.title} — {b.checkouts} checkouts")
        print()

    def list_all_books(self):
        print("\nAll Books:")
        for b in self.books:
            print(b)
        print()


# -------- Menu System --------
def display_menu():
    print("\nLibrary Menu:")
    print("1. View available books")
    print("2. Search for a book")
    print("3. Checkout a book")
    print("4. Return a book")
    print("5. View overdue books")
    print("6. View top 3 most checked-out books")
    print("7. View all books")
    print("8. Quit")

def main():
    library = Library(library_books)

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1–8): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            library.list_available_books()
        elif choice == 2:
            c = input("Search by (author/genre): ").strip().lower()
            if c not in ["author", "genre"]:
                print("Invalid search type.")
                continue
            val = input("Enter search value: ").strip()
            results = library.search_books(c, val)
            if not results:
                print("No books found.")
            else:
                for b in results:
                    print(b)
        elif choice == 3:
            book_id = input("Enter book ID: ")
            library.checkout_book(book_id)
        elif choice == 4:
            book_id = input("Enter book ID: ")
            library.return_book(book_id)
        elif choice == 5:
            library.view_overdue_books()
        elif choice == 6:
            library.view_top_books()
        elif choice == 7:
            library.list_all_books()
        elif choice == 8:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


from library_books import library_books
from datetime import datetime, timedelta


# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def listAvailableBooks():
    print("\nAvailable Books: ")
    for book in library_books:
        if book.get("available")==True:
            print (f"ID: {book['id']} | Title: '{book['title']}' | Author: {book['author']}")

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_Books(characteristic, value):
    value = value.lower()
    results = []
    for book in library_books:
        if characteristic == "author" and value in book["author"].lower():
            results.append(book)
        elif characteristic == "genre" and value in book["genre"].lower():
            results.append(book)
    return results


def searchBooks():
    characteristic = input("Search by (author/genre): ").strip().lower()
    if characteristic not in ["author", "genre"]:
        print("Invalid search. Please enter an 'author' or 'genre'.")
        return
    value = input(f"Enter {characteristic} to search: "). strip().lower()
    results = search_Books(characteristic, value)
    if not results:
        print("No matching books found.")

    
    print(f"\nBooks matching {characteristic} '{value}':")
    for book in results:
        status = "available" if book["available"] else "Checked out"
        print (f"ID: {book['id']} | Title: '{book['title']}' | Author: {book['author']} | Genre: {book['genre']} | Status: {status}")

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def checkout_book(book_id):
    for book in library_books:
        if str(book["id"]) == str(book_id):
            if book["available"]:
                book["available"] = False
                book["due_date"] = datetime.now() + timedelta(weeks=2)
                book["checkouts"] += 1
                return (f"Checked out '{book['title']}' by {book['author']}. Due date is {book['due_date']}.")
            else:
                return "Book is already checked out."
    return "Book not found."

def checkoutBook():
    id = input("Enter the book's ID: ")
    print(checkout_book(id))

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def return_book(book_id):
    for book in library_books:
        if str(book["id"]) == str(book_id):
            if not book["available"]:
                book["available"] = True
                book["due_date"] = None
                return (f"Returned '{book['title']}' by {book['author']}.")
            else:
                return "Book was not checked out."
    return "Book not found."

def returnBook():
    id = input("Enter the book's ID: ")
    print(return_book(id))

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def viewOverdueBooks():
    print("\nOverdue Books: ")
    today = datetime.now()
    overdue_found = False
    for book in library_books:
        if not book["available"] and book["due_date"] and book["due_date"] < today:
            overdue_found = True
            print(f'ID: {book["id"]} | Title: "{book["title"]}" | Author: {book["author"]} | Due Date: {book["due_date"]}')
    if not overdue_found:
        print("No overdue books found.")


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
class Book:
    def __init__(self, id, title, author, genre, available=True, due_date=None, checkouts=0):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts



    def checkout(self):
        if self.available:
            self.available = False
            self.due_date = datetime.now() + timedelta(weeks=2)
            self.checkouts += 1
            return f"Checked out '{self.title}'. Due date is {self.due_date}."
        else:
            return "Book is already checked out."

    def return_book(self):
        if not self.available:
            self.available = True
            self.due_date = None
            return f"Returned '{self.title}'."
        else:
            return "Book was not checked out."

# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.
def displayMenu():
    print("\n Library Menu: ")
    print("1. View available books")
    print("2. Search for a book")
    print("3. Checkout a book")
    print("4. Return a book")
    print("5. View overdue books")
    print("6. View top three most checked out books")
    print("7. Exit")
# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!



def getChoice():
    try:
        return int(input("Enter your choice (1-7): "))
    except ValueError:
        print("Invalid input. Please enter a number listed. ")
        return getChoice()
def viewBooks():
    print("\nAll Books: ")
    for book in library_books:
        status = "Available" if book["available"] else f"Checked out"
        print(f'{book["id"]}: {book["title"]} by {book["author"]} [{status}]')

def viewPopularBooks():
    print("\nTop 3 Most Checked-Out Books: ")
    top_books = sorted(library_books, key=lambda x: x["checkouts"], reverse=True)[:3]
    for book in top_books:
        print(f'{book["title"]} — {book["checkouts"]} checkouts')

def main():
    while True:
        displayMenu()
        choice = getChoice()
        if choice == 1:
            listAvailableBooks()
        elif choice == 2:
            searchBooks()
        elif choice == 3:
            checkoutBook()
        elif choice == 4:
            returnBook()
        elif choice == 5:
            viewOverdueBooks()
        elif choice == 6:
            viewPopularBooks()
        elif choice == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 7.")

if __name__ == "__main__":
    # You can use this space to test your functions
    print(main())
    pass

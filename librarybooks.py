from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def listAvailableBooks():
    print("\nAvailable Books: ")
    for book in library_books:
        if book["Available"]:
            print (f"ID: {id} | Title: '{['title']}' | Author: {['author']}")

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def searchBooks():


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
//
def checkoutBook():
    id = input("Enter the books ID: ")
    print(checkout_book(id))

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def returnBook():
    id = input("Enter the books ID: ")
    print(return_book(id))

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def viewOverdueBooks():


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

def displayMenu():
    print("\n Library Menu: ")
    print("1. View available books")
    print("2. Search for a book")
    print("3. Checkout a book")
    print("4. Return a book/ ")
    print("5. View overdue books")
    print("6. View top three most checked out books")

def getChoice():
    try:
        return int(input("Enter your choice (1-7)"))
    except ValueError:
        print("Invalid input. Please enter a number listed. ")
        return getChoice()
def viewBooks():
    for book in library_books:
        status = "Available"
        if book["available"]
        else print("Checked out")
        print(f'{book["id"]}: {book["title"]} by {book["author"]} [{status}]')



def main();
    while True:
        displayMenu()
        choice = getChoice()
        if choice == 1:
            viewBooks()
        elif choice == 2:
            searchBooks()
        elif choice == 3:
            checkoutBook()
        elif choice == 4:
            returnBook()
        elif choice == 5:
            viewOverdueBooks()
        elif choice == 6:
            viewPopularBooks
        elif choice == 7:
            print("Goodbye!")
            break

if __name__ == "__main__":
    # You can use this space to test your functions
    pass

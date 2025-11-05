def restaurant_chatbot():
    print("Welcome to the Mexicano Resturante Chatbot!")

    name = input("What is your name?")
    age = input("How old are you?")
    print(f"Nice to meet you, {name}!")

    while True:
        print("\nHow can I help you today?")
        print("1. View the menu")
        print("2. Today's Specials")
        print("3. Place an order")
        print("4. Make a Reservation")
        print("5. Exit Chat")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_menu()
        elif choice == "2":
            show_specials()
        elif choice == "3":
            take_order(name)
        elif choice == "4":
            make_reservation(name)
        elif choice == "5":
            print(f"Goodbye, {name}! Thanks for chatting with us.")
            break
        else:
            print("Sorry, I do not understand that. Please choose an option 1-5 from the list")

def show_menu():
    print("\n Our Menu:")
    print("1. Beef Tacos - $3.00")
    print("2. Chicken Tacos - $3.00")
    print("3. Quesadilla - $3.00")
    print("4. Torta - $12.00")
    print("5. Soft Drinks - $3.00")

def show_specials():
    print("\n Today's Specials:")
    print(" Asada Fries - $12.00")
    print(" Loaded Nachos - $12.00")

def take_order(name):
    print("\nWhat would you like to order?")
    order = input("Enter item name: ")
    print(f"Thanks {name}! Your order for '{order}' has been placed.")

def make_reservation(name):
    print("\nLet's make a reservation. ")
    date = input("Enter the date (MM/DD): ")
    time = input("Enter the time (e.g., 6:00 PM): ")
    people = input("How many people? ")
    print(f"Got it! Reservation confirmed for {people} on {date} at {time}, {name}.")

    restaurant_chatbot();

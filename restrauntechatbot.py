order_list = []
total = 0.0

menu = {
    "1.beef tacos": 3.00,
    "2.chicken tacos": 3.00,
    "3.quesadilla": 3.00,
    "4.torta": 12.00,
    "5.soft drinks": 3.00,
    "6.asada fries": 12.00,
    "7.loaded nachos": 12.00
    }


def restaurant_chatbot():
    print("Welcome to the Taco Resturant Chatbot!")

#welcome the user and gather name and age
    name = input("What is your name?")
    age = input("How old are you?")
    print(f"Nice to meet you, {name}!")
#prints the menu and allows the user to choose an option
    while True:
        print("\nHow can I help you today?")
        print("1. View the menu")
        print("2. Today's Specials")
        print("3. Place an order")
        print("4. View Total")
        print("5. Pickup or Delivery")
        print("6. Make a Reservation")
        print("7. Exit Chat")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            show_menu()
        elif choice == "2":
            show_specials()
        elif choice == "3":
            take_order(name)
        elif choice == "4":
            view_total(name)
        elif choice == "5":
            pickup_or_delivery()
        elif choice == "6":
            make_reservation(name)
        elif choice == "7":
            print(f"Goodbye, {name}! Thanks for chatting with us.")
            break
        else:
            print("Sorry, I do not understand that. Please choose an option 1-7 from the list")
#displays the menu
def show_menu():
    print("\n Our Menu:")
    print("1. Beef Tacos - $3.00")
    print("2. Chicken Tacos - $3.00")
    print("3. Quesadilla - $3.00")
    print("4. Torta - $12.00")
    print("5. Soft Drinks - $3.00")
#display any specials for the user
def show_specials():
    print("\n Today's Specials:")
    print("6. Asada Fries - $12.00")
    print("7. Loaded Nachos - $12.00")

def pickup_or_delivery(name):
        print("\nWould you like pickup or delivery?")
        choice = input("Enter 'pickup' or 'delivery': ").lower()

        if choice == "pickup":
            print(f"Got it, {name}! Your order will be ready for pickup in about 20 minutes.")
        elif choice == "delivery":
            address = input("Please enter your delivery address: ")
            print(f"Thanks {name}! Your order will be delivered to {address} in about 40 minutes.")
        else:
            print("Sorry, I did not understand that. Please choose 'pickup' or 'delivery'.")

def view_total():
    global total, order_list
    if order_list:
        print("\nYour order so far:")
        for item in order_list:
            print(f" - {item.title()}")
        print(f"Total: ${total:.2f}")
    else:
        print("\nYou have not ordered anything yet.")

# takes users imput to allow them to place an order
def take_order(name):
    global total, order_list

    print("\nWhat would you like to order?")
    print("You can type 'done' when finished.")

    while True:
        order = input("Enter item name: ").lower()

        if order == "done":
            break
        elif order in menu:
            order_list.append(order)
            total += menu[order]
            print(f"Added {order.title()} - ${menu[order]:.2f} to your order.")
        else:
            print("Sorry, that item is not on the menu. Try again.")

    print(f"\nThanks {name}! You ordered: {', '.join(order_list)}.")
    print(f"Your current total is: ${total:.2f}")

# takes user input to allow the user to make a reservation
def make_reservation(name):
    print("\nLet's make a reservation. ")
    date = input("Enter the date (MM/DD): ")
    time = input("Enter the time (e.g., 6:00 PM): ")
    people = input("How many people? ")
    print(f"Got it! Reservation confirmed for {people} on {date} at {time}, {name}.")
#calls the main function to run the code
restaurant_chatbot()

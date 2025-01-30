
cart = []
prices = {
    "apple": 1.00,
    "banana": 0.50,
    "orange": 0.75,
    "bread": 2.50,
    "milk": 3.00
}

def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your shopping cart:")
        total_cost = 0
        for item in cart:
            name, quantity, price = item
            item_total = quantity * price
            print(f"{name} x {quantity} = ${item_total:.2f}")
            total_cost += item_total
        print(f"Total cost: ${total_cost:.2f}")


def add_item():
    item_name = input("Enter the item name: ").lower()
    if item_name in prices:
        quantity = int(input("Enter the quantity: "))
        cart.append((item_name, quantity, prices[item_name]))
        print(f"{quantity} {item_name}(s) added to the cart.")
    else:
        print("Item not found in the store.")


def remove_item():
    item_name = input("Enter the item name to remove: ").lower()
    found = False
    for item in cart:
        if item[0] == item_name:
            cart.remove(item)
            print(f"{item_name} removed from the cart.")
            found = True
            break
    if not found:
        print("Item not found in the cart.")


def checkout():
    view_cart()
    if cart:
        total_cost = sum(item[1] * item[2] for item in cart)
        print(f"Thank you for shopping with us! Your total is ${total_cost:.2f}.")
    else:
        print("Your cart is empty. No checkout needed.")


while True:
    print("\nShopping Cart Menu:")
    print("1. Add item to cart")
    print("2. View cart")
    print("3. Remove item from cart")
    print("4. Checkout")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        view_cart()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        checkout()
        break
    else:
        print("Invalid choice. Please try again.")
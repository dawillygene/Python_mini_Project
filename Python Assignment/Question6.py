cart = []
prices = {
    "apple": 2500, "banana": 1250, "orange": 1875, "bread": 6250, "milk": 7500,
    "rice (1kg)": 3200, "sugar (1kg)": 3500, "flour (1kg)": 2800, "eggs (tray)": 10500,
    "beef (1kg)": 12000, "chicken (whole)": 15000, "fish (1kg)": 10000, "cooking oil (1L)": 7500,
    "water (1.5L)": 1500, "soft drink (bottle)": 2500, "tea leaves (250g)": 4000, 
    "coffee (250g)": 6000, "soap (bar)": 2000, "toothpaste (tube)": 3500
}

def list_items():
    print("\nAvailable Items:")
    for item, price in prices.items():
        print(f"{item.title()} - {price} Tsh")

def view_cart():
    if not cart:
        print("\nYour cart is empty.")
    else:
        print("\nYour Shopping Cart:")
        total_cost = 0
        for item in cart:
            name, quantity, price = item
            item_total = quantity * price
            print(f"{name.title()} x {quantity} = {item_total} Tsh")
            total_cost += item_total
        print(f"Total Cost: {total_cost} Tsh")

def add_item():
    list_items()  # Show available items before adding
    item_name = input("\nEnter the item name: ").lower()
    if item_name in prices:
        quantity = int(input("Enter the quantity: "))
        cart.append((item_name, quantity, prices[item_name]))
        print(f"{quantity} {item_name}(s) added to the cart.")
    else:
        print("Item not found in the store.")

def remove_item():
    item_name = input("\nEnter the item name to remove: ").lower()
    found = False
    for item in cart:
        if item[0] == item_name:
            cart.remove(item)
            print(f"{item_name.title()} removed from the cart.")
            found = True
            break
    if not found:
        print("Item not found in the cart.")

def checkout():
    view_cart()
    if cart:
        total_cost = sum(item[1] * item[2] for item in cart)
        print(f"\nThank you for shopping with us! Your total is {total_cost} Tsh.")
    else:
        print("\nYour cart is empty. No checkout needed.")

while True:
    print("\nShopping Cart Menu:")
    print("1. View Available Items")
    print("2. Add Item to Cart")
    print("3. View Cart")
    print("4. Remove Item from Cart")
    print("5. Checkout")
    
    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        list_items()
    elif choice == "2":
        add_item()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        checkout()
        break
    else:
        print("Invalid choice. Please try again.")


menu = {
    "popcorn":2000,
    "soda": 700,
    "hot dog": 1200,
    "nachos":4500,
    "candy": 200
}


def display_menu():
    print("\nWelcome to the Concession Stand!")
    print("Menu:")
    for item, price in menu.items():
        print(f"{item.capitalize()}: Tsh{price:.2f}")


def take_order():
    order = []
    while True:
        display_menu()
        item = input("\nEnter the item you'd like to order (or 'done' to finish): ").lower()
        if item == "done":
            break
        elif item in menu:
            order.append(item)
            print(f"{item.capitalize()} added to your order.")
        else:
            print("Sorry, that item is not on the menu.")
    return order


def calculate_total(order):
    total = 0
    for item in order:
        total += menu[item]
    return total


def display_order(order, total):
    print("\nYour order:")
    for item in order:
        print(f"- {item.capitalize()}: Tsh {menu[item]:.2f}")
    print(f"Total: Tsh {total:.2f}")


def main():
    order = take_order()
    if order:
        total = calculate_total(order)
        display_order(order, total)
        print("\nThank you for your order! Enjoy your snacks!")
    else:
        print("\nYou didn't order anything. See you next time!")


if __name__ == "__main__":
    main()
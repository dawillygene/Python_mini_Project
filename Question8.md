### Pseudocode for Concession Stand Program

1. Start
2. Initialize
   - Create a dictionary `menu` to store items and their prices.
   - Create an empty list `order` to store the user's selections.
3. Display Menu
   - Print the menu with item names and prices.
4. Loop
   - While the user wants to continue ordering:
     - Prompt the user to select an item by its name.
     - If the item exists in the `menu`, add it to the `order` list.
     - If the item does not exist, display an error message.
5. Calculate Total
   - Sum the prices of all items in the `order` list.
6. Display Order and Total
   - Print all items in the `order` list.
   - Print the total cost.
7. End



Explanation of the Program

1. Menu
   - The `menu` dictionary stores items as keys and their prices as values.

2. Ordering Process
   - The `take_order` function allows the user to select items from the menu.
   - Items are added to the `order` list if they exist in the `menu`.

3. Total Calculation
   - The `calculate_total` function sums the prices of all items in the `order` list.

4. Order Display
   - The `display_order` function shows the user's selections and the total cost.

5. User Interaction
   - The user can continue ordering until they type "done".



 Example Run

Welcome to the Concession Stand!
Menu:
Popcorn: $5.00
Soda: $3.00
Hot dog: $4.50
Nachos: $6.00
Candy: $2.50

Enter the item you'd like to order (or 'done' to finish): popcorn
Popcorn added to your order.

Welcome to the Concession Stand!
Menu:
Popcorn: $5.00
Soda: $3.00
Hot dog: $4.50
Nachos: $6.00
Candy: $2.50

Enter the item you'd like to order (or 'done' to finish): soda
Soda added to your order.

Welcome to the Concession Stand!
Menu:
Popcorn: $5.00
Soda: $3.00
Hot dog: $4.50
Nachos: $6.00
Candy: $2.50

Enter the item you'd like to order (or 'done' to finish): done

Your order:
- Popcorn: $5.00
- Soda: $3.00
Total: $8.00

Thank you for your order! Enjoy your snacks!

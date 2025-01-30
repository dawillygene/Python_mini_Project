### Pseudocode for Shopping Cart Program

1. Start
2. Initialize:
   - Create an empty list `cart` to store items.
   - Create a dictionary `prices` to store item prices.
3. Loop:
   - While the user wants to continue shopping:
     - Display a menu of options:
       - Add item to cart
       - View cart
       - Remove item from cart
       - Checkout
     - Prompt the user to select an option.
4. Add Item:
   - Prompt the user to input the item name and quantity.
   - If the item exists in `prices`, add it to the `cart` with its price and quantity.
   - If the item does not exist, display an error message.
5. View Cart:
   - Display all items in the `cart` along with their quantities, prices, and total cost.
6. Remove Item:
   - Prompt the user to input the item name to remove.
   - If the item exists in the `cart`, remove it.
   - If the item does not exist, display an error message.
7. Checkout:
   - Calculate the total cost of all items in the `cart`.
   - Display the total cost and a thank-you message.
   - Exit the program.
8. End




### Example Run


Shopping Cart Menu:
1. Add item to cart
2. View cart
3. Remove item from cart
4. Checkout
Enter your choice (1-4): 1
Enter the item name: apple
Enter the quantity: 3
3 apple(s) added to the cart.

Shopping Cart Menu:
1. Add item to cart
2. View cart
3. Remove item from cart
4. Checkout
Enter your choice (1-4): 1
Enter the item name: banana
Enter the quantity: 5
5 banana(s) added to the cart.

Shopping Cart Menu:
1. Add item to cart
2. View cart
3. Remove item from cart
4. Checkout
Enter your choice (1-4): 2
Your shopping cart:
apple x 3 = $3.00
banana x 5 = $2.50
Total cost: $5.50

Shopping Cart Menu:
1. Add item to cart
2. View cart
3. Remove item from cart
4. Checkout
Enter your choice (1-4): 3
Enter the item name to remove: banana
banana removed from the cart.

Shopping Cart Menu:
1. Add item to cart
2. View cart
3. Remove item from cart
4. Checkout
Enter your choice (1-4): 4
Your shopping cart:
apple x 3 = $3.00
Total cost: $3.00
Thank you for shopping with us! Your total is $3.00.

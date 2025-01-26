

# Step 1: Displaying products info
def get_menu():
    return """
            Welcome to the Vending Machine                         

  -- Beverages--       -- Snacks --        -- Chocolates --

Coffee   $3   #1A | Lays      $2   #4D | Mars       $2   #7G
7up      $3   #2B | Doritos   $3   #5E | DairyMilk  $4   #8H
Water    $1   #3C | Cheetos   $3   #6F | Kitkat     $3   #9K
Juice    $2   #11 | Pringles  $2   #12 | Break      $1   #13
"""

# Step 2: Call the function to get and display the menu
print(get_menu())

# Step 3: Menu dictionary with item codes, their details, and stock
menu = {
    "1A": {"name": "Coffee", "price": 3, "stock": 5},
    "2B": {"name": "7up", "price": 3, "stock": 3},
    "3C": {"name": "Water", "price": 1, "stock": 10},
    "11": {"name": "Juice", "price": 2, "stock": 7},
    "4D": {"name": "Lays", "price": 2, "stock": 9},
    "5E": {"name": "Doritos", "price": 3, "stock": 10},
    "6F": {"name": "Cheetos", "price": 3, "stock": 8},
    "12": {"name": "Pringles", "price": 2, "stock": 10},
    "7G": {"name": "Mars", "price": 2, "stock": 10},
    "8H": {"name": "Dairy Milk", "price": 4, "stock": 7},
    "9K": {"name": "Kitkat", "price": 3, "stock": 10},
    "13": {"name": "Break", "price": 1, "stock": 5}
}

# Suggested combos 
suggestions = {
    "1A": "9K",  # Coffee -> Kitkat
    "2B": "4D",  # 7up -> Lays
    "3C": "6F",  # Water -> Cheetos
    "11": "8H",  # Juice -> Dairy Milk
    "4D": "7G",  # Lays -> Mars
    "5E": "2B",  # Doritos -> 7up
    "6F": "3C",  # Cheetos -> Water
    "12": "1A",  # Pringles -> Coffee
    "7G": "1A",  # Mars -> Coffee
    "8H": "11",  # Dairy Milk -> Juice
    "9K": "11",  # Kitkat -> Juice
    "13": "3C"   # Break -> Water
}

# Step: 4 Initialize total amount and selected items
total_amount = 0
selected_items = []

while True:
    # Step 5: Ask user to select an item by code
    item_code = input("\nEnter the code for the item you want to purchase: ")

    # Step 6: Check if the item code is valid
    if item_code in menu:
        selected_item = menu[item_code]

        # Step 7: Check if the item is in stock
        if selected_item["stock"] > 0:
            
            # Stwp 8: Add the item to the selected_items list and update total amount
            selected_items.append(item_code)
            total_amount += selected_item["price"]
            
            print(f"\nYou have selected {selected_item['name']} for ${selected_item['price']}.")
            
            # Step 9: Suggest a complementary item
            if item_code in suggestions:
                suggested_code = suggestions[item_code]
                suggested_item = menu[suggested_code]
                if suggested_item["stock"] > 0:
                    add_suggestion = input(f"\nWould you like to add {suggested_item['name']} for ${suggested_item['price']}? (yes/no): ").lower()
                    if add_suggestion == "yes":
                        selected_items.append(suggested_code)
                        total_amount += suggested_item["price"]
                        print(f"\n{suggested_item['name']} has been added to your purchase.")
        else:
            print(f"\nSorry, {selected_item['name']} is out of stock. Please choose another item.")

    else:
        print("\nInvalid code entered. Please try again.")

    # Step 10: Ask if the user wants to buy another item
    more_items = input("\nDo you want to purchase another item? (yes/no): ").lower()
    if more_items != "yes":
        break

# Step 11: Show selected items and total cost
print("\nYou have selected the following items:")
for code in selected_items:
    print(f"- {menu[code]['name']} for ${menu[code]['price']}")

print(f"\nTotal amount for all selected items: ${total_amount:.2f}")

# Step 12: Ask user to enter the amount to pay
amount_entered = float(input("\nPlease enter the total amount: $"))

# Step 13: Check if the entered amount is enough
while amount_entered < total_amount:
    print("\nInsufficient amount. Please enter more.")
    amount_entered += float(input("Enter additional amount: $"))

# Step 14: Handle payment success
change = amount_entered - total_amount
print("\nPurchase successful!")

if change > 0:
    print(f"Your change is ${change:.2f}.")

# Step 15: Dispense items only after payment
print("\nDispensing items...\n")
for code in selected_items:
    menu[code]["stock"] -= 1  # Reduce stock after payment
    print(f"- {menu[code]['name']} dispensed.")

# Step 16: Thank You Message
print("\nThank you for using the vending machine!")

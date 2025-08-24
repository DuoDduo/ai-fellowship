# A dictionary called store with items and their available quantities.
store = {"Biro": 20, "Ruler": 10, "Pencil": 30, "Crayon": 15, "Book": 9}

# Display available items to the customer
print(f"These are the list of items available in Rhema stores: {store}")

# Start a loop so customers can keep buying until they type 'exit'
while True:
    # Ask the user for the item they want to buy, or 'exit' to quit
    item = input("\nKindly enter the item you want to buy from the list above (or type 'exit' to quit): ").title()

    # Check if user wants to exit
    if item.lower() == "exit":
        print("Thank you for shopping with Rhema Stores!")
        break  # End the loop

    # Check if the entered item exists in the store
    if item not in store:
        print(f"Sorry, {item} is not available in the store.")

    # Check if the item exists but has zero stock
    elif store[item] == 0:
        print(f"Sorry, {item} is currently out of stock.")

    else:
        # Ask for the quantity the user wants to buy
        quantity = int(input(f"Kindly enter the quantity of {item} you want to buy: "))
        
        # Check for invalid quantity like zero
        if quantity <= 0:
            print("Quantity must be greater than zero.")

        # Check if requested quantity is more than what is available
        elif quantity > store[item]:
            print(f"Sorry, we only have {store[item]} {item}(s) left in stock.")

        else:
            # Show stock before purchase
            print("Before Purchase:", store)

            # Deduct purchased quantity from stock
            store[item] -= quantity

            # Confirm successful purchase to the customer
            print(f"Congratulations! You successfully bought {quantity} {item}(s).")

            # Show stock after purchase
            print("After Purchase:", store)

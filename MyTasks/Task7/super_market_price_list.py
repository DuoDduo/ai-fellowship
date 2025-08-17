
shopping_items = ["Fish","Egg", "Milk", "Cheese", "Meat"]
empty_price_list = []
print(shopping_items)

# Collect prices for each item (converted to int for validation)
item1 = int(input(f"Enter the price of {shopping_items[0]}: "))
item2 = int(input(f"Enter the price of {shopping_items[1]}: "))
item3 = int(input(f"Enter the price of {shopping_items[2]}: "))
item4 = int(input(f"Enter the price of {shopping_items[3]}: "))
item5 = int(input(f"Enter the price of {shopping_items[4]}: "))

# Store prices inside the list
empty_price_list.append(item1)
empty_price_list.append(item2)
empty_price_list.append(item3)
empty_price_list.append(item4)
empty_price_list.append(item5)

# Create dictionary from items and prices
shopping_list = {item: price for item, price in zip(shopping_items, empty_price_list)}

# Display the dictionary
print("\n========Super Market Price List========")
print(shopping_list)

# Show available items using .keys()
print("\nAvailable items:", list(shopping_list.keys()))

# Update a price using .update()
item_to_update = input("Enter the item you want to update: ")
new_price = int(input(f"Enter new price for {item_to_update}: "))
shopping_list.update({item_to_update: new_price})

# Display updated dictionary
print("\n======== Updated Super Market Price List========")
print(shopping_list)



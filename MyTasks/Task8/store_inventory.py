#  a dictionary called store with items and their available quantities.
store={"Biro":20, "Ruler": 10, "Pencil": 30, "Crayon": 15, "Book":9}
print(f"These are the list of items available in Rhema stores: {store}")

# Ask the user to input the item they want to buy

item=input("Kindly enter the item you want to buy from the list above: ")
quantity=int(input(f"Kindly enter the quantity of {item} you want to buy: "))

#using the assignment operator -= to update (reduce) the item quantity in the dictionary.
print("Before Purchase:", store)
store[item] -= quantity
print("After Purchase: ",store )

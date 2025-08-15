shopping_items = {"Fish","Egg", "Milk", "Cheese", "Meat","Rice"}
empty_price_list=[]
# print(shopping_items.keys())

item1= input(f"Enter the price of {shopping_items[0]}: ")
item2= input(f"Enter the price of {shopping_items[1]}: ")
item3= input(f"Enter the price of {shopping_items[2]}: ")
item4= input(f"Enter the price of {shopping_items[3]}: ")
item5= input(f"Enter the price of {shopping_items[4]}: ")

empty_price_list.append(item1)
empty_price_list.append(item2)
empty_price_list.append(item3)
empty_price_list.append(item4)
empty_price_list.append(item5)

shopping_list={shopping_items:empty_price_list for shopping_items, empty_price_list in zip(shopping_items,empty_price_list)}

shopping_items.update()

print(shopping_list)

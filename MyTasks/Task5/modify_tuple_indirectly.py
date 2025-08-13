# # Task5
# Ask a user to enter three items for their shopping list.
empty_list=[]
print("Enter 3 shopping items: ")
item1= input("Enter item 1: ")
item2= input("Enter item 2: ")
item3= input("Enter item 3: ")
empty_list.append(item1)
empty_list.append(item2)
empty_list.append(item3)

# - Store in a tuple shopping_list.
shopping_list=tuple(empty_list)

# - Convert it to a list, then ask for two more items to add.
t_shopping_list=list(shopping_list)
print("Enter 2 more shopping items: ")
item4= input("Enter item 4: ")
item5= input("Enter item 5: ")
t_shopping_list.append(item4)
t_shopping_list.append(item5)

# - Convert back to a tuple and print the updated list using join() to display items separated by " | ".
updated_item=tuple(t_shopping_list)
print("|".join(updated_item)) 
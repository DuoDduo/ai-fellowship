
# Task2
#  Create an empty list.
empty_list=[]

# - Ask the user to enter 3 shopping items (one by one).
print("Enter 3 shopping items: ")
item1= input("Enter item 1: ")
item2= input("Enter item 2: ")
item3= input("Enter item 3: ")

#  Add them to the list.
empty_list.append(item1)
empty_list.append(item2)
empty_list.append(item3)
print(empty_list)

# - Display the list as a single string, separated by commas.
print(", ".join(empty_list)) 
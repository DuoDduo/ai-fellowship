
# Task2
empty_name_list=[]
# - Ask the user for 5 best friends’ names.
print("Enter 5 of your best friends' name ")
name1= input("Enter Friend 1 name: ")
name2= input("Enter Friend 2 name: ")
name3= input("Enter Friend 3 name: ")
name4= input("Enter Friend 4 name: ")
name5= input("Enter Friend 5 name: ")
empty_name_list.append(name1)
empty_name_list.append(name2)
empty_name_list.append(name3)
empty_name_list.append(name4)
empty_name_list.append(name5)

#  Store them in a tuple friends.
friends=tuple(empty_name_list)
# - Print the tuple in reverse order.
print(friends[::-1])

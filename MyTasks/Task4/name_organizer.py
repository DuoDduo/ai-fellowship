
# task4
# - Ask the user to enter 5 names (separated by spaces).

# - Convert all names to lowercase.
empty_name_list=[]
print("Enter 5 names of students ")
name1= input("Enter Student 1 name: ").lower()
name2= input("Enter Student 2 name: ").lower()
name3= input("Enter Student 3 name: ").lower()
name4= input("Enter Student 4 name: ").lower()
name5= input("Enter Student 5 name: ").lower()
empty_name_list.append(name1)
empty_name_list.append(name2)
empty_name_list.append(name3)
empty_name_list.append(name4)
empty_name_list.append(name5)

# - Sort the list alphabetically.
empty_name_list.sort()

# - Display them one name per line.
print("\n".join(empty_name_list)) 
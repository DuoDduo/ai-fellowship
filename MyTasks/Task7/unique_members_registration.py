print("Welcome to the Unique Members Registration Portal")
print("We collect your names and unlock your hidden powers\n")

# Collect names one by one
name1 = input("Enter the first brave member's name: ")
name2 = input("Enter the second bold member's name: ")
name3 = input("Enter the third fearless member's name: ")

# Combine into a single string, then split by comma
names_list = [name1, name2, name3]
names = ",".join(names_list)

# Remove duplicates by using a set
set_of_names = set(names.split(","))

# Create dictionary {name: length}
name_dict = {name: len(name) for name in set_of_names}

print("\nRegistration Complete!")
print("Here are your legendary members and the strength of their names:\n")

# Display nicely
for name, length in name_dict.items():
    print(f"{name.strip()} : {length} letters")

print("\nOnly unique names have been accepted into the Hall of Members!")

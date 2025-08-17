# Tuples of names and contact numbers
names = ("Goodness", "Praise", "Divine")
contact_numbers = ("+234 810 123 4567", "+234 813 987 6543", "+234 809 456 7890")

# Create dictionary from tuples
contact_dict = dict(zip(names, contact_numbers))

print("Welcome to your Contact List!")
print("You can search for any of your contacts, just like in your phone.")

# Ask the user for a name
search_name = input("\nWho would you like to call today? Enter their name: ")

# Safe retrieval with .get()
result = contact_dict.get(search_name, f"Oops! '{search_name}' is not saved in your contacts.")

print(f"\nContact Lookup Result: {result}")

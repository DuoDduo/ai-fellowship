# Task 1
#  a program to take a string input from the user and display it in uppercase.
name=input("Welcome to Raiza's Hub, Please enter your name: ")
print(f"Welcome {name.upper()}, It's a delight to have you here")

# Task 2
# given the string "python", print its first and last characters.
text="Python"
print(text[0])
print(text[-1])

# Task 3
#  Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input
user_name= input("Welcome to cafe one, Please enter your user name: ")
print(f"Hello! {user_name}")

# Task 4
# a program to count the number of characters in a string without using len().
word="pronouns"
print(word.find(word[-1])+ 1)

# Task 5
# Given "Hello World", replace "World" with "Python".
message="Hello World!"
print(message.replace("World", "Python"))
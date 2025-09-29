# 7. Mixing Data Types
#  - Ask the user for:
#     - Your age (integer)
#     - Your height in meters (float)
#     - Your name (string)
# - Print a sentence using f-string showing all details in one line, making sure to type-cast where necessary.

print("==========================\n PERSONAL INFO COLLECTOR \n===========================")

name=input("Enter your Full name: ")
age=int(input("Enter your age: "))
height= float(input("Enter your height (in metres) : "))

print(f"{name} is {age} years old and is {height} meters tall. Thanks for filling the form, {name}.")
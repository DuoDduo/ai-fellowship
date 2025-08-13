#  Ask the user for their first name and age, then print a welcome message using an f-string.
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Your name is {name} and you are {age} years old, you will be {age + 1} years old next year\n ")


print("This an operation to add two numbers")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter your second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}/n")

# This talks about the restaurant and orders, customer name and order is taken and processed.  
print("This is North Kitchen Lounge, We are delighted to serve you.")

# This takes customer name
customer_name = input("Enter your name: ")

# This takes cutomer order
order = input(f"Welcome {customer_name}, What would you like to order: \n")

# Confirming customer's order
print(f"We've recived your request for {order}, It will be processed shortly...\n")
# Thanking customer for the order
print(f"Thanks for your order {customer_name}, Please come back again")





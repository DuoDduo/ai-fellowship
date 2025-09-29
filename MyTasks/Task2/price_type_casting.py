
# Task 2(Price Display with Type Casting)
# 2. Price Display with Type Casting
#  - Ask the user for the price of garri per paint in naira (as a string) and convert it to float. Display it with a message showing the amount in naira and kobo using print().

# Variables for market name, product, and date
market_name = "Olomore Market"
product = "garri per paint"
date = "10/08/2025"

# # Display welcome message
print(f"Welcome to {market_name} ")

# Display product price to float
price = (float(input(f"Please enter the price of {product} in naira as at today {date}:  ")))
print(f"The price of {product} that you entered as at today ({date}) in naira and kobo is ₦{price}")
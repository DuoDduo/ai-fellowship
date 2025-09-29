# 8. Transport Fare Calculator
#  - Ask for:
#     - Distance in km (float)
#     - Fare per km (float)
# - Calculate and display the total fare with two decimal places using `f"{value:.2f}"`.

print("\n======================================SHUTTLERS ROUTE FARE BOARD======================================")
print("Please enter details for today's trip.\n")

# Input section
route_name = input("Enter route name (e.g., Lekki to Ikeja): ")
distance = float(input("Enter distance (in km): "))
fare_per_km = float(input("Enter fare per km (₦): "))

# Calculation
total_fare = distance * fare_per_km
print("\n============= RECEIPT ===========")
print(f"Route:\t\t\t{route_name}")
print(f"Distance:\t\t{distance} km")
print(f"Fare per km:\t\t₦{fare_per_km:.2f}")
print(f"Total Fare:\t\t₦{total_fare:,.2f}")
print("======================================")
print("All fares are per passenger. Thank you for riding with Shuttlers!")
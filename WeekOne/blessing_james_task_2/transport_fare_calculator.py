# ======================================
#        SHUTTLERS ROUTE FARE BOARD
# ======================================
# Please enter details for today's trip.

# Enter route name (e.g., Lekki to Ikeja): Lekki to Yaba
# Enter distance (in km): 18.5
# Enter fare per km (₦): 120

# ============= TODAY'S FARE ===========
# Route:			Lekki to Yaba
# Distance:		18.5 km
# Fare per km:		₦120.00
# Total Fare:		₦2,220.00
# ======================================
# RECEIPT. Thank you for riding with Shuttlers!

# Shuttlers Transport Fare Calculator

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
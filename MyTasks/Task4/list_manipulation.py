
# Task 7
print("This is a list of cities in ogun state")
# Create a list of five cities.
cities = ["abeokuta", "Ilaro", "elite", "Olorunsogo", "oluwo"]
print(cities)
#  Replace the third city with a new one (entered by the user).
cities[2] = input("Enter a city to replace the third city listed: ")
print(cities)
# Remove the last city.
removed_city= cities[:-1]
# Add a new city to the beginning of the list.
removed_city.insert(0,"tollgate")
# Print the updated list.
print(removed_city)

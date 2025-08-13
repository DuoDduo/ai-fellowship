# set is an unordered collection of unique elements.
# creating sets
# using curly braces
fruits={"apple", "banana", "mango"}
print(fruits)

# using set() constructor
numbers=set([1,2,3,4])
print(numbers)

# creating an empty set (must use set(), not{})
empty_set=set()
print(empty_set)

# from a string(duplicates removed automatically)
letters=set("mississippi")
print(letters)

# set operations
# 01.adding elements
colors={"red", "blue"}
colors.add("green")
print(colors)

# 02.removing elements
colors.remove("blue")
colors.discard("yellow")
print(colors)

# 03.pop an element
colors={"red", "blue", "green"}
removed=colors.pop()
print("Removed: ", removed)
print("Remaining: ", colors)

# 04.clear a set
colors.clear()
print(colors)

# Mathematical Set Operations
set1={1,2,3,4}
set2={3,4,5,6}

# union
print(set1 | set2)
print(set1.union(set2))

# intersection
print(set1 & set2)
print(set1.intersection(set2))

# difference
print(set1 - set2)
print(set1.difference(set2))

# symmetric difference
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# Working with sets
# collecting unique visitors to an event
visitors=set()
# Adding visitors
visitors.add("Chinedu")
visitors.add("Aisha")
visitors.add("Chinendu")#duplicate, ignored automatically
print("Visitors: ", visitors)

# Checking if a visitor attended
name = "Aisha"
if name in visitors:
    print(f"{name} attended the event.")
else:
    print(f"{name} did not attend the event.")
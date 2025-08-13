empty_list=[]
print(empty_list)

empty_list2 = list()
print(empty_list2)


# List of integers
numbers=[1,2,3,4,5]
print(numbers)

# List of strings
fruits=["apple", "banana", "cherry"]
print(fruits)

# mixed data types
mixed_list=["Alice", 25, 5.8,True]
print(mixed_list)

# from a string (eaach chacrater becomes an element)
chars=list("hello")
print(chars)

# from a tuple
my_tuple=(10,20,30)
list_from_tuple=list(my_tuple)
print(list_from_tuple)

# from a range
numbers_range = list(range(5))
print(numbers_range)

# squares of numbers 0-4
squares=[x**2 for x in range(5)]

# Even numbers between 0-10
evens=[x for x in range(11) if x %2==0]
print(evens)

# creating a nested list matrix-like list
matrix=[[1,2],[3,4]]
# Accessing elements in  a nested list
print(matrix [0]) 
print(matrix[0][1])


# ordered collections
fruits=['Mango','Orange','banana']
print(fruits)       # ['mango', 'orange', 'banana']
print(fruits[0])    # mango (first element)
print(fruits[2])    # banana (third element)



# allows duplicate
items=["rice", "beans", "yam","rice"]

# mutable- can be changed
numbers=[1,2,3]
numbers[1]=20
print(numbers)

# can hold different data types
mixed=[10,"Nigeria", 3.14, True]

# can be nested
nested_list =[[1,2], ["a", "b"]]
print(nested_list[0][1])

# dynamic size
names=["Ada"]
names.append("Bola")
names.append("Chidi")
print(names)
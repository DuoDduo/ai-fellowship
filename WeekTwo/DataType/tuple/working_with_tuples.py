# A tuple is an ordered, immutable (unchangeable) collection of items in python
# creating tuples using parentheses
fruits=("apple","banana","cherry")
print(fruits)

# creating tuples without parentheses(tuple packing)
numbers= 1,2,3
print(numbers)

# single-item tuple(must include a comma)
single_item=("apple",)
print(single_item)
print(type(single_item))

# using tuple constructor
fruits_list=["apple", "banana", "cherry"]
fruits_tuple=tuple(fruits_list)
print(fruits_tuple)

# characteristics of tuple: 01. ordered
colors=("red", "green", "blue")
print(colors[0])

# # 02. Immutable
# colors[1]= "yellow"

# 03. Allow duplicates
numbers=(1,2,2,3)
print(numbers)

# 04. Mixed data types
mixed=("apple",3, True, 5.6)

# 05. Nested Tuples
nested =(("a", "b",(1, 2)))
print(nested)

# Tuple Operations
# 01. Indexing
fruits=("apple", "banana", "cherry")
print(fruits[1])
print(fruits[-1])

# 02. Slicing
print(fruits[0:2])
print(fruits[::-1])

# 03. concatenation
tuple1=(1,2)
tuple2=(3,4)
result=tuple1+ tuple2
print(result)

# 04. Repetition
nums=(1,2)
print(nums*3)

# 05. Membership
fruits=("apple", "banana", "cherry")
print("banana" in fruits)
print("grape" not in fruits)

# 06. Iteration
for fruit in fruits:
    print(fruit)

# Unpacking Tuples
# Tuples have only two methods dont count() and dot index()
numbers=(1,2,2,3,4) 
print(numbers.count(2))  #(ocunts occurence of 2)
print(numbers.index(3))  #(position of first occurence of 3)

# Converting between list and tuple
# tuple to list
t=(1,2,3)
lst=list(t)
lst.append(4)
print(lst)

# list to tuple
t=tuple(lst)
print(t)

# built-im function with Tuples
nums=(4,1,7,3)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))

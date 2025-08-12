# concatenation- joins two lists into a new list
list1=[1,2,3]
list2=[4,5]
result=list1 + list2
print(result)

# repetition(*) - repeats elements in a list a given number of times
nums=[1,2]
repeated=nums*3
print(repeated)

# Indexing- access elements using their position starting from 0
fruits=["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[-1])

# slicing- extract a portion of the list
numbers=[0,1,2,3,4,5]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])

# membership (in/not in)- checks if an element exist in a list
colors=["red", "blue", "green"]
print("green" in colors)
print("yellow" not in colors)

# length(len)- counts the number of elements in a list
items=["pen", "book", "laptop"]
print(len(items))

# min() and max()- returns the smallest or largest element
nums=[5,2,9,1]
print(min(nums))
print(max(nums))

# sum()- adds all numerical in a list
numbers=[1,2,3,4]
print(sum(numbers))

# List comprehension- creates a list in a single line
squares=[x**2 for x in range(5)]
print(squares)

# copying a list
a=[1,2,3]
b=a.copy()  #or b=list(a)
print(b)
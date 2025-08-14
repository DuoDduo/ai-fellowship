# A dictionary is a collection of key-value pairs
# creating dictionaries
# 01. using curly braces
student ={
    "name": "Ada",
    "age": 20,
    "course": "Computer Science"
}
print(student)

# 02. using the dict() constructor
student_info=dict(name="John", age=25, course="Maths")
print(student_info)

# 03. Empty dictionary
empty_dict={}
print(empty_dict)

# Dictionary Comprehension
# syntax-- {key_expression: value_expression for item in iterable if condition}
# a dictionary of numbers and squares
squares={x:x**2 for x in range(1,6)}
print(squares)

# with condition, dictionary of even numbers and their cubes
evens_cube={x:x**3 for x in range(1,10) if x%2==0}
print(evens_cube)

# from existing dictionary
students={"Ada": 85, "John":40, "Musa": 65}
# filter students who passed(score>=50)
passed_students={name:score for name,score in students.items() if score >=50}
print(passed_students)

# using string keys
names=["Ada","John","Musa"]
lengths={name:len(name) for name in names}
print(lengths)

# Accessing dictionary items
# define a dictionary
student={"name": "Ada", "age":20, "course":"Computer Science"}
# using key
print(student["name"])
# using get() method(avoids error if key is missing)
print(student.get("age"))
print(student.get("grade","Not found"))

# modifying dictionaries
student["age"]=21 
print(student)

# removing items from dictionaries
# 01. using pop()
student.pop("name")

# 02.using popitem()- removes last inserted key-value
student.popitem()
# print(student)

# 03. using del keyword
# del student["course"]

# 4. Using clear() - removes all items
student.clear()
print(student)

# Dictionary metnods-- dot keys(), dot values(), dot items(), dot update()
person={"name": "Emeka", "age":30}
# 01. keys()
print(person.keys)
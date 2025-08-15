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

# 02.values()
print(person.values())

# 03. items()
print(person.items())

# 4. update()
person.update({"age": 31, "city": "Lagos"})
print(person)

# Nested dictionaries
students = {
    "student1": {"name": "Ada", "age": 20},
    "student2": {"name": "John", "age": 22}
}

print(students["student1"]["name"])  # Access nested data

# Looping through dictionaries
# Define a dictionary
student = {"name": "Ada", "age": 20, "course": "Computer Science"}

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)  

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")      

# Storing a student's biodata
student = {
    "name": "Chinedu",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
}

print(f"Name: {student['name']}")
print(f"Subjects: {', '.join(student['subjects'])}")   

# How to add  key-value pairs to an empty dictionary
# Create an empty dictionary
student = {}

# Add key-value pairs to it
student["name"] = "Goodness"
student["Interest"] = "AI"
student["Track"] = "AI_Dev"

print(student)

# List of dictionaries - Each student has their own dictionary
students = [
    {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
    {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
    {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
]

print(students[0]["Name"])   
print(students[1]["Track"])  

# Dictionary of dictionaries - Each student is keyed by their ID
students = {
  "AI010"   :  {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
  "AI020" :  {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
  "AI030"  :  {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
}

print(students["AI020"]["Name"])   
print(students["AI030"]["Track"])

# Dictionary of lists - Each subject stores a list of scores
scores = {
    "python": [85, 78, 92],
    "pandas": [88, 74, 90],
    "Scikit-learn": [80, 95, 87]
}

print(scores["python"])    
print(scores["pandas"][1])  
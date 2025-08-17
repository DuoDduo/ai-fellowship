# Task1: Student Bio Data Storage

# Create an empty dictionary to hold student bio-data
student = {}

# Collect details from user
student["name"] = input("Enter student name: ")
student["age"] = int(input("Enter student age: ")) 
student["gender"] = input("Enter student gender: ")

# Collect courses as a list
courses = input("Enter your courses (separated by commas): ")
student["courses"] = courses.split(",")  # convert string to list

# Display bio-data neatly using escape sequences
print("\nStudent Bio Data")
print(f"Name:\t\t{student['name']}")
print(f"Age:\t\t{student['age']}")
print(f"Gender:\t\t{student['gender']}")
print("Courses:\t" + ", ".join(student["courses"]))




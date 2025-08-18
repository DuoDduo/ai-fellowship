student={}

name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
student["name"]=name
student["age"]=age
scores=[70,85,90]
student["scores"]=scores
passed= min(scores) >=50
teenage= 13 >= age >=19

print("\nStudent Record")
print(f"Name:\t\t{student['name']}")
print(f"Age:\t\t{student['age']}")
print(f"Scores:\t\t{student["scores"]}")
print(f"Passed:\t\t{passed}")
print(f"Teenage:\t{teenage}")

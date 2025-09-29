# Task 3 (School Registration Form)
# 3. School Registration Form
# - Ask for student’s name, class, and state of origin. Use string concatenation to print them in one sentence.

print("\tWELCOME TO IDEAL COLLEGE")
print("==============================================")
print("\tSTUDENT REGISTRATION FORM")
print("==============================================")
print("Please provide the following details to complete your registration.\n")

# Student details
# Ask for student’s name, 
student_name = input("Enter your full name: ")
# Ask for student’s class,
student_class = input("Enter the class you are admitted in (e.g., SS1, SS2, JSS3): ")

# Ask for student’s state of origin,
state_of_origin = input("Enter your state of origin: ")

# Output result
print("\n Registration Successful!")
print("----------------------------------------------")
print("Student " + student_name + " is in " + student_class + " and is from " + state_of_origin + " State.")
print("----------------------------------------------")
print(" Welcome to Ideal College, " + student_name + "! We’re glad to have you.\n")

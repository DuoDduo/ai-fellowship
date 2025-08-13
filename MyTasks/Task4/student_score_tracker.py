
#  Task5

# - Store the results in two lists (one for names, one for scores).
student_name=[]
student_score=[]
# Ask the user for 3 student names.
print("Enter 3 student name")
student_1_name= input("Enter student 1 name: ")
student_2_name= input("Enter student 2 name: ")
student_3_name= input("Enter student 3 name: ")

# - For each student, ask for their score.
print("Enter each student scores")
student_1_score= input(f"Enter {student_1_name} score: ")
student_2_score= input(f"Enter {student_2_name} score: ")
student_3_score= input(f"Enter {student_3_name} score: ")

student_name.append(student_1_name)
student_name.append(student_2_name)
student_name.append(student_3_name)
# - Store the results in two lists (one for names, one for scores).
student_score.append(student_1_score)
student_score.append(student_2_score)
student_score.append(student_3_score)

# - Print a formatted output showing Name — Score, aligned neatly.
print("Name\t | Score")
print(f"{student_name[0]} \t | {student_score[0]}")
print(f"{student_name[1]} \t | {student_score[1]}")
print(f"{student_name[2]} \t | {student_score[2]}")

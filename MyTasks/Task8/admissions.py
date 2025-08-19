# UNILAG ADMISSION CHECKER

# collect details from user
name=input("Enter your full name: ")
age=int(input("Enter your age: "))
utme_score=int(input('Enter your  UTME score: '))
first_choice=input("Is UNILAG your firtst choice of University (YES?NO): ").lower()
post_utme_score=int(input('Enter your POST UTME score: '))

# calcultate departmental cut off mark
departmental_cut_off= (utme_score+post_utme_score)/2
# SUBJECTS
print("Enter your O-level grades for 5 subjects (A-C is pass, D-F is Fail)")
grades=[]
english= input("Enter your grade for English: ").lower()
mathematics= input("Enter your grade for mathematics: ").lower()
subject_3= input("Enter your grade for subject 3: ").lower()
subject_4= input("Enter your grade for subject 4: ").lower()
subject_5= input("Enter your grade for subject 5: ").lower()
grades.append(english)
grades.append(mathematics)
grades.append(subject_3)
grades.append(subject_4)
grades.append(subject_5)

eligibility= (age >= 16) and(utme_score >= 200) and (post_utme_score>=50) and ( departmental_cut_off>=50) and(first_choice=="yes" ) and set(grades) <= {"a","b","c"}


print(eligibility and f"Congratulations {name}! You are eligible for admission into UNILAg" or f"Sorry {name}! You are not eligible for admission into UNILAG")
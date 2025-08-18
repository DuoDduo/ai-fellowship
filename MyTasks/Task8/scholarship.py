# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

name = input("Enter your name: ").lower()
nationality = input("Enter your nationality: ").title()
registration_status=input("Are you a registered, full-time undergraduate student in a recognized Nigerian university: ").lower()
scholarship_status=input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international ?(Yes/No) : ").lower()


print("Enter your grade in the just concluded WASSCE in 5 relevant subjects: (A,B,C,D,E)")

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

eligibility = (nationality=="Nigerian") and(registration_status=="yes") and (scholarship_status=="no" ) and set(grades) <= {"a","b"}

print(eligibility and f"Congratulations {name}! You are eligible for the federal government scholarship" or f"Sorry {name}! You are not eligible for the scholarship")
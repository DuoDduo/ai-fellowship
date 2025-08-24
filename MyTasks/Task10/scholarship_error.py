# Federal Government Scholarship
try:
    # Ask for the applicant's Basic Info
    name = input("Enter your name: ").title()
    nationality = input("Enter your nationality: ").title()
    registration_status = input("Are you a registered, full-time undergraduate student in a recognized Nigerian university? (Yes/No): ").lower()
    scholarship_status = input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry? (Yes/No): ").lower()

    # Ask for WASSCE grades
    print("Enter your grade in the just concluded WASSCE in 5 relevant subjects: (A, B, C, D, E)")
    subjects = ["English", "Mathematics", "Subject 3", "Subject 4", "Subject 5"]
    grades = []

    for subject in subjects:
        grade = input(f"Enter your grade for {subject}: ").upper()
        grades.append(grade)

    # Control flow for eligibility
    if nationality != "Nigerian":
        print(f"Sorry {name}, you must be Nigerian to be eligible.")
    elif registration_status != "yes":
        print(f"Sorry {name}, only full-time registered undergraduates are eligible.")
    elif scholarship_status != "no":
        print(f"Sorry {name}, you cannot apply if you already have another scholarship.")
    elif any(grade not in ["A", "B"] for grade in grades):
        print(f"Sorry {name}, all your grades must be A or B to be eligible.")
    else:
        print(f"Congratulations {name}! You are eligible for the federal government scholarship.")

except ValueError:
    print("Input error:. Please enter valid data.")

finally:
    print("Thank you for using the Federal Government Scholarship eligibility checker.")

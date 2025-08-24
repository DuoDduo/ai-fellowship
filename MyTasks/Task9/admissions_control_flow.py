# UNILAG ADMISSION CHECKER

while True:
    # Step 1: Collect student details
    name = input("Enter your full name: ")

    # Age Check
    age = int(input("Enter your age: "))
    if age < 16:
        print(f"Sorry {name}, you are too young for admission into UNILAG.")
        break

    # UTME Check
    utme_score = int(input('Enter your UTME score: '))
    if utme_score < 200:
        print(f"Sorry {name}, your UTME score is too low for admission into UNILAG.")
        break

    # Post-UTME Check
    post_utme_score = int(input('Enter your POST UTME score (1-100): '))
    if post_utme_score < 50:
        print(f"Sorry {name}, your Post-UTME score is too low for admission into UNILAG.")
        break

    # First Choice Check
    first_choice = input("Is UNILAG your first choice of University (yes/no): ").lower()
    if first_choice != "yes":
        print(f"Sorry {name}, UNILAG must be your first choice for admission.")
        break

    # Step 2: O-Level Grades Check
    print("Enter your O-level grades for 5 subjects (A-F):")
    grades = []
    subjects = ["English", "Mathematics", "Subject 3", "Subject 4", "Subject 5"]
    for subject in subjects:
        grade = input(f"Enter your grade for {subject}: ").lower()
        grades.append(grade)

    # Check if all grades are credit pass or better (A–C)
    if set(grades) - {"a", "b", "c"}:
        print(f"Sorry {name}, you must have at least 5 credits (A–C) including English and Math.")
        break

    # Step 3: Departmental Cut-off Check
    departmental_cut_off = (utme_score + post_utme_score) / 2
    if departmental_cut_off < 50:
        print(f"Sorry {name}, you did not meet the departmental cut-off for admission into UNILAG.")
        break

    # Step 4: Final Success Message
    print(f"Congratulations {name}! 🎉 You are eligible for admission into UNILAG.")
    break  # End loop after success

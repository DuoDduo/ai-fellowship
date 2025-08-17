print("\nWelcome to Peartree International College Student Profile Builder")
print("Please fill out the form carefully. All details will be stored in our student database.\n")

# Basic Info
name = input("Enter student's full name: ")
age = int(input("Enter student's age: "))
gender = input("Enter gender (Male/Female): ")

#Academic Scores
print("\nEnter student academic scores below:")
subjects = ("Mathematics", "English", "Biology")
scores = tuple(float(input(f"   - {subj} score: ")) for subj in subjects)

# Guardian Info
print("\nEnter guardian details:")
guardian_name = input("    - Guardian's Full Name: ")
guardian_phone = input("    - Guardian's Phone Number (+234...): ")

# Hobbies
print("\nEnter at least 3 hobbies (comma-separated). Example: reading, football, painting")
hobbies_input = input("   - Hobbies: ")
hobbies_set = set(h.strip().capitalize() for h in hobbies_input.split(","))

# Build Student Profile
student_profile = {
    "Basic Info": {
        "Name": name.title(),
        "Age": age,
        "Gender": gender.capitalize()
    },
    "Academics": {subj: score for subj, score in zip(subjects, scores)},
    "Guardian": {
        "Name": guardian_name.title(),
        "Phone": guardian_phone
    },
    "Hobbies": list(hobbies_set)
}

#Derived Data
student_profile["Academics"]["Average"] = sum(scores) / len(scores)
student_profile["Basic Info"]["Initials"] = "".join([n[0].upper() for n in name.split()])
student_profile["Hobbies Count"] = len(hobbies_set)

# Output Section
print("\n\t========PEARTREE INTERNATIONAL COLLEGE - STUDENT PROFILE========")
print(f" Name:\t\t{student_profile['Basic Info']['Name']}")
print(f" Age:\t\t{student_profile['Basic Info']['Age']}")
print(f" Gender:\t{student_profile['Basic Info']['Gender']}")
print(f" Initials:\t{student_profile['Basic Info']['Initials']}")

print("\n========Academic Scores========")
for subject, score in student_profile["Academics"].items():
    if subject != "Average":
        print(f"   {subject}: {score}")

print(f"    Average Score: {student_profile['Academics']['Average']:.2f}")

print("\n========Guardian Info========")
print(f"   Name: {student_profile['Guardian']['Name']}")
print(f"   Phone: {student_profile['Guardian']['Phone']}")

print("\n========Hobbies========")
print(f"   {', '.join(student_profile['Hobbies'])}")
print(f"   Total Hobbies: {student_profile['Hobbies Count']}")

print("\nProfile successfully created and stored in Peartree International College database!")

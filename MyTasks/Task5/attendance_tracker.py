# Task 6
# a Python program that; - Stores the days of the week in a tuple.
week_days = ("Sunday","Monday", "Tuesday", "Wednesday", "Thursday","Friday")

# a Python program that; Stores the months of the year in another tuple.
months= ("January", "February", "March", "April","May", "June","July","August","September","October","November","December" )

#  - Asks the user to enter: - Student’s name- Gender- Course Track- Current month number (1-12)- Current day number (1-7)
print("Enter the following details to track your attendance:  ")
student_name= input("Enter your name: ")
gender= input("Enter your gender: ")
course_track= input("Enter course track: ")
month_number= int(input("Enter current month number(1-12): "))
day_number= int(input("Enter current day number(1-7): "))
date= input("Enter current date number(1-31): ")

# To get the index of the weekday from week_days tuple
day= week_days[day_number-1]
# To get the index of the month from months tuple
month=months[month_number-1]

print(f"{student_name} is a {gender} in the {course_track} track,\nAttendance: present today {day}, {date} {month}, 2025. ")

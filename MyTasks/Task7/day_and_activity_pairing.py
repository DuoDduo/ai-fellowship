# a Python program that; - Stores the days of the week in a tuple.
week_days = ("Sunday","Monday", "Tuesday", "Wednesday", "Thursday","Friday")

# user inputs an activity for three specific days.
day_activity=[]
print("Enter an activity for Monday-Wednesday: ")
monday= input("Enter Monday activity: ")
tuesday= input("Enter Tuesday activity: ")
wednesday= input("Enter Wednesday activity: ")
day_activity.append(monday)
day_activity.append(tuesday)
day_activity.append(wednesday)

# Using dictionary comprehension to pair days and activities and also zip().
week_activities={week_days:day_activity for week_days, day_activity in zip(week_days,day_activity)}

# Printing the dictionary.
print(week_activities)
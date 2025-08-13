# Task4
#  Ask a user for their;
empty_user_list=[]
print("Enter Your details to complete the registration: ")

#   - First name
name= input("Enter your first name: ")
# - Age
person_age= input("Enter your age: ")
#  Favorite color
color= input("Enter your favorite color: ")
#   - Home town
town= input("Enter your home town: ")
empty_user_list.append(name)
empty_user_list.append(person_age)
empty_user_list.append(color)
empty_user_list.append(town)

#  Store them in a tuple profile and unpack into variables.
user_list=tuple(empty_user_list)
first_name,age,favorite_color,home_town=user_list

#  - Print and use  escape sequence to align each piece of information nicely.
print(f"============User Details==========\nFirst Name\t| {first_name}\nAge\t\t| {age}\nFavorite Color\t| {favorite_color}\nHome Town\t| {home_town}")
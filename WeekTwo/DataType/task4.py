#  Task 1a
quote=input("Enter your favourite quote: ")
print("\""+ quote.title() + "\"")

# Task2
empty_list=[]
print("Enter 3 shopping items: ")
item1= input("Enter item 1: ")
item2= input("Enter item 2: ")
item3= input("Enter item 3: ")
empty_list.append(item1)
empty_list.append(item2)
empty_list.append(item3)
print(empty_list)
print(", ".join(empty_list)) 

# Task3
sentence=input("Introduce yourself in one sentence: ")
print(sentence.split())
print(len(sentence)) 

# task4
empty_name_list=[]
print("Enter 5 names of students ")
name1= input("Enter Student 1 name: ").lower()
name2= input("Enter Student 2 name: ").lower()
name3= input("Enter Student 3 name: ").lower()
name4= input("Enter Student 4 name: ").lower()
name5= input("Enter Student 5 name: ").lower()
empty_name_list.append(name1)
empty_name_list.append(name2)
empty_name_list.append(name3)
empty_name_list.append(name4)
empty_name_list.append(name5)
print(" ".join(empty_name_list)) 
empty_name_list.sort()
print("\n".join(empty_name_list)) 


#  Task5
student_name=[]
student_score=[]
print("Enter 3 student name")
student_1_name= input("Enter student 1 name: ")
student_2_name= input("Enter student 2 name: ")
student_3_name= input("Enter student 3 name: ")

print("Enter each student scores")
student_1_score= input(f"Enter {student_1_name} score: ")
student_2_score= input(f"Enter {student_2_name} score: ")
student_3_score= input(f"Enter {student_3_name} score: ")

student_name.append(student_1_name)
student_name.append(student_2_name)
student_name.append(student_3_name)

student_score.append(student_1_score)
student_score.append(student_2_score)
student_score.append(student_3_score)

print("Name\t | Score")
print(f"{student_name[0]} \t | {student_score[0]}")
print(f"{student_name[1]} \t | {student_score[1]}")
print(f"{student_name[2]} \t | {student_score[2]}")


# Task 6
word=input("Enter a word: ")
print(len(word))
is_upper=word.isupper()
print(f"The word typed is in uppercase: {is_upper}")
is_lower=word.islower()
print(f"The word typed is in lowercase: {is_lower}")
is_title= word.istitle()
print(f"The word typed is in title format: {is_title}")
reversed_word=word[::-1]
print(reversed_word)

# Task 7
print("This is a list of cities in ogun state")
cities = ["abeokuta", "Ilaro", "elite", "Olorunsogo", "oluwo"]
print(cities)
cities[2] = input("Enter a city to replace the third city listed: ")
print(cities)
removed_city= cities[:-1]
removed_city.insert(0,"tollgate")
print(removed_city)



# Conditional Statements
# if statement
age=20
if age >= 18:
    print("You are elgible to vote")

# if-else statement
wallet=400
price=500

if wallet >= price:
    print("Purchase succesful")
else: 
    print("Insufficient balance")   

# if-elif-else 
score=85
if score>=70:
    print("Grade A")
elif score >=50:
    print("Grade B") 
else:
    print("Grade C")

#Nested if
age =19
citizen=True

if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else: 
    print("Too young to vote")  


#  Loops
# for loop
fruits=["apple", "banana", "orange"]
for fruits in fruits:
    print(f"I like {fruits}")


coordinates=(0.34654, -0.48585, 0.57477)
for point in coordinates:
    print(f"Point: {point}") 

student={"name":"Tunde", "age":16, "grade":"A"}
for key,value in student.items():
    print(f"{key}: {value}")    

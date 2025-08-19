

# - Explain each output of the program below.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# num1=4
# num2=5
print(f"{num1} == {num2} : {num1 == num2}")
# Output is false because num1 value is different from num2 value

print(f"{num1} != {num2} : {num1 != num2}")
# output is true because the value of num1 is not equal to the value of num2

print(f"{num1} > {num2} : {num1 > num2}")
# output is false because The value of  num1 is not greater than num2
#  
print(f"{num1} < {num2} : {num1 < num2}")
# # Output is True because The value of  num1 is less than num2

#  Give 3 usecases or scenarios where you can apply the program below.
# i. To verify students eligibility for admission into the university using age.
# ii. To verify citizen's eligibility for recruitment into the Nigeria Police force using height.
# iii. To verify student's elgibility for promotion into the next class using their test scores.


# - Write the code for 1 of the 3 use cases.

# student promotion eligibility check
passmark = 75 
student_score = 60

print(f"You passed the test : {passmark == student_score}") # False; test score is lower than expected range.
print(f"Your score is lower than the passmark : {passmark != student_score}") # True; test score is lower than passmark
print(f"You didn't met up to the passmark: {passmark < student_score}") # False; the passmark is higher than the student score.
print(f"Your test score is relatively low: {passmark > student_score}") # True; test score is lower than the pass mark.
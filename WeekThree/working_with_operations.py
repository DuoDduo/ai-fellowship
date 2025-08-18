# python operators

# comparison operators
a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=10)
print(a<=25)
print(b<=25)

# use case example
score=75
print(score >=50)
print(score<50)
print(score==100)

# assignment operators
x = 10
print("Initial value: ", x)
x +=5
print("After x += 5: ",x)
x -=2
print("After x -= 2: ", x)
x *=3
print("After x *= 3: ", x)
x /=4
print("After x /= 4: ", x)
x %=3
print("After x %= 3: ", x)

x = 4
x **=2
print("After x **=2: ", x)

x //=3
print("After x //= 3: ", x)

# use case example
balance=1000
deposit=200
withdraw=150

balance += deposit
balance -= withdraw

print("Updated Balance: ", balance)

# Logical Operators
x=10
y=20

print(x > 5 and y >15)
print(x < 5 or y > 15)
print(not(x == 10))

# use case one
age = 17
score = 85

# must be younger than 18 AND score above 80
eligible = (age < 18) and (score > 80)
print("Scholarship Eligible: ", eligible)

# Use case example2 - Event Access
age = 22
has_ticket = False

can_enter = (age >= 18) and (has_ticket or age < 25)

print("Access Granted: ", can_enter)
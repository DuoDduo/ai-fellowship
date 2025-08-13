# Task1
# - Ask the user to enter three favorite Nigerian dishes (one at a time).
nigerian_dishes=[]
print("Enter your 3 favorite Nigerian dish: ")
dish1= input("Enter dish 1: ")
dish2= input("Enter dish 2: ")
dish3= input("Enter dish 3: ")
nigerian_dishes.append(dish1)
nigerian_dishes.append(dish2)
nigerian_dishes.append(dish3)
#  - Store them in a tuple called dishes.
dishes=tuple(nigerian_dishes)

#  Print the tuple in a single line, separating items with commas.
print(", ".join(dishes)) 
# - Use the \n escape sequence to print each dish on a new line.
print("\n".join(dishes)) 
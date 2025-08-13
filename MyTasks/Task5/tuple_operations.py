# Task3
state_list=[]
# - Create a tuple of 5 Nigerian states entered by the user.
print("Enter 5 Nigerian states ")
state1= input("Enter State 1: ")
state2= input("Enter State 2: ")
state3= input("Enter State 3: ")
state4= input("Enter State 4: ")
state5= input("Enter State 5: ")
state_list.append(state1)
state_list.append(state2)
state_list.append(state3)
state_list.append(state4)
state_list.append(state5)
states=tuple(state_list)

# - Print the first state and last state.
print(states[0])
print(states[-1])
#  - Check if "Lagos" is in the tuple and print "Yes" or "No".
print("Lagos" in states)  # True
print("Lagos" not in states)
#  - Print the number of states entered
print(len(states))

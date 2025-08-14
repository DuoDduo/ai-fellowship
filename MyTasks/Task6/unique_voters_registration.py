voters={"Tola", "Louise"}
# Ask for voter names
voters_name=input("Enter your name to vote for your preferred candidate: ").title()
# Store them in a set

# If a voter tries to register twice, display a warning.
name=voters_name
if name in voters:
    print(f"{name} is registered already and you can't vote twice.")
else:
   voters.add(voters_name)  
   print(f"{name} has succesfuly registered, Happy voting.")

# After registration, display the total number of unique voters.    
print(len(voters))    
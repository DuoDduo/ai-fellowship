print("Welcome to RaizaHub Mobile Serevice")
print("   Your Trusted Naija USSD Platform!\n")

ussd_code = input("Dial your USSD code to proceed (e.g., *123#): ")

menu = "Please select an option:\n1. Check Airtime Balance\n2. Check Data Balance\n3. Buy Airtime\n4. Buy Data\n5.Exit"
print("\n" + menu)


choice = input("\nEnter your choice (1, 2, 3,4,5): ")
if choice == "1":
    selected_option = "Check Airtime Balance"
elif choice == "2":
    selected_option = "Check Data balance"
elif choice == "3":
    selected_option = "Buy Airtime"
elif choice == "4":
    selected_option = "Buy Data"    
else:
    selected_option = "Thanks for stopping by."

print(f"\nYou selected: {selected_option}")
airtime_balance= 5000
data_balance= 4741.56
amount=0.0
if choice == "1":
    print("Fetching your Airtime balance... Please wait.")
    print(f"Your current airtime balance is ₦{airtime_balance}")
elif choice == "2":
    print("Fetching your data balance... Please wait.")
    print(f"Your current data balance is ₦{data_balance}")
elif choice == "3":
    amount = float(input("Enter airtime amount in Naira (₦): "))
    print(f"Your request to purchase ₦{amount:,.2f} airtime is successful\n")
    print(f"Your new airtime balance is ₦{amount+ airtime_balance}\n") 
elif choice == "4":
    print("Please select a data plan from the option below:\n1.Monthly plan\n2. Weekly Plan\n3. Daily Plan\n4.Exit")
    
    plan_option = input("\nEnter your choice (1, 2, 3,4): ")
    if plan_option == "1":
           print("Please select one option below:\n1.5000 for 20GB\n2. 11000 for 36GB\n3. 20000 for 54GB\n4.Exit")
           if choice == "1":
            print("Y")
            print(f"Your new airtime balance is ₦{amount+ airtime_balance}\n") 
    elif plan_option == "2":
        print("Please select one option below:\n1.500 for 500MB\n2. 800 for 1GB\n3. 1000 for 1.5GB\n4.1500 for 3.5GB\n5.2500 fro 6GB")
    elif plan_option == "3":
        print("Please select one option below:\n1. 75 for 75MB\n2. 100 for 110MB\n3. 200 for 200MB\n4.350 for 500MB\n5. 500 for 1GB\n6. 750 for 2.5GB\n7. Exit")  
    else:
        selected_option = "4"
        print("Invalid option")
    

         
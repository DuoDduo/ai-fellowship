# Welcome message for the user
print("Welcome to RaizaHub Mobile Service")
print("   Your Trusted Naija USSD Platform!\n")

# Step 1: Simulate USSD Code Input
ussd_code = input("Dial your USSD code to proceed (e.g., *123#): ")

# Step 2: Display main menu options to the user
menu = """Please select an option:
1. Check Airtime Balance
2. Check Data Balance
3. Buy Airtime
4. Buy Data
5. Exit"""
print("\n" + menu)

# Step 3: Collect user's choice from menu
choice = input("\nEnter your choice (1, 2, 3, 4, 5): ")

# Initialize balances for airtime (₦) and data (MB)
airtime_balance = 5000
data_balance = 4741.56  # in MB

# Step 4: Menu Selection Handling with conditions
if choice == "1":
    # Option 1: Check Airtime Balance
    print("\nFetching your Airtime balance... Please wait.")
    print(f"Your current airtime balance is ₦{airtime_balance}")

elif choice == "2":
    # Option 2: Check Data Balance
    print("\nFetching your Data balance... Please wait.")
    print(f"Your current data balance is {data_balance}MB")

elif choice == "3":
    # Option 3: Buy Airtime - user adds funds to airtime balance
    amount = float(input("Enter airtime amount in Naira (₦): "))
    airtime_balance += amount  # Increase airtime balance by user's amount
    print(f"Your request to purchase ₦{amount:,.2f} airtime is successful.")
    print(f"Your new airtime balance is ₦{airtime_balance}\n")

elif choice == "4":
    # Option 4: Buy Data - Show submenu for data plans
    print("\nPlease select a data plan type:")
    print("1. Monthly Plan\n2. Weekly Plan\n3. Daily Plan\n4. Exit")
    plan_option = input("\nEnter your choice (1, 2, 3, 4): ")

    # Monthly Data Plans using if-elif
    if plan_option == "1":
        print("Select Monthly Plan:\n1. ₦5000 for 20GB\n2. ₦11000 for 36GB\n3. ₦20000 for 54GB\n4. Exit")
        monthly_choice = input("Enter your choice: ")

        # Check user choice and available balance before deducting airtime
        if monthly_choice == "1" and airtime_balance >= 5000:
            airtime_balance -= 5000
            data_balance += 20000
            print("20GB purchased successfully!")
        elif monthly_choice == "2" and airtime_balance >= 11000:
            airtime_balance -= 11000
            data_balance += 36000
            print("36GB purchased successfully!")
        elif monthly_choice == "3" and airtime_balance >= 20000:
            airtime_balance -= 20000
            data_balance += 54000
            print("54GB purchased successfully!")
        else:
            print("Insufficient balance or exiting Monthly Plans.")

    # Weekly Data Plans using if-elif
    elif plan_option == "2":
        print("Select Weekly Plan:\n1. ₦500 for 500MB\n2. ₦800 for 1GB\n3. ₦1000 for 1.5GB\n4. ₦1500 for 3.5GB\n5. ₦2500 for 6GB\n6. Exit")
        weekly_choice = input("Enter your choice: ")

        # Check user choice and balance for weekly plans
        if weekly_choice == "1" and airtime_balance >= 500:
            airtime_balance -= 500
            data_balance += 500
            print("500MB purchased successfully for ₦500!")
        elif weekly_choice == "2" and airtime_balance >= 800:
            airtime_balance -= 800
            data_balance += 1000
            print("1GB purchased successfully for ₦800!")
        elif weekly_choice == "3" and airtime_balance >= 1000:
            airtime_balance -= 1000
            data_balance += 1500
            print("1.5GB purchased successfully for ₦1000!")
        elif weekly_choice == "4" and airtime_balance >= 1500:
            airtime_balance -= 1500
            data_balance += 3500
            print("3.5GB purchased successfully for ₦1500!")
        elif weekly_choice == "5" and airtime_balance >= 2500:
            airtime_balance -= 2500
            data_balance += 6000
            print("6GB purchased successfully for ₦2500!")
        else:
            print("Insufficient balance or exiting Weekly Plans.")

    # Daily Data Plans using if-elif
    elif plan_option == "3":
        print("Select Daily Plan:\n1. ₦75 for 75MB\n2. ₦100 for 110MB\n3. ₦200 for 200MB\n4. ₦350 for 500MB\n5. ₦500 for 1GB\n6. ₦750 for 2.5GB\n7. Exit")
        daily_choice = input("Enter your choice: ")

        # Check user choice and balance for daily plans
        if daily_choice == "1" and airtime_balance >= 75:
            airtime_balance -= 75
            data_balance += 75
            print("75MB purchased successfully for ₦75!")
        elif daily_choice == "2" and airtime_balance >= 100:
            airtime_balance -= 100
            data_balance += 110
            print("110MB purchased successfully for ₦100!")
        elif daily_choice == "3" and airtime_balance >= 200:
            airtime_balance -= 200
            data_balance += 200
            print("200MB purchased successfully for ₦200!")
        elif daily_choice == "4" and airtime_balance >= 350:
            airtime_balance -= 350
            data_balance += 500
            print("500MB purchased successfully for ₦350!")
        elif daily_choice == "5" and airtime_balance >= 500:
            airtime_balance -= 500
            data_balance += 1000
            print("1GB purchased successfully for ₦500!")
        elif daily_choice == "6" and airtime_balance >= 750:
            airtime_balance -= 750
            data_balance += 2500
            print("2.5GB purchased successfully for ₦750!")
        else:
            print("Insufficient balance or exiting Daily Plans.")

    else:
        # Exiting data plan menu if user selects 4 or invalid option
        print("Exiting Data Plan menu...")

else:
    # Exit Option from main menu if user selects 5
    print("Thanks for stopping by. Goodbye!")

# Final balances displayed after all transactions
print(f"\nFinal Airtime Balance: ₦{airtime_balance}")
print(f"Final Data Balance: {data_balance}MB")

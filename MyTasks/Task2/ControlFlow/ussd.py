print("Welcome to RaizaHub Mobile Service")
print("   Your Trusted Naija USSD Platform!\n")

# Step 1: USSD Code Input
ussd_code = input("Dial your USSD code to proceed (e.g., *123#): ")

# Step 2: Menu Display
menu = """Please select an option:
1. Check Airtime Balance
2. Check Data Balance
3. Buy Airtime
4. Buy Data
5. Exit"""
print("\n" + menu)

# Step 3: User Choice
choice = input("\nEnter your choice (1, 2, 3, 4, 5): ")
airtime_balance = 5000
data_balance = 4741.56  # in MB

# Step 4: Menu Selection Handling
if choice == "1":
    print("\nFetching your Airtime balance... Please wait.")
    print(f"Your current airtime balance is ₦{airtime_balance}")

elif choice == "2":
    print("\nFetching your Data balance... Please wait.")
    print(f"Your current data balance is {data_balance}MB")

elif choice == "3":
    amount = float(input("Enter airtime amount in Naira (₦): "))
    airtime_balance += amount
    print(f"Your request to purchase ₦{amount:,.2f} airtime is successful.")
    print(f"Your new airtime balance is ₦{airtime_balance}\n")

elif choice == "4":
    print("\nPlease select a data plan type:")
    print("1. Monthly Plan\n2. Weekly Plan\n3. Daily Plan\n4. Exit")
    plan_option = input("\nEnter your choice (1, 2, 3, 4): ")

    # Monthly Plans
    if plan_option == "1":
        print("Select Monthly Plan:\n1. ₦5000 for 20GB\n2. ₦11000 for 36GB\n3. ₦20000 for 54GB\n4. Exit")
        monthly_choice = input("Enter your choice: ")
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

    # Weekly Plans
    elif plan_option == "2":
        print("Select Weekly Plan:\n1. ₦500 for 500MB\n2. ₦800 for 1GB\n3. ₦1000 for 1.5GB\n4. ₦1500 for 3.5GB\n5. ₦2500 for 6GB\n6. Exit")
        weekly_choice = input("Enter your choice: ")
        prices = {"1": (500, 500), "2": (800, 1000), "3": (1000, 1500), "4": (1500, 3500), "5": (2500, 6000)}
        if weekly_choice in prices and airtime_balance >= prices[weekly_choice][0]:
            cost, data = prices[weekly_choice]
            airtime_balance -= cost
            data_balance += data
            print(f"{data}MB purchased successfully for ₦{cost}!")
        else:
            print("Insufficient balance or exiting Weekly Plans.")

    # Daily Plans
    elif plan_option == "3":
        print("Select Daily Plan:\n1. ₦75 for 75MB\n2. ₦100 for 110MB\n3. ₦200 for 200MB\n4. ₦350 for 500MB\n5. ₦500 for 1GB\n6. ₦750 for 2.5GB\n7. Exit")
        daily_choice = input("Enter your choice: ")
        daily_prices = {"1": (75, 75), "2": (100, 110), "3": (200, 200), "4": (350, 500), "5": (500, 1000), "6": (750, 2500)}
        if daily_choice in daily_prices and airtime_balance >= daily_prices[daily_choice][0]:
            cost, data = daily_prices[daily_choice]
            airtime_balance -= cost
            data_balance += data
            print(f"{data}MB purchased successfully for ₦{cost}!")
        else:
            print("Insufficient balance or exiting Daily Plans.")

    else:
        print("Exiting Data Plan menu...")

# Exit Option
else:
    print("Thanks for stopping by. Goodbye!")

# Show balances after any transaction
print(f"\nFinal Airtime Balance: ₦{airtime_balance}")
print(f"Final Data Balance: {data_balance}MB")

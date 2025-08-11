print("Welcome to RaizaHub Mobile Service")
print("   Your Trusted Naija USSD Platform!\n")

ussd_code = input("Dial your USSD code to proceed (e.g., *123#): ")

menu = "Please select an option:\n1. Check Balance\n2. Buy Airtime\n3. Buy Data"
print("\n" + menu)

choice = input("\nEnter your choice (1, 2, or 3): ")

if choice == "1":
    selected_option = "Check Balance"
elif choice == "2":
    selected_option = "Buy Airtime"
elif choice == "3":
    selected_option = "Buy Data"
else:
    selected_option = "Invalid Option"

print(f"\nYou selected: {selected_option}")
# 
amount = 0.0
if choice == "2" or choice == "3":
    amount = float(input("Enter amount in Naira (₦): "))
    print(f"Processing ₦{amount:,.2f} for your {selected_option}...\n")

if choice == "1":
    print("Fetching your balance... Please wait.")
    print("Your current balance is ₦15,000.00\n")
elif choice == "2" or choice == "3":
    print(f"Success! ₦{amount:,.2f} credited to your {selected_option}.\n")
else:
    print("Invalid choice entered. Please restart and try again.\n")

print("Thank you for choosing RaizaHub. Stay connected, stay empowered!")
print("Need help? Call 0800-RAIZAHUB or visit www.raizahub.com\n")

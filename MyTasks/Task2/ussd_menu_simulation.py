# 12. Simulated USSD Menu Interaction
#  - You are to design a mock USSD interface for a mobile service.
#  - Requirements:
#    1. When the user runs the program, display a welcome screen with a Nigerian context greeting.
#    2. Ask the user to "dial" a USSD code (e.g., *123#) and store it in a variable.
#    3. Print a menu with at least 3 options (e.g., "Check Balance", "Buy Airtime", "Buy Data") using newline escape sequences `(\n)` for formatting.
#    4. Ask the user to choose an option (1, 2, or 3) and store their choice in a variable.
#    5. Use f-strings and/or concatenation to display a confirmation message showing the selected option.
#    6. Ask for an amount (if applicable) and store it as a number using type casting.
#    7. Display a final message summarizing the transaction.


print("Welcome to RaizaHub Mobile Service")
print("Your Trusted Naija USSD Platform!\n")

ussd_code = input("Dial your USSD code to proceed (e.g., *123#): ")

menu = "Please select an option:\n1. Check Data Balance\n2. Check Mifi Balance\n3. Check Router Balance"
print("\n" + menu)

choice = input("\nEnter your choice (1, 2, or 3): ")
print(f"You selected option {choice}")
print("Your data balance is 25.00GB")
print("Thank you for choosing RaizaHub. Stay connected, stay empowered!")
print("Need help? Call 0800-RAIZAHUB or visit www.raizahub.com\n")
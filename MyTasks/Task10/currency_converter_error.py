# ==============================================
#          NAIJAFX EXCHANGE SERVICES
#     Accurate & Reliable Currency Converter
# ==============================================

print("====================NAIJAFX EXCHANGE SERVICES======================")
print("\t\tAccurate and Reliable Currency Converter")
print("Welcome! Manage your Naira and convert to USD or GBP instantly.\n")

# starting balance
balance = 500000.0

#exchange rates
USD_RATE = 0.0026  # Naira to USD
GBP_RATE = 0.0021  # Naira to GBP

#transaction history
transaction_history = []

# control flow
while True:
    try:
        # Display current balance and menu
        print(f"\nYour current balance is: ₦{balance:,.2f}")
        print("What would you like to do?")
        print("1. Convert Naira to USD or GBP")
        print("2. Convert USD or GBP to Naira")
        print("3. Deposit Naira to your balance")
        print("4. View transaction history")
        print("5. Exit")

        main_choice = input("Enter 1, 2, 3, 4, or 5: ")

        # Option 1: Naira to USD/GBP
        if main_choice == "1":
            naira_to_convert = float(input("Enter amount in Naira (₦) to convert: "))
            if naira_to_convert <= 0:
                print("Amount must be greater than 0.")
                continue
            if naira_to_convert > balance:
                print(f"Insufficient balance. Your current balance is ₦{balance:,.2f}")
                continue

            print("\nChoose conversion option:")
            print("1. Convert to US Dollars only")
            print("2. Convert to British Pounds only")
            print("3. Convert to both USD and GBP")
            choice = input("Enter 1, 2, or 3: ")

            print("\n=========================Conversion Summary========================")
            print("Currency \t\t\t| \tAmount")
            print(f"Nigeria (₦)\t\t\t|\t₦{balance:,.2f}")

            if choice == "1":
                usd_amount = naira_to_convert * USD_RATE
                balance -= naira_to_convert
                print(f"US Dollars ($)\t\t\t|\t${usd_amount:,.2f}")
                transaction_history.append(f"Converted ₦{naira_to_convert:,.2f} to ${usd_amount:,.2f}")
            elif choice == "2":
                gbp_amount = naira_to_convert * GBP_RATE
                balance -= naira_to_convert
                print(f"British Pounds (£)\t\t|\t£{gbp_amount:,.2f}")
                transaction_history.append(f"Converted ₦{naira_to_convert:,.2f} to £{gbp_amount:,.2f}")
            elif choice == "3":
                usd_amount = naira_to_convert * USD_RATE
                gbp_amount = naira_to_convert * GBP_RATE
                balance -= naira_to_convert
                print(f"US Dollars ($)\t\t\t|\t${usd_amount:,.2f}")
                print(f"British Pounds (£)\t\t|\t£{gbp_amount:,.2f}")
                transaction_history.append(f"Converted ₦{naira_to_convert:,.2f} to ${usd_amount:,.2f} and £{gbp_amount:,.2f}")
            else:
                print("Invalid choice. No conversion performed.")
                continue
            print(f"Remaining balance in Naira: ₦{balance:,.2f}")

        # Option 2: USD/GBP to Naira
        elif main_choice == "2":
            print("\nChoose currency to convert to Naira:")
            print("1. US Dollars ($)")
            print("2. British Pounds (£)")
            currency_choice = input("Enter 1 or 2: ")

            if currency_choice == "1":
                usd_amount = float(input("Enter amount in USD ($) to convert to Naira: "))
                if usd_amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
                naira_equiv = usd_amount / USD_RATE
                balance += naira_equiv
                print(f"${usd_amount:,.2f} = ₦{naira_equiv:,.2f}")
                transaction_history.append(f"Converted ${usd_amount:,.2f} to ₦{naira_equiv:,.2f}")

            elif currency_choice == "2":
                gbp_amount = float(input("Enter amount in GBP (£) to convert to Naira: "))
                if gbp_amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
                naira_equiv = gbp_amount / GBP_RATE
                balance += naira_equiv
                print(f"£{gbp_amount:,.2f} = ₦{naira_equiv:,.2f}")
                transaction_history.append(f"Converted £{gbp_amount:,.2f} to ₦{naira_equiv:,.2f}")
            else:
                print("Invalid choice.")
                continue

            print(f"Updated balance in Naira: ₦{balance:,.2f}")

        # Option 3: Deposit Naira
        elif main_choice == "3":
            deposit_amount = float(input("Enter amount to deposit in Naira (₦): "))
            if deposit_amount <= 0:
                print("Deposit amount must be greater than 0.")
                continue
            balance += deposit_amount
            print(f"Deposit successful! Your new balance is ₦{balance:,.2f}")
            transaction_history.append(f"Deposited ₦{deposit_amount:,.2f}")

        # Option 4: View transaction history
        elif main_choice == "4":
            if not transaction_history:
                print("No transactions yet.")
            else:
                print("\n=================Transaction History=================")
                for i, transaction in enumerate(transaction_history, start=1):
                    print(f"{i}. {transaction}")
                print("====================================================")

        # Option 5: Exit program
        elif main_choice == "5":
            print("Exiting the converter. Thank you for choosing NaijaFX!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")

    finally:
        print("NAIJAFX EXCHANGE SERVICES Accurate & Reliable Currency Converter\n")

#printing the title of the  

print("====================NAIJAFX EXCHANGE SERVICES======================\n\t\tAccurate and Reliable Currency Converter\n====================================================================")
print("Welcome! Convert your Naira to USD or GBP instantly.\nPlease enter the amount and current exchange rates below.")

naira= float(input("Enter amount in naira (₦) "))
dollars= float(input("Enter exchange rate to US Dollars (₦ to $)"))
pounds=float(input("Enter exchange rate to British Pounds (₦ to £)\n"))
dollar_exchange= naira/dollars
pound_exchange= naira/pounds
input(f"You're about to convert ₦{naira} to dollars and pounds at the rate of ${dollars} per USD and £{pounds} per pounds\n Enter yes to continue:  ")

print("=========================Conversion Summary========================")
print("Currency \t\t\t| \tAmount")
print("------------------------------------------------------------")
print(f"Nigeria (₦)\t\t\t|\t₦{naira:,.2f}")
print(f"US Dollars ($)\t\t\t|\t${dollar_exchange:,.2f}")
print(f"British Pounds (£)\t\t|\t£{pound_exchange:,.2f}")
print("------------------------------------------------------------")


print("Thank you for choosing NaijaFX Exchange Services!")
print("Visit us at www.naijafx.com or call 0800-NAIJA-FX for assistance.")
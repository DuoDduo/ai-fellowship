# ==============================================
#          NAIJAFX EXCHANGE SERVICES
#     Accurate & Reliable Currency Converter
# ==============================================

# Welcome! Convert your Naira to USD or GBP instantly.
# Please enter the amount and current exchange rates below.

# Enter amount in Naira (₦): 500000
# Enter exchange rate to US Dollars (₦ to $): 0.0026
# Enter exchange rate to British Pounds (₦ to £): 0.0021

# -------------------- Conversion Summary --------------------
# Currency                |       Amount
# ------------------------------------------------------------
# Nigeria (₦)             |       ₦500,000.00
# US Dollars ($)          |       $1,300.00
# British Pounds (£)      |       £1,050.00
# ------------------------------------------------------------


# Thank you for choosing NaijaFX Exchange Services!
# Visit us at www.naijafx.com or call 0800-NAIJA-FX for assistance.
# # 

print("====================NAIJAFX EXCHANGE SERVICES======================\n\t\tAccurate and Reliable Currency Converter\n====================================================================")
print("Welcome! Convert your Naira to USD or GBP instantly.\nPlease enter the amount and current exchange rates below.")

naira= float(input("Enter amount in naira (₦) "))
dollars= float(input("Enter exchange rate to US Dollars (₦ to $)"))
pounds=float(input("Enter exchange rate to British Pounds (₦ to £)\n"))

print("=========================Conversion Summary========================")
print("Currency \t\t\t| \tAmount")
print("------------------------------------------------------------")
print(f"Nigeria (₦)\t\t\t|\t₦{naira:,.2f}")
print(f"US Dollars ($)\t\t\t|\t${dollars:,.2f}")
print(f"British Pounds (£)\t\t|\t£{pounds:,.2f}")
print("------------------------------------------------------------")


print("Thank you for choosing NaijaFX Exchange Services!")
print("Visit us at www.naijafx.com or call 0800-NAIJA-FX for assistance.")
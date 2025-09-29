#6. Electricity Bill Formatter
#  - Ask for:
#    - Customer’s full name
#    - Units consumed (kWh) – integer
#    - Cost per unit – float
# - Calculate the total bill and print it in a neatly formatted receipt using escape sequences for line breaks.

print("PHCN- POWER HOLDING COMPANY OF NIGERIA\n===================================")
customer_name=input("Enter your full name: ")
bill_month=input("Enter billing month e.g December: ")
unit_consumed=int(input("Enter units consumed (kWh): "))
cost_per_unit = float(input("Enter cost per unit (₦): \n"))

print("ELECTRICITY CONSUMPTION BILL\n=============================")
print(f"Customer Name: {customer_name}\n Bill Month: {bill_month}\n Units Consumed: {unit_consumed}\n Cost per Unit: {cost_per_unit}\n Total Amount: {(unit_consumed*cost_per_unit)}\n Kindly pay on time to PHCN ACCOUNT: 1029246789 (ZENITH BANK) avoid disconnection. \n Thanks for your prompt payment")
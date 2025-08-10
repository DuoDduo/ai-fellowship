# 	PHCN - POWER HOLDING COMPANY OF NIGERIA
# 	----------------------------------------
# Enter your full name: Adeola Johnson
# Enter your account number: 10293847
# Enter bill date (DD/MM/YYYY): 10/08/2025
# Enter units consumed (kWh): 250
# Enter cost per unit (₦): 65.5

# 	ELECTRICITY CONSUMPTION BILL
# 	========================================
# 	Customer Name:	Adeola Johnson
# 	Account No.:	10293847
# 	Bill Date:	10/08/2025
# 	Units Consumed:	250 kWh
# 	Cost per Unit:	₦65.5
# 	Total Amount:	₦16,375.00
# 	========================================
# 	Please pay before the due date to avoid disconnection.
# 	Thank you for your prompt payment.
# # 

print("PHCN- POWER HOLDING COMPANY OF NIGERIA\n===================================")
customer_name=input("Enter your full name: ")
bill_month=input("Enter billing month e.g December: ")
unit_consumed=int(input("Enter units consumed (kWh): "))
cost_per_unit = float(input("Enter cost per unit (₦): \n"))

print("ELECTRICITY CONSUMPTION BILL\n=============================")
print(f"Customer Name: {customer_name}\n Bill Month: {bill_month}\n Units Consumed: {unit_consumed}\n Cost per Unit: {cost_per_unit}\n Total Amount: {(unit_consumed*cost_per_unit)}\n Kindly pay on time to PHCN ACCOUNT: 1029246789 (ZENITH BANK) avoid disconnection. \n Thanks for your prompt payment")
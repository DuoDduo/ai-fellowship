# 5. Daily Market Report
# Ask the user to input:
#  - Market name
#  - Number of traders
#  - Daily revenue in naira
# - Display the result using f-string formatting with commas for thousands separator.

print("WELOCME TO NIGERIA MARKET WATCH")
print("==========================")
print("Please enter today's market update: ")
market_name=input("Enter market name: ")
traders=int(input("Enter number of traders: "))
revenue=float(input("Enter otal daily revenue of all traders in naira: "))
print(f" DAILY MARKET REPORT\n====================\n Market Name: {market_name}\n Number of Traders: {traders} \n Daily Revenue:{revenue} \n On average, each trader at {market_name} made ₦{(revenue/traders):,.2f} today.\n Thank you for staying informed with Nigeria Market Watch " )

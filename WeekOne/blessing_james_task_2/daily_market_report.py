#  WELCOME TO NIGERIA MARKET WATCH 
# =====================================
# Please enter today's market update:

# Enter market name: Mile 12 International Market
# Enter number of traders: 1520
# Enter daily revenue in naira: 2450000

# DAILY MARKET REPORT
# ======================
# Market Name: Mile 12 International Market
# Number of Traders: 1,520
# Total Daily Revenue: ₦2,450,000.00

#  On average, each trader at Mile 12 International Market made ₦1,611.84 today.
# Thank you for staying informed with Nigeria Market Watch!
# # 

print("WELOCME TO NIGERIA MARKET WATCH")
print("==========================")
print("Please enter today's market update: ")
market_name=input("Enter market name: ")
traders=int(input("Enter number of traders: "))
revenue=float(input("Enter otal daily revenue of all traders in naira: "))
print(f" DAILY MARKET REPORT\n====================\n Market Name: {market_name}\n Number of Traders: {traders} \n Daily Revenue:{revenue} \n On average, each trader at {market_name} made ₦{(revenue/traders):,.2f} today.\n Thank you for staying informed with Nigeria Market Watch " )

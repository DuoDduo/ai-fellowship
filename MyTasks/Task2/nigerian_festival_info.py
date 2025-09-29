# 9. Nigerian Festival Info
#  - Ask for:
#      - Festival name (string)
#      - Location (string)
#      - Month held (string)
# - Display the info with quotation marks around the festival name using escape sequences `(\")`.

print("\n======================================FEDERAL MINISTRY OF INFORMATION & CULTURE OFFICIAL CULTURAL HERITAGE NOTICE======================================")
print("To get information about a Nigerian cultural festival,please provide the following details.\n")
festival_name=input("Enter the festival name: ")
location=input("Enter the location (city/state): ")
month=input("Enter the month it is held: ")

print("\n========================================")
print(f"Official Notice: The \"{festival_name}\" Festival will be celebrated in {location} this {month}.This annual event showcases Nigeria's rich cultural heritage, attracting both local and international visitors. Mark your calendar and be part of the celebration!")


# 10. School Fees Breakdown
#   - Ask for:
#     - School name
#     - Tuition fee (float)
#     - Hostel fee (float)
#     - Feeding fee (float)

# - Calculate the total and print it in receipt format with each fee on a new line.

# printing the title
print("\n=====================SCHOOL FEES RECEIPT GENERATOR =========================\n")

# Input
school_name = input("Enter your school name: ")
tuition_fee = float(input("Enter tuition fee  (₦): "))
hostel_fee = float(input("Enter hostel fee (₦): "))
feeding_fee = float(input("Enter feeding fee (₦): \n"))


# Calculate total
total_fee = tuition_fee + hostel_fee + feeding_fee

# printing the receipt
print(f"==================={school_name.upper()}=====================")
print(f"Tuition Fee:  \t₦{tuition_fee:,.2f}")
print(f"Hostel Fee: \t₦{hostel_fee:,.2f}")
print(f"Feeding Fee: \t₦{feeding_fee:,.2f}")
print("==============================================")
print(f"Total Fee: \t₦{total_fee:,.2f}\n")
print("==============================================")

print("Thank you for your payment. Wishing you a great academic session!")

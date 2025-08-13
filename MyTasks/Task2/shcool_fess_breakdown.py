# ========================================
#         OFFICIAL SCHOOL FEES RECEIPT
# ========================================

# Enter the school name: Ideal College
# Enter tuition fee (₦): 85000
# Enter hostel fee (₦): 40000
# Enter feeding fee (₦): 30000

# ----------------------------------------
# School: Ideal College
# Receipt No: RCPT2025001
# Date: 10-Aug-2025
# ----------------------------------------
# Tuition Fee:     ₦85,000.00
# Hostel Fee:      ₦40,000.00
# Feeding Fee:     ₦30,000.00
# ----------------------------------------
# Total Fee:       ₦155,000.00
# ----------------------------------------
# Thank you for your payment. Wishing you a great academic session!


print("\n=====================SCHOOL FEES RECEIPT GENERATOR =========================\n")

# Input
school_name = input("Enter your school name: ")
tuition_fee = float(input("Enter tuition fee  (₦): "))
hostel_fee = float(input("Enter hostel fee (₦): "))
feeding_fee = float(input("Enter feeding fee (₦): \n"))


# Calculate total
total_fee = tuition_fee + hostel_fee + feeding_fee


print(f"==================={school_name.upper()}=====================")
print(f"Tuition Fee:  \t₦{tuition_fee:,.2f}")
print(f"Hostel Fee: \t₦{hostel_fee:,.2f}")
print(f"Feeding Fee: \t₦{feeding_fee:,.2f}")
print("==============================================")
print(f"Total Fee: \t₦{total_fee:,.2f}\n")
print("==============================================")

print("Thank you for your payment. Wishing you a great academic session!")

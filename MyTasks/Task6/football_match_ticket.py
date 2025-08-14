# **Task3: Simulate a football match ticket system**

# - Store all seat numbers (1 to 50) in a set.

seat_number = set(range(1,51))
# print(seat_number)

ticket=int(input("Enter a number between 1-50 to book a seat: "))
#  Remove booked seats from the set.
seat_number.discard(ticket)
booked_seat=seat_number

# - Show remaining seats after each booking.
print(f"This is the remaining seat numbers after seat{booked_seat} has been booked")
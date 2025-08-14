# Collecting unique attendees to an event
attendees = set()

# Adding attendees
attendees.add("Taiwo")
attendees.add("Bolu")
attendees.add("Gold") 
attendees.add("Praise")
attendees.add("Divine")
attendees.add("Justina")
new_attendee=input("Enter your name: ")
attendees.add(new_attendee)

# displays them in alphabetical order.
sorted_attendee=sorted(attendees)
print("This is the list of names registered for the seminar:", sorted_attendee)

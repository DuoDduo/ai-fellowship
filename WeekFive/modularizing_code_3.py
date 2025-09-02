# creating class

class Baby:
    def __init__(self, child_name,gender, parent_name, state_of_origin):
        self.child_name = child_name
        self.gender = gender
        self.parent_name = parent_name
        self.date_of_birth = self.birthday()
        self.state_of_origin = state_of_origin
        print(f"Baby {child_name}, Gender:{gender}, whose parents are Mr. and Mrs. {parent_name} and was born {self.date_of_birth} all hail from {state_of_origin}" )   

    def birthday(self):
        from datetime import date
        today = date.today()
        return today    

# creating a student object
Dominion= Baby("Dominion James","Female", "James", "Ogun State")

# accessing attributes
print(Dominion.child_name)
print(Dominion.parent_name)
print(Dominion.state_of_origin)
print(Dominion.date_of_birth)



class Student:
    def __init__(self,name,course,level):
        print("Creating a new student...")
        self.name=name
        self.course = course
        self.level = level
        print(f"Student {name} has been created!")



kemi = Student("Kemi Adebayo", "Computer Science", 300)

# how init and self work together
# `self` is a reference to the specific object you're working with. It's like saying "this particular student" or "this specific bank account."
class NigerianStudent:
    def __init__(self, name, state, course):
        print(f"Step 1: Creating student object...")
        self.name = name           # Step 2: Assign name to THIS object
        self.state_of_origin = state    # Step 3: Assign state to THIS object
        self.course = course       # Step 4: Assign course to THIS object
        self.student_id = self.generate_id()  # Step 5: Generate ID for THIS object
        print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")

    def generate_id(self):
        import random
        return f"UNISAIL{random.randint(1000,9999)}"   

ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")     
print(ayo.name)
print(ayo.student_id)
        
class PhoneUser:
    def __init__(self,name,network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{self.name} joined {self.network} network")

    def buy_airtime(self,amount):
        self.airtime += amount    
        return f"{self.name} now has ₦{self.airtime} airtime"
    

# Creating multiple users
abeeb = PhoneUser("Abeeb Bakare", "MTN")     
onisemo = PhoneUser("Onisemo Williams", "Airtel")      

# each person's actions affect only their own account
print(abeeb.buy_airtime(500))
print(onisemo.buy_airtime(1000))
print(abeeb.airtime)
print(onisemo.airtime)

class Student:
    def __init__(self, name, course, level, state_of_origin):
        self.name = name
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin
        self.cgpa = 0.0
        print(f"Name: {name}, Course: {course}, level: {level}, State:{state_of_origin}, CGPA: {self.cgpa}")

    def get_cgpa(self,grade):
        self.cgpa += grade
        return self.cgpa

# creating a student object
Fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun State")

# accessing attributes
print(Fathia.get_cgpa(4.7))
print(Fathia.course)
print(Fathia.state_of_origin)

# # instance attributes
# student1= Student("Anthony Johnson", "Engineering", 200, "Ogun")
# student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")
# print(student1.name)  
# print(student2.name)

# # class attribute shared by all objects of the class
# class Student:
#     def __init__(self, name, course,university):
#         self.name = name         
#         self.course = course
#         self.university= university
#     university = "Federal University of Technology Akure"      

# print(Student.university)   
# # print(student1.university)   
# print(student2.university)    


# methods
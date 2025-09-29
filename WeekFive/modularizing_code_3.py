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

# instance attributes
# student1= Student("Anthony Johnson", "Engineering", 200, "Ogun")
# student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")
# print(student1.name)  
# print(student2.name)
# class attribute shared by all objects of the class
class Student:
    university = "Federal University of Technology Akure" 
    def __init__(self, name, course):
        self.name = name         
        self.course = course
        self.university= self.get_university()
    
    
    def get_university(self):
      return"Federal University of Technology Akure"

student1= Student("Anthony Johnson", "Engineering")
student2 = Student("Fadilat Hassan", "Medicine")
print(student1.name)  
print(student2.name) 
# 
print(Student.university)   
print(student1.university)   
print(student2.university)    


# methods

class Student:
    def __init__(self, name, course, level):
        # Attributes
        self.name = name
        self.course = course
        self.level = level
        self.cgpa = 0.0
        self.fees_paid = False
    

     # Method: action the student can do
    def pay_school_fees(self):                   
        self.fees_paid = True
        return f"{self.name} has paid school fees for {self.level} level"
    
    # Method: another action
    def register_courses(self):                   
        if self.fees_paid:
            return f"{self.name} has registered courses for {self.course}"
        else:
            return f"{self.name} must pay school fees first!"
    
      # Method: calculates CGPA
    def calculate_cgpa(self, grades):           
        if grades:
            self.cgpa = sum(grades) / len(grades)
            return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
        return "No grades provided"
    
# Using methods
Abiodun = Student("Abiodun Akinola", "Gistology", 600)
print(Abiodun.pay_school_fees())        
print(Abiodun.register_courses())       
print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))     

# types of methods
# instance methods- work with specific object data
def pay_school_fees(self):
    return f"{self.name} has paid school fees"

# class methods-works iwth class-level data
@classmethod
def get_university(cls):
    return cls.university

# static methods-don't need object or class data
@staticmethod
def academic_calendar():
    return "Academic session runs from september to July"

# how attribute and method works together
class BankAccount:
    def __init__(self, owner, bank_name, balance=0):
        # ATTRIBUTES - What the account HAS
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()
    
    # METHODS - What the account can DO
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount  # Method changes attribute
            return f"₦{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance:,}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Remove money from the account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount  # Method changes attribute
            return f"₦{amount:,} withdrawn from {self.owner}'s account. New balance: ₦{self.balance:,}"
        return "Insufficient funds or invalid amount"
    
    def transfer(self, amount, recipient):
        """Transfer money to another account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: ₦{self.balance:,}"
        return "Transfer failed: Insufficient funds"
    
    def check_balance(self):
        """Check current balance"""
        return f"{self.owner}'s {self.bank_name} account balance: ₦{self.balance:,}"
    
    def generate_account_number(self):
        """Generate a unique account number"""
        import random
        return f"01{random.randint(10000000, 99999999)}"

# Creating and using the account
adunni_account = BankAccount("Adunni Olaleye", "AXT Bank", 50000)

# Attributes (characteristics)
print(f"Owner: {adunni_account.owner}")
print(f"Bank: {adunni_account.bank_name}")
print(f"Account Number: {adunni_account.account_number}")


# Methods (actions)
print(adunni_account.deposit(25000))    
print(adunni_account.withdraw(10000))  
print(adunni_account.transfer(15000, "Sunday James"))  
print(adunni_account.check_balance())   


class NaijaPhone:
    def __init__(self, brand, model, network_provider):
        self.brand = brand
        self.model = model
        self.network_provider = network_provider
        self.airtime_balance = 0
        self.data_balance = 0
        self.is_on = False
    
    def power_on(self):
        self.is_on = True
        return f"{self.brand} phone is now on. Network: {self.network_provider}"
    
    def buy_airtime(self, amount):
        self.airtime_balance += amount
        return f"₦{amount} airtime purchased. Balance: ₦{self.airtime_balance}"
    
    def make_call(self, number):
        if self.is_on and self.airtime_balance > 0:
            self.airtime_balance -= 10
            return f"Calling {number}... Remaining airtime: ₦{self.airtime_balance}"
        return "Cannot make call. Check phone power and airtime balance"
    
    def send_sms(self, message, number):
        if self.airtime_balance >= 4:
            self.airtime_balance -= 4
            return f"SMS sent to {number}: '{message}'. Remaining airtime: ₦{self.airtime_balance}"
        return "Insufficient airtime to send SMS"
    
dare_network = NaijaPhone("Samsung", "A12", "MTN") 
# Attributes (characteristics)
print(f"Brand: {dare_network.brand}")
print(f"Model: {dare_network.model}")
print(f"Network Provider: {dare_network.network_provider}")


# Methods (actions)
print(dare_network.power_on())    
print(dare_network.buy_airtime(10000))  
print(dare_network.make_call(15000))  
print(dare_network.send_sms("Please call me", 234567890))    

class BRTBus:
    def __init__(self, route, bus_number):
       
        self.route = route            
        self.bus_number = bus_number    
        self.current_stop = "Ikorodu"
        self.passenger_count = 0
        self.fare = 300
    
 
    def announce_stop(self):
        return f"Next stop: {self.current_stop}. Fare is ₦{self.fare}"
    
    def board_passengers(self, count):
        self.passenger_count += count
        return f"{count} passengers boarded. Total: {self.passenger_count}"
    
    
class MarketTrader:
    def __init__(self, name, market_name, goods):
       
        self.name = name                
        self.market_name = market_name 
        self.goods = goods             
        self.daily_sales = 0
    
  
    def advertise_goods(self):
        return f"{self.name} at {self.market_name}: Fresh {', '.join(self.goods)} available!"
    
    def make_sale(self, amount):
        self.daily_sales += amount
        return f"Sale made! Today's total: ₦{self.daily_sales:,}"    
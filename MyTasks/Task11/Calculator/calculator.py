import math  # for square root

# Function to perform addition
def add(a, b):
    return a + b

# Function to perform subtraction
def subtract(a, b):
    return a - b

# Function to perform multiplication
def multiply(a, b):
    return a * b

# Function to perform division
def divide(a, b):
    if b == 0:  # Denominator can't be zero
        return "Error: Division by zero!"
    return a / b

# Function to perform modulus
def modulus(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a % b

# Function to perform exponential
def exponent(a, b):
    return a ** b

# Function to calculate square root
def square_root(a):
    if a < 0:
        return "Error: Cannot take square root of a negative number!"
    return math.sqrt(a)

# Main program
def main():
    while True:
        try:
            # Display calculator menu
            print("\nThis is a basic calculator")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Modulus")
            print("6. Exponential")
            print("7. Square Root")
            print("8. Exit")

            choice = int(input("Enter between (1-8) to select your desired calculator operation: "))

            # Validate choice using range
            if choice not in range(1, 9):
                print("Invalid choice! Please choose a number between 1 and 8.")
                continue

            # Exit condition
            if choice == 8:
                print("Exiting calculator... Goodbye!")
                break

            # Handle operations requiring two inputs
            if choice in range(1,7):
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == 1:
                    result = add(a, b)
                elif choice == 2:
                    result = subtract(a, b)
                elif choice == 3:
                    result = multiply(a, b)
                elif choice == 4:
                    result = divide(a, b)
                elif choice == 5:
                    result = modulus(a, b)
                elif choice == 6:
                    result = exponent(a, b)

            # Handle square root (only one input)
            elif choice == 7:
                a = float(input("Enter a number: "))
                result = square_root(a)
             # Exit condition
            elif choice == 8:
                print("Exiting calculator... Goodbye!")
                break    

            print(f"Result = {result}")
            
            # Ask if user wants another calculation
            again = input("Do you want to perform another operation? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Thanks for using the calculator. Goodbye!")
                break

        except ValueError:
            print("Error: Please enter a valid number!")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Run the calculator
if __name__ == "__main__":
    main()

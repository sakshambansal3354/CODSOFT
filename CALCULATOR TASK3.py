# Simple Calculator

# Prompt the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operation choices
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get operation choice
choice = input("Enter your choice (1/2/3/4): ")

# Perform calculation based on user choice
if choice == '1':
    result = num1 + num2
    operation = '+'
elif choice == '2':
    result = num1 - num2
    operation = '-'
elif choice == '3':
    result = num1 * num2
    operation = '*'
elif choice == '4':
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        exit()
    result = num1 / num2
    operation = '/'
else:
    print("Invalid choice.")
    exit()

# Display the result
print(f"{num1} {operation} {num2} = {result}")

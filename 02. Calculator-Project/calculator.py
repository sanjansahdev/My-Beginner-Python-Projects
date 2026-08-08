# -------------------------------------------------------
# Program : Simple Calculator
# Author  : G. Sanjansah
# Purpose : Perform basic arithmetic operations.
# -------------------------------------------------------

print("========== Simple Calculator ==========\n")

# Ask the user to enter the first number.
# input() always returns data as a string.
# float() converts the string into a decimal number.
num1 = float(input("Enter the first number: "))

# Ask the user to enter the second number.
num2 = float(input("Enter the second number: "))

# Display the results.
print("\n========== Results ==========")

# Addition (+)
print(f"Addition       : {num1 + num2}")

# Subtraction (-)
print(f"Subtraction    : {num1 - num2}")

# Multiplication (*)
print(f"Multiplication : {num1 * num2}")

# Division (/)
# Check if the second number is zero before dividing.
if num2 != 0:
    print(f"Division       : {num1 / num2}")
else:
    print("Division       : Cannot divide by zero.")

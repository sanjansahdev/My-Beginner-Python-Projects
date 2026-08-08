# ----------------------------------------------------------
# Program : Number Converter
# Author  : G. Sanjansah
# Purpose : Convert a decimal number into Binary,
#           Octal, and Hexadecimal formats.
# ----------------------------------------------------------

# Read a decimal number from the user.
number = int(input("Enter a decimal number: "))

# Convert the decimal number into different number systems.
print("Binary      :", bin(number))
print("Octal       :", oct(number))
print("Hexadecimal :", hex(number))
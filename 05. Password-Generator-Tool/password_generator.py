# ----------------------------------------------------------
# Program : Password Generator
# Author  : G. Sanjansah
# Purpose : Generate a random and secure password.
# ----------------------------------------------------------

# Import the random module.
# It helps us select random characters.
import random

# Import the string module.
# It provides ready-made collections of letters, digits, and symbols.
import string

print("=" * 40)
print("🔐 PASSWORD GENERATOR")
print("=" * 40)

# Ask the user for the desired password length.
length = int(input("Enter password length: "))

# Combine uppercase letters, lowercase letters,
# numbers, and special characters into one string.
characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

# Start with an empty password.
password = ""

# Repeat 'length' times.
for i in range(length):

    # Pick one random character and add it to the password.
    password += random.choice(characters)

# Display the generated password.
print(f"\n🔑 Your Generated Password: {password}")
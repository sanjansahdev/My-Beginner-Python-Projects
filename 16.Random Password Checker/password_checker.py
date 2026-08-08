# ----------------------------------------------------------
# Program : Password Strength Checker
# Author  : G. Sanjansah
# Purpose : Check whether a password meets basic
#           strength requirements.
# ----------------------------------------------------------

# Read the password from the user.
password = input("Enter your password: ")

# ------------------ Check Length ------------------

# A good password should contain at least 8 characters.
if len(password) < 8:
    print("❌ Weak Password (Minimum 8 characters required)")
else:
    print("✅ Good Password Length")

# ------------------ Check for Numbers ------------------

# Check whether the password contains at least one digit.
if any(char.isdigit() for char in password):
    print("✔ Contains Numbers")

# ------------------ Check for Uppercase Letters ------------------

# Check whether the password contains at least one uppercase letter.
if any(char.isupper() for char in password):
    print("✔ Contains Uppercase Letters")

# ------------------ Check for Lowercase Letters ------------------

# Check whether the password contains at least one lowercase letter.
if any(char.islower() for char in password):
    print("✔ Contains Lowercase Letters")
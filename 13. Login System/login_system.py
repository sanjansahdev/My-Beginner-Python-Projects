# ----------------------------------------------------------
# Program : Login System
# Author  : G. Sanjansah
# Purpose : Verify a user's username and password.
# ----------------------------------------------------------

# Store the correct login credentials.
USERNAME = "admin"
PASSWORD = "1234"

print("=" * 35)
print("🔐 LOGIN SYSTEM")
print("=" * 35)

# Read login details from the user.
user = input("Enter Username: ").strip()
pwd = input("Enter Password: ").strip()

# Check whether both username and password are correct.
if user == USERNAME and pwd == PASSWORD:
    print("✅ Login Successful!")
    print(f"Welcome, {USERNAME}!")

else:
    print("❌ Invalid Username or Password!")
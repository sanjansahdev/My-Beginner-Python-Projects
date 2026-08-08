# ----------------------------------------------------------
# Program : Temperature Converter
# Author  : G. Sanjansah
# Purpose : Convert temperature between Celsius
#           and Fahrenheit.
# ----------------------------------------------------------

# Display the conversion menu.
print("========== TEMPERATURE CONVERTER ==========")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

# Read the user's choice.
choice = input("Choose an option (1 or 2): ")

# ---------------- Celsius to Fahrenheit ----------------
if choice == "1":

    # Read temperature in Celsius.
    celsius = float(input("Enter Celsius: "))

    # Apply conversion formula.
    fahrenheit = (celsius * 9 / 5) + 32

    # Display the result.
    print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")

# ---------------- Fahrenheit to Celsius ----------------
elif choice == "2":

    # Read temperature in Fahrenheit.
    fahrenheit = float(input("Enter Fahrenheit: "))

    # Apply conversion formula.
    celsius = (fahrenheit - 32) * 5 / 9

    # Display the result.
    print(f"Temperature in Celsius: {celsius:.2f}°C")

# ---------------- Invalid Choice ----------------
else:
    print("❌ Invalid Choice")
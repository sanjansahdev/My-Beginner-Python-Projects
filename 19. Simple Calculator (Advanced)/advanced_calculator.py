# ----------------------------------------------------------
# Program : Simple Advanced Calculator
# Author  : G. Sanjansah
# Purpose : Perform multiple arithmetic operations
#           until the user chooses to exit.
# ----------------------------------------------------------

# Keep displaying the calculator menu until the user exits.
while True:

    print("\n========== ADVANCED CALCULATOR ==========")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Read the user's choice.
    choice = input("Choose an option (1-5): ")

    # Exit the program.
    if choice == "5":
        print("Thank you for using the calculator!")
        break

    # Read two numbers.
    a = float(input("First Number: "))
    b = float(input("Second Number: "))

    # Perform the selected operation.
    if choice == "1":
        print("Answer:", a + b)

    elif choice == "2":
        print("Answer:", a - b)

    elif choice == "3":
        print("Answer:", a * b)

    elif choice == "4":
        if b != 0:
            print("Answer:", a / b)
        else:
            print("❌ Cannot divide by zero.")

    else:
        print("❌ Invalid Choice.")
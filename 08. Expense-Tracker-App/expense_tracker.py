# ----------------------------------------------------------
# Program : Expense Tracker
# Author  : G. Sanjansah
# Purpose : Add, view, and calculate daily expenses.
# ----------------------------------------------------------

# Create an empty list to store expenses.
# Each expense will be stored as a tuple:
# (Expense Name, Amount)
expenses = []

# Keep showing the menu until the user exits.
while True:

    print("\n" + "=" * 35)
    print("💰 EXPENSE TRACKER")
    print("=" * 35)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    # Read the user's menu choice.
    choice = input("Enter your choice (1-4): ")

    # ------------------ Add Expense ------------------
    if choice == "1":

        # Read the expense details.
        item = input("Expense Name: ").strip()
        amount = float(input("Amount (₹): "))

        # Store the expense as a tuple.
        expenses.append((item, amount))

        print("✅ Expense added successfully!")

    # ------------------ View Expenses ------------------
    elif choice == "2":

        if not expenses:
            print("📭 No expenses found.")

        else:
            print("\n📋 Your Expenses")
            print("-" * 35)

            # Display every expense.
            for item, amount in expenses:
                print(f"{item:<20} ₹{amount:.2f}")

    # ------------------ Show Total ------------------
    elif choice == "3":

        total = 0

        # Add every expense amount.
        for item, amount in expenses:
            total += amount

        print(f"\n💵 Total Expense: ₹{total:.2f}")

    # ------------------ Exit ------------------
    elif choice == "4":
        print("👋 Thank you for using Expense Tracker!")
        break

    # ------------------ Invalid Choice ------------------
    else:
        print("❌ Invalid choice. Please enter 1-4.")
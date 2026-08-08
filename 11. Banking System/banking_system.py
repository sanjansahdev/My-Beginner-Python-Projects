# ----------------------------------------------------------
# Program : Banking System
# Author  : G. Sanjansah
# Purpose : Perform basic banking operations such as
#           deposit, withdraw, and balance inquiry.
# ----------------------------------------------------------

# Store the current account balance.
balance = 0.0


# ------------------ Deposit ------------------
def deposit():
    """Deposit money into the account."""

    global balance

    amount = float(input("Enter amount to deposit (₹): "))

    # Check if the amount is valid.
    if amount > 0:
        balance += amount
        print(f"✅ ₹{amount:.2f} deposited successfully!")

    else:
        print("❌ Deposit amount must be greater than zero.")


# ------------------ Withdraw ------------------
def withdraw():
    """Withdraw money from the account."""

    global balance

    amount = float(input("Enter amount to withdraw (₹): "))

    # Validate the amount.
    if amount <= 0:
        print("❌ Withdrawal amount must be greater than zero.")

    # Check whether enough balance is available.
    elif amount > balance:
        print("❌ Insufficient balance!")

    else:
        balance -= amount
        print(f"✅ ₹{amount:.2f} withdrawn successfully!")


# ------------------ Check Balance ------------------
def check_balance():
    """Display the current account balance."""

    print(f"\n💰 Current Balance: ₹{balance:.2f}")


# ------------------ Main Menu ------------------
while True:

    print("\n" + "=" * 35)
    print("🏦 BANKING SYSTEM")
    print("=" * 35)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        deposit()

    elif choice == "2":
        withdraw()

    elif choice == "3":
        check_balance()

    elif choice == "4":
        print("👋 Thank you for using our Banking System!")
        break

    else:
        print("❌ Invalid choice. Please select 1-4.")
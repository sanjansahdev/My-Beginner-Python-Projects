# ----------------------------------------------------------
# Program : Contact Book
# Author  : G. Sanjansah
# Purpose : Store, search, view, and delete contacts.
# ----------------------------------------------------------

# Create an empty dictionary to store contacts.
# Format:
# {
#     "Name": "Phone Number"
# }
contacts = {}

# Keep displaying the menu until the user exits.
while True:

    print("\n" + "=" * 35)
    print("📞 CONTACT BOOK")
    print("=" * 35)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    # Read the user's menu choice.
    choice = input("Enter your choice (1-5): ")

    # ------------------ Add Contact ------------------
    if choice == "1":

        # Remove extra spaces before and after the input.
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone Number: ").strip()

        # Store the contact in the dictionary.
        contacts[name] = phone

        print("✅ Contact added successfully!")

    # ------------------ View Contacts ------------------
    elif choice == "2":

        # Check if the dictionary is empty.
        if not contacts:
            print("📭 No contacts found.")

        else:
            print("\n📋 Contact List")
            print("-" * 30)

            # Loop through each key-value pair.
            for name, phone in contacts.items():
                print(f"{name} : {phone}")

    # ------------------ Search Contact ------------------
    elif choice == "3":

        name = input("Enter name to search: ").strip()

        # Check if the contact exists.
        if name in contacts:
            print(f"📱 {name} : {contacts[name]}")
        else:
            print("❌ Contact not found.")

    # ------------------ Delete Contact ------------------
    elif choice == "4":

        name = input("Enter name to delete: ").strip()

        if name in contacts:

            # Delete the contact from the dictionary.
            del contacts[name]

            print("🗑️ Contact deleted successfully!")

        else:
            print("❌ Contact not found.")

    # ------------------ Exit ------------------
    elif choice == "5":
        print("👋 Thank you for using Contact Book!")
        break

    # ------------------ Invalid Choice ------------------
    else:
        print("❌ Invalid choice. Please select 1-5.")
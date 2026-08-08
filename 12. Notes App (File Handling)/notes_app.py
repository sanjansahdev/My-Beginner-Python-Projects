# ----------------------------------------------------------
# Program : Notes App
# Author  : G. Sanjansah
# Purpose : Save, view, and clear notes using a text file.
# ----------------------------------------------------------

# Name of the file where notes will be stored.
FILE_NAME = "notes.txt"

# Keep displaying the menu until the user exits.
while True:

    print("\n" + "=" * 35)
    print("📝 NOTES APP")
    print("=" * 35)
    print("1. Add Note")
    print("2. View Notes")
    print("3. Clear Notes")
    print("4. Exit")

    # Read the user's menu choice.
    choice = input("Enter your choice (1-4): ")

    # ------------------ Add Note ------------------
    if choice == "1":

        # Read the note from the user.
        note = input("Enter your note: ").strip()

        # Open the file in Append (a) mode.
        # If the file doesn't exist, Python creates it.
        with open(FILE_NAME, "a") as file:
            file.write(note + "\n")

        print("✅ Note saved successfully!")

    # ------------------ View Notes ------------------
    elif choice == "2":

        try:
            # Open the file in Read (r) mode.
            with open(FILE_NAME, "r") as file:

                # Read the entire file.
                notes = file.read()

                if notes:
                    print("\n📒 Your Notes")
                    print("-" * 35)
                    print(notes)

                else:
                    print("📭 No notes found.")

        except FileNotFoundError:
            print("📭 No notes found.")

    # ------------------ Clear Notes ------------------
    elif choice == "3":

        # Opening a file in write mode clears its contents.
        with open(FILE_NAME, "w") as file:
            pass

        print("🗑️ All notes deleted successfully!")

    # ------------------ Exit ------------------
    elif choice == "4":
        print("👋 Thank you for using Notes App!")
        break

    # ------------------ Invalid Choice ------------------
    else:
        print("❌ Invalid choice. Please enter 1-4.")
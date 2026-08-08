# ----------------------------------------------------------
# Program : Library Management System
# Author  : G. Sanjansah
# Purpose : Manage books by adding, viewing,
#           and removing them from a library.
# ----------------------------------------------------------

# List to store book names.
books = []

# Keep the program running until the user exits.
while True:

    print("\n========== LIBRARY MANAGEMENT ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Remove Book")
    print("4. Exit")

    # Read the user's choice.
    choice = input("Enter Choice: ")

    # ---------------- Add Book ----------------
    if choice == "1":

        # Read the book name.
        book = input("Enter Book Name: ").strip()

        # Add the book to the list.
        books.append(book)

        print("✅ Book Added Successfully!")

    # ---------------- View Books ----------------
    elif choice == "2":

        # Check if the library is empty.
        if not books:
            print("📚 No Books Available.")

        else:
            print("\nAvailable Books:")

            # Display all books with serial numbers.
            for index, book in enumerate(books, start=1):
                print(f"{index}. {book}")

    # ---------------- Remove Book ----------------
    elif choice == "3":

        # Read the book name.
        book = input("Enter Book Name to Remove: ").strip()

        # Remove the book if found.
        if book in books:
            books.remove(book)
            print("✅ Book Removed Successfully!")

        else:
            print("❌ Book Not Found!")

    # ---------------- Exit ----------------
    elif choice == "4":

        print("Thank you for using the Library Management System!")
        break

    # ---------------- Invalid Choice ----------------
    else:
        print("❌ Invalid Choice!")
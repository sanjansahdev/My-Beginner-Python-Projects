# ----------------------------------------------------------
# Program : Student Management System
# Author  : G. Sanjansah
# Purpose : Add, view, search, and delete student records.
# ----------------------------------------------------------

# Dictionary to store all student records.
#
# Structure:
# {
#     "101": {
#         "name": "Rahul",
#         "marks": 92.5
#     }
# }
students = {}


# ------------------ Add Student ------------------
def add_student():
    """Add a new student record."""

    roll = input("Enter Roll Number: ").strip()
    name = input("Enter Student Name: ").strip()
    marks = float(input("Enter Marks: "))

    # Store student information inside a nested dictionary.
    students[roll] = {
        "name": name,
        "marks": marks
    }

    print("✅ Student added successfully!")


# ------------------ View Students ------------------
def view_students():
    """Display all student records."""

    if not students:
        print("📭 No students found.")
        return

    print("\n===== STUDENT LIST =====")

    # Loop through every student.
    for roll, data in students.items():

        print(f"Roll Number : {roll}")
        print(f"Name        : {data['name']}")
        print(f"Marks       : {data['marks']:.2f}")
        print("-" * 30)


# ------------------ Search Student ------------------
def search_student():
    """Search a student using the roll number."""

    roll = input("Enter Roll Number: ").strip()

    if roll in students:

        data = students[roll]

        print("\nStudent Found")
        print(f"Name  : {data['name']}")
        print(f"Marks : {data['marks']:.2f}")

    else:
        print("❌ Student not found.")


# ------------------ Delete Student ------------------
def delete_student():
    """Delete a student record."""

    roll = input("Enter Roll Number: ").strip()

    if roll in students:

        del students[roll]

        print("🗑️ Student deleted successfully!")

    else:
        print("❌ Student not found.")


# ------------------ Main Menu ------------------
while True:

    print("\n" + "=" * 35)
    print("🎓 STUDENT MANAGEMENT SYSTEM")
    print("=" * 35)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("👋 Thank you for using Student Management System!")
        break

    else:
        print("❌ Invalid choice. Please enter 1-5.")
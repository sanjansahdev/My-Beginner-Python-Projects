# ----------------------------------------------------------
# Program : To-Do List
# Author  : G. Sanjansah
# Purpose : Manage daily tasks (Add, View, Remove).
# ----------------------------------------------------------

# Create an empty list to store tasks.
tasks = []

# Keep showing the menu until the user chooses to exit.
while True:

    print("\n" + "=" * 35)
    print("📝 TO-DO LIST")
    print("=" * 35)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    # Read the user's menu choice.
    choice = input("Enter your choice (1-4): ")

    # ------------------ Add Task ------------------
    if choice == "1":

        # Get the new task from the user.
        task = input("Enter a new task: ")

        # Add the task to the end of the list.
        tasks.append(task)

        print("✅ Task added successfully!")

    # ------------------ View Tasks ------------------
    elif choice == "2":

        # Check if the task list is empty.
        if len(tasks) == 0:
            print("📭 No tasks available.")

        else:
            print("\n📋 Your Tasks:")

            # enumerate() gives both the task number and task name.
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    # ------------------ Remove Task ------------------
    elif choice == "3":

        # Check whether there are tasks to remove.
        if len(tasks) == 0:
            print("📭 No tasks to remove.")

        else:

            print("\n📋 Your Tasks:")

            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                # Ask which task should be removed.
                task_number = int(input("Enter task number to remove: "))

                # Remove the selected task.
                removed_task = tasks.pop(task_number - 1)

                print(f"🗑️ '{removed_task}' removed successfully!")

            # Handle invalid input or invalid index.
            except (ValueError, IndexError):
                print("❌ Invalid task number!")

    # ------------------ Exit ------------------
    elif choice == "4":
        print("👋 Thank you for using the To-Do List!")
        break

    # ------------------ Invalid Choice ------------------
    else:
        print("❌ Invalid choice. Please select 1-4.")
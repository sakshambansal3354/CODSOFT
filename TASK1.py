# Simple Python To-Do List (user input driven)

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")  # USER INPUT for new task
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            status = "Done" if t["completed"] else "Pending"
            print(f"{i}. {t['task']} - [{status}]")

def mark_completed(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as completed: "))  # USER INPUT for task number
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))  # USER INPUT for task number
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Select an option (1-5): ")  # USER INPUT to select menu option
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting application. Have a productive day!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

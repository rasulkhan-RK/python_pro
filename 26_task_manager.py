tasks = []


def display_tasks():
    print("=== Task Manager ===")
    print("1. Add task")
    print("2. View task")
    print("3. Complete task")
    print("4. Delete task")
    print("0. Exit")


# Add Task
def add_task():
    title = input("Enter your task: ").title().strip()
    if title == "":
        print("Task can't be empty ❌")
        return
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added successfully! ✔")


# View Task
def view_tasks():
    if not tasks:
        print("No tasks found.")

    print("=== My Tasks ====")
    for index, task in enumerate(tasks):
        status = "✔" if task["completed"] else ""
        print(f"{index + 1} [{status}] {task["title"]}")

    print("\n=========================")


# Complete Task
def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(
            input("Enter your task number to mark as completed: "))
        if task_number < 1 or task_number > len(tasks):
            print("Please enter a valid number between (1-4) ❌")

        task_to_completed = tasks[task_number - 1]
        task_to_completed["completed"] = True
        print(f"Task '[{task_to_completed["title"]}]' marked as completed! ✔")
    except ValueError:
        print("Invalid prompt ❌")


# Delete Task
def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter a number to delete a task: "))
        if task_number < 1 or task_number > len(tasks):
            print("Please enter a valid number between (1-4) ❌")

        task_to_delete = tasks.pop(task_number - 1)
        print(f"Task '{task_to_delete["title"]}' deleted successfully! ✔")
    except ValueError:
        print("Invalid prompt ❌")


def main():
    while True:
        display_tasks()

        try:
            choice = input("Enter the task number: ")
            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                complete_task()
            elif choice == "4":
                delete_task()
            elif choice == "0":
                print("Goodbye 👋🏻")
                break
            else:
                print("Enter a valid number between (1-4)")
        except ValueError:
            print("Please enter a valid number ❌")


main()

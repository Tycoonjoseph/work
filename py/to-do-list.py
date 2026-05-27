import datetime
tasks = []


def show_intro():
    print("This is the future of to-do lists!")
    print("You can add tasks, mark them as complete, set reminders, and delete tasks.")


def show_menu():
    print("\nTo-Do List Menu")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Mark task as complete")
    print("4. Set reminder")
    print("5. Delete task")
    print("6. Exit")


def show_tasks():
    if not tasks:
        print("Your to-do list is empty.")
        return

    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "done" if task["complete"] else "pending"
        reminder = f", reminder: {task['reminder']}" if task["reminder"] else ""
        print(f"{index}. {task['name']} [{status}]{reminder}")


def add_task():
    name = input("Enter a task to add: ").strip()

    if not name:
        print("Task name cannot be empty.")
        return

    tasks.append({"name": name, "complete": False, "reminder": ""})
    print(f"Task '{name}' added to the to-do list.")


def get_task_number(action):
    show_tasks()

    if not tasks:
        return None

    try:
        task_number = int(input(f"Enter the task number to {action}: "))
    except ValueError:
        print("Please enter a valid number.")
        return None

    if task_number < 1 or task_number > len(tasks):
        print("That task number does not exist.")
        return None

    return task_number - 1


def mark_complete():
    task_index = get_task_number("mark as complete")

    if task_index is None:
        return

    tasks[task_index]["complete"] = True
    print(f"Task '{tasks[task_index]['name']}' marked as complete.")


def set_reminder():
    task_index = get_task_number("set a reminder for")

    if task_index is None:
        return

    reminder_time = input("Enter the reminder time (for example, 2 PM): ").strip()

    if not reminder_time:
        print("Reminder time cannot be empty.")
        return

    tasks[task_index]["reminder"] = reminder_time
    print(f"Reminder set for task '{tasks[task_index]['name']}' at {reminder_time}.")


def delete_task():
    task_index = get_task_number("delete")

    if task_index is None:
        return

    removed_task = tasks.pop(task_index)
    print(f"Task '{removed_task['name']}' deleted from the to-do list.")


def main():
    show_intro()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            set_reminder()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()

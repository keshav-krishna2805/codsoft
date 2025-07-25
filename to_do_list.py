import os

TASK_FILE = "mytodo.txt"


def read_tasks():
    if not os.path.isfile(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        lines = f.readlines()
        return [line.strip() for line in lines if line.strip()]


def write_tasks(task_list):
    with open(TASK_FILE, "w") as f:
        for task in task_list:
            f.write(task + "\n")


def display(task_list):
    if not task_list:
        print("\n📭 No tasks right now.\n")
        return
    print("\n📋 Current Tasks:")
    for idx, task in enumerate(task_list, 1):
        print(f"  {idx}. {task}")
    print()


def add(task_list):
    task = input("✏️  Enter task description: ").strip()
    if task:
        task_list.append(task)
        write_tasks(task_list)
        print("✅ Task added.\n")
    else:
        print("⚠️  Empty task not added.\n")


def remove(task_list):
    if not task_list:
        print("⚠️  No tasks to delete.\n")
        return
    try:
        number = int(input("❌ Enter task number to remove: "))
        if 1 <= number <= len(task_list):
            removed = task_list.pop(number - 1)
            write_tasks(task_list)
            print(f"🗑️  Removed task: '{removed}'\n")
        else:
            print("❗ Invalid task number.\n")
    except ValueError:
        print("❗ Please enter a number.\n")


def run():
    print("🧠 Welcome to Your To-Do Manager!\n")
    task_list = read_tasks()

    while True:
        print("Menu:")
        print("  1. Show Tasks")
        print("  2. Add Task")
        print("  3. Remove Task")
        print("  4. Exit")

        option = input("\nChoose an option (1-4): ").strip()

        if option == "1":
            display(task_list)
        elif option == "2":
            add(task_list)
        elif option == "3":
            remove(task_list)
        elif option == "4":
            print("👋 Exiting. Stay productive!")
            break
        else:
            print("🚫 Invalid choice. Please enter 1–4.\n")

if __name__ == "__main__":
    run()

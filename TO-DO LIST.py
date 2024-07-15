tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task, status = line.strip().split(":")
                tasks.append({"task": task, "status": status})
    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']}: {task['status']}\n")

def view_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} - {'Done' if task['status'] == '1' else 'Undone'}")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "status": "0"})

def mark_done():
    task_id = int(input("Enter task ID to mark as done: ")) - 1
    if task_id < len(tasks):
        tasks[task_id]["status"] = "1"
    else:
        print("Invalid task ID")

def mark_undone():
    task_id = int(input("Enter task ID to mark as undone: ")) - 1
    if task_id < len(tasks):
        tasks[task_id]["status"] = "0"
    else:
        print("Invalid task ID")

def remove_task():
    task_id = int(input("Enter task ID to remove: ")) - 1
    if task_id < len(tasks):
        del tasks[task_id]
    else:
        print("Invalid task ID")

def main():
    load_tasks()
    while True:
        print("\nMenu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Mark task as undone")
        print("5. Remove task")
        print("6. Save and exit")
        choice = input("Enter choice: ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            mark_undone()
        elif choice == "5":
            remove_task()
        elif choice == "6":
            save_tasks()
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

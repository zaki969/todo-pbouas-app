from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\nTo-Do List")
        for i, task in enumerate(manager.get_all_tasks()):
            print(f"{i + 1}. {task}")

        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose: ")
        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)
        elif choice == "2":
            index = int(input("Enter task number to toggle: ")) - 1
            if 0 <= index < len(manager.tasks):
                manager.tasks[index].toggle_status()
        elif choice == "3":
            index = int(input("Enter task number to delete: ")) - 1
            manager.delete_task(index)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

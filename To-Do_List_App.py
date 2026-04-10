def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            print("\nYOUR TASKS:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        elif choice == '2':
            new_task = input("Enter the task: ")
            tasks.append(new_task)
            print("Task added!")
        elif choice == '3':
            task_num = int(input("Enter the task number to remove: "))
            if 0 < task_num <= len(tasks):
                tasks.pop(task_num - 1)
                print("Task removed.")
            else:
                print("Invalid number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

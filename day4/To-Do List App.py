# Day 4 - To-Do List App (CLI)
print("#30 coding challenge")

tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Clear All Tasks")
    print("6. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    
    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        print(f"✅ '{new_task}' added to your list.")
    
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"🗑 '{removed}' removed from your list.")
            else:
                print("Invalid task number.")
    
    elif choice == "4":
        if not tasks:
            print("No tasks to mark as done.")
        else:
            task_num = int(input("Enter task number to mark as done: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1] += " ✅"
                print(f"🎯 Task {task_num} marked as done.")
            else:
                print("Invalid task number.")
    
    elif choice == "5":
        confirm = input("Are you sure you want to clear all tasks? (y/n): ")
        if confirm.lower() == 'y':
            tasks.clear()
            print("🧹 All tasks cleared.")
    
    elif choice == "6":
        print("👋 Goodbye! Keep coding!")
        break
    
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")

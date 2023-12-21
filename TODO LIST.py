todo_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Clear all tasks")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

def view_tasks():
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def mark_as_done():
    view_tasks()
    if todo_list:
        try:
            task_index = int(input("Enter the task number to mark as done: "))
            if 1 <= task_index <= len(todo_list):
                done_task = todo_list.pop(task_index - 1)
                print(f"Task '{done_task}' marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No tasks to mark as done.")

def clear_all_tasks():
    global todo_list
    todo_list = []
    print("All tasks cleared.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_as_done()
    elif choice == '4':
        clear_all_tasks()
    elif choice == '5':
        print("Exiting the to-do list program.")
        break
    else:
        print("Invalid input. Please enter a valid choice.")
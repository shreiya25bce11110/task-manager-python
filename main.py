import datetime
def to_get_the_summary(tasks):
    completed =0
    pending =0
    for task in tasks:
       if task["status"]=="completed":
           completed+=1
       else:
           pending+=1
    all_tasks =len(tasks)
    return{"completed":completed,"pending":pending,"total tasks":all_tasks}

def bunch_of_overdue_tasks(tasks):
    today = datetime.date.today()
    overdue_tasks=[]

    for task in tasks :
        deadline = datetime.datetime.strptime(task["deadline"],"%Y-%m-%d").date()
        if deadline< today and task["status"]!= "completed":
            overdue_tasks.append(task)
    return overdue_tasks

def get_upcoming_task(tasks,window_days =3):
    today = datetime.date.today()
    window_end = today +datetime.timedelta(days=window_days)
    upcoming_tasks =[]

    for task in tasks :
        deadline = datetime.datetime.strptime(task["deadline"],"%Y-%m1-%d").date()
        if today <=deadline<=window_end:
            upcoming_tasks.append(task)
    return upcoming_tasks
def add_task(tasks):
    if tasks:
        new_id = tasks[-1]["id"] + 1
    else:
        new_id = 1
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    task = {
        "id": new_id ,"title": title,"description": description,"deadline": deadline,"status": "pending"}
    tasks.append(task)
    print(" Task added.")
    return tasks

def view_tasks(tasks):
    if not tasks:
        print("No tasks added yet.")
    else:
        for task in tasks:
            print(f'ID: {task["id"]} | Title: {task["title"]} | Deadline: {task["deadline"]} | Status: {task["status"]}')

def mark_completed(tasks):
    try:
        task_id = int(input("Enter task ID to mark as completed: "))
    except ValueError:
        print("Invalid ID.")
        return tasks
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "completed"
            found = True
            print("✅ Task marked as completed.")
            break
    if not found:
        print("Task ID not found.")
    return tasks

def delete_task(tasks):
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return tasks
    new_list = []
    found = False
    for task in tasks:
        if task["id"] == task_id:
            found = True
            print("✅ Task deleted.")
            continue
        new_list.append(task)
    if not found:
        print("Task ID not found.")
    return new_list

def edit_task(tasks):
    try:
        task_id = int(input("Enter task ID to edit: "))
    except ValueError:
        print("Invalid ID.")
        return tasks
    for task in tasks:
        if task["id"] == task_id:
            print("Which field do you want to edit? (title/description/deadline/status)")
            field = input("Field: ").strip().lower()
            if field in ["title", "description", "deadline", "status"]:
                new_value = input(f"Enter new value for {field}: ")
                task[field] = new_value
                print(f"{field.capitalize()} updated.")
            else:
                print("Invalid field.")
            return tasks
    print("Task ID not found.")
    return tasks
import json

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"✅ Tasks saved to {filename}")



def main():
    filename = "tasks.json"
    tasks = load_tasks(filename)

    while True:
        print("\n==== Task Manager ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Show Productivity Summary")
        print("7. Show Overdue Tasks")
        print("8. Show Upcoming Tasks")
        print("9. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            tasks = add_task(tasks)
            save_tasks(tasks, filename)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            tasks = mark_completed(tasks)
            save_tasks(tasks, filename)

        elif choice == "4":
            tasks = edit_task(tasks)
            save_tasks(tasks, filename)

        elif choice == "5":
            tasks = delete_task(tasks)
            save_tasks(tasks, filename)

        elif choice == "6":
            summary = to_get_the_summary(tasks)
            print("\n---- Summary ----")
            print(f"Total: {summary['total tasks ']}")
            print(f"Completed: {summary['completed']}")
            print(f"Pending: {summary['pending ']}")

        elif choice == "7":
            overdue = bunch_of_overdue_tasks(tasks)
            print("\n---- Overdue Tasks ----")
            if not overdue:
                print("No overdue tasks.")
            else:
                for task in overdue:
                    print(f"ID: {task['id']} | Title: {task['title']} | Deadline: {task['deadline']} | Status: {task['status']}")

        elif choice == "8":
            upcoming = get_upcoming_task(tasks)
            print("\n---- Upcoming Tasks ----")
            if not upcoming:
                print("No upcoming tasks.")
            else:
                for task in upcoming:
                    print(f"ID: {task['id']} | Title: {task['title']} | Deadline: {task['deadline']} | Status: {task['status']}")

        elif choice == "9":
            save_tasks(tasks, filename)
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

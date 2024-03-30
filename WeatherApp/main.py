def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. View To-Do List")
    print("2. Add Item to To-Do List")
    print("3. Mark Item as Completed")
    print("4. Clear To-Do List")
    print("5. Exit")


def view_list(todo_list):
    print("\n===== To-Do List =====")
    if todo_list:
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your To-Do list is empty!")


def add_item(todo_list):
    item = input("\nEnter the task you want to add: ")
    todo_list.append(item)
    print(f"'{item}' has been added to your To-Do list!")


def mark_completed(todo_list):
    view_list(todo_list)
    if todo_list:
        index = int(input("\nEnter the number of the task you completed: ")) - 1
        if 0 <= index < len(todo_list):
            print(f"'{todo_list[index]}' has been marked as completed!")
            del todo_list[index]
        else:
            print("Invalid task number!")
    else:
        print("Your To-Do list is empty!")


def clear_list(todo_list):
    todo_list.clear()
    print("Your To-Do list has been cleared!")


def main():
    todo_list = []

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            view_list(todo_list)
        elif choice == '2':
            add_item(todo_list)
        elif choice == '3':
            mark_completed(todo_list)
        elif choice == '4':
            clear_list(todo_list)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()

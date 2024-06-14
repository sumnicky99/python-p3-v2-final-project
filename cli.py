from lib.user import User
from lib.category import Category
from lib.expense import Expense



def MainMenu () :

    """Main menu loop to navigate between user, category, and expense menus."""
    while True :
         # Display main menu options
        menu = (
            "\nMain Menu:\n"
            "1. User Menu\n"
            "2. Category Menu\n"
            "3. Expense Menu\n"
            "4. Exit\n"
            "Select an option: "
        )
        choice = input(menu)
        
        if choice == '1':
            user_menu()
        elif choice == '2':
            category_menu()
        elif choice == '3':
            expense_menu()
        elif choice == '4':
            input("Exiting... Press Enter to continue.")
            break
        else:
            input("Invalid choice. Please select a valid option. Press Enter to continue.")


def user_menu () :
    while True:
        menu = (
            "\nUser Menu:\n"
            "1. Create User\n"
            "2. Find User by Username \n"
            "3. Delete an Existing User Account\n"
            "4. Back to Main Menu\n"
            "Select an option: "
        )
        choice = input(menu)

        if choice == "1":
            create_user()
        elif choice == "2":
            find_user_by_username()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            break
        else:
            input("Invalid choice. Please select a valid option. Press Enter to continue.")


def create_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    user = User.create(username, email)
    input(f"User created with ID: {user.id}. Press Enter to continue.")


def find_user_by_username():
    username = input("Enter username to search: ")
    user = User.find_user_by_username(username)
    if user:
        input(f"User found: {user}. Press Enter to continue.")
    else:
        input("User not found. Press Enter to continue.")

    
def delete_user():
    user_id = input("Enter user ID to delete: ")
    if user_id.isdigit():  
        user_id = int(user_id)
        user = User.find_user_by_id(user_id)
        if user:
            confirmation = input(f"Are you sure you want to delete user {user.username}? (yes/no): ")
            if confirmation.lower() == "yes":
                User.delete(user_id)
                input(f"User {user.username} deleted successfully. Press Enter to continue.")
            else:
                input("Deletion canceled. Press Enter to continue.")
        else:
            input(f"User with ID {user_id} not found. Press Enter to continue.")
    else:
        input("Invalid input. User ID must be an integer. Press Enter to continue.")


def category_menu () :
    while True:
        menu = (
            "\nCategory Menu:\n"
            "1. Create Category\n"
            "2. List Categories\n"
            "3. Find Category by Name\n"
            "4. Delete Category\n"
            "5. Back to Main Menu\n"
            "Select an option: "
        )
        choice = input(menu)

        if choice == "1":
            create_category()
        elif choice == "2":
            list_categories()
        elif choice == "3":
            find_category_by_name()
        elif choice == "4":
            delete_category()
        elif choice == "5":
            break
        else:
            input("Invalid choice. Please select a valid option. Press Enter to continue.")
def create_category():
    name = input("Enter category name: ")
    #description = input("Enter category description: ")
    category = Category.create(name)  # Change the method signature to pass only one argument
    input(f"Category '{category.name}' created with ID: {category.id}. Press Enter to continue.")

def list_categories():
    categories = Category.get_all_categories()  # Use the correct method name
    if categories:
        print("\nList of Categories:")
        for category in categories:
            description = getattr(category, 'description', 'No description')  # Assuming description is a property of the Category class
            print(f"{category.id}: {category.name} - {description}")
    else:
        print("No categories found.")
    input("Press Enter to continue.")


def find_category_by_name():
    name = input("Enter category name to search: ")
    category = Category.find_category_by_name(name)  # Use the correct method name
    if category:
        print(f"Category found: {category.id}: {category.name} - {category.description}")
    else:
        print("Category not found.")
    input("Press Enter to continue.")

def delete_category():
    category_id = input("Enter category ID to delete: ")
    if category_id.isdigit():
        category_id = int(category_id)
        category = Category.find_category_by_id(category_id)  
        if category:
            confirmation = input(f"Are you sure you want to delete category '{category.name}'? (yes/no): ")
            if confirmation.lower() == "yes":
                Category.delete(category_id)  
                input(f"Category '{category.name}' deleted successfully. Press Enter to continue.")
            else:
                input("Deletion canceled. Press Enter to continue.")
        else:
            input(f"Category with ID {category_id} not found. Press Enter to continue.")
    else:
        input("Invalid input. Category ID must be an integer. Press Enter to continue.")


def expense_menu():
    while True:
        menu = (
            "\nExpense Menu:\n"
            "1. Add Expense\n"
            "2. List Expenses\n"
            "3. Find Expense by ID\n"
            "4. Delete Expense\n"
            "5. Back to Main Menu\n"
            "Select an option: "
        )
        choice = input(menu)

        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            find_expense_by_id()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            break
        else:
            input("Invalid choice. Please select a valid option. Press Enter to continue.")



def add_expense():
    try:
        category_id = int(input("Enter category ID for the expense: "))
        amount = float(input("Enter amount for the expense: "))
        description = input("Enter description for the expense: ")
        date = input("Enter date for the expense (YYYY-MM-DD): ")
        
        expense = Expense.create(category_id, amount, description, date)  # Make sure to pass the date
        print(f"Expense added successfully with ID: {expense.id}")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
    input("Press Enter to continue.")

def list_expenses():
    try:
        expenses = Expense.all()  # Fetch all expenses
        if not expenses:
            print("No expenses found.")
        else:
            print("List of Expenses:")
            for expense in expenses:
                print(expense)  # Assuming __str__ method is implemented in Expense class
    except Exception as e:
        print(f"An error occurred: {e}")
    input("Press Enter to continue.")

def find_expense_by_id():
    try:
        expense_id = int(input("Enter expense ID to search: "))
        expense = Expense.find_by_id(expense_id)  # Assuming find_by_id method exists
        if expense:
            print(expense)
        else:
            print("Expense not found.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
    input("Press Enter to continue.")

def delete_expense():
    try:
        expense_id = int(input("Enter expense ID to delete: "))
        expense = Expense.find_by_id(expense_id)  # Assuming find_by_id method exists
        if expense:
            confirm = input(f"Are you sure you want to delete expense '{expense.description}'? (yes/no): ")
            if confirm.lower() == 'yes':
                Expense.delete(expense_id)  # Assuming delete method exists
                print(f"Expense '{expense.description}' deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("Expense not found.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
    input("Press Enter to continue.")

if __name__ =="__main__" :
    MainMenu ()
  
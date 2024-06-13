from lib.user import User
from lib.category import Category
from lib.expense import Expense
from  db.connection  import get_db_connection

# Drop tables
print("Dropping tables...")
User.drop_table()
Category.drop_table()
Expense.drop_table()

# Create tables
print("Creating tables...")
User.create_table()
Category.create_table()
Expense.create_table()

# Create and save new users
print("Creating users...")
user1 = User.create(username="Maya", email="Maya@example.com")
print(f"User created: {user1.username}, {user1.email}, {user1.id}")

user2 = User.create(username="John", email="John@example.com")
print(f"User created: {user2.username}, {user2.email}, {user2.id}")

user3 = User.create(username="Debra", email="Debra@example.com")
print(f"User created: {user3.username}, {user3.email}, {user3.id}")

# Update user
print("Updating user...")
fetched_user = User.find_user_by_id(user2.id)
if fetched_user:
    fetched_user.username = "George"
    fetched_user.email = "George@gmail.com"
    fetched_user.save()
    print(f"User updated: {fetched_user.username}, {fetched_user.email}, {fetched_user.id}")

# Delete user
print("Deleting user...")
User.delete(user3.id)
print(f"User with ID {user3.id} deleted")


# Create categories
categories = [
    Category.create(name="Entertainment"),
    Category.create(name="Utilities"),
    Category.create(name="Transportation"),
    Category.create(name="Clothing")
]

for category in categories:
    print(f"Category created: {category.name}, {category.id}")

# Update a category (watch how it updates utilities to household)
print("Updating category...")
category_to_update = Category.find_category_by_id(categories[1].id)
if category_to_update:
    category_to_update.name = "Household"
    category_to_update.save()
    print(f"Category updated: {category_to_update.name}, {category_to_update.id}")


# Delete a category (watch how it deletes clothing)
print("Deleting category...")
Category.delete(categories[3].id)
print(f"Category with ID {categories[3].id} deleted")

# Create expenses
expenses = [
    Expense.create(user_id=user1.id, category_id=categories[0].id, amount=100.0, description="Dinner", date="2024-06-12"),
    Expense.create(user_id=user2.id, category_id=categories[1].id, amount=30.0, description="Movie tickets", date="2024-06-10"),
    Expense.create(user_id=user1.id, category_id=categories[2].id, amount=50.0, description="Electricity bill", date="2024-06-11"),
    Expense.create(user_id=user2.id, category_id=categories[3].id, amount=20.0, description="Bus fare", date="2024-06-09")
]

for expense in expenses:
    print(f"Expense created: {expense.user_id}, {expense.category_id}, {expense.amount}, {expense.description}, {expense.date}, {expense.id}")


# Fetch an expense and update it (watch how the movies amount gets updated)
print("Updating expense...")
updated_expense = Expense.find_by_id(expenses[1].id)
if updated_expense:
    updated_expense.amount = 120.0
    updated_expense.save()
    print(f"Expense updated: {updated_expense.user_id}, {updated_expense.category_id}, {updated_expense.amount}, {updated_expense.description}, {updated_expense.date}, {updated_expense.id}")


# Delete an expense (watch how the electricity bill gets deleted)
print("Deleting expense...")
deleted_expense = expenses[2]  # Assuming expenses[2] is the expense you want to delete
Expense.delete(deleted_expense.id)
print(f"Expense with ID {deleted_expense.id} deleted")


# Fetch and update user1
print("Fetching and updating user...")
fetched_user = User.find_user_by_id(user1.id)
if fetched_user:
    print(f"User fetched: {fetched_user.username}, {fetched_user.email}, {fetched_user.id}")
    fetched_user.email = "maya@example.com"
    fetched_user.save()
    print(f"User updated: {fetched_user.username}, {fetched_user.email}, {fetched_user.id}")

# Verify data in tables
def fetch_all_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_all_categories():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM categories')
    rows = cursor.fetchall()
    conn.close()
    return rows

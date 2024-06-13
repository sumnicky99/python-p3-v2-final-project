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

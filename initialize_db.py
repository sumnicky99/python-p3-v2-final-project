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
created: {user3.username}, {user3.email}, {user3.id}")



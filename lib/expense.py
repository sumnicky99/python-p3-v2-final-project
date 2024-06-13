#importing from connection
from connection import get_db_connection
#creating class for expense
class Expense:
    #intializing
    def __init__(self, user_id, category_id, amount, description, date, expense_id=None):
        self.id = expense_id
        self.user_id = user_id
        self.category_id = category_id
        self.amount = amount
        self.description = description
        self.date = date
  #adding properties
#giving id a property
@property
def id(self):
    return self._id

#setting id 
@id.setter
def id(self, value):
    if not isinstance(value, int) and value is not None:
        raise TypeError("ID must be an integer or None.")
    self._id = value

#giving amount a property
@property
def amount(self):
    return self._amount

#setting amount 
@amount.setter
def amount(self, value):
    self._amount = value

#giving description a property
@property
def description(self):
    return self._description

#setting description
@description.setter
def description(self, value):
    self._description = value
#giving date a property 
@property
def date(self):
    return self._date

#setting date
@date.setter
def date(self, value):
    self._date = value

#class methods
#creating a table
@classmethod
def create_table(cls):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = '''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            category_id INTEGER,
            amount REAL,
            description TEXT,
            date TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(category_id) REFERENCES categories(id)
        )
    '''
    cursor.execute(sql)
    conn.commit()
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

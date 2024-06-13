#doing importation
from connection import get_db_connection
#creating the class for category
class Category:
    #intializing the class method
    def __init__(self, name, category_id=None):
        self._name = name
        self._id = category_id


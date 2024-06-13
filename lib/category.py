#doing importation
from connection import get_db_connection
#creating the class for category
class Category:
    #intializing the class method
    def __init__(self, name, category_id=None):
        self._name = name
        self._id = category_id
#Giving a property to name
    @property
    def name(self):
        return self._name
#setting the id
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        self._name = value
#Giving a property to id
    @property
    def id(self):
        return self._id
#setting the id
    @id.setter
    def id(self, value):
        if not isinstance(value, int) and value is not None:
            raise TypeError("ID must be an integer or None.")
        self._id = value
#use of repr
    def __repr__(self):
        return f"<Category {self.name}, {self.id}>"


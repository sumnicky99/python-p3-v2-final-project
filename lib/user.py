#importing get_db_connection from connection file
from connection import get_db_connection

#creating a class method for the user
class User:
    def __init__(self, username, email, user_id=None):
        self._username = username
        self._email = email
        self._id = user_id
#adding a property to the username
    @property
    def username(self):
        return self._username
#setting the username
    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeError("Username must be a string.")
        self._username = value
#
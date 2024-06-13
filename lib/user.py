#importing get_db_connection from connection file
from connection import get_db_connection

#creating a class method for the user
class User:
    def __init__(self, username, email, user_id=None):
        self._username = username
        self._email = email
        self._id = user_id
#adding property to the username
    @property
    def username(self):
        return self._username
#setting the username
    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeError("Username must be a string.")
        self._username = value
#giving a property to the email
    @property
    def email(self):
        return self._email
#setting the email
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email must be a string.")
        self._email = value
#giving a property to the id
    @property
    def id(self):
        return self._id
#setting the id
    @id.setter
    def id(self, value):
        if not isinstance(value, int) and value is not None:
            raise TypeError("ID must be an integer or None.")
        self._id = value

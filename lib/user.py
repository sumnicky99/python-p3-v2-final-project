#importing get_db_connection from connection file
from connection import get_db_connection

#creating a class method for the user
class User:
    def __init__(self, username, email, user_id=None):
        self._username = username
        self._email = email
        self._id = user_id

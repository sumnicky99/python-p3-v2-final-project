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
#using repr method
    def __repr__(self):
        return f"<User {self.username}, {self.email}, {self.id}>"
    #creating the user table
    @classmethod
    def create_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL
            )
        '''
        cursor.execute(sql)
        conn.commit()
        conn.close()
    #dropping the table
    @classmethod
    def drop_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = 'DROP TABLE IF EXISTS users'
        cursor.execute(sql)
        conn.commit()
        conn.close()
    #creating a save method
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            sql = '''
                INSERT INTO users (username, email)
                VALUES (?, ?)
            '''
            cursor.execute(sql, (self.username, self.email))
            self.id = cursor.lastrowid
        else:
            sql = '''
                UPDATE users
                SET username = ?, email = ?
                WHERE id = ?
            '''
            cursor.execute(sql, (self.username, self.email, self.id))
        conn.commit()
        conn.close()
    #c
   
       
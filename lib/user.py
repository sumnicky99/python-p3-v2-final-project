from db.connection import get_db_connection

class User:
    def __init__(self, username, email, user_id=None):
        self._username = username
        self._email = email
        self._id = user_id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeError("Username must be a string.")
        self._username = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email must be a string.")
        # Add more validation logic if necessary
        self._email = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int) and value is not None:
            raise TypeError("ID must be an integer or None.")
        self._id = value

    def __repr__(self):
        return f"<User {self.username}, {self.email}, {self.id}>"

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

    @classmethod
    def drop_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = 'DROP TABLE IF EXISTS users'
        cursor.execute(sql)
        conn.commit()
        conn.close()

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

    @classmethod
    def create(cls, username, email):
        existing_user = cls.find_user_by_username_and_email(username, email)
        if existing_user:
            return existing_user
        user = cls(username, email)
        user.save()
        return user

    @classmethod
    def find_user_by_id(cls, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, username, email FROM users WHERE id = ?', (user_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row[1], row[2], row[0])
        return None

    @classmethod
    def find_user_by_username_and_email(cls, username, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, username, email FROM users WHERE username = ? AND email = ?', (username, email))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row[1], row[2], row[0])
        return None

    @classmethod
    def delete(cls, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all_users(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, username, email FROM users')
        rows = cursor.fetchall()
        conn.close()
        return [cls(row[1], row[2], row[0]) for row in rows]

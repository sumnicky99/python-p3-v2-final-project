#importing from connection
from db.connection import get_db_connection

class Expense:
    #intializing
    def __init__(self, user_id, category_id, amount, description, date, expense_id=None):
        self.id = expense_id
        self.user_id = user_id
        self.category_id = category_id
        self.amount = amount
        self.description = description
        self.date = date
#creating expense table
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
#dropping the created table
    @classmethod
    def drop_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = 'DROP TABLE IF EXISTS expenses'
        cursor.execute(sql)
        conn.commit()
#saving
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            sql = '''
                INSERT INTO expenses (user_id, category_id, amount, description, date)
                VALUES (?, ?, ?, ?, ?)
            '''
            cursor.execute(sql, (self.user_id, self.category_id, self.amount, self.description, self.date))
            self.id = cursor.lastrowid
        else:
            sql = '''
                UPDATE expenses
                SET user_id = ?, category_id = ?, amount = ?, description = ?, date = ?
                WHERE id = ?
            '''
            cursor.execute(sql, (self.user_id, self.category_id, self.amount, self.description, self.date, self.id))
        conn.commit()

    @classmethod
    def create(cls, user_id, category_id, amount, description, date):
        expense = cls(user_id, category_id, amount, description, date)
        expense.save()
        return expense
#finding by id
    @classmethod
    def find_by_id(cls, expense_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM expenses WHERE id = ?', (expense_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row[1], row[2], row[3], row[4], row[5], row[0])
        return None
#updating
    def update(self, user_id=None, category_id=None, amount=None, description=None, date=None):
        if user_id is not None:
            self.user_id = user_id
        if category_id is not None:
            self.category_id = category_id
        if amount is not None:
            self.amount = amount
        if description is not None:
            self.description = description
        if date is not None:
            self.date = date

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE expenses SET user_id=?, category_id=?, amount=?, description=?, date=? WHERE id=?',
            (self.user_id, self.category_id, self.amount, self.description, self.date, self.id)
        )
        conn.commit()
#deleting
    @classmethod
    def delete(cls, expense_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        conn.commit()
#getting all expenses
    @classmethod
    def get_all_expenses(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, user_id, category_id, amount, description, date FROM expenses')
        rows = cursor.fetchall()
        conn.close()
        return [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]


    @classmethod
    def all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, user_id, category_id, amount, description, date FROM expenses')
        rows = cursor.fetchall()
        conn.close()
        return [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]

    def __str__(self):
        return f"ID: {self.id}, User ID: {self.user_id}, Category ID: {self.category_id}, Amount: {self.amount}, Description: {self.description}, Date: {self.date}"
from connection import get_db_connection

class Expense:
    def __init__(self, user_id, category_id, amount, description, date, expense_id=None):
        self.id = expense_id
        self.user_id = user_id
        self.category_id = category_id
        self.amount = amount
        self.description = description
        self.date = date
  
   #Adding properties

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int) and value is not None:
            raise TypeError("ID must be an integer or None.")
        self._id = value

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        self._amount = value

    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value
    
    
    @property
    def date(self):
        return self._date
    
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

    @classmethod
    def drop_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = 'DROP TABLE IF EXISTS expenses'
        cursor.execute(sql)
        conn.commit()

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

    @classmethod
    def delete(cls, expense_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        conn.commit()

    @classmethod
    def get_all_expenses(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, user_id, category_id, amount, description, date FROM expenses')
        rows = cursor.fetchall()
        conn.close()
        return [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]


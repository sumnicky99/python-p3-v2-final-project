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
#creating the Category table
    @classmethod
    def create_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        '''
        cursor.execute(sql)
        conn.commit()
        conn.close()
#dropped the created table
    @classmethod
    def drop_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = 'DROP TABLE IF EXISTS categories'
        cursor.execute(sql)
        conn.commit()
        conn.close()
#created a  method for saving
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            sql = '''
                INSERT INTO categories (name)
                VALUES (?)
            '''
            cursor.execute(sql, (self.name,))
            self.id = cursor.lastrowid
        else:
            sql = '''
                UPDATE categories
                SET name = ?
                WHERE id = ?
            '''
            cursor.execute(sql, (self.name, self.id))
        conn.commit()
        conn.close()

    @classmethod
    def create(cls, name):
        category = cls(name)
        category.save()
        return category
#created a class method for getting  categories by name
    @classmethod
    def find_category_by_id(cls, category_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM categories WHERE id = ?', (category_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row[1], row[0])
        return None
 #created a class method for getting  categories by name
    @classmethod
    def find_category_by_name(cls, name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM categories WHERE name = ?', (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row[1], row[0])
        return None
     #created a class method for deleting a specific category
    @classmethod
    def delete(cls, category_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM categories WHERE id = ?', (category_id,))
        conn.commit()
        conn.close()
    
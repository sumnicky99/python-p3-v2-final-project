# lib/db.py
import sqlite3


def get_db_connection():
    return sqlite3.connect('db/expense_tracker.db')

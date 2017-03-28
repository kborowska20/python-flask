import sqlite3
import os

class DB:

    """Class for database connection"""

    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, "todo.db")

    @classmethod
    def get_connection(cls):
        base = sqlite3.connect(cls.filename)
        return base
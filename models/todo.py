import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "data/todo.db")

class Todo:
    """ Class representing todo item."""

    def __init__(self, id, name, deadline, done=False):
        self.id = id
        self.name = name
        self.deadline = deadline
        self.done = done

    def toggle(self):
        """ Toggles item's state """
        self.done = not self.done
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("UPDATE TodoList SET done = ? WHERE id = ?",
                  (self.done, self.id,))
        conn.commit()
        conn.close()

    def save(self):
        """ Saves/updates todo item in database """
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO TodoList (id, name, deadline, done) VALUES (?, ?, ?, ?)",
                (self.id, self.name, self.deadline, self.done,))
        c.execute("UPDATE TodoList SET name = ?, done = ?, deadline = ? WHERE id = ?",
                                 (self.name, self.done, self.deadline, self.id))
        conn.commit()
        conn.close()


    def delete(self):
        """ Removes todo item from the database """
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("DELETE FROM TodoList WHERE id = ?", (self.id,))
        conn.commit()
        c.close()
        return None

    @classmethod
    def get_all(cls):
        """ Retrieves all Todos form database and returns them as list.
        Returns:
            list(Todo): list of all todos
        """
        all_todo =[]
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT * FROM TodoList")

        for row in c:
            todo = Todo(row[0],row[1],row[2],row[3])
            all_todo.append(todo)

        conn.close()
        return all_todo

    @classmethod
    def get_by_id(cls, id):
        """ Retrieves todo item with given id from database.
        Args:
            id(int): item id
        Returns:
            Todo: Todo object with a given id
        """
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT * FROM TodoList WHERE id = ?", (id,))

        for row in c:
            todo = Todo(row[0], row[1], row[2], row[3])

        conn.close()
        return todo


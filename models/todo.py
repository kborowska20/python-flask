from data.database import DB
import sqlite3


class Todo:
    """ Class representing todo item."""

    def __init__(self, id, name, done=False):
        self.id = id
        self.name = name
        self.done = done

    def toggle(self):
        """ Toggles item's state """
        self.done = not(self.done)


    def save(self):
        """ Saves/updates todo item in database """


    def delete(self):
        """ Removes todo item from the database """
        c.execute("DELETE FROM todolist WHERE id = ?", (self.id))
        con.commit()


    @classmethod
    def get_all(cls):
        """ Retrieves all Todos form database and returns them as list.
        Returns:
            list(Todo): list of all todos
        """
        con = sqlite3.connect('data/tdl.db')
        allToDo = []
        c = con.cursor()
        c.execute("SELECT * FROM todolist")
        records = c.fetchall()

        for item in records:

            td = Todo(item[0],item[1],item[2])
            allToDo.append(td)

        con.close()

        return allToDo




    @classmethod
    def get_by_id(cls, id):
        """ Retrieves todo item with given id from database.
        Args:
            id(int): item id
        Returns:
            Todo: Todo object with a given id
        """
        con = sqlite3.connect('data/tdl.db')
        c = con.cursor()
        c.execute("SELECT * FROM todolist WHERE id = ?", (id))

        record = c.fetchone()

        id = record[0]
        name = record[1]

        todo_item = Todo(id,name)
        con.close()

        return todo_item



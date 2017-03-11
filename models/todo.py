import sqlite3

class Todo:
    """ Class representing todo item."""

    def __init__(self, id, name, done=False):
        self.id = id
        self.name = name
        self.done = done

    def toggle(self):
        """ Toggles item's state """
        self.done = True

    def save(self):
        """ Saves/updates todo item in database """
        pass

    def delete(self):
        """ Removes todo item from the database """
        pass

    @classmethod
    def get_all(cls):
        """ Retrieves all Todos form database and returns them as list.
        Returns:
            list(Todo): list of all todos
        """
        conn = sqlite3.connect('tdl.db')
        c = conn.cursor()
        c.execute("SELECT * FROM todolist")
        return [item for item in c]



    @classmethod
    def get_by_id(cls, id):
        """ Retrieves todo item with given id from database.
        Args:
            id(int): item id
        Returns:
            Todo: Todo object with a given id
        """
        conn = sqlite3.connect('tdl.db')
        c = conn.cursor()
        ex = "SELECT * FROM todolist WHERE id = {}".format(id)
        c.execute(ex)
        for att in c:
            TD = Todo(att[0],att[1],att[2])
        return TD


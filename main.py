from flask import Flask, render_template, request
from models.todo import Todo


app = Flask(__name__)


@app.route("/")
def list():
    """ Shows list of todo items stored in the database.
    """
    list_to_do = Todo.get_all()
    return render_template("index.html", list_to_do=list_to_do)


@app.route("/add", methods=['GET', 'POST'])
def add():
    """ Creates new todo item
    If the method was GET it should show new item form.
    If the method was POST it shold create and save new todo item.
    """
    if request.method == 'GET':
        return render_template("add.html")

    elif request.method == "POST":
        render_template('add.html')
        todo_name = request.form['name']
        print(todo_name)
        new_todo_item = Todo(3,todo_name, "True")
        Todo.save(new_todo_item)
        list_to_do = Todo.get_all()
        return render_template("index.html", list_to_do = list_to_do)


@app.route("/remove/<todo_id>")
def remove(todo_id):
    """ Removes todo item with selected id from the database """
    Todo.remove(todo_id)
    list_to_do = Todo.get_all()
    return render_template("index.html",list_to_do=list_to_do)


@app.route("/edit/<todo_id>", methods=['GET', 'POST'])
def edit(todo_id):
    """ Edits todo item with selected id in the database
    If the method was GET it should show todo item form.
    If the method was POST it shold update todo item in database.
    """
    if request.method == 'GET':
        render_template("edit.html", todo_id = todo_id)
    elif request.method == "POST":
        list_to_do = Todo.get_all()
        render_template("index.html",list_to_do=list_to_do)

#@app.route("/toggle/<todo_id>")
#def toggle(todo_id):
#    """ Toggles the state of todo item (save + toggle) """
#    #return "Toggle " + todo_id

if __name__ == "__main__":
    app.run()

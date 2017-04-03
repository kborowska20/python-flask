from flask import Flask, render_template, request, redirect, url_for
from models.todo import Todo


app = Flask(__name__)


@app.route("/")
def list():
    """ Shows list of todo items stored in the database.
    """
    todolist = Todo.get_all()
    return render_template('index.html', todolist=todolist)

@app.route("/add", methods=['GET','POST'])
def add():
    """ Creates new todo item
    If the method was GET it should show new item form.
    If the method was POST it shold create and save new todo item.
    """
    if request.method == 'GET':
        return render_template('add.html')

    elif request.method == 'POST':

        name = request.form['name']
        deadline = request.form['deadline']
        done = request.form.get('done') != None
        new_item = Todo(None, name, deadline, done)
        new_item.save()
        return redirect(url_for('list'))


@app.route("/remove/<todo_id>")
def remove(todo_id):
    """ Removes todo item with selected id from the database """
    item = Todo.get_by_id(todo_id)
    item.delete()
    return redirect(url_for('list'))


@app.route("/edit/<todo_id>", methods=['GET', 'POST'])
def edit(todo_id):
    """ Edits todo item with selected id in the database
    If the method was GET it should show todo item form.
    If the method was POST it shold update todo item in database.
    """
    if request.method == 'GET':

        item = Todo.get_by_id(todo_id)
        return render_template('edit.html', item=item)

    elif request.method == 'POST':

        task_name = request.form['name']
        deadline = request.form['deadline']
        done = request.form.get('done') != None
        item = Todo.get_by_id(todo_id)
        item.name = task_name
        item.deadline = deadline
        item.done = done
        item.save()
        return redirect(url_for('list'))

@app.route("/toggle/<todo_id>")
def toggle(todo_id):
    """ Toggles the state of todo item """
    item = Todo.get_by_id(todo_id)
    item.toggle()
    return redirect(url_for('list'))

@app.route("/jokes")
def carousel():
    return render_template("carusel.html")


if __name__ == "__main__":
    app.run(debug=True)

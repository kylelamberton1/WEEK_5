from application import app, db
from application.models import Tasks

@app.route('/create/<name>', methods=['GET'])
def create(name):
    task = Tasks(name=name, description="A new task")
    db.session.add(task)
    db.session.commit()
    return f'Added new task with name: {name}'

@app.route('/read', methods=['GET'])
def read():
    tasks = Tasks.query.all()
    return_string = ""
    for task in tasks:
        return_string += str(task.name) + '<br>'
    if return_string == "":
        return f'There are no tasks in the database'
    else:
        return f'{return_string}'

@app.route('/update/<newname>', methods=['GET'])
def update(newname):
    task = Tasks.query.first()
    old_name = task.name
    task.name = newname
    db.session.commit()
    return f'The task with name: {old_name}, has been renamed to {newname}'

@app.route('/delete/<name>', methods=['GET'])
def delete(name):
    task = Tasks.query.filter_by(name=name).first()
    old_name = task.name
    db.session.delete(task)
    db.session.commit()
    return f'The task with name: {old_name}, has been deleted'

@app.route('/complete/<name>', methods=['GET'])
def complete(name):
    task = Tasks.query.filter_by(name=name).first()
    if task:
        task.completed = True
        db.session.commit()
        return f'The task with name: {name}, has been set as complete'
    else:
        return f'No task with that name could be found in the database, please try again.'

@app.route('/incomplete/<name>', methods=['GET'])
def incomplete(name):
    task = Tasks.query.filter_by(name=name).first()
    if task:
        task.completed = False
        db.session.commit()
        return f'The task with name: {name}, has been set as incomplete'
    else:
        return f'No task with that name could be found in the database, please try again.'
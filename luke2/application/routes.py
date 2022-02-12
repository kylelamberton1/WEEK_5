from application import app, db
from application.models import Tasks
from flask import render_template

@app.route('/create/<name>', methods=['GET'])
def create(name):
    task = Tasks(name=name, description="A new task")
    db.session.add(task)
    db.session.commit()
    return render_template('create.html', name=name)

@app.route('/read', methods=['GET'])
def read():
    tasks = Tasks.query.all()
    return render_template('read.html', tasks=tasks)


@app.route('/update/<newname>', methods=['GET'])
def update(newname):
    task = Tasks.query.first()
    old_name = task.name
    task.name = newname
    db.session.commit()
    return render_template('update.html', oldname=old_name, newname=newname)

@app.route('/delete/<name>', methods=['GET'])
def delete(name):
    task = Tasks.query.filter_by(name=name).first()
    old_name = task.name
    db.session.delete(task)
    db.session.commit()
    return render_template('delete.html', oldname=old_name)

@app.route('/complete/<name>', methods=['GET'])
def complete(name):
    task = Tasks.query.filter_by(name=name).first()
    tasks = Tasks.query.all()
    error = ""
    if task:
        task.completed = True
        db.session.commit()
    else:
        error = f'No task with that name could be found in the database, please try again.'
    return render_template('tasks.html', error=error, tasks=tasks)

@app.route('/incomplete/<name>', methods=['GET'])
def incomplete(name):
    task = Tasks.query.filter_by(name=name).first()
    tasks = Tasks.query.all()
    error = ""
    if task:
        task.completed = False
        db.session.commit()
    else:
        error = f'No task with that name could be found in the database, please try again.'
    return render_template('tasks.html', error=error, tasks=tasks)
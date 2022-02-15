from application import app, db
from application.models import To_do
from flask import render_template

   
@app.route('/add/<task>')
def add(task):
    add_task = To_do (task=task, description = "a new task")
    db.session.add(add_task)
    db.session.commit()
    return render_template('add.html', task=task)

@app.route('/read')
def read():
    all_to_do = To_do.query.all()
    return render_template('read.html',all_to_do=all_to_do) 

@app.route('/update/<newtask>')
def update(newtask):
    update_task = To_do.query.first()
    old_name=update_task.task
    update_task.task = newtask
    db.session.commit()
    return render_template('update.html', oldname=old_name, newname=newtask)

@app.route('/delete/<task>')
def delete(task):
    first_task = To_do.query.filter_by(task=task).first()
    db.session.delete(first_task)
    db.session.commit()
    return render_template('delete.html', task=task)


@app.route('/completed/<task>')
def completed(task):
    first_task = To_do.query.filter_by(task=task).first()
    first_tasks = To_do.query.all()
    error = ""
    if first_task:
        first_task.completed = True
        db.session.commit()
    else:
        error = f'No task with that name could be found in the database, please try again.'
    return render_template('completed.html', error=error, first_tasks=first_tasks)

@app.route('/incomplete/<task>')
def incomplete(task):
    first_task = To_do.query.filter_by(task=task).first()
    first_tasks = To_do.query.all()
    error = ""
    if first_task:
        first_task.completed = False
        db.session.commit()
    else:
        error = f'No task with that name could be found in the database, please try again.'
    return render_template('completed.html', error=error, first_tasks=first_tasks)

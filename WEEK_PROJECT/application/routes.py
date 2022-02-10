from application import app, db
from application.models import To_do

@app.route('/add')
def add():
    new_task = To_do (task="New Task")
    db.session.add(new_task)
    db.session.commit()
    return "Added new task to database"

@app.route('/read')
def read():
    all_to_do = To_do.query.all()
    to_do_string = ""
    for task in all_to_do:
        to_do_string += "<br>"+ task.task
    return to_do_string

@app.route('/update/<task>')
def update(task):
    first_task = To_do.query.first()
    first_task.task = task
    db.session.commit()
    return first_task.task

@app.route('/delete')
def delete():
    first_task = To_do.query.first()
    db.session.delete(first_task)
    db.session.commit()
    return "You have deleted the first task"


@app.route('/update')
def complete():
    first_task = To_do.query.first()
    first_task.complete = True
    db.session.commit()
    return first_task.complete

'''
@app.route('/update/')
def incomplete():
    first_task = To_do.query.first()
    first_task.incomplete = True
    db.session.commit()
    return first_task.incomplete
'''





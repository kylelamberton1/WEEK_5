from application import app, db
from application.models import To_do

    
@app.route('/add/<task>')
def add(task):
    add_task = To_do (task=task, description = "a new task")
    db.session.add(add_task)
    db.session.commit()
    return f"Added a new task to the database: '{task}'" 

@app.route('/read')
def read():
    all_to_do = To_do.query.all()
    to_do_string = ""
    for task in all_to_do:
        to_do_string += "<br>"+ task.task
    return to_do_string

@app.route('/update/<newtask>')
def update(newtask):
    update_task = To_do.query.first()
    old_name=update_task.task
    update_task.task = newtask
    db.session.commit()
    return f"The first task named: '{old_name}', has been replaced with: '{newtask}'"

@app.route('/delete/<task>')
def delete(task):
    first_task = To_do.query.filter_by(task=task).first()
    db.session.delete(first_task)
    db.session.commit()
    return f"You have deleted the task named: '{task}'"


@app.route('/completed/<task>')
def completed(task):
    first_task = To_do.query.filter_by(task=task).first()
    first_task.completed = True
    db.session.commit()
    return f"You have completed this task: '{task}'"

@app.route('/incomplete/<task>')
def incomplete(task):
    first_task = To_do.query.filter_by(task=task).first()
    first_task.incomplete = True
    db.session.commit()
    return f"You have not completed this task: '{task}'"









from application import db

class To_do(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(500))
    due_date = db.Column(db.DateTime)
    complete = db.Column(db.Boolean)
    incomplete = db.Column(db.Boolean)


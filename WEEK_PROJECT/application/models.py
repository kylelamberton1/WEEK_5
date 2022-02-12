from application import db

class To_do(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50))
    description = db.Column(db.String(200))
    due_date = db.Column(db.DateTime)
    completed = db.Column(db.Boolean)
    


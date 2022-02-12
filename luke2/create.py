from application import db
from application.models import Tasks

db.drop_all()
db.create_all()
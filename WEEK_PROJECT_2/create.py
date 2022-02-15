from application import db
from application.models import To_do

db.drop_all()
db.create_all()
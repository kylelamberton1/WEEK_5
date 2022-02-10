from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os

app = Flask(__name__) # Declare Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # Set the connection string to connect to a database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Declare SQLAlchemy object

class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    cities = db.relationship('Cities', backref='country') 

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

#  many 2 many exercise
class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(30), nullable=False)
    orders_products = db.relationship('orders_products', backref='orders')
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    orders_products = db.relationship('orders_products', backref='products')

class Orders_Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.ForeignKey,('orders.id'), nullable=False)
    product_id = db.Column(db.ForeignKey('products.id'), nullable=False)


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
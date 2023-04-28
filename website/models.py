from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class ClientInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(10000))
    address1 = db.Column(db.String(10000))
    address2 = db.Column(db.String(10000))
    city = db.Column(db.String(10000))
    state = db.Column(db.String(10000))
    zipcode = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gallons = db.Column(db.Integer)
    address = db.Column(db.String(10000))
    date = db.Column(db.String(10000))
    price_to_gallon = db.Column(db.Float(10))
    cost = db.Column(db.Float(10))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    profile = db.relationship('ClientInformation', backref='User', lazy=True) 
    #right now can make multiple profiles
    quotes = db.relationship('Quote', backref='User', lazy=True)


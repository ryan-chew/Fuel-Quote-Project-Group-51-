from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

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
    address1 = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    profile = db.relationship('ClientInformation')
    profile = db.relationship('Quote')


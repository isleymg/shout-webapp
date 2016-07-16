from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event, ForeignKey
from sqlalchemy.pool import Pool
from shout import app

db = SQLAlchemy(app)
# event.listens_for(Pool, 'checkout')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
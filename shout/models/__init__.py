from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event, ForeignKey
from sqlalchemy.pool import Pool
from shout import app

db = SQLAlchemy(app)
event.listens_for(Pool, 'checkout')

class MapPoint(db.Model):
	data_id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.DateTime)
	category = db.Column(db.DateTime)
	latitude = db.Column(db.Float, nullable=False)
	longitude = db.Column(db.Float, nullable=False)

	def __init__(self, date, category, latitude, longitude):
		self.date = date
		self.category = category
		self.latitude = latitude
		self.longitude = longitude

class BlogPost(db.Model):
	blog_id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.DateTime)
	title = db.Column(db.String(32))
	body = db.Column(db.String(512), nullable=False)
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	location = db.Column(db.String(128))

	def __init__(self, date, title, body, latitude, longitude, location):
		self.date = date
		self.title = title
		self.body = body
		self.latitude = latitude
		self.longitude = longitude
		self.location = location

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+oursql://db_user@localhost/sample_db'

# this isn't at the top because LOL circular imports
from models import db, User
db.init_app(app)
db.create_all()

# circular imports...again
import shout.views
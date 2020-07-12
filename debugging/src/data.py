
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import Flask
#from debugging.src.demo import app

class Config(object):
    # debug
    DEBUG = False

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "postgresql://scott:tiger@localhost/shelter"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
db = SQLAlchemy(app)

engine = create_engine('postgresql://scott:tiger@localhost/mydatabase')

class Host(db.Model):
    __tablename__ = "host"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    refugee = db.relationship('Refugee', backref='host')


class Refugee(db.Model):
    __tablename__ = "refugee"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    phone = db.Column(db.String(11), unique=True)
    address = db.Column(db.Text)
    guest = db.Column(db.Integer)
    suburbs = db.Column(db.String(255))
    is_flaged = db.Column(db.Boolean(), default=0)

    user_id = db.Column(db.Integer, db.ForeignKey('host.id'))

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))




from flask_sqlalchemy import SQLAlchemy
from debugging.src.demo import app

db = SQLAlchemy(app)

class Host(db.Model):
    __tablename__ = "host"

    id = db.column(db.Integer, primary_key = True)
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

    id = db.column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))





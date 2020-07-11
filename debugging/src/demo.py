from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)

class Config(object):
    DEBUG = True
    ITCAST = "python"

app.config.from_object(Config)

db = SQLAlchemy(app)

class Host(db.Model):
    __tablename__ = "tbl_hosts"

    id = db.column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    refugee =





# the main page
@app.route("/")
def homepage():
    return app.send_static_file('homepage.html')

@app.route("/signin/")
def signIn():
    return

@app.route("/register/", methods=["GET","POST"])
def register():




if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)
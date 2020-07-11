from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, redirect, flash, session, request
from werkzeug.security import generate_password_hash

from debugging.src.form import LoginForm,RegisterForm
from debugging.src.data import Host, Refugee, User

app = Flask(__name__)

db = SQLAlchemy(app)


# the main page
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/signin/")
def signIn():
    return render_template("signin.html")

@app.route("/logout/")
def logout():
    session.pop("user_id", None)
    return render_template("homepage.html")

@app.route("/register/user", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        user = User(
            username = data["username"],
            email = data["email"],
            pwd = generate_password_hash(data["pwd"]),
        )
        db.session.add(user)
        db.session.commit()
        flash("successful！", "ok")
    return render_template("register.html", form=form)


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(email=data["email"]).first()
        if not user :
            flash("Email not exist！", "err")
            return redirect(url_for("home.login"))
        if not user.check_pwd(data["pwd"]):
            flash("password is not correct！", "err")
            return redirect(url_for("home.login"))

        session["user_id"] = user.id
        return redirect(url_for("home.index"))
    return render_template("home/login.html", form=form)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)
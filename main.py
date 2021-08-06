from flask import Flask, render_template, request, redirect, url_for
from hashlib import sha1
from data import db_session
from data.users import User
from forms.login import LoginForm
from forms.registration import RegistrationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "yan_dushkin_secret_key"


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def not_found():
    return render_template("404.html")


@app.errorhandler(401)
def authentification_needed():
    return redirect("/login")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        form = RegistrationForm()
        return render_template("register.html", form=form)

    else:
        email = request.form["email"]
        password = request.form["password"]
        repeated_password = request.form["password_repeated"]

        if password != repeated_password:
            return "You didn't enter the same password!"
        
        db_session.global_init("db/database.db")
        session = db_session.create_session()

        user = User()
        user.email = email
        user.hashed_password = sha1(password.encode()).hexdigest()


        #emails = cursor.execute("FROM users SELECT email")
        
        #session.add(user)
        #session.commit()

        return redirect("/success")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        form = LoginForm()
        return render_template("login.html", form=form)
    else:
        email = request.form["email"]
        password = request.form["password"]
        password_hash = sha1(password.encode()).hexdigest()

        return redirect("/")

@app.route("/create_article", methods=["POST", "GET"])
def create_publication():
    if request.method == "GET":
        form = ArticleForm()
        return render_template("create_article.html", form=form)
    else:
        title = request.form["title"]
        short_text = request.form["text"]
        link = request.form["link"]

        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


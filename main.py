from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from hashlib import sha1
# I need to make databases here

app = Flask(__name__)
app.config["SECRET_KEY"] = "yan_dushkin_secret_key"


class RegistrationForm(FlaskForm):
    email = StringField("Login/Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password_repeated = PasswordField("Repeat password", validators=[DataRequired()])
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    email = StringField("Login/Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


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
        # here i must add user's data to database

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
        # here i have to check data
        password_hash = sha1(password.encode()).hexdigest()


        return redirect("/success")


@app.route("/cryptos/bitcoin")
def bitcoin():
    return render_template("bitcoin.html")


@app.route("/cryptos/dash")
def dash():
    return render_template("dash.html")

@app.route("/cryptos/monero")
def monero():
    return render_template("monero.html")


@app.route("/algorithms/pow")
def pow():
    return render_template("pow.html")


@app.route("/algorithms/pos")
def pos():
    return render_template("pos.html")


@app.route("/transactions")
def transactions():
    return render_template("transactions.html")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import *
from wtforms.validators import *
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
bootstrap = Bootstrap5(app)

class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and \
            login_form.password.data == "admin123":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://username:password@localhost/dbname"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.before_first_request()
def init_db():
    db.create_all()
    print("Created the Database")

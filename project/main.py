from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)

app.config.from_object(config)

db = SQLAlchemy(app)


@app.route("/")  # this is the default display when the page is run
def home():
    return render_template("home.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.before_first_request()  # this is for the hardcoded database and it should be done only once
def init_db():
    db.create_all()
    print("Created the Database")

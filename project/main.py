from flask import Flask, render_template
from config import *  # contains DB config
from extension import db
from models import *  # important: ensure your models are imported here

app = Flask(__name__)
app.config.from_object("config")

db.init_app(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/menu/burgers")
def burgers():
    return render_template("burgers.html")


@app.route("/menu/pizza")
def pizza():
    return render_template("pizza.html")


@app.route("/menu/drinks")
def drinks():
    return render_template("drinks.html")


# Create tables once at startup
with app.app_context():
    db.create_all()
    print("✅ Database tables created.")

if __name__ == "__main__":
    app.run(debug=True)

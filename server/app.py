# Routes defined in app.py
from flask import Flask
from flask_migrate import Migrate
from models import db,  Card, Binder

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
migrate = Migrate(app, db)
db.init_app(app)

@app.route("/")
def hello_world():
    return '<p>hello world</p>'
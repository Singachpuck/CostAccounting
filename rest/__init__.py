import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from rest.model.Account import Account
from rest.model.Category import Category
from rest.model.Transaction import Transaction
from rest.model.User import User

with app.app_context():
    db.drop_all()
    db.create_all()

from rest import views
import os
from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_smorest import Api, Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["API_TITLE"] = "Cost Accounting Rest Api"
app.config["API_VERSION"] = "v3"
app.config["OPENAPI_VERSION"] = "3.0.2"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=3600)

db = SQLAlchemy(app)


from .model.Account import Account
from .model.Category import Category
from .model.Transaction import Transaction
from .model.User import User

with app.app_context():
    db.drop_all()
    db.create_all()


from .controller.auth import blp as auth_blueprint
from .controller.user import blp as user_blueprint
from .controller.category import blp as category_blueprint
from .controller.account import blp as account_blueprint
from .controller.transaction import blp as transaction_blueprint

BASE_URL = '/api/' + app.config["API_VERSION"]

parent_blp = Blueprint('base', __name__, url_prefix=BASE_URL)
parent_blp.register_blueprint(auth_blueprint)
parent_blp.register_blueprint(user_blueprint)
parent_blp.register_blueprint(category_blueprint)
parent_blp.register_blueprint(account_blueprint)
parent_blp.register_blueprint(transaction_blueprint)

api = Api(app)
api.register_blueprint(parent_blp)

jwt = JWTManager(app)

from .controller import errorHandler

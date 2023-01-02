from flask_jwt_extended import create_access_token
from flask_smorest import abort
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from rest import app
from rest.service.UserService import getUserByUsername


def get_access_token(auth):

    user = getUserByUsername(auth['name'])

    if user is None:
        abort(400, message=f'User {auth["name"]} doesn\'t exist')

    if not pbkdf2_sha256.verify(auth['password'], user.password):
        abort(400, message='Illegal password')

    return {
        "access_token": create_access_token(identity=user.id),
        "expires_in": app.config["JWT_ACCESS_TOKEN_EXPIRES"].seconds
    }

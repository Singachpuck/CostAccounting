from flask_smorest import abort
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from rest.dao.impl.orm.UserDaoORM import UserDaoORM
from rest.model.User import User

userDao = UserDaoORM()


def getAllUsers():
    return list(map(lambda user: user.to_dict(), userDao.getUsers()))


def getUserById(id):
    return userDao.getUserById(id)


def getUserByUsername(username):
    return userDao.getUserByUsername(username)


def createUser(data):
    old_user = getUserByUsername(data['name'])

    if old_user is not None:
        abort(400, message=f'User {data["name"]} already exists!')

    old_user = userDao.getUserByPassword(data['password'])

    if old_user is not None:
        abort(400, message='Password already exists!')

    new_user = User(name=data['name'], password=pbkdf2_sha256.hash(data['password']))
    userDao.createUser(new_user)

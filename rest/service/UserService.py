from rest.dao.UserDao import getUsers, createUser as create, getUserById as getById
from rest.model.User import User


def getAllUsers():
    return list(map(lambda user: {'id': user.id, 'name': user.name}, getUsers()))


def getUserById(id):
    return getById(id)


def createUser(data):
    newUser = User(name=data['name'])
    create(newUser)

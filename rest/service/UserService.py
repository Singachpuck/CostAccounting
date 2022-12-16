from rest.dao.impl.orm.UserDaoORM import UserDaoORM
from rest.model.User import User

userDao = UserDaoORM()


def getAllUsers():
    return list(map(lambda user: user.to_dict(), userDao.getUsers()))


def getUserById(id):
    return userDao.getUserById(id)


def createUser(data):
    newUser = User(name=data['name'])
    userDao.createUser(newUser)

from rest import db
from rest.dao.UserDao import UserDao
from rest.model.User import User


class UserDaoORM(UserDao):

    def getUsers(self) -> list[User]:
        return db.session.query(User).all()

    def getUserById(self, id):
        return db.session.query(User).get(id)

    def createUser(self, user) -> None:
        db.session.add(user)
        db.session.commit()

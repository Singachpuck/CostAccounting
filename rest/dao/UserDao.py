from rest.model.User import User


class UserDao:

    def getUsers(self) -> list[User]:
        raise NotImplementedError()

    def getUserById(self, id):
        raise NotImplementedError()

    def createUser(self, user) -> None:
        raise NotImplementedError()

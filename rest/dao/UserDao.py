from rest.model.User import User


class UserDao:

    def getUsers(self) -> list[User]:
        raise NotImplementedError()

    def getUserById(self, id) -> User:
        raise NotImplementedError()

    def getUserByPassword(self, password) -> User:
        raise NotImplementedError()

    def createUser(self, user) -> None:
        raise NotImplementedError()

    def getUserByUsername(self, username) -> User:
        raise NotImplementedError()

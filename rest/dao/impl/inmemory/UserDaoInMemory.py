from rest.dao.UserDao import UserDao
from rest.model.User import User

users = [
    User(1, "John Sallivan"),
    User(2, "Linda Mure"),
    User(3, "Bob Winkers")
]


class UserDaoInMemory(UserDao):

    def __generateId(self):
        return max(users, key=lambda user: user.id).id + 1

    def getUsers(self) -> list[User]:
        return list(users)

    def getUserById(self, id):
        for user in users:
            if user.id == id:
                return user

        raise AttributeError(f'User with id {id} doesn\'t exist')

    def createUser(self, user) -> None:
        if user.id is None:
            user.id = self.__generateId()
        elif user.id in [u.id for u in users]:
            raise AttributeError(f'Category with id {user.id} already exists')

        users.append(user)

from rest.dao.UserDao import users
from rest.dao.CategoryDao import categories
from rest.model.Transaction import Transaction
from datetime import datetime

transactions = [
    Transaction(1, users[0], categories[0], datetime(2022, 9, 14, 14, 00, 00), 1000),
    Transaction(2, users[1], categories[1], datetime(2022, 8, 10, 17, 00, 00), 10000),
    Transaction(3, users[2], categories[2], datetime(2022, 9, 14, 18, 30, 00), 679),
    Transaction(4, users[0], categories[3], datetime(2022, 9, 30, 10, 10, 00), 2500),
    Transaction(5, users[1], categories[4], datetime(2022, 6, 5, 19, 00, 00), 3100),
    Transaction(6, users[2], categories[0], datetime(2022, 1, 1, 20, 00, 00), 48000),
    Transaction(7, users[0], categories[1], datetime(2022, 2, 19, 12, 00, 00), 5120),
    Transaction(8, users[1], categories[2], datetime(2022, 3, 25, 3, 00, 00), 10700),
    Transaction(9, users[2], categories[3], datetime(2022, 4, 8, 21, 00, 00), 3170),
    Transaction(10, users[0], categories[4], datetime(2022, 5, 12, 15, 20, 00), 43809)
]


def __generateId():
    return max(transactions, key=lambda transaction: transaction.id).id + 1

def getTransactionsByUserId(userId) -> list[Transaction]:
    return list(filter(lambda transaction: transaction.user.id == userId, transactions))


def getTransactionsByUserIdAndCategory(userId, category) -> list[Transaction]:
    return list(
        filter(lambda transaction: transaction.user.id == userId and transaction.category == category, transactions))


def createTransaction(transaction: Transaction) -> None:
    if transaction.id is None:
        transaction.id = __generateId()
    elif transaction.id in [t.id for t in transactions]:
        raise AttributeError(f'Category with id {transaction.id} already exists')

    transactions.append(transaction)

from datetime import datetime

from rest.dao.TransactionDao import getTransactionsByUserId as getByUserId
from rest.dao.TransactionDao import getTransactionsByUserIdAndCategory as getByUserIdAndCategory, \
    createTransaction as create
from rest.model.Transaction import Transaction
from rest.service.CategoryService import getCategoryByName, getCategoryById
from rest.service.UserService import getUserById


def getTransactionsByUserId(userId):
    return list(map(lambda transaction: transaction.to_dict(), getByUserId(userId)))


def getTransactionsByUserIdAndCategory(userId, categoryName):
    return list(map(lambda transaction: transaction.to_dict(),
                    getByUserIdAndCategory(userId, getCategoryByName(categoryName))))


def createTransaction(data):
    user = getUserById(data['userId'])
    category = getCategoryById(data['categoryId'])
    newTransaction = Transaction(user=user, category=category, timestamp=datetime.now(), amount=data['amount'])
    create(newTransaction)

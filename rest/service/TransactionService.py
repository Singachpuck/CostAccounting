from datetime import datetime

from rest.dao.impl.orm.TransactionDaoORM import TransactionDaoORM
from rest.model.Transaction import Transaction
from rest.service.AccountService import *
from rest.service.CategoryService import getCategoryByName, getCategoryById

transactionDao = TransactionDaoORM()


def getTransactionsByUserId(userId):
    return list(map(lambda transaction: transaction.to_dict(), transactionDao.getTransactionsByUserId(userId)))


def getTransactionsByUserIdAndCategory(userId, categoryName):
    category = getCategoryByName(categoryName)
    if category is None:
        raise AttributeError(f'Category {categoryName} doesn\'t exist')

    return list(map(lambda transaction: transaction.to_dict(),
                    transactionDao.getTransactionsByUserIdAndCategory(userId, category)))


def createTransaction(data):
    amount = float(data['amount'])
    category = getCategoryById(data['categoryId'])
    account_from = getAccountById(data['accountFrom'])
    account_to = getAccountById(data['accountTo'])

    if account_to.id == account_from.id:
        raise AttributeError('Transaction between the same accounts is not allowed')

    withdraw(account_from, amount)
    deposit(account_to, amount)
    newTransaction = Transaction(account_to=account_to,
                                 account_from=account_from,
                                 category=category,
                                 timestamp=datetime.now(),
                                 amount=amount)
    transactionDao.createTransaction(newTransaction)

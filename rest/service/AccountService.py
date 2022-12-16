from rest.dao.impl.orm.AccountDaoORM import AccountDaoORM
from rest.model.Account import Account

from rest.service.UserService import getUserById

accountDao = AccountDaoORM()


def getAllAccounts():
    return list(map(lambda account: account.to_dict(), accountDao.getAllAccounts()))


def getAccountById(id: int):
    return accountDao.getAccountById(id)


def createAccount(data):
    user = getUserById(data['user'])
    amount = float(data['amount'])
    newAccount = Account(user=user, amount=amount)
    accountDao.createAccount(newAccount)


def deposit(account: Account, amount: float):
    if amount <= 0:
        raise AttributeError('Amount can not be negative')

    account.amount += amount
    accountDao.updateAccount(account)


def withdraw(account: Account, amount: float):
    if amount <= 0:
        raise AttributeError('Amount can not be negative')

    if account.amount < amount:
        raise AttributeError(f'Not enough money on account: {account.id}')

    account.amount -= amount
    accountDao.updateAccount(account)
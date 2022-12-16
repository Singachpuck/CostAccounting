from rest import db
from rest.dao.AccountDao import AccountDao
from rest.model.Account import Account


class AccountDaoORM(AccountDao):

    def getAllAccounts(self) -> list[Account]:
        return db.session.query(Account).all()

    def getAccountById(self, id: int) -> Account:
        return db.session.query(Account).get(id)

    def createAccount(self, account: Account) -> None:
        db.session.add(account)
        db.session.commit()

    def updateAccount(self, account: Account) -> None:
        db.session.merge(account)
        db.session.commit()

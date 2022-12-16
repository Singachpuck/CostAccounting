from rest import db
from rest.dao.TransactionDao import TransactionDao
from rest.model.Account import Account
from rest.model.Transaction import Transaction


class TransactionDaoORM(TransactionDao):

    def getTransactionsByUserId(self, userId) -> list[Transaction]:
        return db.session.query(Transaction).join(Transaction.account_from).filter(Account.user_id == userId).all()

    def getTransactionsByUserIdAndCategory(self, userId, category) -> list[Transaction]:
        return db.session\
            .query(Transaction)\
            .join(Transaction.account_from)\
            .filter(Account.user_id == userId, Transaction.category_id == category.id)

    def createTransaction(self, transaction: Transaction) -> None:
        db.session.add(transaction)
        db.session.commit()

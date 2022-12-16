from rest.model.Transaction import Transaction


class TransactionDao:

    def getTransactionsByUserId(self, userId) -> list[Transaction]:
        raise NotImplementedError()

    def getTransactionsByUserIdAndCategory(self, userId, category) -> list[Transaction]:
        raise NotImplementedError()

    def createTransaction(self, transaction: Transaction) -> None:
        raise NotImplementedError()


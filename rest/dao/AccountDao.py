from rest.model.Account import Account


class AccountDao:

    def getAllAccounts(self) -> list[Account]:
        raise NotImplementedError()

    def getAccountById(self, id: int) -> Account:
        raise NotImplementedError()

    def createAccount(self, account: Account) -> None:
        raise NotImplementedError()

    def updateAccount(self, account: Account) -> None:
        raise NotImplementedError()

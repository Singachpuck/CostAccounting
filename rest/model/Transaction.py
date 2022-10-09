from rest.model.Category import Category
from rest.model.User import User
import datetime


class Transaction:

    def __init__(self, id: int = None, user: User = None, category: Category = None, timestamp: datetime = None, amount: float = None):
        self.id = id
        self.user = user
        self.category = category
        self.timestamp = timestamp
        self.amount = amount

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.id,
            'category': self.category.id,
            'timestamp': self.timestamp,
            'amount': self.amount
        }

import datetime

from rest import db
from rest.model.Account import Account
from rest.model.Category import Category


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_from_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    account_from = db.relationship('Account', foreign_keys=[account_from_id])
    account_to_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    account_to = db.relationship('Account', foreign_keys=[account_to_id])
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category')
    amount = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, id: int = None, account_from: Account = None, account_to: Account = None, category: Category = None, timestamp: datetime = None, amount: float = None):
        self.id = id
        self.account_from = account_from
        self.account_to = account_to
        self.category = category
        self.timestamp = timestamp
        self.amount = amount

    def to_dict(self):
        return {
            'id': self.id,
            'account_from': self.account_from.id,
            'account_to': self.account_to.id,
            'category': self.category.id,
            'timestamp': self.timestamp,
            'amount': self.amount
        }

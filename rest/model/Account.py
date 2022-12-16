from rest import db
from rest.model.User import User


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User')
    amount = db.Column(db.Float)

    def __init__(self, id: int = None, user: User = None, amount: float = None):
        self.id = id
        self.user = user
        self.amount = amount

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.id,
            'amount': self.amount
        }

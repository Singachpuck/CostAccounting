from rest import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, id: int = None, name: str = None):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

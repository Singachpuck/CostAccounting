from rest import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100), unique=True)

    def __init__(self, id: int = None, name: str = None, password: str = None):
        self.id = id
        self.name = name
        self.password = password

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

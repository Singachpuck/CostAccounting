from rest import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, id: int = None, name: str = None):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

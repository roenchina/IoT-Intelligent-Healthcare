from database.extension import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    cash = db.Column(db.Integer)

    def __init__(self, name, thrust):
        self.name = name
        self.thrust = thrust

    def __repr__(self):
        return '<User %r>' % self.name

    def __str__(self):
        return '<User %s>' % self.name

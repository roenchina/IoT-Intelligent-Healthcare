'''
0. 从extension中import db
1. 表的创建
2. 定义许多类，设置表之间的对应关系

'''
from extension import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, name, thrust):
        self.name = name
        self.thrust = thrust

    def __repr__(self):
        return '<User %r>' % self.name

    def __str__(self):
        return '<User %s>' % self.name

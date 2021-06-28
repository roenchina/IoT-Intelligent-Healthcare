from datetime import datetime

from database.extension import db


class User(db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    passwd = db.Column(db.String(30), nullable=False)
    role = db.Column(db.Enum('doctor', 'patient', 'manager'), default='manager', nullable=False)

    allown = db.relationship('Own', backref='user')

    def __repr__(self):
        return f'<User: {self.id}, {self.name}>'


class Facility(db.Model):
    __tablename__ = 'tb_facility'
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    type = db.Column(db.Enum('temp', 'humi', 'bodyt', 'rate'), default='temp', nullable=False)
    status = db.Column(db.Enum('online', 'offline', 'error'), default='online', nullable=False)
    unit = db.Column(db.String(10), nullable=False)
    step = db.Column(db.Numeric(6, 2), nullable=False)
    wardID = db.Column(db.String(10))
    bedID = db.Column(db.String(10))

    alldata = db.relationship('Data', backref='facility')

    def __repr__(self):
        return f'<Facility {self.id}, {self.name}>'

class Data(db.Model):
    __tablename__ = 'tb_data'
    id = db.Column(db.String(10), primary_key=True)
    # facID = db.Column(db.String(10))
    time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    location_lng = db.Column(db.Numeric(9, 6), nullable=False)
    location_lat = db.Column(db.Numeric(9, 6), nullable=False)
    type = db.Column(db.Enum('normal', 'warning'), default='normal', nullable=False)
    amount = db.Column(db.Numeric(5, 2), nullable=False)

    facID = db.Column(db.String(10), db.ForeignKey('tb_facility.id'))

    def __repr__(self):
        return f'<Data {self.id}>'


class Own(db.Model):
    __tablename__ = 'tb_own'
    id = db.Column(db.Integer, primary_key=True)
    # userID = db.Column(db.String(10), nullable=False)
    wardID = db.Column(db.String(10), nullable=False)
    bedID = db.Column(db.String(10), nullable=False)

    userID = db.Column(db.String(10), db.ForeignKey('tb_user.id'))

    def __repr__(self):
        return f'<Own {self.id}>'

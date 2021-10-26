from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))



class customer(db.Model):
    custID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(32), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    suburb = db.Column(db.String(64), nullable=False)
    orders = db.relationship('order', backref='orderingCust', lazy='dynamic')

    def __repr__(self):
        return '<Customer {}>'.format(self.name)

class driver(db.Model):
    driverID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    vehicle = db.Column(db.String(64), nullable=False)
    orders = db.relationship('order', backref='placedWithDriver', lazy='dynamic')

    def __repr__(self):
        return '<Driver {}>'.format(self.name)

class register(db.Model):
    accesslevel = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    password2 = db.Column(db.String(128), nullable=False)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')    


    def __repr__(self):
        return '<register {}>'.format(self.name)


class signin(db.Model):
    email1 =db.Column(db.String(128), primary_key=True)
    paskey = db.Column(db.String(128), nullable=False)
    remember_me = db.Column(db.String(128), nullable=False)
    submit1 = db.Column(db.String(128), nullable=False)


    def validate_password(self, paskey):
        user = User.query.filter_by(paskey=paskey.data).first()
        if user is None:
            raise ValidationError('That is not correct')
            return check_password_hash(self.password_hash, paskey)   


    def __repr__(self):
        return '<signin {}>'.format(self.name)


class order(db.Model):
    price =db.Column(db.String(128))
    email1 =db.Column(db.String(128), primary_key=True)
    size = db.Column(db.String(128), nullable=False)
    ordernum= db.Column(db.String(128))
    creit = db.Column(db.String(128), nullable=False)
    expiredata = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)


    def __repr__(self):
        return '<checkout {}>'.format(self.name)




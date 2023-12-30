from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    resources = db.relationship('Resource', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Resource(db.Model):
    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    name = db.Column(db.String(120))
    position = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Resource {}>'.format(self.usage, self.name)

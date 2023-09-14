from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, unique=True)
    pages = db.Column(db.Integer)
    type = db.Column(db.String(32))

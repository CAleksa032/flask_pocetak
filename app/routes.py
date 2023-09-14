from http.client import OK
from app import app, db
from app.schemas import BookRequestSchema
from flask import request
from app.models import Book

book_request_schema = BookRequestSchema()


@app.route('/')
def index():
    return "<p>Hellow world!</p>"


@app.route('/user', methods=['POST'])
def add_user():
    book = book_request_schema.load(request.json)
    book_instance = Book(title=book['title'], pages=book['pages'], type=book['type'])
    db.session.add(book_instance)
    db.session.commit()

    return '12345', OK

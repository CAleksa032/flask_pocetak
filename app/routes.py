from http.client import OK
from app import app
from schemas import BookResponseSchema
from models import Book


@app.route('/')
def index():
    return "<p>Hellow world!</p>"


@app.route('/user', methods=['POST'])
def add_user():
    tmp_book = Book(BookResponseSchema)
    return '', OK

from marshmallow import Schema
from marshmallow.fields import Str, Int


class BookResponseSchema(Schema):
    title = Str(data_key='bookTitle', required=True)
    pages = Int(data_key='bookPages', required=True)

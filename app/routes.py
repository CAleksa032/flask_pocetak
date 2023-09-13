from app import app


@app.route('/')
def index():
    return "<p>Hellow world!</p>"

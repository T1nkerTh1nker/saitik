from flask import Flask


app = Flask(__name__)

from src.view import *

if __name__ == '__main__':
    app.run(debug=True)

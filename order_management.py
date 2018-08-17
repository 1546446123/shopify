import os

from flask import Flask
app = Flask(__name__)

s = os.environ['MY']

@app.route('/')
def hello_world():
    return s

if __name__ == '__main__':
    app.run()
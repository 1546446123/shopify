import os

from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return ""

@app.route('/orders', methods=['POST'])
def orders_manage():
    if request.method == 'POST':
        print(request.form)
        return "a"
    else:
        return "asdasd"
    return "v"

if __name__ == '__main__':
    app.run()
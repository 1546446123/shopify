import os

from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return ""

@app.route('/orders')
def orders_manage():
    if request.method == 'POST':
        print(request.form)
        return
    else:
        return
    return ""

if __name__ == '__main__':
    app.run()
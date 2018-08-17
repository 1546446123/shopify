# coding: utf8
import shopify
from flask import Flask, request, redirect
import os

API_KEY = os.environ["API_KEY"]
PASSWORD = os.environ["PASSWORD"]
SHOP_URL = os.environ["SHOP_URL"]
shop_url =  "https://%s:%s@%s/admin" % (API_KEY, PASSWORD, SHOP_URL)

shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current()
app = Flask(__name__)


@app.route('/')
def hello_world():
    return ""

@app.route('/orders', methods=['POST'])
def orders_manage():
    if request.method == 'POST':
        print(request.form)
        return redirect("http://www.google.com", code=302)
    else:
        return "asdasd"
    return "v"

if __name__ == '__main__':
    app.run()
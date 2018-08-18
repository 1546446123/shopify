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


def create_order(first_name, last_name, phone, town, address1, user_id):
    order = shopify.Order()

    shipping_address = shopify.ShippingAddress()
    shipping_address.first_name = first_name
    shipping_address.last_name = last_name
    shipping_address.city = town
    shipping_address.address1 = address1
    shipping_address.phone = phone
    shipping_address.country = "Ukraine"

    billing_address = shopify.BillingAddress()
    billing_address.first_name = first_name
    billing_address.last_name = last_name
    billing_address.city = town
    billing_address.address1 = address1
    billing_address.phone = phone
    billing_address.country = "Ukraine"

    customer = shopify.Customer.find(user_id)

    item = shopify.LineItem()
    item.variant_id = 12438658154559
    item.quantity = 1

    order.shipping_address = shipping_address
    order.billing_address = billing_address
    order.line_items = [item]
    order.gateway = "Оплата при отриманні"
    order.payment_gateway_names = ["Оплата при отриманні"]

    order.customer = customer

    order.contact_email = customer.email

    #d["user_id"] = 686081769535
    order.email = customer.email
    order.fulfillment_status = 'fulfilled'
    order.send_receipt = True
    order.send_fulfillment_receipt = False
    order.suppress_notifications = False

    order.save()
    return order.order_status_url


@app.route('/')
def hello_world():
    return ""

@app.route('/orders', methods=['POST'])
def orders_manage():
    result = "zzzz"
    try:
        if request.method == 'POST':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            shipping = request.form['shipping']
            tel = request.form['tel']
            town = request.form['town']
            user_id = request.form['user_id']
            address1 = request.form['warehouses']

            redirect_url = create_order(first_name, last_name, tel, town, address1, user_id)
            result = redirect_url
    except Exception as e:
        result = e.message
    finally:
        return result



if __name__ == '__main__':
    app.run()
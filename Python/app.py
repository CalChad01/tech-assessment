from flask import Flask
from flask import request
from flask import render_template
import random
import json

ORDERS = "api/data/orders.json"

app = Flask(__name__)

@app.route("/")
def home():
    html = ''
    html += '<h1>Welcome to my take on the Sogeti Tech Assignment</h1>'

    html += 'Click <a href=/view>       here</a> to view all orders<br>'
    html += 'Click <a href=/create>     here</a> to create an order<br>'
    html += 'Click <a href=/update>     here</a> to update an order<br>'
    html += 'Click <a href=/delete>     here</a> to delete an order<br>'

    html += "<font color = white><a href=https://www.youtube.com/watch?v=dQw4w9WgXcQ style=color:#ffffff> secret</a> </font>"

    return html


@app.route("/view")
def view():
    html = ''
    
    # this works, which is cool

    try:
        orders = json.load(open(ORDERS))
        html += json.dumps(orders, indent=2)
        html += '<br>'
        html += 'Click <a href=/> here</a> to go back<br>'
    except:
        html += 'No orders found<br>'
        html += 'Click <a href=/> here</a> to go back<br>'

    return html


@app.route("/create", methods = ['GET'])
def create():
    return  render_template('textboxC.html')

@app.route("/create", methods = ['POST'])
def create_post():

    customerID = request.form['customerID']
    orderID = request.form['orderID']
    orderInfo = request.form['orderInfo']

    # this should read these into json format then save them into orders.json
    # currently gets a 400 error

    data =  {
        'customerID':   customerID,
        'orderID':      orderID,
        'orderInfo':    orderInfo,
    }
    temp_json = json.dumps(data)
    with open(ORDERS, "w") as orders:
        json.dump(temp_json, orders)


    html = ''
    html = 'Thank you for submitting your order<br>'
    html += 'Click <a href=/> here</a> to go back<br>'

    return html


@app.route("/update", methods = ['GET'])
def update():
    return  render_template('textboxU.html')

@app.route("/update", methods = ['POST'])
def update_post():

        orderID = request.form['orderID']
        orders = json.load(open(ORDERS))

        # search for the order and update if found
        order_found = False

        html = ''

        if order_found:
            html += 'Your order has been updated<br>'
            html += 'Click <a href=/> here</a> to go back<br>'
        else:
            html += 'Could not find your order<br>'
            html += 'Click <a href=/> here</a> to go back<br>'

        return html


@app.route("/delete", methods = ['GET'])
def delete():
    return  render_template('textboxD.html')

@app.route("/delete", methods = ['POST'])
def delete_post():

        orderID = request.form['orderID']
        orders = json.load(open(ORDERS))

        # search for the order and delete if found
        order_found = False

        html = ''

        if order_found:
            html += 'Your order has been deleted<br>'
            html += 'Click <a href=/> here</a> to go back<br>'
        else:
            html += 'Could not find your order<br>'
            html += 'Click <a href=/> here</a> to go back<br>'

        return html

# definitely ran out of time with the delete and update functions

# it seems the common theme here is Json stuff not working
# oh well

if __name__ == "__main__":
    app.run(debug=True)
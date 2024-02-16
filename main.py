import json

from flask import Flask, request, jsonify
from requests import HTTPError

from config.config import Config
from api.orders_api import OrdersAPI
from utils.api_utils import ApiResponse

app = Flask(__name__)
app.config.from_object(Config)
orders_api = OrdersAPI()
VENDOR_ID = '364124'
ORDER_ID = '5424514d-e146-4130-84e3-e34a36c2b94c'

# TODO localmente se levanta en: http://127.0.0.1:5000/


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/v1/healthcheck')
def healthcheck():
    try:
        return orders_api.healthcheck()
    except HTTPError as e:
        return jsonify({'error': str(e)}), 500


@app.route('/v1/orders/')
def get_orders():
    try:
        return orders_api.get_orders(VENDOR_ID)
    except HTTPError as e:
        return jsonify({'error': str(e)}), 500


@app.route('/v1/order/')
def get_order():
    try:
        return orders_api.get_order(ORDER_ID)
    except HTTPError as e:
        return jsonify({'error': str(e)}), 500


@app.route('/webhook-pos/ordenes-test', methods=['POST'])
def webhook_handler():
    try:
        data = request.json
        order_json = json.dumps(data, indent=2)
        print(order_json)
        return 'Webhook received successfully', 200

    except Exception as e:
        return ApiResponse.error(str(e)), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

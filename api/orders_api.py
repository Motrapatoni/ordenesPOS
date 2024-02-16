from datetime import datetime, timedelta
import requests
from flask import jsonify, request
from config.config import Config


class OrdersAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = {
            'Authorization': Config.PEDIDOSYA_TOKEN,
            'Content-Type': 'application/json'
        }

    def healthcheck(self):
        url = f'{self.base_url}/ping'
        response = requests.get(url)
        if response.status_code == 200:
            return 'pong', response.status_code
        else:
            return 'Not healed', response.status_code

    def get_orders(self, partner_id, start_created_at_datetime=None,
                   end_created_at_datetime=None):
        page_size = 20
        page = 1
        if not start_created_at_datetime:
            start_created_at_datetime = datetime.now() - timedelta(days=2)
        if not end_created_at_datetime:
            end_created_at_datetime = datetime.now()

        start_created_at_datetime_str = start_created_at_datetime.strftime('%Y-%m-%dT%H:%M:%S')
        end_created_at_datetime_str = end_created_at_datetime.strftime('%Y-%m-%dT%H:%M:%S')
        print(f"Start: {start_created_at_datetime_str}, End: {end_created_at_datetime_str}")

        url = (f'{self.base_url}/v1/orders/vendors/{partner_id}?page_size={page_size}&'
               f'page={page}&'
               f'start_created_at_datetime={start_created_at_datetime_str}&'
               f'end_created_at_datetime={end_created_at_datetime_str}')
        response = requests.get(url, headers=self.headers)
        return jsonify(response.json()), response.status_code

    def get_order(self, order_id):
        url = f'{self.base_url}/v1/orders/{order_id}'
        response = requests.get(url, headers=self.headers)
        return jsonify(response.json()), response.status_code

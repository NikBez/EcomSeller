import datetime
import json

import requests

from config.config import Settings


class OzonAPIHandler:
    def __init__(self, client_id, ozon_api_key):
        self.client_id = client_id
        self.api_key = ozon_api_key

    def get_etgb(self):
        url = 'https://api-seller.ozon.ru/v1/posting/global/etgb'

        headers = {
            'Content-Type': 'application/json',
            'Client-Id': Settings.OZON_CLIENT_ID,
            'Api-Key': Settings.OZON_API_KEY,
        }

        current_date = datetime.datetime.utcnow()
        from_date = current_date - datetime.timedelta(days=-4)

        data = {
            "date": {
                "from": from_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                "to": current_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            }
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response = response.text
        return json.loads(response)

    def get_etgb_by_endpoint(self):
        url = 'https://api-seller.ozon.ru/v1/posting/global/etgb'

        headers = {
            'Content-Type': 'application/json',
            'Client-Id': Settings.OZON_CLIENT_ID,
            'Api-Key': Settings.OZON_API_KEY,
        }

        current_date = datetime.datetime.utcnow()
        from_date = current_date - datetime.timedelta(days=-4)

        data = {
            "date": {
                "from": from_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                "to": current_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            }
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response = response.text
        return json.loads(response)

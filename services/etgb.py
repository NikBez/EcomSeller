import json
from datetime import datetime, timedelta
from fastapi import HTTPException
import aiohttp

from clickhouse.connect import db
from clickhouse.crud import insert_record
from random import randint

from api.schemas import EtgbBase


async def transfer_ETGB_from_ozon_to_ch(Client_Id, Api_Key):
    async with aiohttp.ClientSession() as session:
        url = 'https://api-seller.ozon.ru/v1/posting/global/etgb'
        headers = {
            'Content-Type': 'application/json',
            'Client-Id': Client_Id,
            'Api-Key': Api_Key
        }
        current_date = datetime.utcnow()
        from_date = current_date - timedelta(days=-4)
        data = {
            "date": {
                "from": from_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                "to": current_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            }
        }
        response = await session.post(url, headers=headers, json=data)
        if response.status == 403:
            raise HTTPException(status_code=403, detail="Autentication faild")
        response = await response.text()
        new_etgbs = json.loads(response)

    new_etgbs = {

        "result": [
            {
                "posting_number": f"{randint(0, 999999)}",
                "etgb": {
                    "number": "985478",
                    "date": "st34243ring",
                    "url": "str432ing"
                }
            },
            {
                "posting_number": f"{randint(0, 999999)}",
                "etgb": {
                    "number": "77897",
                    "date": "7897",
                    "url": "7987"
                }
            }
        ]
    }
    if new_etgbs['result']:
        session = db.connect()
        new_records = []
        for etgb in new_etgbs['result']:
            is_new = insert_record(session, etgb['posting_number'], etgb['etgb'])
            if is_new:
                new_records.append(EtgbBase(**etgb))
        return new_records

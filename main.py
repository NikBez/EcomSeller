from clickhouse.connect import db
from clickhouse.crud import insert_record
from ozon.api import OzonAPIHandler

if __name__ == '__main__':
    # ozon_api = OzonAPIHandler()
    # new_etgbs = ozon_api.get_etgb()

    new_etgbs = {
        "result": [
            {
                "posting_number": "2",
                "etgb": {
                    "number": "11111",
                    "date": "11111",
                    "url": "11111"
                }
            }
        ]
    }
    if new_etgbs['result']:
        session = db.connect()
        for etgb in new_etgbs['result']:
            insert_record(session, etgb['posting_number'], etgb['etgb'])
    else:
        print('Запрос к OZON не выдал результатов')

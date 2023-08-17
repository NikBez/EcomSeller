from clickhouse.connect import db
from clickhouse.crud import insert_record
from config.config import Settings
from ozon.api import OzonAPIHandler


def parse():
    ozon_api = OzonAPIHandler(Settings.OZON_CLIENT_ID, Settings.OZON_API_KEY)
    new_etgbs = ozon_api.get_etgb()
    db.check_before_laungh()

    new_etgbs = {

        "result": [
            {
                "posting_number": "234243",
                "etgb": {
                    "number": "432342",
                    "date": "st34243ring",
                    "url": "str432ing"
                }
            },
            {
                "posting_number": "98789",
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
        for etgb in new_etgbs['result']:
            insert_record(session, etgb['posting_number'], etgb['etgb'])
    else:
        print('Запрос к OZON не выдал результатов')


if __name__ == '__main__':
    parse()
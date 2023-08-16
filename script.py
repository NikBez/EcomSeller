from clickhouse.connect import db
from clickhouse.crud import insert_record
from ozon.api import OzonAPIHandler


def parse():
    ozon_api = OzonAPIHandler()
    new_etgbs = ozon_api.get_etgb()

    if new_etgbs['result']:
        session = db.connect()
        for etgb in new_etgbs['result']:
            insert_record(session, etgb['posting_number'], etgb['etgb'])
    else:
        print('Запрос к OZON не выдал результатов')


if __name__ == '__main__':
    parse()
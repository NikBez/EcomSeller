import asyncio

from clickhouse.connect import db
from clickhouse.crud import insert_record
from config.config import Settings
from ozon.api import OzonAPIHandler


async def parse():
    ozon_api = OzonAPIHandler(Settings.OZON_CLIENT_ID, Settings.OZON_API_KEY)
    new_etgbs = await ozon_api.get_etgb()
    db.check_before_laungh()
    if new_etgbs['result']:
        session = db.connect()
        for etgb in new_etgbs['result']:
            insert_record(session, etgb['posting_number'], etgb['etgb'])
    else:
        print('Запрос к OZON не выдал результатов')


if __name__ == '__main__':
    asyncio.run(parse())

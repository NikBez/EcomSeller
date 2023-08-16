from clickhouse_driver import Client

from config.config import Settings


def record_exists(session, posting_number):
    query = f"SELECT * FROM ozon.etgb WHERE posting_number = '{posting_number}' LIMIT 1"
    session = Client(Settings.CLICKHOUSE_HOST, password=Settings.CLICKHOUSE_PASSWORD)
    result = session.execute(query)
    return bool(result)  # Return True if the record exists, False otherwise


def insert_record(session, posting_number, etgb_data):
    if not record_exists(session, posting_number):
        query = f"INSERT INTO ozon.etgb VALUES ('{posting_number}', {etgb_data['number']}, {etgb_data['date']}, {etgb_data['url']})"
        session.execute(query)
        print(f'Запись с номером {posting_number} добавлена в базу')


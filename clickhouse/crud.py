from clickhouse.connect import ClickHouseConnector


def record_exists(session: ClickHouseConnector, posting_number):
    query = f"SELECT * FROM ozon.etgb WHERE posting_number = '{posting_number}' LIMIT 1"
    result = session.execute(query)
    return bool(result)


def insert_record(session: ClickHouseConnector, posting_number, etgb_data):
    if not record_exists(session, int(posting_number)):
        query = f"INSERT INTO ozon.etgb VALUES ('{posting_number}', {etgb_data['number']}, {etgb_data['date']}, {etgb_data['url']})"
        session.execute(query)
        print(f'Запись с номером {posting_number} добавлена в базу')

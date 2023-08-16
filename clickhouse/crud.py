from clickhouse.connect import ClickHouseConnector, db


def record_exists(session: ClickHouseConnector, posting_number: str) -> bool:
    query = f"SELECT * FROM ozon.etgb WHERE posting_number = '{posting_number}' LIMIT 1"
    result = session.execute(query)
    return bool(result)


def insert_record(session: ClickHouseConnector, posting_number: str, etgb_data: str) -> None:
    if not record_exists(session, int(posting_number)):
        query = f"INSERT INTO ozon.etgb VALUES ('{posting_number}', {etgb_data['number']}, {etgb_data['date']}, {etgb_data['url']})"
        session.execute(query)
        print(f'Запись с номером {posting_number} добавлена в базу')


def get_records() -> dict:
    with db.connect() as session:
        query = "SELECT posting_number, etgb_number, etgb_date, etgb_url FROM ozon.etgb"
        result = session.execute(query)
        dict_result = []
        for etgb in result:
            record = {
                'posting_number': etgb[0],
                'etgb': {
                    'number': etgb[1],
                    'date': etgb[2],
                    'url': etgb[3]
                }
            }
            dict_result.append(record)
        return dict_result

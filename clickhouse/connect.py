from clickhouse_driver import Client

from config.config import Settings


class ClickHouseConnector:

    @staticmethod
    def check_before_laungh():
        session = db.connect()
        session.execute('CREATE DATABASE IF NOT EXISTS ozon')
        table_schema = """
                CREATE TABLE IF NOT EXISTS ozon.etgb (
                    posting_number String,
                    etgb_number String,
                    etgb_date DateTime,
                    etgb_url String
        
                ) ENGINE = MergeTree()
                ORDER BY posting_number
                """
        session.execute(table_schema)

    def connect(self):
        try:
            with Client(Settings.CLICKHOUSE_HOST, password=Settings.CLICKHOUSE_PASSWORD) as client:
                return client
        except Exception as e:
            print(f"Error connecting to ClickHouse: {e}")
            return None


db = ClickHouseConnector()
db.check_before_laungh()

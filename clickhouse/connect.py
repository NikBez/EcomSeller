from clickhouse_driver import connect
from config.config import Settings

class ClickHouseConnector:

    @staticmethod
    def create_db(con):
        with con.cursor() as cursor:
            cursor.execute('SHOW databases')
            result = cursor.fetchall()
            print(result)

    def connect(self):
        con = connect(Settings.CLICKHOUSE_DSN)
        self.create_db(con)


    def create_tables(self):
        pass


db = ClickHouseConnector()
db.connect()

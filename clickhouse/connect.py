from clickhouse_driver import connect


class ClickHouseConnector:
    con = connect('clickhouse://localhost')

    @classmethod
    def create_db(cls):
        with cls.con.cursor() as cursor:
            cursor.execute('SHOW databases')
            result = cursor.fetchall()
            print(result)

    @classmethod
    def create_tables(self):
        pass

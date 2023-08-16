from environs import Env

env = Env()
env.read_env()

class Settings:
    OZON_CLIENT_ID = env('OZON_CLIENT_ID')
    OZON_API_KEY = env('OZON_API_KEY')

    CLICKHOUSE_DSN = env('CLICKHOUSE_DSN')



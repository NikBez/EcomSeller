from fastapi import FastAPI

from api.routers import api_router
from clickhouse.connect import db

app = FastAPI(title='Elektronik Ticaret Gümrük Beyannamesi (ETGB) для продавцов из Турции.')
app.include_router(api_router, prefix='/api')
db.check_before_laungh()

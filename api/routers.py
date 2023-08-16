from fastapi import APIRouter
from clickhouse.crud import get_records


api_router = APIRouter(tags=['ETGB'])

@api_router.get('')
async def get_ETGB():
    records = get_records()
    return records

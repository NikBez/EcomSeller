from typing import Annotated

from fastapi import APIRouter, Header, HTTPException

from api.schemas import EtgbList
from clickhouse.crud import get_records
from services.etgb import transfer_ETGB_from_ozon_to_ch

api_router = APIRouter(tags=['ETGB'])


@api_router.get('/get_clickhouse',
                summary='All records from clickhouse',
                description='Get all ETGB from clickhouse'
                )
async def get_ETGB():
    records = get_records()
    return records


@api_router.post('/get_ozon', response_model=EtgbList,
                 summary='Get last 4 days in Ozon API and wright to Clickhouse',
                 description='Return only new records'
                 )
async def get_ETGB_from_ozon(
        Client_Id: Annotated[str | None, Header()] = None,
        Api_Key: Annotated[str | None, Header()] = None
):
    new_etgb_from_ch = await transfer_ETGB_from_ozon_to_ch(Client_Id, Api_Key)
    if new_etgb_from_ch:
        return EtgbList(result=new_etgb_from_ch)
    raise HTTPException(status_code=404, detail="No new records")

from pydantic import BaseModel


class Etgb(BaseModel):
    number: str
    date: str
    url: str


class EtgbBase(BaseModel):
    posting_number: str | None = None
    etgb: Etgb | None = None


class EtgbList(BaseModel):
    result: list[EtgbBase] | None = None

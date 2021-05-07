from ..api.schema import RespuestaApi as SchemaResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from typing import List, Optional, TypeVar, Generic
from pydantic.generics import GenericModel

T = TypeVar('T')
DataT = TypeVar('DataT')
Optional[DataT]


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


def createResponseSuccess(customtype: DataT, response: Optional[DataT]) -> dict:
    json = SchemaResponse[customtype](
        code=0, date=datetime.now(), message="Good", data=response)
    return jsonable_encoder(json)


def createResponseError() -> dict:
    json = SchemaResponse[dict](code=1, date=datetime.now(
    ), message="An issue has occurred, please try again.", data=None)
    return jsonable_encoder(json)


def createResponseErrorUvicorn(exceptionuv: UnicornException) -> dict:
    json = SchemaResponse[dict](code=2, date=datetime.now(
    ), message=exceptionuv.__dict__['name'], data=None)
    return jsonable_encoder(json)

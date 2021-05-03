from datetime import date, datetime
from pydantic import BaseModel

from typing import Any, List, Optional, TypeVar, Generic,NamedTuple
from pydantic.generics import GenericModel
from pydantic.types import Json

from enum import Enum as enumModel
T = TypeVar('T')

DataT = TypeVar('DataT')

class AjedrezEnum(str, enumModel):
    DISPONIBLE = 'Disponible'
    OBSTACULO = 'Obstaculo'
    REINA = 'Reina'

class Point(NamedTuple):
    fila: int
    columna: int

class FiguraResponse(BaseModel):
    selected:bool
    figura:AjedrezEnum

class ParamProblemTres(BaseModel):
    n: int
    k: int
    rq: int
    cq: int
    obstaculo: Optional[List[List[int]]]

class ParamProblemTresResponse(BaseModel):
    color: str
    #icono: str
    #selected:bool
    #disponible:bool
    #obstaculo:bool
    indice: int
    coordenada:Point
    detalle:FiguraResponse
    class Config:
        orm_mode = True


class RespuestaApi(GenericModel, Generic[DataT]):
    codigo: int
    fechahora: datetime
    mensaje: str
    data: Optional[DataT]

    class Config:
        schema_extra = {
            "examplex": {
                "codigo": 1,
                "fechahora": "20/10/2020",
                "mensaje": "Msg Sistem",
                "data": "Mensaje",
            }
        }

from datetime import date, datetime
from pydantic import BaseModel

from typing import Any, List, Optional, TypeVar, Generic, NamedTuple
from pydantic.generics import GenericModel
from pydantic.types import Json

from enum import Enum as enumModel
T = TypeVar('T')

DataT = TypeVar('DataT')


class AjedrezEnum(str, enumModel):
    DISPONIBLE = 'Disponible'
    OBSTACULO = 'Obstaculo'
    REINA = 'Reina'
    NINGUNO = 'Ninguno'


class PositionEnum(str, enumModel):
    TOP = 'Top'
    DOWN = 'Down'
    LEFT = 'Left'
    RIGHT = 'Right'
    TOPLEFT = 'TopLeft'
    TOPRIGHT = 'TopRight'
    DOWNLEFT = 'DownLeft'
    DOWNRIGHT = 'DownRight'


class ParamProblemTree(BaseModel):
    world: str

class DetailTeam(BaseModel):
    name: str
    sets: int

class Team(BaseModel):
    local: DetailTeam
    visitant: DetailTeam

class Category(BaseModel):
    name: str
    teams: List[Team]

class ResponsePadel(BaseModel):
    category: str
    team: str
    tie: bool
    stadistic: List[dict]


class ObstacleModel(BaseModel):
    row: int
    column: int


class Point(NamedTuple):
    row: int
    column: int


class DetailChees(BaseModel):
    info: int
    position: Point


class FigureResponse(BaseModel):
    selected: bool
    imageurl: Optional[str]
    figure: AjedrezEnum


class ParamProblemTwo(BaseModel):
    n: int
    k: int
    rq: int
    cq: int
    obstacle: Optional[List[ObstacleModel]]


class ParamProblemTwoResponse(BaseModel):
    color: str
    index: int
    coordinate: Point
    detail: FigureResponse

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

from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional, TypeVar, Generic, NamedTuple
from pydantic.generics import GenericModel

from enum import Enum as enumModel
T = TypeVar('T')

DataT = TypeVar('DataT')


class ChessEnum(str, enumModel):
    AVAILABLE = 'Available'
    OBSTACLE = 'Obstacle'
    QUEEN = 'Queen'
    NONEDATA = 'NoneData'


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
    figure: ChessEnum


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
    code: int
    date: datetime
    message: str
    data: Optional[DataT]

    class Config:
        schema_extra = {
            "examplex": {
                "code": 1,
                "date": "20/10/2020",
                "message": "Msg Sistem",
                "data": "Mensaje",
            }
        }

from datetime import datetime
from typing import List
from fastapi import APIRouter
from ..repository.repolaboratory import RepoLaboratory as RepoLab
from .schema import RespuestaApi as SchemaResponse, ResponsePadel, ParamProblemTree, DetailChees, ParamProblemTwo, ParamProblemTwoResponse, ParamProblemTwoResponse, FigureResponse, AjedrezEnum, Point, Category as SchemaCategory
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi import Body
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/laboratory")


# nombre categoria
# todos resultados
# pareja juega en  casa -sets 5 -- pareja visistante sets 88
# no mas de 16 caracteres

# Fin

# salida
# Por Categoriaa
# Ganador Name
# Empate
# victoria = 2
# derrota =1
# no hay empate

# GANANDO B
# Partido no jugador

@router.post("/problemone", response_model=SchemaResponse[List[ResponsePadel]])
async def problemuno(request: List[SchemaCategory]):
    try:
        response = await RepoLab.GeneratePadel(request)
        json = SchemaResponse[List[ResponsePadel]](
            codigo=0, fechahora=datetime.now(), mensaje="Bien", data=response)
        json_compatible_item_data = jsonable_encoder(json)
        return JSONResponse(status_code=200, content=json_compatible_item_data)
    except Exception as e:
        print(e)
        json_compatible_item_data = jsonable_encoder(SchemaResponse[dict](codigo=1, fechahora=datetime.now(
        ), mensaje="An error has occurred", data=None))
        return JSONResponse(status_code=200, content=json_compatible_item_data)


@router.post("/problemtwo", response_model=SchemaResponse[List[List[ParamProblemTwoResponse]]])
async def problemdos(request: ParamProblemTwo):
    try:
        print(request)
        response = await RepoLab.GenerateChess(request)
        json = SchemaResponse[List[List[ParamProblemTwoResponse]]](
            codigo=0, fechahora=datetime.now(), mensaje="Bien", data=response)
        json_compatible_item_data = jsonable_encoder(json)
        return JSONResponse(status_code=200, content=json_compatible_item_data)
    except Exception as e:
        json_compatible_item_data = jsonable_encoder(SchemaResponse[dict](codigo=1, fechahora=datetime.now(
        ), mensaje="An error has occurred", data=None))
        return JSONResponse(status_code=200, content=json_compatible_item_data)


@router.post("/problemtree", response_model=SchemaResponse[int])
async def problemtree(request: ParamProblemTree):
    try:
        print(request)
        response = await RepoLab.GenerateResultTree(request.world)
        json = SchemaResponse[int](
            codigo=0, fechahora=datetime.now(), mensaje="Bien", data=response)
        json_compatible_item_data = jsonable_encoder(json)
        return JSONResponse(status_code=200, content=json_compatible_item_data)
    except Exception as e:
        json_compatible_item_data = jsonable_encoder(SchemaResponse[dict](codigo=1, fechahora=datetime.now(
        ), mensaje="An error has occurred", data=None))
        return JSONResponse(status_code=200, content=json_compatible_item_data)

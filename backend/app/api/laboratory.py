from datetime import datetime
from typing import List
from fastapi import APIRouter
from ..repository.repolaboratory import RepoLaboratory as RepoLab
from .schema import RespuestaApi as SchemaResponse, ResponsePadel, DetailChees, ParamProblemTres, ParamProblemTresResponse, ParamProblemTresResponse as ShemaTres, FiguraResponse as SchemaFigura, AjedrezEnum, Point, Categoria as SchemaCategoria
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

@router.post("/problemone")
async def problemuno(request: List[SchemaCategoria]):
    try:
        response: ResponsePadel = await RepoLab.GeneratePadel(request)
        dataxx = SchemaResponse[ResponsePadel](
            codigo=0, fechahora=datetime.now(), mensaje="Bien", data=response)
        json_compatible_item_data = jsonable_encoder(dataxx)
        return JSONResponse(status_code=200, content=json_compatible_item_data)
    except Exception as e:
        print(e)
        # customdict = post_utils.LoadExcepcion(e)
        # print(customdict)
        json_compatible_item_data = jsonable_encoder(SchemaResponse[dict](codigo=1, fechahora=datetime.now(
        ), mensaje="Ha Ocurrido Un Error", data=None))
        return JSONResponse(status_code=200, content=json_compatible_item_data)


@router.post("/problemtree", response_model=SchemaResponse[List[List[ShemaTres]]])
async def problemtres(request: ParamProblemTres):
    try:
        response: List[List[ShemaTres]] = await RepoLab.GenerateChess(request)
        #mimenu = []
        dataxx = SchemaResponse[List[List[ShemaTres]]](
            codigo=0, fechahora=datetime.now(), mensaje="Bien", data=response)
        json_compatible_item_data = jsonable_encoder(dataxx)
        return JSONResponse(status_code=200, content=json_compatible_item_data)
    except Exception as e:
        print(e)
        # customdict = post_utils.LoadExcepcion(e)
        # print(customdict)
        json_compatible_item_data = jsonable_encoder(SchemaResponse[dict](codigo=1, fechahora=datetime.now(
        ), mensaje="Ha Ocurrido Un Error", data=None))
        return JSONResponse(status_code=200, content=json_compatible_item_data)

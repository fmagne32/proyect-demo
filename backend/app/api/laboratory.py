from datetime import datetime
from typing import List
from fastapi import APIRouter
from ..repository.repolaboratory import RepoLaboratory as RepoLab
from .schema import  RespuestaApi as SchemaResponse, ParamProblemTres, ParamProblemTresResponse, ParamProblemTresResponse as ShemaTres, FiguraResponse as SchemaFigura, AjedrezEnum,Point
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi import Body
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/laboratory")



@router.post("/problemtree", response_model=SchemaResponse[List[ShemaTres]])
async def problemtres(request: ParamProblemTres):
    try:
        response:List[ShemaTres] = await RepoLab.GenerateChess(request)
        #mimenu = []
        dataxx = SchemaResponse[List[ShemaTres]](
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

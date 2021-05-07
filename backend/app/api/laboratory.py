from typing import List
from fastapi import APIRouter
from ..repository.repolaboratory import RepoLaboratory as RepoLab
from .schema import RespuestaApi as SchemaResponse, ResponsePadel, ParamProblemTree, ParamProblemTwo, ParamProblemTwoResponse, ParamProblemTwoResponse, FigureResponse, Category as SchemaCategory
from fastapi.responses import JSONResponse

from ..api.utility import createResponseSuccess, createResponseError

router = APIRouter(prefix="/laboratory")

@router.post("/problemone", response_model=SchemaResponse[List[ResponsePadel]])
async def problemone(request: List[SchemaCategory]):
    try:
        data = await RepoLab.GeneratePadel(request)
        response: dict = createResponseSuccess(List[ResponsePadel], data)
        return JSONResponse(status_code=200, content=response)
    except Exception as e:
        response: dict = createResponseError(dict, None)
        return JSONResponse(status_code=200, content=response)

@router.post("/problemtwo", response_model=SchemaResponse[List[List[ParamProblemTwoResponse]]])
async def problemdos(request: ParamProblemTwo):
    try:
        data = await RepoLab.GenerateChess(request)
        response: dict = createResponseSuccess(List[List[ParamProblemTwoResponse]], data)
        return JSONResponse(status_code=200, content=response)
    except Exception as e:
        response: dict = createResponseError(dict, None)
        return JSONResponse(status_code=200, content=response)


@router.post("/problemtree", response_model=SchemaResponse[int])
async def problemtree(request: ParamProblemTree):
    try:
        data: int = await RepoLab.GenerateResultTree(request.world)
        response: dict = createResponseSuccess(int, data)
        return JSONResponse(status_code=200, content=response)
    except Exception as e:
        response: dict = createResponseError(dict, None)
        return JSONResponse(status_code=200, content=response)

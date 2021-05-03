from datetime import datetime
from typing import List
from fastapi import APIRouter
from .schema import  RespuestaApi as SchemaResponse, ParamProblemTres, ParamProblemTresResponse, ParamProblemTresResponse as ShemaTres, FiguraResponse as SchemaFigura, AjedrezEnum,Point
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi import Body
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/laboratory")



@router.post("/problematres", response_model=SchemaResponse[dict])
async def problematres(modelo: ParamProblemTres):
    try:
        # #6d4c41 Cafe
        # #efebe9 Plomo claro

        # Basico
        # N 4 K-> obstaculo 0
        # La reina 4 4

        a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
        # print(type(a))
        """for i in range(len(a)):
            for j in range(len(a[i])):
                # print(a[i][j], end=' ')"""

        """unidadx = []

        for i in range(modelo.n):
            uno = []
            uno.append(i)
            unidadx.append(uno)
            # print(uno)
            for j in range(modelo.n):
                print(f'El resultado de {i} - {j}')
        print(unidadx)"""

        n = modelo.n
        a = [[0] * n for i in range(n)]
        b = [[0] * n for i in range(n)]

        contador = 0
        for i in range(n):
            for j in range(n):
                # print(f'El resultado de {i} - {j}')
                numerox = NumeroPar(j, i)
                a[i][j] = numerox
            #contador += 1
        print(a)
        print(contador)

        print("===========OPCION B==========")
        mimenu: List[ShemaTres] = []
        for i in range(n):
            for j in range(n):
                # print(f'El resultado de {i} - {j}')
                #numerox = NumeroPar(j,i)
                demoxxxx = LoadInfo(i,j)
                #MensajeX("Dd")
                print(demoxxxx)
                mimenu.append(demoxxxx)
                b[i][j] = n-contador
            contador += 1
        print(b)
        #https://javarevisited.blogspot.com/2015/09/how-to-loop-two-dimensional-array-in-java.html#axzz6tpTSaSja
        print("=========V2=========")
        unico =b[1][1]
        print(unico)
        print(mimenu)
        info = jsonable_encoder(modelo.dict())
        dataxx = SchemaResponse[dict](
            codigo=0, fechahora=datetime.now(), mensaje="Bien", data=info)
        json_compatible_item_data = jsonable_encoder(dataxx)
        return JSONResponse(status_code=200, content=json_compatible_item_data)
    except Exception as e:
        # customdict = post_utils.LoadExcepcion(e)
        # print(customdict)
        json_compatible_item_data = jsonable_encoder(RespuestaApi[dict](codigo=1, fechahora=datetime.now(
        ), mensaje="Ha Ocurrido Un Error", data=None))
        return JSONResponse(status_code=200, content=json_compatible_item_data)

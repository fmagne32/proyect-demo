from datetime import datetime
import json
from typing import List
from ..api.schema import  RespuestaApi as SchemaResponse, ParamProblemTres, ParamProblemTresResponse, ParamProblemTresResponse as ShemaTres, FiguraResponse as SchemaFigura, AjedrezEnum,Point


class RepoLaboratory:
    @classmethod
    def NumeroPar(cls,numero: int, index: int) -> int:
        b = 0
        if index % 2 == 0:
            if numero % 2 == 0:
                b = 1
        else:
            if numero % 2 != 0:
                b = 1
        return b
    
    @classmethod
    def LoadInfo(cls,indice: int, valor: int,value_extra:int) -> ShemaTres:
        numero: int = cls.NumeroPar(indice,valor)
        micolor: str = numero == 0 and "#6d4c41" or "#efebe9"
        detallex = SchemaFigura(selected=False, figura=AjedrezEnum.DISPONIBLE)
        inicial = indice+ 1
        second = valor+ 1
        info = ShemaTres(color=micolor,coordenada=Point(inicial,second), indice=value_extra, detalle=detallex)
        return info

    @classmethod
    async def GenerateChess(cls,entity:ParamProblemTres) -> List[ShemaTres]:
        try:
            n = entity.n

            filareina= entity.rq
            columnareina= entity.cq
            b = [[0] * n  for i in range(n)]
            contador = 0
            mimenu: List[ShemaTres] = []
            for i in range(n):
                for j in range(n):
                    # print(f'El resultado de {i} - {j}')
                    #numerox = NumeroPar(j,i)
                    value_extra = n-contador
                    demoxxxx = cls.LoadInfo(i,j,value_extra)
                    mimenu.append(demoxxxx)
                    b[i][j] = value_extra
                contador += 1
            
            print(b)
            #print(mimenu)
            return mimenu
        except Exception as e:
            print(e)
            raise Exception(e)

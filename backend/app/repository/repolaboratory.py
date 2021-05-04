from datetime import datetime
import json
import functools
from typing import List, Optional
from ..api.schema import RespuestaApi as SchemaResponse, PadelEnum, DetalleEquipo, ResponsePadel, ParamProblemTres, ParamProblemTresResponse, ParamProblemTresResponse as ShemaTres, FiguraResponse as SchemaFigura, AjedrezEnum, Point, DetailChees, Categoria as SchemaCategoria
from pydantic.schema import schema
from pydantic import parse_obj_as


class RepoLaboratory:
    # Load Reina
    @classmethod
    def FiltradoArray(cls, lista: List[ShemaTres], fila: int, columna: int):
        for x in lista:
            if cls.GetReina(x, fila, columna):
                x.detalle = SchemaFigura(
                    selected=True, figura=AjedrezEnum.REINA)
                # print("indice")
                # print(lista.index(x))
            # mimenu[index] = filtradovv[0]
        return lista

    # Load Ataque

    @classmethod
    def FiltradoDinamico(cls, lista: List[List[ShemaTres]], fila: int, columna: int, longitud: int):
        contador = longitud
        contadory = 0
        listaunixo = []
        filtrox = []
        columna_x = 0
        columna_y = 0
        for y in lista:

            filtroxsub = []
            for x in y:
                if ((x.detalle.figura != AjedrezEnum.REINA)):
                    if x.indice == fila:
                        x.detalle = SchemaFigura(
                            selected=True, figura=AjedrezEnum.DISPONIBLE)
                    if x.coordenada.columna == columna:  # Columna Reina Load Vertica
                        x.detalle = SchemaFigura(
                            selected=True, figura=AjedrezEnum.DISPONIBLE)
                # filtroxsub.append()

                detail = dict(
                    info=contador, posicion=dict(fila=columna_x, columna=columna_y))
                filtroxsub.append(detail)

                columna_x = ((fila-contadory)+1)
                columna_y = ((columna - contadory)+1)

                if ((x.coordenada.fila == columna_x) and (x.coordenada.columna == columna_y)):  # MINI BUG
                    # Ok

                    print(
                        f'filtrado abajo izquierda 222  {columna_x} - {columna_y} CONTADOR x {contador} CONTADOR y {contadory} Indice {x.indice}')
                    print(
                        f'coordenada encontrada 222 {x.coordenada.fila} - {x.coordenada.columna}')
                    x.detalle = SchemaFigura(
                        selected=True, figura=AjedrezEnum.DISPONIBLE)

                """if ((x.coordenada.fila == 3) and (x.coordenada.columna == 2)):  # MINI BUG
                    # Ok

                    print(
                        f'filtrado abajo izquierda vvv  {columna_x} - {columna_y} CONTADOR x {contador} CONTADOR y {contadory} Indice {x.indice}')
                    print(
                        f'coordenada encontrada vvv {x.coordenada.fila} - {x.coordenada.columna}')
                    x.detalle = SchemaFigura(
                        selected=True, figura=AjedrezEnum.DISPONIBLE)"""

            filtrox.append(filtroxsub)
            # detail = DetailChees(
            #    info=contador, posicion=Point(columna_x, columna_y))

            # listaunixo.append(y)

            listaunixo.append(y)
            contador -= 1
            contadory += 1
        # print(filtrox)
        print("contador")
        print(contador)
        print("====================================")

        mijson = json.dumps(filtrox, ensure_ascii=False)
        # print(mijson)
        return listaunixo

    @classmethod
    def FiltradoArrayDos(cls, lista: List[ShemaTres], fila: int, columna: int):

        print("llamado")
        newfila = fila
        newcol = columna
        contador = 0
        # Horinzontal
        for x in lista:
            if ((x.detalle.figura != AjedrezEnum.REINA)):
                if x.indice == fila:
                    x.detalle = SchemaFigura(
                        selected=True, figura=AjedrezEnum.DISPONIBLE)
                if x.coordenada.columna == columna:  # Columna Reina Load Vertica
                    x.detalle = SchemaFigura(
                        selected=True, figura=AjedrezEnum.DISPONIBLE)

                filaq = (fila-contador)
                columnaq = (columna-contador)

                # region Abajo Derecha
                # 4,3 ==> 3,4 Derecha Abajo
                # f -1; c+1 ++
                filak = (fila-contador)
                columnak = (columna+contador)

                if ((x.coordenada.fila == filaq) and (x.coordenada.columna == columnaq)):
                    """print(
                        f'filtrado  {filaq} - {columnaq} CONTADOR {contador}')
                    print(
                        f'coordenada {x.coordenada.fila} - {x.coordenada.columna}')"""
                    x.detalle = SchemaFigura(
                        selected=True, figura=AjedrezEnum.DISPONIBLE)

                if ((x.coordenada.fila == 3) and (x.coordenada.columna == 4)):

                    print(
                        f'filtrado derecha  {filak} - {columnak} CONTADOR {contador}')
                    print(
                        f'coordenada {x.coordenada.fila} - {x.coordenada.columna}')
                    x.detalle = SchemaFigura(
                        selected=True, figura=AjedrezEnum.DISPONIBLE)

                if ((x.coordenada.fila == 2) and (x.coordenada.columna == 5)):

                    print(
                        f'filtrado derecha  {filak} - {columnak} CONTADOR {contador}')
                    print(
                        f'coordenada {x.coordenada.fila} - {x.coordenada.columna}')
                    x.detalle = SchemaFigura(
                        selected=True, figura=AjedrezEnum.DISPONIBLE)

                """if ((x.coordenada.fila == 3) and (x.coordenada.columna == 2)):  # MINI BUG
                    filauno = fila-contador
                    columnauno = columna-contador

                    print(
                        f'filtrado abajo izquierda V1  {filauno} - {columnauno} CONTADOR {contador}')
                    print(
                        f'coordenada encontrada  V1 {x.coordenada.fila} - {x.coordenada.columna}')
                    x.detalle = SchemaFigura(
                        selected=True, figura=AjedrezEnum.DISPONIBLE)

                if ((x.coordenada.fila == 2) and (x.coordenada.columna == 1)):  # MINI BUG
                    filados = fila-contador
                    columnados = columna-contador
                    print(
                        f'filtrado abajo izquierda V2  {filados} - {columnados} CONTADOR {contador}')
                    print(
                        f'coordenada encontrada V2  {x.coordenada.fila} - {x.coordenada.columna}')
                    x.detalle = SchemaFigura(
                        selected=True, figura=AjedrezEnum.DISPONIBLE)"""

            contador += 1
        print("mi filtro")
        print(contador)
        return lista

     # 4,3 ==> 5,2 Izquierda Arriba
        # f +1; c-1

        # 4,3 ==> 5,4 Derecha Arriba
        # f +1; c+1

        # 4,3 ==> 3,2 Izquierda Abajo
        # f -1; c-1 +++

        # 4,3 ==> 3,4 Derecha Abajo
        # f -1; c+1 ++

    @classmethod
    def ObtenerCoordenadaReina(cls, lista: List[ShemaTres]) -> Optional[ParamProblemTresResponse]:
        for x in lista:
            if x.detalle.figura == AjedrezEnum.REINA:
                return x
        return None

    @classmethod
    def GetReina(cls, entity: ShemaTres, fila: int, columna: int) -> bool:
        filtrounox = Point(fila, columna)
        datax = entity.coordenada == filtrounox
        return datax

    @classmethod
    def NumeroPar(cls, numero: int, index: int) -> int:
        b = 0
        if index % 2 == 0:
            if numero % 2 == 0:
                b = 1
        else:
            if numero % 2 != 0:
                b = 1
        return b

    @classmethod
    def LoadInfo(cls, indice: int, valor: int, value_extra: int) -> ShemaTres:
        numero: int = cls.NumeroPar(indice, valor)
        micolor: str = numero == 0 and "#6d4c41" or "#efebe9"
        detallex = SchemaFigura(selected=False, figura=AjedrezEnum.NINGUNO)
        # inicial = indice+ 1
        second = valor + 1
        info = ShemaTres(color=micolor, coordenada=Point(
            value_extra, second), indice=value_extra, detalle=detallex)
        return info

    @classmethod
    def NroFecha(cls, nro: int) -> int:
        print(nro)
        resultado: int = ((nro-1) * 2)
        return resultado

    @classmethod
    async def GeneratePadel(cls, entity: List[SchemaCategoria]) -> ResponsePadel:
        try:
            nropartidojugado = 0
            # print(len(string))
            # Lista de Equipos
            equipos: List[str] = []
            for x in entity:
                for y in x.detalle:
                    equipos.append(y.local.nombre)
                    equipos.append(y.visitante.nombre)
                    nropartidojugado += 1

            # for z in entity:

            res = []
            for i in equipos:
                if i not in res:
                    res.append(i)
            # print(equipos)
            # print(res)

            nro = len(res)
            print("equipos")
            print(res)
            print(nro)
            fechas: int = cls.NroFecha(nro)
            print("mi fecha")
            print(fechas)

            # Nro partidos x fecha
            nropartidos = nro/2
            totalpartido = fechas * nropartidos
            print(totalpartido)

            partidofaltante = totalpartido - nropartidojugado
            print(partidofaltante)

            print("equipo ganado")
            return ResponsePadel(categoria="s", equipo="ss", status=PadelEnum.EMPATE)
        except Exception as e:
            print(e)
            raise Exception(e)

    @classmethod
    async def GenerateChess(cls, entity: ParamProblemTres) -> List[List[ShemaTres]]:
        try:
            n = entity.n

            filareina = entity.rq
            columnareina = entity.cq

            b = [[0] * n for i in range(n)]
            contador = 0
            contadorx = 0

            mimenu_extra: List[List[ShemaTres]] = []

            for i in range(n):
                union = n-contadorx
                print(f'La fila {union}')
                mimenu: List[ShemaTres] = []
                for j in range(n):
                    # print(f'El resultado de {i} - {j}')
                    value_extra = n-contador
                    demoxxxx = cls.LoadInfo(i, j, union)
                    if ((demoxxxx.coordenada.columna == columnareina) and (demoxxxx.coordenada.fila == filareina)):
                        demoxxxx.detalle = SchemaFigura(
                            selected=True, figura=AjedrezEnum.REINA)

                    mimenu.append(demoxxxx)
                    b[i][j] = j+1
                contador += 1
                mimenu_extra.append(mimenu)
                contadorx += 1

            # print(mimenu_extra)
            # print(b)
            # print(type(b))
            # print(f'Get Reina de {filareina} - {columnareina}')
            # filtrado =list(filter(cls.GetReina(filareina,columnareina),mimenu))
            filtrounox = Point(filareina, columnareina)
            # return entity.coordenada==filtrounox
            # https://www.programiz.com/python-programming/methods/list/index

            # https://www.digitalocean.com/community/tutorials/how-to-use-the-python-filter-function-es
            # filtradovv = list(
            #    filter(lambda x: x.coordenada == filtrounox, mimenu))
            # print(filtradovv)
            print("**********************")
            # index = mimenu.index(filtradovv[0])
            # print("mi indez")
            # print(index)
            # print(mimenu[0])
            """filtradovv[0].detalle = SchemaFigura(
                selected=True, figura=AjedrezEnum.REINA)
            mimenu[index] = filtradovv[0]"""

            # FiltradoArrayCustom = list( map(cls.FiltradoArray, [[filareina], [columnareina]], mimenu_extra))

            # over_75 = list(filter(FiltradoArray, mimenu_extra))

            """map(add,
            [[3,2,4]],
            [2])"""
            add3 = functools.partial(
                cls.FiltradoArrayDos, fila=filareina, columna=columnareina)
            # print(add3)

            # resultxxx = map(add3, mimenu_extra)
            result_list = cls.FiltradoDinamico(
                mimenu_extra, filareina, columnareina, n)  # list(resultxxx)
            # print(result_list)
            print(len(result_list))
            # print(FiltradoArrayCustom)
            return result_list
        except Exception as e:
            print(e)
            raise Exception(e)

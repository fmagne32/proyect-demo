from datetime import datetime
import json
import functools
from typing import List, Optional
from ..api.schema import RespuestaApi as SchemaResponse, PadelEnum, DetalleEquipo, ResponsePadel, ParamProblemTres, ParamProblemTresResponse, ParamProblemTresResponse as ShemaTres, FiguraResponse as SchemaFigura, AjedrezEnum, Point, DetailChees, Categoria as SchemaCategoria
from pydantic.schema import schema
from pydantic import parse_obj_as


class RepoLaboratory:

    # FiltroDisponible
    @classmethod
    def FiltroDisponible(cls, lista: List[List[ShemaTres]], fila: int, columna: int, size: int):
        maxnum = size+1
        contador = (size-fila)+1
        n = (size - contador)+1
        diccionariox = []

        # Arriba Derecha
        # f+1
        # c+1

        contador_m = 0
        contador_n = 0
        contador_p = 0
        contador_o = 0

        contador_q = 0
        contador_r = 0
        contador_s = 0
        contador_t = 0

        for x in range(n):
            contador_m += 1
            fila_m = fila+contador_m
            columna_m = columna+contador_m
            if ((fila_m > 0) and (columna_m > 0) and (fila_m < maxnum) and (columna_m < maxnum)):
                info_uno = dict(fila=fila_m, columna=columna_m)
                diccionariox.append(info_uno)

        # Arriba Izquierda
        # f+1
        # c-1

        for x in range(n):
            contador_p += 1
            fila_p = fila+contador_p
            columna_p = columna-contador_p
            if ((fila_p > 0) and (columna_p > 0) and (fila_p < maxnum) and (columna_p < maxnum)):
                info_dos = dict(fila=fila_p, columna=columna_p)
                diccionariox.append(info_dos)
        # Abajo Izquierda
        # f-1
        # c-1

        for x in range(n):
            contador_n += 1
            fila_n = fila-contador_n
            columna_n = columna-contador_n

            if ((fila_n > 0) and (columna_n > 0) and (fila_n < maxnum) and (columna_n < maxnum)):
                info_tres = dict(fila=fila_n, columna=columna_n)
                diccionariox.append(info_tres)
        # Abajo Derecha
        # f-1
        # c+1
        for x in range(n):
            contador_o += 1
            fila_o = fila-contador_o
            columna_o = columna+contador_o
            if ((fila_o > 0) and (columna_o > 0) and (fila_o < maxnum) and (columna_o < maxnum)):
                info_cuatro = dict(fila=fila_o, columna=columna_o)
                diccionariox.append(info_cuatro)

        # Arriba Only

        for x in range(n):
            contador_q += 1
            fila_q = fila + contador_q
            if ((fila_q > 0) and (fila_q < maxnum)):
                info_cinco = dict(fila=fila_q, columna=columna)
                diccionariox.append(info_cinco)
        # Abajo Only
        for x in range(n):
            contador_r += 1
            fila_r = fila - contador_r
            if ((fila_r > 0) and (fila_r < maxnum)):
                info_seis = dict(fila=fila_r, columna=columna)
                diccionariox.append(info_seis)

        # Izquierda Only
        for x in range(n):
            contador_s += 1
            columna_s = columna - contador_s
            if ((columna_s > 0) and (columna_s < maxnum)):
                info_siete = dict(fila=fila, columna=columna_s)
                diccionariox.append(info_siete)

        # Derecha Only

        for x in range(n):
            contador_t += 1
            columna_t = columna + contador_t
            if ((columna_t > 0) and (columna_t < maxnum)):
                info_ocho = dict(fila=fila, columna=columna_t)
                diccionariox.append(info_ocho)

        return diccionariox

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
    def FiltradoDinamico(cls, lista: List[List[ShemaTres]], casilla: List[dict], obstaculo: List[dict]):
        listaunixo = []

        for y in lista:
            for x in y:
                if ((x.detalle.figura != AjedrezEnum.REINA)):
                    # print('hola')
                    status: bool = cls.GetCasillaDisponible(
                        casilla, x.coordenada.fila, x.coordenada.columna)
                    if status:
                        x.detalle = SchemaFigura(
                            selected=True, imageurl='https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Circle-green.svg/1024px-Circle-green.svg.png', figura=AjedrezEnum.DISPONIBLE)
            listaunixo.append(y)
        print("====================================")
        #mijson = json.dumps(filtrox, ensure_ascii=False)
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
    def GetCasillaDisponible(cls, lista: List[dict], fila: int, columna: int) -> bool:
        data: bool = False

        for entity in lista:
            if ((entity['fila'] == fila) and (entity['columna'] == columna)):
                data = True
        # datax:int = ((entity['fila'] == fila) and (entity['columna'] == columna))
        # print("Resultado Busqueda")
        # print(datax)
        return data

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

            # for item in res:
            clave: str = "Buenisimos"

            for item in entity[0].detalle:
                if item.local.nombre == clave:
                    print(item)
                    puntos = 0
                    if item.local.sets > item.visitante.sets:
                        puntos += 2
                    if item.local.sets < item.visitante.sets:
                        puntos += 1
                if item.visitante.nombre == clave:
                    if item.visitante.sets > item.local.sets:
                        puntos += 2
                    if item.visitante.sets > item.local.sets:
                        puntos += 1

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
                            selected=True, imageurl='https://pic.onlinewebfonts.com/svg/img_546821.png', figura=AjedrezEnum.REINA)

                    mimenu.append(demoxxxx)
                    b[i][j] = j+1
                contador += 1
                mimenu_extra.append(mimenu)
                contadorx += 1

            # filtrado =list(filter(cls.GetReina(filareina,columnareina),mimenu))
            filtrounox = Point(filareina, columnareina)
            # return entity.coordenada==filtrounox
            # https://www.programiz.com/python-programming/methods/list/index

            # https://www.digitalocean.com/community/tutorials/how-to-use-the-python-filter-function-es
            # filtradovv = list(
            #    filter(lambda x: x.coordenada == filtrounox, mimenu))
            # print(filtradovv)
            print("**********************")

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

            filtrado_casilla = cls.FiltroDisponible(
                mimenu_extra, filareina, columnareina, n)

            obstaculo = []
            result_list = cls.FiltradoDinamico(
                mimenu_extra, filtrado_casilla, obstaculo)
            print("======================")

            return result_list
        except Exception as e:
            print(e)
            raise Exception(e)

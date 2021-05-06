from datetime import datetime
import json
import functools
from typing import List, Optional
from ..api.schema import RespuestaApi as SchemaResponse, Team, ObstaculoModel, PadelEnum, DetailTeam, ResponsePadel, ParamProblemTres, ParamProblemTresResponse, ParamProblemTresResponse as ShemaTres, FiguraResponse as SchemaFigura, AjedrezEnum, Point, DetailChees, Category as SchemaCategory
from pydantic.schema import schema
from pydantic import parse_obj_as


class RepoLaboratory:

    # FiltroDisponible
    @classmethod
    def FiltroDisponible(cls, lista: List[List[ShemaTres]], obstaculo: Optional[List[ObstaculoModel]], fila: int, columna: int, size: int):
        maxnum = size+1
        contador = (size-fila)+1
        n = (size - contador)+1
        diccionariox = []

        # Arriba Derecha
        # f+1
        # c+1
        sin_obstaculo = True
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

            is_obstacle = cls.GetCasillaObstaculo(
                obstaculo, fila_m, columna_m)

            if is_obstacle:
                sin_obstaculo = False

            if sin_obstaculo:
                if ((fila_m > 0) and (columna_m > 0) and (fila_m < maxnum) and (columna_m < maxnum)):
                    info_uno = dict(fila=fila_m, columna=columna_m)
                    diccionariox.append(info_uno)

        sin_obstaculo = True
        # Arriba Izquierda
        # f+1
        # c-1

        for x in range(n):
            contador_p += 1
            fila_p = fila+contador_p
            columna_p = columna-contador_p

            is_obstacle = cls.GetCasillaObstaculo(
                obstaculo, fila_p, columna_p)

            if is_obstacle:
                sin_obstaculo = False
            if sin_obstaculo:
                if ((fila_p > 0) and (columna_p > 0) and (fila_p < maxnum) and (columna_p < maxnum)):
                    info_dos = dict(fila=fila_p, columna=columna_p)
                    diccionariox.append(info_dos)

        sin_obstaculo = True
        # Abajo Izquierda
        # f-1
        # c-1
        infoleft = []
        for x in range(n):
            contador_n += 1
            fila_n = fila-contador_n
            columna_n = columna-contador_n

            is_obstacle = cls.GetCasillaObstaculo(
                obstaculo, fila_n, columna_n)

            if is_obstacle:
                sin_obstaculo = False

            if sin_obstaculo:
                if ((fila_n > 0) and (columna_n > 0) and (fila_n < maxnum) and (columna_n < maxnum)):
                    info_tres = dict(fila=fila_n, columna=columna_n)
                    diccionariox.append(info_tres)
                    infoleft.append(info_tres)
        print(infoleft)

        sin_obstaculo = True
        # Abajo Derecha
        # f-1
        # c+1
        for x in range(n):
            contador_o += 1
            fila_o = fila-contador_o
            columna_o = columna+contador_o

            is_obstacle = cls.GetCasillaObstaculo(
                obstaculo, fila_o, columna_o)

            if is_obstacle:
                sin_obstaculo = False

            if sin_obstaculo:
                if ((fila_o > 0) and (columna_o > 0) and (fila_o < maxnum) and (columna_o < maxnum)):
                    info_cuatro = dict(fila=fila_o, columna=columna_o)
                    diccionariox.append(info_cuatro)

        sin_obstaculo = True
        # Arriba Only

        for x in range(n):
            contador_q += 1
            fila_q = fila + contador_q

            is_obstacle = cls.GetCasillaObstaculo(
                obstaculo, fila_q, columna)

            if is_obstacle:
                sin_obstaculo = False

            if sin_obstaculo:
                if ((fila_q > 0) and (fila_q < maxnum)):
                    info_cinco = dict(fila=fila_q, columna=columna)
                    diccionariox.append(info_cinco)

        sin_obstaculo = True
        # Abajo Only
        for x in range(n):
            contador_r += 1
            fila_r = fila - contador_r

            is_obstacle = cls.GetCasillaObstaculo(
                obstaculo, fila_r, columna)

            if is_obstacle:
                sin_obstaculo = False

            if sin_obstaculo:
                if ((fila_r > 0) and (fila_r < maxnum)):
                    info_seis = dict(fila=fila_r, columna=columna)
                    diccionariox.append(info_seis)

        sin_obstaculo = True
        # Izquierda Only
        for x in range(n):
            contador_s += 1
            columna_s = columna - contador_s

            is_obstacle = cls.GetCasillaObstaculo(
                obstaculo, fila, columna_s)
            if is_obstacle:
                sin_obstaculo = False

            if sin_obstaculo:
                if ((columna_s > 0) and (columna_s < maxnum)):
                    info_siete = dict(fila=fila, columna=columna_s)
                    diccionariox.append(info_siete)

        # Derecha Only
        sin_obstaculo = True
        for x in range(n):
            contador_t += 1
            columna_t = columna + contador_t

            is_obstacle = cls.GetCasillaObstaculo(
                obstaculo, fila, columna_t)

            if is_obstacle:
                sin_obstaculo = False

            if sin_obstaculo:
                if ((columna_t > 0) and (columna_t < maxnum)):
                    info_ocho = dict(fila=fila, columna=columna_t)
                    diccionariox.append(info_ocho)

        return diccionariox

    # Load Ataque

    @classmethod
    def FiltradoDinamico(cls, lista: List[List[ShemaTres]], casilla: List[dict]):
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
    def GetCasillaDisponible(cls, lista: List[dict], fila: int, columna: int) -> bool:
        for entity in lista:
            if ((entity['fila'] == fila) and (entity['columna'] == columna)):
                return True
        return False

    @classmethod
    def GetCasillaObstaculo(cls, lista: Optional[List[ObstaculoModel]], fila: int, columna: int) -> bool:
        data = False
        if lista is not None:
            for entity in lista:
                if ((entity.fila == fila) and (entity.columna == columna)):
                    data = True
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
    def LoadInfo(cls, obstaculo: Optional[List[ObstaculoModel]], indice: int, valor: int, value_extra: int) -> ShemaTres:
        numero: int = cls.NumeroPar(indice, valor)
        micolor: str = numero == 0 and "#6d4c41" or "#efebe9"

        detallex = SchemaFigura(selected=False, figura=AjedrezEnum.NINGUNO)
        # inicial = indice+ 1
        second = valor + 1

        is_obstacle = cls.GetCasillaObstaculo(
            obstaculo, value_extra, second)
        if is_obstacle:
            print(f'indice {value_extra}- {second}')
            info_close = ShemaTres(color=micolor, coordenada=Point(value_extra, second), indice=value_extra, detalle=SchemaFigura(
                selected=True, imageurl='https://img.pngio.com/cancel-close-delete-dismiss-exit-recycle-remove-icon-close-png-512_512.png', figura=AjedrezEnum.OBSTACULO))
            return info_close
        info = ShemaTres(color=micolor, coordenada=Point(
            value_extra, second), indice=value_extra, detalle=detallex)
        return info

    @classmethod
    def NroMatch(cls, nro: int) -> int:
        resultado: int = ((nro-1) * 2)
        return resultado

    @classmethod
    def pointsxmatch(cls, match: List[Team], name: str) -> dict:
        points = 0
        winner = 0
        lostmatch = 0
        datelocal = 0
        datevistant = 0
        for item in match:
            if item.local.name == name:
                datelocal += 1
                if item.local.sets > item.visitant.sets:
                    points += 2
                    winner += 1
                if item.local.sets < item.visitant.sets:
                    points += 1
                    lostmatch += 1
            if item.visitant.name == name:
                datevistant += 1
                if item.visitant.sets > item.local.sets:
                    points += 2
                    winner += 1
                if item.visitant.sets < item.local.sets:
                    points += 1
                    lostmatch += 1
        totaldate = datelocal+datevistant
        info = dict(team=name, matchdate=totaldate, points=points,
                    winner=winner, lost=lostmatch)
        return info

    @classmethod
    def checkIfDuplicates(cls, listOfElems):
        if len(listOfElems) == len(set(listOfElems)):
            return False
        else:
            return True

    @classmethod
    def TeamUnique(cls, teams: List[Team]) -> dict:
        teamonlywinner = ""
        countmatch = 0
        tie = False
        list_team = []
        for item in teams:
            list_team.append(item.local.name)
            list_team.append(item.visitant.name)
            countmatch += 1

        res = []
        for i in list_team:
            if i not in res:
                res.append(i)
        nro = len(res)
        dates: int = cls.NroMatch(nro)
        # Nro partidos x fecha
        nromatchx = nro/2
        totalmatch = dates * nromatchx
        print(totalmatch)

        missingmatch = totalmatch - countmatch

        filterx = []
        for i in res:
            detail = cls.pointsxmatch(teams, i)
            filterx.append(detail)

        getwinner = [d for d in filterx if d['lost'] == 0]

        if len(getwinner) > 0:
            teamonlywinner = getwinner[0]['team']

        array_ponts = []
        for x in getwinner:
            array_ponts.append(x['points'])
        print("mi puntos")
        print(array_ponts)
        tie = cls.checkIfDuplicates(array_ponts)
        print("stadistic")
        print(filterx)
        response = dict(team=teamonlywinner,
                        missing=missingmatch, tie=tie, data=filterx)
        return response

    @classmethod
    async def GeneratePadel(cls, entity: List[SchemaCategory]) -> List[ResponsePadel]:
        try:
            response: List[ResponsePadel] = []
            for x in entity:
                list_team = []
                entity: dict = cls.TeamUnique(x.teams)
                item = ResponsePadel(
                    category=x.name, team=entity['team'], tie=entity['tie'], stadistic=entity['data'])
                response.append(item)
            return response
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
                #print(f'La fila {union}')
                mimenu: List[ShemaTres] = []
                for j in range(n):
                    value_extra = n-contador
                    demoxxxx = cls.LoadInfo(entity.obstaculo, i, j, union)

                    if ((demoxxxx.coordenada.columna == columnareina) and (demoxxxx.coordenada.fila == filareina)):
                        demoxxxx.detalle = SchemaFigura(
                            selected=True, imageurl='https://pic.onlinewebfonts.com/svg/img_546821.png', figura=AjedrezEnum.REINA)

                    mimenu.append(demoxxxx)
                    b[i][j] = j+1
                contador += 1
                mimenu_extra.append(mimenu)
                contadorx += 1

            print("**********************")
            filtrado_casilla = cls.FiltroDisponible(
                mimenu_extra, entity.obstaculo, filareina, columnareina, n)

            obstaculo = []
            result_list = cls.FiltradoDinamico(
                mimenu_extra, filtrado_casilla)
            print("======================")
            print(len(filtrado_casilla))
            return result_list
        except Exception as e:
            print(e)
            raise Exception(e)

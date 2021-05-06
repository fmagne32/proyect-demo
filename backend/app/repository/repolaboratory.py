from datetime import datetime
import json
import functools
from typing import List, Optional
from ..api.schema import RespuestaApi as SchemaResponse, Team, ObstacleModel, PadelEnum, DetailTeam, ResponsePadel, ParamProblemTwo, ParamProblemTwo, ParamProblemTwoResponse, FigureResponse, AjedrezEnum, Point, DetailChees, Category as SchemaCategory
from pydantic.schema import schema
from pydantic import parse_obj_as


class RepoLaboratory:

    # FiltroDisponible
    @classmethod
    def FiltroDisponible(cls, lista: List[List[ParamProblemTwoResponse]], obstaculo: Optional[List[ObstacleModel]], row: int, column: int, size: int):
        maxnum = size+1
        contador = (size-row)+1
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
            row_m = row+contador_m
            column_m = column+contador_m

            is_obstacle = cls.GetObstacleBox(
                obstaculo, row_m, column_m)

            if is_obstacle:
                sin_obstaculo = False

            if sin_obstaculo:
                if ((row_m > 0) and (column_m > 0) and (row_m < maxnum) and (column_m < maxnum)):
                    info_uno = dict(row=row_m, column=column_m)
                    diccionariox.append(info_uno)

        sin_obstaculo = True
        # Arriba Izquierda
        # f+1
        # c-1

        for x in range(n):
            contador_p += 1
            row_p = row+contador_p
            column_p = column-contador_p

            is_obstacle = cls.GetObstacleBox(
                obstaculo, row_p, column_p)

            if is_obstacle:
                sin_obstaculo = False
            if sin_obstaculo:
                if ((row_p > 0) and (column_p > 0) and (row_p < maxnum) and (column_p < maxnum)):
                    info_dos = dict(row=row_p, column=column_p)
                    diccionariox.append(info_dos)

        sin_obstaculo = True
        # Abajo Izquierda
        # f-1
        # c-1
        infoleft = []
        for x in range(n):
            contador_n += 1
            row_n = row-contador_n
            column_n = column-contador_n

            is_obstacle = cls.GetObstacleBox(
                obstaculo, row_n, column_n)

            if is_obstacle:
                sin_obstaculo = False

            if sin_obstaculo:
                if ((row_n > 0) and (column_n > 0) and (row_n < maxnum) and (column_n < maxnum)):
                    info_tres = dict(row=row_n, column=column_n)
                    diccionariox.append(info_tres)
                    infoleft.append(info_tres)
        print(infoleft)

        sin_obstaculo = True
        # Abajo Derecha
        # f-1
        # c+1
        for x in range(n):
            contador_o += 1
            row_o = row-contador_o
            column_o = column+contador_o

            is_obstacle = cls.GetObstacleBox(
                obstaculo, row_o, column_o)

            if is_obstacle:
                sin_obstaculo = False

            if sin_obstaculo:
                if ((row_o > 0) and (column_o > 0) and (row_o < maxnum) and (column_o < maxnum)):
                    info_cuatro = dict(row=row_o, column=column_o)
                    diccionariox.append(info_cuatro)

        sin_obstaculo = True
        # Arriba Only

        for x in range(n):
            contador_q += 1
            row_q = row + contador_q

            is_obstacle = cls.GetObstacleBox(
                obstaculo, row_q, column)

            if is_obstacle:
                sin_obstaculo = False

            if sin_obstaculo:
                if ((row_q > 0) and (row_q < maxnum)):
                    info_cinco = dict(row=row_q, column=column)
                    diccionariox.append(info_cinco)

        sin_obstaculo = True
        # Abajo Only
        for x in range(n):
            contador_r += 1
            row_r = row - contador_r

            is_obstacle = cls.GetObstacleBox(
                obstaculo, row_r, column)

            if is_obstacle:
                sin_obstaculo = False

            if sin_obstaculo:
                if ((row_r > 0) and (row_r < maxnum)):
                    info_seis = dict(row=row_r, column=column)
                    diccionariox.append(info_seis)

        sin_obstaculo = True
        # Izquierda Only
        for x in range(n):
            contador_s += 1
            column_s = column - contador_s

            is_obstacle = cls.GetObstacleBox(
                obstaculo, row, column_s)
            if is_obstacle:
                sin_obstaculo = False

            if sin_obstaculo:
                if ((column_s > 0) and (column_s < maxnum)):
                    info_siete = dict(row=row, column=column_s)
                    diccionariox.append(info_siete)

        # Derecha Only
        sin_obstaculo = True
        for x in range(n):
            contador_t += 1
            column_t = column + contador_t

            is_obstacle = cls.GetObstacleBox(
                obstaculo, row, column_t)

            if is_obstacle:
                sin_obstaculo = False

            if sin_obstaculo:
                if ((column_t > 0) and (column_t < maxnum)):
                    info_ocho = dict(row=row, column=column_t)
                    diccionariox.append(info_ocho)

        return diccionariox

    # Load Ataque

    @classmethod
    def listattackbox(cls, response: List[List[ParamProblemTwoResponse]], box: List[dict]):
        listfilter = []
        for y in response:
            for x in y:
                if ((x.detail.figure != AjedrezEnum.REINA)):
                    status: bool = cls.GetAvailableBox(
                        box, x.coordinate.row, x.coordinate.column)
                    if status:
                        x.detail = FigureResponse(
                            selected=True, imageurl='https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Circle-green.svg/1024px-Circle-green.svg.png', figure=AjedrezEnum.DISPONIBLE)
            listfilter.append(y)
        return listfilter

    @classmethod
    def GetAvailableBox(cls, response: List[dict], row: int, column: int) -> bool:
        for entity in response:
            if ((entity['row'] == row) and (entity['column'] == column)):
                return True
        return False

    @classmethod
    def GetObstacleBox(cls, listobstacle: Optional[List[ObstacleModel]], row: int, column: int) -> bool:
        data = False
        if listobstacle is not None:
            for entity in listobstacle:
                
                if ((entity.row == row) and (entity.column == column)):
                    data = True
        
        return data

    @classmethod
    def evennumber(cls, number: int, index: int) -> int:
        if index % 2 == 0:
            if number % 2 == 0:
                return 1
        else:
            if number % 2 != 0:
                return 1
        return 0

    @classmethod
    def LoadInfo(cls, obstaculo: Optional[List[ObstacleModel]], index: int, paramx: int, value_extra: int) -> ParamProblemTwoResponse:
        numberx: int = cls.evennumber(index, paramx)
        color: str = numberx == 0 and "#6d4c41" or "#efebe9"
        second = paramx + 1
        
        is_obstacle = cls.GetObstacleBox(
            obstaculo, value_extra, second)

        #
        
        if is_obstacle:
            info_close = ParamProblemTwoResponse(color=color, coordinate=Point(value_extra, second), index=value_extra, detail=FigureResponse(
                selected=True, imageurl='https://img.pngio.com/cancel-close-delete-dismiss-exit-recycle-remove-icon-close-png-512_512.png', figure=AjedrezEnum.OBSTACULO))
            return info_close

        info = ParamProblemTwoResponse(color=color, coordinate=Point(
            value_extra, second), index=value_extra, detail=FigureResponse(selected=False, figure=AjedrezEnum.NINGUNO))

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
    def checkIfDuplicates(cls, listOfElems: List[int]) -> bool:
        count = 0
        maximo = max(listOfElems)
        for x in listOfElems:
            if x == maximo:
                count += 1
        return count >= 2 and True or False

    @classmethod
    def LoadTeam(cls, teams: List[Team]) -> dict:
        teamonlywinner = ""
        countmatch = 0
        list_team = []
        for item in teams:

            if len(item.local.name) >= 16:
                print('f')

            if len(item.visitant.name) >= 16:
                print('f')

            list_team.append(item.local.name)
            list_team.append(item.visitant.name)
            countmatch += 1

        res = []
        for i in list_team:
            if i not in res:
                res.append(i)
        nro = len(res)

        dates: int = cls.NroMatch(nro)
        nromatchx = nro/2
        totalmatch = dates * nromatchx

        missingmatch = totalmatch - countmatch
        filterx = []
        for i in res:
            detail = cls.pointsxmatch(teams, i)
            filterx.append(detail)

        getwinner = [d for d in filterx if d['lost'] == 0]
        if len(getwinner) > 0:
            teamonlywinner = getwinner[0]['team']

        array_ponts = []
        for x in filterx:
            array_ponts.append(x['points'])
        tie = cls.checkIfDuplicates(array_ponts)

        return {'team': teamonlywinner, 'missing': missingmatch, 'tie': tie, 'data': filterx}

    @classmethod
    async def GeneratePadel(cls, entity: List[SchemaCategory]) -> List[ResponsePadel]:
        try:
            response: List[ResponsePadel] = []

            """if getcategoria is None:
                print("inicio")
                raise UnicornException(
                    name='No Existe La categoria con id {}'.format(categoria['id']))"""
            for x in entity:
                entity: dict = cls.LoadTeam(x.teams)
                item = ResponsePadel(
                    category=x.name, team=entity['team'], tie=entity['tie'], stadistic=entity['data'])
                response.append(item)
            return response
        except Exception as e:
            print(e)
            raise Exception(e)

    @classmethod
    async def GenerateChess(cls, entity: ParamProblemTwo) -> List[List[ParamProblemTwoResponse]]:
        try:
            n = entity.n
            rowqueen = entity.rq
            columnqueen = entity.cq
            count = 0
            countx = 0
            array_aux: List[List[ParamProblemTwoResponse]] = []
            for i in range(n):
                extra = n-countx
                elementsub: List[ParamProblemTwoResponse] = []
                for j in range(n):
                    value_extra = n-count
                    item = cls.LoadInfo(entity.obstacle, i, j, extra)

                    if ((item.coordinate.column == columnqueen) and (item.coordinate.row == rowqueen)):
                        item.detail = FigureResponse(
                            selected=True, imageurl='https://pic.onlinewebfonts.com/svg/img_546821.png', figure=AjedrezEnum.REINA)

                    elementsub.append(item)
                count += 1
                array_aux.append(elementsub)
                countx += 1

            #print(array_aux)
            filter_box = cls.FiltroDisponible(
                array_aux, entity.obstacle, rowqueen, columnqueen, n)

            result_list = cls.listattackbox(
                array_aux, filter_box)

            print(len(filter_box))
            return result_list
        except Exception as e:
            print(e)
            raise Exception(e)

    @classmethod
    # temporal
    async def GenerateResultTree(cls, world: str) -> int:
        n = len(world)

        # for por n
        resultc = int(n * (n + 1) / 2)
        return resultc

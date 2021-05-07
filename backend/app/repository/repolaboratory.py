from datetime import datetime
import json
import functools
from typing import List, Optional
from ..api.schema import RespuestaApi as SchemaResponse, PositionEnum, Team, ObstacleModel, DetailTeam, ResponsePadel, ParamProblemTwo, ParamProblemTwo, ParamProblemTwoResponse, FigureResponse, AjedrezEnum, Point, DetailChees, Category as SchemaCategory
from pydantic.schema import schema
from pydantic import parse_obj_as


class RepoLaboratory:

    @classmethod
    def FilterAvailableAttack(cls, index: int, option: PositionEnum, obstacle: Optional[List[ObstacleModel]], rowqueen: int, columnqueen: int, maxnum: int) -> Optional[dict]:

        if option == PositionEnum.TOP:
            row_x = rowqueen + index
            is_obstacle = cls.GetObstacleBox(
                obstacle, row_x, columnqueen)
            if not is_obstacle:
                if ((row_x > 0) and (row_x < maxnum)):
                    return {'row': row_x, 'column': columnqueen}
                else:
                    return None

        elif option == PositionEnum.LEFT:
            column_x = columnqueen - index
            is_obstacle = cls.GetObstacleBox(
                obstacle, rowqueen, column_x)
            if not is_obstacle:
                if ((column_x > 0) and (column_x < maxnum)):
                    return {'row': rowqueen, 'column': column_x}
                else:
                    return None

        elif option == PositionEnum.RIGHT:

            column_x = columnqueen + index
            is_obstacle = cls.GetObstacleBox(
                obstacle, rowqueen, column_x)
            if not is_obstacle:
                if ((column_x > 0) and (column_x < maxnum)):
                    return {'row': rowqueen, 'column': column_x}
                else:
                    return None

        elif option == PositionEnum.DOWN:

            row_x = rowqueen - index
            is_obstacle = cls.GetObstacleBox(
                obstacle, row_x, columnqueen)
            if not is_obstacle:
                if ((row_x > 0) and (row_x < maxnum)):
                    return {'row': row_x, 'column': columnqueen}
                else:
                    return None
        elif option == PositionEnum.TOPLEFT:
            row_x = rowqueen + index
            column_x = columnqueen - index

            is_obstacle = cls.GetObstacleBox(
                obstacle, row_x, column_x)
            if not is_obstacle:
                if ((row_x > 0) and (column_x > 0) and (row_x < maxnum) and (column_x < maxnum)):
                    return {'row': row_x, 'column': column_x}
                else:
                    return None

        elif option == PositionEnum.TOPRIGHT:
            row_x = rowqueen + index
            column_x = columnqueen + index

            is_obstacle = cls.GetObstacleBox(
                obstacle, row_x, column_x)
            if not is_obstacle:
                if ((row_x > 0) and (column_x > 0) and (row_x < maxnum) and (column_x < maxnum)):
                    return {'row': row_x, 'column': column_x}
                else:
                    return None

        elif option == PositionEnum.DOWNLEFT:
            row_x = rowqueen - index
            column_x = columnqueen - index

            is_obstacle = cls.GetObstacleBox(
                obstacle, row_x, column_x)
            if not is_obstacle:
                if ((row_x > 0) and (column_x > 0) and (row_x < maxnum) and (column_x < maxnum)):
                    return {'row': row_x, 'column': column_x}
                else:
                    return None
        elif option == PositionEnum.DOWNRIGHT:
            row_x = rowqueen - index
            column_x = columnqueen + index

            is_obstacle = cls.GetObstacleBox(
                obstacle, row_x, column_x)
            if not is_obstacle:
                if ((row_x > 0) and (column_x > 0) and (row_x < maxnum) and (column_x < maxnum)):
                    return {'row': row_x, 'column': column_x}
                else:
                    return None

        return None

    @classmethod
    def FilterAvailable(cls, lista: List[List[ParamProblemTwoResponse]], obstacle: Optional[List[ObstacleModel]], row: int, column: int, size: int):
        maxnum = size+1
        contador = (size-row)+1
        n = (size - contador)+1
        contador_m = 0
        diccionariox = []
        count_top = 0
        count_down = 0
        count_left = 0
        count_right = 0
        count_topleft = 0
        count_topright = 0
        count_downleft = 0
        count_downright = 0

        for x in range(n):
            contador_m += 1
            # TOP
            top = cls.FilterAvailableAttack(
                contador_m, PositionEnum.TOP, obstacle, row, column, maxnum)

            if not top:
                count_top += 1
            if count_top == 0:
                diccionariox.append(top)
            # DOWN
            down = cls.FilterAvailableAttack(
                contador_m, PositionEnum.DOWN, obstacle, row, column, maxnum)
            if not down:
                count_down += 1
            if count_down == 0:
                diccionariox.append(down)
            # LEFT
            left = cls.FilterAvailableAttack(
                contador_m, PositionEnum.LEFT, obstacle, row, column, maxnum)
            if not left:
                count_left += 1
            if count_left == 0:
                diccionariox.append(left)
            # RIGHT
            right = cls.FilterAvailableAttack(
                contador_m, PositionEnum.RIGHT, obstacle, row, column, maxnum)

            if not right:
                count_right += 1

            if count_right == 0:
                diccionariox.append(right)

            # TOPRIGHT
            topright = cls.FilterAvailableAttack(
                contador_m, PositionEnum.TOPRIGHT, obstacle, row, column, maxnum)

            if not topright:
                count_topright += 1

            if count_topright == 0:
                diccionariox.append(topright)

            # TOPLEFT
            topleft = cls.FilterAvailableAttack(
                contador_m, PositionEnum.TOPLEFT, obstacle, row, column, maxnum)

            if not topleft:
                count_topleft += 1

            if count_topleft == 0:
                diccionariox.append(topleft)

            # DOWNRIGHT
            downright = cls.FilterAvailableAttack(
                contador_m, PositionEnum.DOWNRIGHT, obstacle, row, column, maxnum)
            if not downright:
                count_downright += 1

            if count_downright == 0:
                diccionariox.append(downright)
            # DOWNLEFT
            downleft = cls.FilterAvailableAttack(
                contador_m, PositionEnum.DOWNLEFT, obstacle, row, column, maxnum)
            if not downleft:
                count_downleft += 1

            if count_downleft == 0:
                diccionariox.append(downleft)
        return diccionariox

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
    def LoadInfo(cls, obstacle: Optional[List[ObstacleModel]], index: int, paramx: int, value_extra: int) -> ParamProblemTwoResponse:
        numberx: int = cls.evennumber(index, paramx)
        color: str = numberx == 0 and "#6d4c41" or "#efebe9"
        second = paramx + 1

        is_obstacle = cls.GetObstacleBox(
            obstacle, value_extra, second)

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

            # print(array_aux)
            filter_box = cls.FilterAvailable(
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

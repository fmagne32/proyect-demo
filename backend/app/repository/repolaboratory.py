from typing import List, Optional
from ..api.schema import PositionEnum, Team, ProblemTwoResponse, ObstacleModel, DetailTeam, ResponsePadel, ParamProblemTwo, ParamProblemTwo, ParamProblemTwoResponse, FigureResponse, ChessEnum, Point, DetailChees, Category as SchemaCategory
from ..api.utility import UnicornException


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
                if ((x.detail.figure != ChessEnum.QUEEN)):
                    status: bool = cls.GetAvailableBox(
                        box, x.coordinate.row, x.coordinate.column)
                    if status:
                        x.detail = FigureResponse(
                            selected=True, imageurl='https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Circle-green.svg/1024px-Circle-green.svg.png', figure=ChessEnum.AVAILABLE)
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
        if listobstacle is not None:
            for entity in listobstacle:
                if ((entity.row == row) and (entity.column == column)):
                    return True
        return False

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
        data = ParamProblemTwoResponse(color=color, coordinate=Point(
            value_extra, second), index=value_extra, detail=FigureResponse(selected=False, figure=ChessEnum.NONEDATA))
        is_obstacle = cls.GetObstacleBox(
            obstacle, value_extra, second)
        if is_obstacle:
            data.detail.figure = ChessEnum.OBSTACLE
            data.detail.selected = True
            data.detail.imageurl = "https://img.pngio.com/cancel-close-delete-dismiss-exit-recycle-remove-icon-close-png-512_512.png"
        return data

    @classmethod
    def NroMatch(cls, nro: int) -> int:
        data: int = ((nro-1) * 2)
        return data

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
        return {'team': name, 'matchdate': totaldate, 'points': points, 'winner': winner, 'lost': lostmatch}

    @classmethod
    def checkIfDuplicates(cls, listOfElems: List[int]) -> bool:
        count = 0
        maximo = max(listOfElems)
        for x in listOfElems:
            if x == maximo:
                count += 1
        return count >= 2 and True or False

    @classmethod
    def ValidatePadel(cls, item: Team):
        if len(item.local.name.strip()) >= 16:
            raise UnicornException(
                name=f'The team local name {item.local.name} must not be longer than 16 characters.')
        if len(item.visitant.name.strip()) >= 16:
            raise UnicornException(
                name=f'The team visitant name {item.visitant.name} must not be longer than 16 characters.')
        if item.local.sets < 0:
            raise UnicornException(
                name=f'Local set must be greater than zero.')
        if item.visitant.sets < 0:
            raise UnicornException(
                name=f'Visitant set must be greater than zero.')
        if item.local.sets == item.visitant.sets:
            raise UnicornException(name=f'A tie is not allowed in the padel.')

    @classmethod
    def LoadTeam(cls, teams: List[Team]) -> dict:
        teamonlywinner = ""
        countmatch = 0
        list_team = []
        for item in teams:
            cls.ValidatePadel(item)
            list_team.append(item.local.name.strip())
            list_team.append(item.visitant.name.strip())
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
            if len(entity) == 0:
                raise UnicornException(
                    name='required team.')
            for x in entity:
                if len(x.name.strip()) >= 16:
                    raise UnicornException(
                        name='the category name must not be longer than 16 characters.')
                entity: dict = cls.LoadTeam(x.teams)
                item = ResponsePadel(
                    category=x.name, team=entity['team'], tie=entity['tie'], stadistic=entity['data'], message="END")
                response.append(item)
            return response
        except UnicornException as e:
            raise UnicornException(name=e.__dict__['name'])
        except Exception as e:
            raise Exception(e)

    @classmethod
    def validateChess(cls, request: ParamProblemTwo):
        if request.n <= 0:
            raise UnicornException(
                name=f'the N value is required')

        if request.rq <= 0:
            raise UnicornException(name=f'the RQ value is required')

        if request.cq <= 0:
            raise UnicornException(name=f'the CQ value is required')

        if request.obstacle is not None:

            if request.k <= 0:
                raise UnicornException(name=f'the K value is required')

            if request.k != len(request.obstacle):
                raise UnicornException(
                    name=f'the obstacle length must be equal to k {request.k}')
                for x in request.obstacle:
                    if ((x.row == request.rq) and (x.column == request.cq)):
                        raise UnicornException(
                            name=f'the obstacle square cannot be the same as the queen')

    @classmethod
    async def GenerateChess(cls, entity: ParamProblemTwo) -> ProblemTwoResponse:
        try:
            cls.validateChess(entity)
            n = entity.n
            rowqueen = entity.rq
            columnqueen = entity.cq
            countx = 0
            array_aux = []
            for i in range(n):
                extra = n-countx
                elementsub = []
                for j in range(n):
                    item = cls.LoadInfo(entity.obstacle, i, j, extra)

                    if ((item.coordinate.column == columnqueen) and (item.coordinate.row == rowqueen)):
                        item.detail = FigureResponse(
                            selected=True, imageurl='https://pic.onlinewebfonts.com/svg/img_546821.png', figure=ChessEnum.QUEEN)

                    elementsub.append(item)
                array_aux.append(elementsub)
                countx += 1

            filter_box = cls.FilterAvailable(
                array_aux, entity.obstacle, rowqueen, columnqueen, n)

            result_list = cls.listattackbox(
                array_aux, filter_box)

            # print(len(filter_box))
            data = ProblemTwoResponse(
                attack=len(filter_box), chess=result_list)
            return data
        except UnicornException as e:
            raise UnicornException(name=e.__dict__['name'])
        except Exception as e:
            print(e)
            raise Exception(e)

    @classmethod
    async def GenerateResultTree(cls, world: str) -> int:
        try:
            n = len(world)
            # for por n
            resultc = int(n * (n + 1) / 2)
            return resultc
        except UnicornException as e:
            raise UnicornException(name=e.__dict__['name'])
        except Exception as e:
            raise Exception(e)

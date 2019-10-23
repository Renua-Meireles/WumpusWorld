
from random import randrange

class Environment(object):
    def __init__(self, dimension:int, n_pits:int, n_golds:int=1, n_wumpus:int=1):
        self.matrix = [['empty']*dimension]*dimension
        self.dimension = dimension
        self.generate({'name': 'pit','amount':n_pits})
        self.generate({'name': 'gold','amount':n_golds})
        self.generate({'name': 'wumpus','amount':n_wumpus})

    def generate(self, obj:dict)->None:
        for _ in range(obj['amount']):
            x,y = self.randomCoordinate()
            self.matrix[x][y] = obj['name']
            #TODO: GENERATE PERCEPTIONS


    def getState(self, coordinate:tuple)->list:
        #TODO: RETURN PERCEPTIONS
        pass

    def isPit(self, coordinate:tuple)->bool:
        x, y = coordinate
        return self.matrix[x][y] == 'pit'

    def isWumpus(self, coordinate:tuple)->bool:
        x, y = coordinate
        return self.matrix[x][y] == 'wumpus'

    def isExit(self, coordinate:tuple)->bool:
        return coordinate == (0,0)

    def removeWumpus(self, coordinate:tuple)->None:
        x, y = coordinate
        self.matrix[x][y] = 'empty'

    def removeGold(self, coordinate:tuple)->None:
        x, y = coordinate
        self.matrix[x][y] = 'empty'


    def randomCoordinate(self, )->tuple:
        x,y = (0,0)
        while( ((x,y) == (0,0)) and (self.matrix[x][y] != 'empty')):
            x, y = randrange(self.dimension), randrange(self.dimension)
        return (x,y)
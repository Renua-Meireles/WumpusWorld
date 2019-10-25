
from random import randrange

class Environment(object):
    def __init__(self, dimension:int, n_pits:int, n_golds:int=1, n_wumpus:int=1):
        self.matrix = [['empty' for column in range(dimension)] for line in range(dimension)]
        self.matrix[0][0] = 'start'
        self.matrix_perceptions = [[ [] for column in range(dimension)] for line in range(dimension)]
        self.dimension = dimension
        self.generate({'name': 'pit','amount':n_pits})
        self.generate({'name': 'gold','amount':n_golds})
        self.generate({'name': 'wumpus','amount':n_wumpus})
        self.screamTrigger = False

        self.perceptions = {
            "pit": "breeze",
            "gold": "glitter",
            "wumpus": "stench"
        }
        self.matrix_perceptions = [['empty'] * dimension] * dimension


    def generate(self, obj: dict) -> None:
        for _ in range(obj['amount']):
            x, y = self.randomCoordinate()
            self.matrix[x][y] = obj['name']
            # TODO: GENERATE PERCEPTIONS

            # verifica se estar na primeira linha
            if x == 0:
                self.matrix_perceptions[x + 1][y].append(self.perceptions[obj['name']])

                # verifica se estar na primeira coluna
                if y == 0:
                    self.matrix_perceptions[x][y + 1].append(self.perceptions[obj['name']])

                #verifica se estar na ultima coluna
                elif y == (self.dimension-1):
                    self.matrix_perceptions[x][y - 2].append(self.perceptions[obj['name']])

                #verifica se estar nas colunas do meio
                else:
                    self.matrix_perceptions[x][y+1].append(self.perceptions[obj['name']])
                    self.matrix_perceptions[x][y-1].append(self.perceptions[obj['name']])


            # verifica se estar na ultima linha
            elif x == (self.dimension - 1):
                self.matrix_perceptions[x - 2][y].append(self.perceptions[obj['name']])

                # verifica se estar na primeira coluna
                if y == 0:
                    self.matrix_perceptions[x][y + 1].append(self.perceptions[obj['name']])

                # verifica se estar na ultima coluna
                if y == (self.dimension - 1):
                    self.matrix_perceptions[x][y - 2].append(self.perceptions[obj['name']])

                # verifica se estar nas colunas do meio
                else:
                    self.matrix_perceptions[x][y + 1].append(self.perceptions[obj['name']])
                    self.matrix_perceptions[x][y - 1].append(self.perceptions[obj['name']])

            # verifica se estar nas linhas do meio
            else:
                self.matrix_perceptions[x + 1][y].append(self.perceptions[obj['name']])
                self.matrix_perceptions[x - 1][y].append(self.perceptions[obj['name']])

                # verifica se estar na primeira coluna
                if y == 0:
                    self.matrix_perceptions[x][y + 1].append(self.perceptions[obj['name']])

                # verifica se estar na ultima coluna
                if y == (self.dimension - 1):
                    self.matrix_perceptions[x][y - 2].append(self.perceptions[obj['name']])

                # verifica se estar nas colunas do meio
                else:
                    self.matrix_perceptions[x][y + 1].append(self.perceptions[obj['name']])
                    self.matrix_perceptions[x][y - 1].append(self.perceptions[obj['name']])



    def printMatrix(self):
          for line in self.matrix:
              print(line)
    
    def getPerceptions(self, coordinate:tuple)->list:
        perceptions = []
        if self.isPerception(coordinate, 'breeze'): perceptions.append('breeze')
        if self.isPerception(coordinate, 'stentch'): perceptions.append('stench')
        if self.isPerception(coordinate, 'glitter'): perceptions.append('glitter')
        if self.screamTrigger: 
            perceptions.append('scream')
            self.screamTrigger = False         
        return perceptions

    def isPerception(self, coordinate, perception)-> bool:
        x,y = coordinate
        return perception in self.matrix_perceptions[x][y]
            
        
    def isPit(self, coordinate:tuple)->bool:
        x, y = coordinate
        return self.matrix[x][y] == 'pit'

    def isWumpus(self, coordinate:tuple)->bool:
        x, y = coordinate
        return self.matrix[x][y] == 'wumpus'

    def isExit(self, coordinate:tuple)->bool:
        return coordinate == (0,0)

    def removeWumpus(self, coordinate:tuple)->None:
        self.screamTrigger = True
        x, y = coordinate
        self.matrix[x][y] = 'empty'

    def removeGold(self, coordinate:tuple)->None:
        x, y = coordinate
        self.matrix[x][y] = 'empty'


    def randomCoordinate(self, )->tuple:
        x,y = (0,0)
        while( ((x,y) == (0,0)) or (self.matrix[x][y] != 'empty') ):
            x, y = randrange(self.dimension), randrange(self.dimension)
            
        return (x,y)
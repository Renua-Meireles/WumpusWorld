
from game.environment import Environment as GameEnvironment
from game.game import Game
from ga.environment import Environment as GAEnvironment

def main():
    game_environment = GameEnvironment(dimension = 5, n_pits = 4)
    game = Game(game_environment, gui_enabled=True)

    ga = GAEnvironment(game)
    
    solution = ga.start()
    game_environment.printMatrix(solution.coordinate)
    print(solution)
    
if __name__ == '__main__':
    main()
    #quit()

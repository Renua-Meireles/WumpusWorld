
from action import Action
from random import choice

def agentFunction(state:dict) -> None:
    size:int                = state['size']
    x, y                    = state['coordinates']
    perceptions:list(str)   = state['perceptions']
    arrow:bool              = state['arrow']

    """
        Tratamento das sensacoes por prioridade: BRILHO > GRITO > FEDOR > BRISA > NADA.
            Brilho -> Pegar (nao importa mais nada!, apenas pegue aquele bendito ouro!).
            Grito -> Mover (wumpus ja esta morto, apenas se move).
            Fedor -> Atirar/Mover (wumpus pode estar vivo ou morto, tenta atirar).
            Brisa -> Mover (nao há nada para se fazer, apenas mover)
            Nada -> Mover (avante!).
            
        Estao sendo tratadas as coordenadas em que os comportamentos sao iguais:
            se estiver na PRIMEIRA COLUNA:
                se estiver na PRIMEIRA LINHA:
                    | | | | |
                    | | | | |
                    | | | | |
                    |X| | | |
                senao se estiver na ULTIMA LINHA:
                    |X| | | |
                    | | | | |
                    | | | | |
                    | | | | |
                senao:
                    | | | | |
                    |X| | | |
                    |X| | | |
                    | | | | |
            senao se estiver na ULTIMA COLUNA:
                se estiver na PRIMEIRA LINHA:
                    | | | | |
                    | | | | |
                    | | | | |
                    | | | |X|
                senao se estiver na ULTIMA LINHA:
                    | | | |X|
                    | | | | |
                    | | | | |
                    | | | | |
                senao:
                    | | | | |
                    | | | |X|
                    | | | |X|
                    | | | | |
            senao se estiver nas COLUNAS CENTRAIS:
                se estiver na PRIMEIRA LINHA:
                    | | | | |
                    | | | | |
                    | | | | |
                    | |X|X| |
                senao se estiver na ULTIMA LINHA:
                    | |X|X| |
                    | | | | |
                    | | | | |
                    | | | | |
                senao:
                    | | | | |
                    | |X|X| |
                    | |X|X| |
                    | | | | |
    """

    if ('glitter' in perceptions): return Action('pickup')

    # primeira coluna
    if y == 0:
        # primeira linha
        if x == 0:
            if ('scream' in perceptions): return Action('move', direction = choice(['N','L']))

            elif ('stench' in perceptions):
                actionName = 'move' if not arrow else 'shoot'
                return Action(actionName, direction = choice(['N','L']))
                
            elif ('breeze' in perceptions): return Action('move', direction = choice(['N','L']))

            else: return Action('move', direction = choice(['N','L']))

        # ultima linha
        elif x == size-1:
            if ('scream' in perceptions): return Action('move', direction = choice(['S','L']))

            elif ('stench' in perceptions):
                actionName = 'move' if not arrow else 'shoot'
                return Action(actionName, direction = choice(['S','L']))
                
            elif ('breeze' in perceptions): return Action('move', direction = choice(['S','L']))

            else: return Action('move', direction = choice(['S','L']))

        # linhas do meio
        else:
            if ('scream' in perceptions): return Action('move', direction = choice(['N','L','S']))

            elif ('stench' in perceptions):
                actionName = 'move' if not arrow else 'shoot'
                return Action(actionName, direction = choice(['N','L','S']))
                
            elif ('breeze' in perceptions): return Action('move', direction = choice(['N','L','S']))

            else: return Action('move', direction = choice(['N','L','S']))

    # ultima coluna
    elif y == size-1:
        # primeira linha
        if x == 0:
            if ('scream' in perceptions): return Action('move', direction = choice(['O','S']))

            elif ('stench' in perceptions):
                actionName = 'move' if not arrow else 'shoot'
                return Action(actionName, direction = choice(['O','S']))

            elif ('breeze' in perceptions): return Action('move', direction = choice(['O','S']))

            else: return Action('move', direction = choice(['O','S']))

        # ultima linha
        elif x == size-1:
            if ('scream' in perceptions): return Action('move', direction = choice(['O','N']))

            elif ('stench' in perceptions):
                actionName = 'move' if not arrow else 'shoot'
                return Action(actionName, direction = choice(['O','N']))

            elif ('breeze' in perceptions): return Action('move', direction = choice(['O','N']))

            else: return Action('move', direction = choice(['O','N']))

        # linhas do meio
        else:
            if ('scream' in perceptions): return Action('move', direction = choice(['N','O','S']))

            elif ('stench' in perceptions):
                actionName = 'move' if not arrow else 'shoot'
                return Action(actionName, direction = choice(['N','O','S']))

            elif ('breeze' in perceptions): return Action('move', direction = choice(['N','O','S']))

            else: return Action('move', direction = choice(['N','O','S']))

    # colunas do meio
    else:
        # primeira linha
        if x == 0:
            if ('scream' in perceptions): return Action('move', direction=choice(['N', 'O', 'L']))

            elif ('stench' in perceptions):
                actionName='move' if not arrow else choice(['move', 'shoot'])
                return Action(actionName, direction=choice(['N', 'O', 'L']))

            elif ('breeze' in perceptions): return Action('move', direction=choice(['N', 'O', 'L']))

            else: return Action('move', direction=choice(['N', 'O', 'L']))
        # ultima linha
        elif x == size-1:
            if ('scream' in perceptions): return Action('move', direction=choice(['L', 'O', 'S']))

            elif ('stench' in perceptions):
                actionName = 'move' if not arrow else choice(['move', 'shoot'])
                return Action(actionName, direction=choice(['L', 'O', 'S']))

            elif ('breeze' in perceptions): return Action('move', direction=choice(['L', 'O', 'S']))

            else: return Action('move', direction=choice(['L', 'O', 'S']))
        # linhas do meio
        else:
            if ('scream' in perceptions): return Action('move', direction=choice(['L', 'O', 'S', 'N']))

            elif ('stench' in perceptions):
                actionName = 'move' if not arrow else choice(['move', 'shoot'])
                return Action(actionName, direction=choice(['L', 'O', 'S', 'N']))

            elif ('breeze' in perceptions): return Action('move', direction=choice(['L', 'O', 'S', 'N']))

            else: return Action('move', direction=choice(['L', 'O', 'S', 'N']))

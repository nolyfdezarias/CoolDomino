import copy
import random

def get_tokens(domino_type=7):
    '''
        Return all tokens in a domino game
        :param domino_type int: Game fashion
        :return list(list(int)): List of tokens
    '''
    return [[i, j] for i in range(domino_type) for j in range(i, domino_type)]

def distribute_tokens(players=4, domino_type=7):
    '''
        Return a random distribution of the tokens
        :param players int: Number of players
        :param domino_type int: Game fashion
        :return list(list(list(int))): List of tokens that each player has, 
            index 0 is the rest of remaining tokens 
    '''
    if players not in (2, 4):
        raise Exception('Wrong number of players!')

    tokens = get_tokens(domino_type)
    random.shuffle(tokens)
    choices = [i for i in range(1, players+1) for j in range(domino_type)]
    choices += [0] * (len(tokens) - players * domino_type)
    random.shuffle(choices)

    res = [[] for _ in range(players+1)]
    for i, choice in enumerate(choices):
       res[choice].append(tokens[i])

    return res


if __name__ == "__main__":
    board = distribute_tokens(4, 7)
    print(board)

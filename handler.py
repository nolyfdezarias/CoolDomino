from getTokens import *
from importlib import import_module as load

class Player:
	def __init__(self, name, play_function):
		self.name = name
		self.play = play_function

players_names = ['dummy_player', 'fat_thrower_player','minimize_fails_player']

def get_players(players_names):
    res = []
    for player in players_names:
        mod = load(player)
        res.append(Player(player, mod.play))
    return res

def count_tokens(tokens):
    _sum = [0] * len(tokens)
    for i in range(len(tokens)):
        for token in tokens[i]:
            _sum[i] += sum(token)
    return _sum.index(min(_sum)) 

def run(players):
    board = []
    tokens  = distribute_tokens(len(players))[1:]
    # to do
    # who starts? the one with the biggest double
    start = pas = 0
    while(True):
        token, pos = players[start].play(board, tokens[start])
        if token == None:
            pas += 1
            if pas == len(players):
                # tranque
                winner = count_tokens(tokens)
                print(str(winner) + ' won!')
                return start
            start = (start + 1) % len(players)
            continue
        pas = 0
        board.insert(pos, token)
        tokens[start].remove(token)

        #print(board)
        #print(tokens)

        if not len(tokens[start]):
            print(str(start) + ' won!')
            return start

        start = (start + 1) % len(players)

def simulate(times=1000):
    players = get_players(players_names)
    result = [0] * len(players)

    for i in range(times):
        result[run(players)] += 1
    
    for i in range(len(players)):
        print(f'{players_names[i]} has won {result[i]} games')

if __name__ == "__main__":
    simulate()
from getTokens import *
from importlib import import_module as load
from tqdm import tqdm
import pandas as pd

class Player:
	def __init__(self, name, play_function):
		self.name = name
		self.play = play_function

players_names = ['dummy_player', 'fat_thrower_player','minimize_fails_player', 'most_accompanied_player']

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

def run(players, domino_type=7):
    board = []
    tokens  = distribute_tokens(len(players), domino_type)[1:]
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
                # print(str(winner) + ' won!')
                return start
            start = (start + 1) % len(players)
            continue
        pas = 0
        board.insert(pos, token)
        tokens[start].remove(token)

        #print(board)
        #print(tokens)

        if not len(tokens[start]):
            # print(str(start) + ' won!')
            return start

        start = (start + 1) % len(players)

def simulate(times=10000):
    players = get_players(players_names)
    result = [0] * len(players)

    for i in tqdm(range(times)):
        result[run(players, 10)] += 1
    
    # Idea no solo contar que gano tb contar cuantas veces gano
    # por pegarse o por tranque

    print()
    data = list(zip(players_names, result))
    df = pd.DataFrame(data, columns=['player_name', 'won'])
    df = df.sort_values(by=['won'], ascending=False)
    print(df)


if __name__ == "__main__":
    simulate()
import copy

def play(board, tokens):
    count = [0] * 10
    for token in tokens:
        count[token[0]] += 1
        count[token[1]] += 1
    most_repited_token = count.index(max(count))
    
    if not len(board):
        # go out with the double of the most repited token
        # in case of having it, or with the biggest one with 
        # a face of the most repeated token
        biggest = [-1, -1]
        for token in tokens:
            if token[0] == most_repited_token and token[1] == most_repited_token:
                # got the double
                return token, 0
            elif (token[0] == most_repited_token or token[1] == most_repited_token) and sum(token) > biggest[0]:
                biggest[0] = sum(token)
                biggest[1] = token
        return biggest[1], 0

    left  = board[0][0]
    right = board[-1][1]
    possible_moves = []
    for token in tokens:
        # Of all the tokens that I can play, 
        # I order them by the number of repetitions 
        # that I have on the other side of the token 
        # and I play the one that has the less repetition
        if token[0] == left:
            token.reverse()
            possible_moves.append((-1*count[token[0]], copy.deepcopy(token), 0))
        elif token[0] == right:
            possible_moves.append((-1*count[token[1]], copy.deepcopy(token), len(board)))
        elif token[1] == left:
            possible_moves.append((-1*count[token[0]], copy.deepcopy(token), 0))
        elif token[1] == right:
            token.reverse()
            possible_moves.append((-1*count[token[1]], copy.deepcopy(token), len(board)))
    
    possible_moves.sort()
    return (None, None) if len(possible_moves) == 0 else (possible_moves[-1][1], possible_moves[-1][2])
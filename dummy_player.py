import copy

def play(board, tokens):
    '''
        Return token and where to play the token 
        head or tail of the board
    '''
    if not len(board):
        return tokens[0], 0

    left  = board[0][0]
    right = board[-1][1]
    for token in tokens:
        if token[0] == left:
            token.reverse()
            return copy.deepcopy(token), 0
        elif token[0] == right:
            return copy.deepcopy(token), len(board)
        elif token[1] == left:
            return copy.deepcopy(token), 0
        elif token[1] == right:
            token.reverse()
            return copy.deepcopy(token), len(board)
    return None, None
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

    posible_moves = []

    for token in tokens:
        if token[0] == left:
            token.reverse()
            posible_moves.append((sum(token),copy.deepcopy(token),0))
        elif token[0] == right:
            posible_moves.append((sum(token),copy.deepcopy(token),len(board)))
        elif token[1] == left:
            posible_moves.append((sum(token),copy.deepcopy(token),0))
        elif token[1] == right:
            token.reverse()
            posible_moves.append((sum(token),copy.deepcopy(token),len(board)))
    
    posible_moves.sort()
    return (None, None) if len(posible_moves) == 0 else (copy.deepcopy(posible_moves[-1][1]),posible_moves[-1][2])
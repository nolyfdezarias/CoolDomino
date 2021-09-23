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
    fails = [0] * 11
    c_fails = 0

    for token in tokens:
        fails[token[0]] += 1
        fails[token[1]] += 1

    for fail in fails:
        if fail == 0:
            c_fails += 1

    for token in tokens:
        if fails[token[0]] == 1 and fails[token[1]] == 1:
            c_fail = c_fails + 2
        elif fails[token[0]] == 1 or fails[token[1]] == 1:
            c_fail = c_fails + 1
        else:
            c_fail = c_fails

        if token[0] == left:
            token.reverse()
            posible_moves.append((c_fail,-1*sum(token),copy.deepcopy(token),0))
        elif token[0] == right:
            posible_moves.append((c_fail,-1*sum(token),copy.deepcopy(token),len(board)))
        elif token[1] == left:
            posible_moves.append((c_fail,-1*sum(token),copy.deepcopy(token),0))
        elif token[1] == right:
            token.reverse()
            posible_moves.append((c_fail,-1*sum(token),copy.deepcopy(token),len(board)))
    
    posible_moves.sort()
    return (None, None) if len(posible_moves) == 0 else (copy.deepcopy(posible_moves[0][2]),posible_moves[0][3])
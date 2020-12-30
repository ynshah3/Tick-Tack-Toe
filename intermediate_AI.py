from random import randint


def int_ai_move(board):
    moves_left = []
    val_00 = board[0][0]
    val_01 = board[0][1]
    val_02 = board[0][2]
    val_10 = board[1][0]
    val_11 = board[1][1]
    val_12 = board[1][2]
    val_20 = board[2][0]
    val_21 = board[2][1]
    val_22 = board[2][2]
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] is None:
                moves_left.append((j, i))
    if (val_00 == val_01 is not None) and (val_02 is None):
        move = (2, 0)
        return move
    if (val_00 == val_02 is not None) and (val_01 is None):
        move = (1, 0)
        return move
    if (val_01 == val_02 is not None) and (val_00 is None):
        move = (0, 0)
        return move
    if (val_10 == val_11 is not None) and (val_12 is None):
        move = (2, 1)
        return move
    if (val_10 == val_12 is not None) and (val_11 is None):
        move = (1, 1)
        return move
    if (val_11 == val_12 is not None) and (val_10 is None):
        move = (0, 1)
        return move
    if (val_20 == val_21 is not None) and (val_22 is None):
        move = (2, 2)
        return move
    if (val_20 == val_22 is not None) and (val_21 is None):
        move = (1, 2)
        return move
    if (val_21 == val_22 is not None) and (val_20 is None):
        move = (0, 2)
        return move
    if (val_00 == val_10 is not None) and (val_20 is None):
        move = (0, 2)
        return move
    if (val_00 == val_20 is not None) and (val_10 is None):
        move = (0, 1)
        return move
    if (val_10 == val_20 is not None) and (val_00 is None):
        move = (0, 0)
        return move
    if (val_01 == val_11 is not None) and (val_21 is None):
        move = (1, 2)
        return move
    if (val_01 == val_21 is not None) and (val_11 is None):
        move = (1, 1)
        return move
    if (val_11 == val_21 is not None) and (val_01 is None):
        move = (1, 0)
        return move
    if (val_02 == val_12 is not None) and (val_22 is None):
        move = (2, 2)
        return move
    if (val_02 == val_22 is not None) and (val_12 is None):
        move = (2, 1)
        return move
    if (val_12 == val_22 is not None) and (val_02 is None):
        move = (2, 0)
        return move
    if (val_00 == val_11 is not None) and (val_22 is None):
        move = (2, 2)
        return move
    if (val_00 == val_22 is not None) and (val_11 is None):
        move = (1, 1)
        return move
    if (val_11 == val_22 is not None) and (val_00 is None):
        move = (0, 0)
        return move
    if (val_02 == val_11 is not None) and (val_20 is None):
        move = (0, 2)
        return move
    if (val_02 == val_20 is not None) and (val_11 is None):
        move = (1, 1)
        return move
    if (val_11 == val_20 is not None) and (val_02 is None):
        move = (2, 0)
        return move
    return moves_left[randint(0, len(moves_left) - 1)]

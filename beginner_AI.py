from random import randint


def beg_ai_move(board):
    moves_left = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] is None:
                moves_left.append((j, i))
    return moves_left[randint(0, len(moves_left) - 1)]

from game_controls import winner
from game_controls import update_board
import copy
import math


def invert(val):
    if val == 'O':
        return 'X'
    elif val == 'X':
        return 'O'


def get_available_moves(board):
    moves = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] is None:
                moves.append((j, i))
    return moves


def minimax_score(player, board, alpha, beta):
    available_moves = get_available_moves(board)
    if winner('X', board):
        return math.inf
    elif winner('O', board):
        return -math.inf
    elif not available_moves:
        return 0
    if player == 'X':
        best_score = -math.inf
        for move in available_moves:
            sample_board = copy.deepcopy(board)
            update_board(player, move, sample_board)
            score = minimax_score('O', sample_board, alpha, beta)
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for move in available_moves:
            sample_board = copy.deepcopy(board)
            update_board(player, move, sample_board)
            score = minimax_score('X', sample_board, alpha, beta)
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score


def tra_ai_move(board):
    move_to_make = None
    max_score = None
    moves = get_available_moves(board)
    for move in moves:
        sample_board = copy.deepcopy(board)
        update_board('X', move, sample_board)
        score = minimax_score('O', sample_board, -math.inf, math.inf)
        if max_score is None or score > max_score:
            max_score = score
            move_to_make = move
    return move_to_make

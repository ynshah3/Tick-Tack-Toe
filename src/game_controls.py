
def build_new_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]


def check(i):
    if i is None:
        return " "
    else:
        return i


def pretty_print(board):
    print("  0 1 2")
    print("  ------")
    k = 0
    for i in board:
        print("{}|".format(k), end='')
        for j in i[0:2]:
            print("{}".format(check(j)), end=' ')
        print("{}".format(check(i[2])), end='')
        print("|")
        k += 1
    print("  ------")


def user_move(player, board):
    x = int(input("{}, Enter X (horizontal) coordinate between 0-2: ".format(player)))
    y = int(input("{}, Enter Y (vertical) coordinate between 0-2: ".format(player)))
    if move_validity(x, y, board) is False:
        move = user_move(player, board)
        return move
    else:
        move = (x, y)
        return move


def update_board(player, move, board):
    board[move[1]][move[0]] = player


def move_validity(x, y, board):
    if x not in range(0, 3) or y not in range(0, 3):
        print("Error! Coordinates out of bounds! Try Again")
        return False
    else:
        if board[y][x] is not None:
            print("Invalid move! Coordinate has already been occupied! Try again!")
            return False
        else:
            return True


def winner(val, board):
    for i in range(0, 3):
        if board[i][0] is board[i][1] is board[i][2] is val or \
                board[0][i] is board[1][i] is board[2][i] is val:
            return True
    if board[0][0] is board[1][1] is board[2][2] is val or \
            board[0][2] is board[1][1] is board[2][0] is val:
        return True
    return False

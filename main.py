from game_controls import build_new_board
from game_controls import pretty_print
from game_controls import user_move
from game_controls import update_board
from game_controls import winner
from beginner_AI import beg_ai_move
from intermediate_AI import int_ai_move
from trained_AI import tra_ai_move
import time

if __name__ == '__main__':
    print("\n\nWelcome to the traditional game of Tick-Tack-Toe :D")
    time.sleep(2)
    print("\nMain Menu\n")
    print("1. Single-Player")
    print("2. Two-Player")
    choice = int(input("\nDo you want to fight a single-player or a two-player battle? Choose a single number: "))
    if choice == 1:
        print("\n1. Beginner AI")
        print("2. Intermediate AI")
        print("3. Trained AI")
        choice2 = int(input("\nWhich AI do you want to battle? Enter a number: ") or "1")
        ply = input("\nEnter your name: ")
    elif choice == 2:
        print("\nSelect which one of you wants to go first!\n\n")
        time.sleep(1)
        ply1 = input("Enter name of player going first: " or "Anon1")
        ply2 = input("Enter name of player going second: " or "Anon2")
    else:
        print("Invalid choice! Exiting!")
        exit(1)
    print("\nAnd now, let the battle begin...\n")
    time.sleep(1)
    game_board = build_new_board()
    pretty_print(game_board)
    times = 0
    while True:
        if choice == 1:
            coord = user_move(ply, game_board)
        else:
            coord = user_move(ply1, game_board)
        update_board('O', coord, game_board)
        print()
        pretty_print(game_board)
        print()
        time.sleep(1)
        times += 1
        if winner('O', game_board):
            if choice == 1:
                print("You are the winner! Hooray! Kudos!")
            else:
                print("{} is the winner! Hooray! Kudos!".format(ply1))
            break
        if times == 9:
            print("It is a tie! Better Luck next time!")
            break
        else:
            if choice == 1:
                if choice2 == 1:
                    coord = beg_ai_move(game_board)
                elif choice2 == 2:
                    coord = int_ai_move(game_board)
                    print(coord)
                else:
                    coord = tra_ai_move(game_board)
                print("\nIt is your opponent's chance...\n")
            else:
                coord = user_move(ply2, game_board)
            update_board('X', coord, game_board)
            print()
            pretty_print(game_board)
            print()
            times += 1
            if winner('X', game_board):
                if choice == 1:
                    print("You lose :( The AI beat you this time!")
                else:
                    print("{} is the winner! Hooray! Kudos!".format(ply2))
                break

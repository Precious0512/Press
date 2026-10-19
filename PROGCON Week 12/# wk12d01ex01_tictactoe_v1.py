# wk12d01ex01_tictactoe_v1.py
# PROGCON IT261 - Week 12 Day 01 Flowcharting Exercise #1
# Name: Precious Arellano
# Tic-Tac-Toe version 1: one row only (3 boxes).
# Player = O, Computer = X. random decides who starts.

import random

USER = "O"
COMPUTER = "X"


def create_board():
    """Create the one-row board."""
    return ["1", "2", "3"]


def show_board(board):
    """Display the one-row board."""
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print()


def choose_starter():
    """Use random to decide who starts. Returns 'user' or 'computer'."""
    if random.randint(0, 1) == 0:
        return "user"
    return "computer"


def is_free(board, position):
    """Check if a box is still free."""
    return board[position] != USER and board[position] != COMPUTER


def user_move(board):
    """Ask the user for a box number and place O."""
    while True:
        choice = input("Enter box number (1, 2, 3): ")
        if choice in ("1", "2", "3") and is_free(board, int(choice) - 1):
            board[int(choice) - 1] = USER
            return
        print("Invalid choice or box taken")


def computer_move(board):
    """Computer picks a random free box and places X."""
    free_boxes = [i for i in range(3) if is_free(board, i)]
    choice = random.choice(free_boxes)
    board[choice] = COMPUTER
    print("Computer's choice", choice + 1)


def check_winner(board, mark):
    """Check if the one row is all the same mark."""
    return board[0] == mark and board[1] == mark and board[2] == mark


def board_full(board):
    """Check if there are no free boxes left."""
    for i in range(3):
        if is_free(board, i):
            return False
    return True


def play_game():
    board = create_board()
    turn = choose_starter()
    print("You are O. The computer is X.")
    if turn == "user":
        print("You start!")
    else:
        print("Computer starts!")
    show_board(board)

    while True:
        if turn == "user":
            user_move(board)
            mark = USER
            turn = "computer"
        else:
            computer_move(board)
            mark = COMPUTER
            turn = "user"

        show_board(board)

        if check_winner(board, mark):
            if mark == USER:
                print("You win!")
            else:
                print("Computer wins!")
            break
        if board_full(board):
            print("It's a draw!")
            break


play_game()

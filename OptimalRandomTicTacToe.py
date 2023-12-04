# AI Tic Tac Toe Game (optimal and random)

import numpy as np
import random
from time import sleep

def create_game_board():
    return np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])

def available_positions(game_board):
    positions = []
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == 0:
                positions.append((i, j))
    return positions

def random_place(game_board, player):
    possible_moves = available_positions(game_board)
    current_position = random.choice(possible_moves)
    game_board[current_position] = player
    return game_board

def check_row_win(game_board, player):
    for x in range(len(game_board)):
        win = True
        for y in range(len(game_board)):
            if game_board[x, y] != player:
                win = False
                continue
        if win == True:
            return win
    return win

def check_column_win(game_board, player):
    for x in range(len(game_board)):
        win = True
        for y in range(len(game_board)):
            if game_board[y][x] != player:
                win = False
                continue
        if win == True:
            return win
    return win

def check_diagonal_win(game_board, player):
    win = True
    y = 0
    for x in range(len(game_board)):
        if game_board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(game_board)):
            y = len(game_board) - 1 - x
            if game_board[x, y] != player:
                win = False
    return win

def evaluate_game(game_board):
    winner = 0
    for player in [1, 2]:
        if (check_row_win(game_board, player) or
            check_column_win(game_board, player) or
            check_diagonal_win(game_board, player)):
            winner = player
    if np.all(game_board != 0) and winner == 0:
        winner = -1
    return winner

def print_game_board(game_board):
    for row in game_board:
        print(' '.join(['X' if cell == 1 else 'O' if cell == 2 else '-' for cell in row]))

def player_move(game_board):
    row = int(input("Enter the row (0, 1, 2): "))
    col = int(input("Enter the column (0, 1, 2): "))
    while game_board[row][col] != 0:
        print("Cell already filled. Pick another cell.")
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))
    game_board[row][col] = 1
    return game_board

def computer_move(game_board):
    possible_moves = available_positions(game_board)
    current_position = random.choice(possible_moves)
    game_board[current_position] = 2
    return game_board

def play_tic_tac_toe():
    game_board = create_game_board()
    winner = 0
    counter = 1
    print("Initial game board:")
    print_game_board(game_board)
    sleep(1)

    while winner == 0:
        if counter % 2 == 1:
            game_board = player_move(game_board)
        else:
            print("Computer's turn:")
            sleep(1)
            game_board = computer_move(game_board)
        print("Game board after move", counter)
        print_game_board(game_board)
        sleep(1)
        winner = evaluate_game(game_board)
        if winner != 0:
            break
        counter += 1

    if winner == -1:
        print("It's a tie!")
    elif winner == 1:
        print("Player wins!")
    elif winner == 2:
        print("Computer wins!")

play_tic_tac_toe()

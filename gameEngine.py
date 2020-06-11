# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 00:43:10 2020

@author: Mathias
"""


from Board import Board
from minimax import minimax_player
from randomMover import random_player

print("New Game!")

players = ['X', 'O']
gameBoard = Board
gameBoard.newGame(Board)

player_choice = input("Choose X (first move) or O:")
            
print(player_choice)
            
winner = None
current_state = "In Progress"
    
if player_choice == 'X' or player_choice == 'x':
    current_player = 0
else:
    current_player = 1
                
while current_state == "In Progress":
    if current_player == 0:
        move = int(input("Choose a tile (1 to 9): "))
        if move == 10:
            break #to get out so I don't have to restart kernel
                        
        gameBoard.play_move(gameBoard, gameBoard.game_state, players[current_player], move)
        winner = Board.check_winner(gameBoard, players[current_player])
    else:
                    
        #minmax = minimax_player(gameBoard)
        #move = minmax.getBestMove(gameBoard, players[current_player])
        randPlayer = random_player
        
        availables = gameBoard.find_available(gameBoard)
        move = randPlayer.get_move(availables)
        #move = 3;
        gameBoard.play_move(gameBoard, gameBoard.game_state, players[current_player], move)
        winner = Board.check_winner(gameBoard, players[current_player])
                    
    Board.print_board(gameBoard.game_state)
                
    if winner is not None:
        print(str(winner) + "won")
    else:
        current_player = (current_player + 1)%2 #this is an ugly way of switching players
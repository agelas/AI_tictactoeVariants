# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:21:15 2020

@author: Mathias
"""

players = ['X', 'O']

class Board:
    
        game_state = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' '],]
        
        def newGame():
            print('1 | 2 | 3' )
            print('---------')
            print('4 | 5 | 6')
            print('---------')
            print('7 | 8 | 9')
            
        
        def play_move(state, player, move_num):
            #Row column indexing to access positions in state
            if state[int((move_num-1)/3)][(move_num-1)%3] == ' ': 
                state[int((move_num-1)/3)][(move_num-1)%3] = player
            else:
                move_num = int(input("Position is not empty. Choose again: "))
                Board.play_move(state, player, move_num) #hmm idk if I like this, might need to be cls or this or idk
                
        def copy_game_state(state):
            new_state = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' '],]
            for i in range(3):
                for j in range(3):
                    new_state[i][j] = state[i][j]
            return new_state
        
        def check_winner(self):
            
            #Check horizontals
            if(self.game_state[0][0] == self.game_state[0][1] and self.game_state[0][1] == self.game_state[0][2] and self.game_state[0][0] != ' '):
                return self.game_state[0][0], "Done" #State [0][0] is an X or Y
            if(self.game_state[1][0] == self.game_state[1][1] and self.game_state[1][1] == self.game_state[1][2] and self.game_state[1][0] != ' '):
                return self.game_state[1][0], "Done"
            if(self.game_state[2][0] == self.game_state[2][1] and self.game_state[2][1] == self.game_state[2][2] and self.game_state[2][0] != ' '):
                return self.game_state[2][0], "Done"
            
            #Check Verticals
            if(self.game_state[0][0] == self.game_state[1][0] and self.game_state[1][0] == self.game_state[2][0] and self.game_state[0][0] != ' '):
                return self.game_state[0][0], "Done" #State [0][0] is an X or Y
            if(self.game_state[0][1] == self.game_state[1][1] and self.game_state[1][1] == self.game_state[2][1] and self.game_state[0][1] != ' '):
                return self.game_state[0][1], "Done"
            if(self.game_state[0][2] == self.game_state[1][2] and self.game_statev[1][2] == self.game_state[2][2] and self.game_state[0][2] != ' '):
                return self.game_state[0][2], "Done"
            
            #Check Diagonals
            if(self.game_state[0][0] == self.game_state[1][1] and self.game_state[1][1] == self.game_state[2][2] and self.game_state[0][0] != ' '):
                return self.game_state[0][0], "Done" #State [0][0] is an X or Y
            if(self.game_state[2][0] == self.game_state[1][1] and self.game_state[1][1] == self.game_state[0][2] and self.game_state[2][0] != ' '):
                return self.game_state[2][0], "Done"
            
            
            draw_flag = 0
            for i in range(3):
                for j in range(3):
                    if self.game_state[i][j] is ' ':
                        draw_flag = 1 #If empty, moves still available
            if draw_flag is 0:
                return None, "Draw" #If draw_flag still 0 
            
            return None, "In Progress"
        
        def print_board(state, player):
            print(str(state[0][0]) + ' | ' + str(state[0][1]) + ' | ' + str(state[0][2]))
            print('---------')
            print(str(state[1][0]) + ' | ' + str(state[1][1]) + ' | ' + str(state[1][2]))
            print('---------')
            print(str(state[2][0]) + ' | ' + str(state[2][1]) + ' | ' + str(state[2][2]))
            
            
        

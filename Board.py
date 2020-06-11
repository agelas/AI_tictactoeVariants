# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:21:15 2020

@author: Mathias
"""


class Board:
    
        game_state = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' '],]
        
        def newGame(self):
            print('1 | 2 | 3' )
            print('---------')
            print('4 | 5 | 6')
            print('---------')
            print('7 | 8 | 9')
            
            
            
        def play_move(self, state, player, move_num):
            #Row column indexing to access positions in state
            if self.game_state[int((move_num-1)/3)][(move_num-1)%3] == ' ': 
                self.game_state[int((move_num-1)/3)][(move_num-1)%3] = player
            else:
                move_num = int(input("Position is not empty. Choose again: "))
                Board.play_move(self, state, player, move_num) 
                #Rn after the second move you start moving for 'O' because you 
                #trigger not empty basically
                
        def copy_game_state(state):
            new_state = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' '],]
            for i in range(3):
                for j in range(3):
                    new_state[i][j] = state[i][j]
            return new_state
        
        #Checks if either player has won
        def check_winner(self, player):
            
            #Check horizontals
            win_states = [
            [ self.game_state[0][0], self.game_state[0][1], self.game_state[0][2] ],
            [ self.game_state[1][0], self.game_state[1][1], self.game_state[1][2] ],
            [ self.game_state[2][0], self.game_state[2][1], self.game_state[2][2] ],
            [ self.game_state[0][0], self.game_state[1][0], self.game_state[2][0] ],
            [ self.game_state[0][1], self.game_state[1][1], self.game_state[2][1] ],
            [ self.game_state[0][2], self.game_state[1][2], self.game_state[2][2] ],
            [ self.game_state[0][0], self.game_state[1][1], self.game_state[2][2] ],
            [ self.game_state[2][0], self.game_state[1][1], self.game_state[0][2] ],
            ]
            
            if [player, player, player] in win_states:
                print('HEY')
                return player, "Done"
            
            draw_flag = 0
            for i in range(3):
                for j in range(3):
                    if self.game_state[i][j] is ' ':
                        draw_flag = 1 #If empty, moves still available
            if draw_flag is 0:
                return None, "Draw" #If draw_flag still 0 
            
            return None
        
        def find_available(self):
            available_tiles = []
            for i in range(3):
                for j in range(3):
                    if self.game_state[i][j] is ' ':
                        available_tiles.append(i*3+(j+1))
            print(' '.join(map(str, available_tiles)))
            return available_tiles
        
        def print_board(state):
            print(str(state[0][0]) + ' | ' + str(state[0][1]) + ' | ' + str(state[0][2]))
            print('---------')
            print(str(state[1][0]) + ' | ' + str(state[1][1]) + ' | ' + str(state[1][2]))
            print('---------')
            print(str(state[2][0]) + ' | ' + str(state[2][1]) + ' | ' + str(state[2][2]))
            
            
        

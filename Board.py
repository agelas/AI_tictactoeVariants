# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:21:15 2020

@author: Mathias
"""


class Board:
    
        game_state = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' ']]
        
        def newGame(self):
            '''
            Prints the tiles and the numbers corresponding to them.

            Returns
            -------
            None.

            '''
            print('1 | 2 | 3' )
            print('---------')
            print('4 | 5 | 6')
            print('---------')
            print('7 | 8 | 9')
            print()
            
            
            
        def play_move(self, state, player, move_num):
            '''
            Places a player's corresponding tile on the selected position.
            May be called recursivley if player attempts to occupy a cell that is not open.

            Parameters
            ----------
            state : The board instance to place pieces on.
            player : The 'X' or 'O' to be placed.
            move_num : The number of the tile we're placing the 'X'/'O' on.

            Returns
            -------
            None.

            '''
            #Row column indexing to access positions in state
            if self.game_state[int((move_num-1)/3)][(move_num-1)%3] == ' ': 
                self.game_state[int((move_num-1)/3)][(move_num-1)%3] = player
            else:
                move_num = int(input("Position is not empty. Choose again: "))
                Board.play_move(self, state, player, move_num) 
                
                
        def copy_game_state(state):
            new_state = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' '],]
            for i in range(3):
                for j in range(3):
                    new_state[i][j] = state[i][j]
            return new_state
        
        def check_winner(self, player):
            '''
            Checks whether a player 'X' or 'O' has won by going through self.game_state
            and seeing if there's a three in a row of 'X' or 'O' markers.

            Parameters
            ----------
            player : The 'X' or 'O'.

            Returns
            -------
            If a winner is found, it will return the player and "Done", the latter is a flag
            for the game engine to exit out of game loop. 
            
            If no winners then function returns None, and "Draw" if no more moves are possible

            '''
            
            #Check combinations
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
                    #if self.game_state[i][j] is ' ':
                    if self.game_state[i][j] == ' ':
                        draw_flag = 1 #If empty, moves still available
            #if draw_flag is 0:
            if draw_flag == 0:
                return None, "Draw" #If draw_flag still 0 then out of available tiles
            
            return None
        
        def find_available(self):
            '''
            Finds all available tiles in self.game_state

            Returns
            -------
            available_tiles : A list of all remaining tiles.

            '''
            available_tiles = []
            for i in range(3):
                for j in range(3):
                    if self.game_state[i][j] is ' ':
                        available_tiles.append(i*3+(j+1))
            print(' '.join(map(str, available_tiles)))
            return available_tiles
        
        def print_board(state):
            '''
            Prints the board
            '''
            print(str(state[0][0]) + ' | ' + str(state[0][1]) + ' | ' + str(state[0][2]))
            print('---------')
            print(str(state[1][0]) + ' | ' + str(state[1][1]) + ' | ' + str(state[1][2]))
            print('---------')
            print(str(state[2][0]) + ' | ' + str(state[2][1]) + ' | ' + str(state[2][2]))
            print()
            
        def interable_board(self):
            '''
            Gives the game engine an iterable game_state object that can be 
            fiddled with. 

            Returns
            -------
            The game_state list.

            '''
            return self.game_state;
        
        def unparse(state, human_tile):
            '''
            Some of the AI players turn the board into a format that they need
            in order to interpret it coorectly. This function is responsible for
            taking those boards and turning it back into something with 'X'/'O'.

            Parameters
            ----------
            state : The board.
            human_tile : Whether player is the 'X' or 'O'

            Returns
            -------
            state : The un-parsed board that is a list with 'X' or 'O' on the tiles

            '''
            
            #if human_tile == 'X':           
            if human_tile == 'X' or human_tile == 'x':
                AI_tile = 'O'
                human_tile = 'X'
            else:
                AI_tile = 'X'
                human_tile = 'O'
                
            for i in range(3):
                for j in range(3):
                    if state[i][j] == 1:
                        state[i][j] = AI_tile
                    if state[i][j] == -1:
                        state[i][j] = human_tile
            return state
           
                    
            
            
        

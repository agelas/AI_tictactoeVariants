# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 22:40:11 2020

@author: Mathias
"""
import random


class tabularQ_player:
    
    
    def hashBoard(state):
        
        hashC = 0
        
        for i in range(9):
            hashC *= 3
            hashC += state[i]
        return hashC
    
    def trainingCycle(self, training_cycles, player):
        
        state = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' ']]
        tabularDictionary = {{}};
        
        i = 0
        while(i < training_cycles):
            
            if player == 'X':
                tiles = ['X', 'O']
            else:
                tiles = ['O', 'X']
                
            states_list = []
            moves_list = []
        
            game_state = "In Progress"
            
            while(game_state == "In Progress"):
            
                hashed_board = self.hashBoard(state)
                
                available_moves = self.empty_tiles(state)
                length = len(available_moves)
                randMove = random.randint(1, length)
                
                if not self.game_over(state):
                    self.play_move(state, 'X', randMove)
                    
                #If AI is X, add to states_list and moves_list
                if player == 'X':
                    states_list.append(hashed_board)
                    moves_list.append(randMove)
                
                winner = self.check_winner(state, 'X')    
           
                if winner is not None:
                    print(str(winner) + "won")
                    game_state = "Done"
                
                #Recalculate available_moves and randMove
                available_moves = self.empty_tiles(state)
                length = len(available_moves)
                randMove = random.randint(1, length)
                
                if not self.game_over(state):
                    self.play_move(state, 'O', randMove)
                    
                #If AI is O, add to states_list and moves_list
                if player == 'O':
                    states_list.append(hashed_board)
                    moves_list.append(randMove)
                    
                winner = self.check_winner(state, 'O')
                if winner is not None:
                    print(str(winner) + "won")
                    game_state = "Done"
                
                #Calculate quality starting with last state and move
                
            i+=1
            #Resetting board happens out here
                
        
        return #Not sure this function even returns, just fills in hash map
    
    def check_winner(self, state, player):
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
        [ state[0][0], state[0][1], state[0][2] ],
        [ state[1][0], state[1][1], state[1][2] ],
        [ state[2][0], state[2][1], state[2][2] ],
        [ state[0][0], state[1][0], state[2][0] ],
        [ state[0][1], state[1][1], state[2][1] ],
        [ state[0][2], state[1][2], state[2][2] ],
        [ state[0][0], state[1][1], state[2][2] ],
        [ state[2][0], state[1][1], state[0][2] ],
        ]
        
        if [player, player, player] in win_states:
            print('HEY')
            return player, "Done"
        
        draw_flag = 0
        for i in range(3):
            for j in range(3):
                if self.game_state[i][j] == ' ':
                    draw_flag = 1 #If empty, moves still available
        if draw_flag == 0:
            return None, "Draw" #If draw_flag still 0 then out of available tiles
        
        return None
    
    def game_over(self, state):
        '''
        Checks if the game is over.

        Parameters
        ----------
        state : 
            The current board state. 

        Returns
        -------
        bool
            True or false if a win is detected for either player designated by 'X' or 'O'.

        '''
        return self.wins(state, 'X') or self.wins(state, 'O')
    
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
            self.play_move(self, state, player, move_num)
            
    def empty_tiles(state):
        '''
        Find available tiles in self.state.
        '''
        tiles = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    tiles.append(i*3+(j+1))
        return tiles
    
    def valid_move(self, position):
        '''
        Checks if a hypothetical move is valid. 

        Parameters
        ----------
        position : 
            The board position under consideration.

        Returns
        -------
        bool
            True if move is valid.

        '''
        if position in self.empty_tiles():
            return True
        else:
            return False
        
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
    
    
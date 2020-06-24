# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 22:40:11 2020

@author: Mathias
"""


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
        i = 0
        while(i < training_cycles):
        
            game_state = "In Progress"
            
            while(game_state == "In Progress"):
            
                hashed_board = self.hashBoard(state)
                
        
        return #Not sure this function even returns, just fills in hash map
    
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
                if self.game_state[i][j] == ' ':
                    draw_flag = 1 #If empty, moves still available
        if draw_flag == 0:
            return None, "Draw" #If draw_flag still 0 then out of available tiles
        
        return None
    
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
            
    def empty_tiles(self):
        '''
        Find available tiles in self.state.
        '''
        tiles = []
        for i in range(3):
            for j in range(3):
                #if self.state[i][j] is ' ':
                if self.state[i][j] == ' ':
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
    
    
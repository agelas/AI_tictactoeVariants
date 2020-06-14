# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:40:31 2020

@author: Mathias

TODO: Minimax doesn't block minimizing player
"""


from math import inf as infinity

#Class which contains all the methods for implementing the minimax algorithm
class minimax_player:
    
    USER = -1
    AI = 1
    state = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' ']]
        
        
    def evaluate(self, state):
        '''
        Evaluates whether there is a winner using the internal board state

        Parameters
        ----------
        state : TYPE
            DESCRIPTION.

        Returns
        -------
        score : 
            +1 for AI wins(maximizing player), -1 for opponent wins, 0 for 
            inconclusie at this iteration.

        '''
        if self.wins(self.state, self.AI):
            score = 1
        elif self.wins(self.state, self.USER):
            score = -1
        else:
            score = 0
            
        return score
    
    def parseBoard(self, AI_Tile, User_Tile):
        '''
        The minimax AI is looking at the board as a bunch of 1's and -1's. So this
        function converts X's and O's in self.state to 1 and -1 depending on who's who.

        Parameters
        ----------
        AI_Tile : The 'X' or 'O' that will be converted into 1's
        User_Tile : The 'X' or 'O' that will be converted into -1's

        Returns
        -------
        None.

        '''
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == AI_Tile:
                    self.state[i][j] = 1
                if self.state[i][j] == User_Tile:
                    self.state[i][j] = -1
         
    def wins(self, state, player):
        '''
        Checks if either player has won in current board instance. 

        Parameters
        ----------
        state : The state of the current board. 
        player : 1 (maximizing agent) or -1 (minimizing agent).

        Returns
        -------
        bool
           If a win was detected.

        '''
        
        win_states = [
            [ self.state[0][0], self.state[0][1], self.state[0][2] ],
            [ self.state[1][0], self.state[1][1], self.state[1][2] ],
            [ self.state[2][0], self.state[2][1], self.state[2][2] ],
            [ self.state[0][0], self.state[1][0], self.state[2][0] ],
            [ self.state[0][1], self.state[1][1], self.state[2][1] ],
            [ self.state[0][2], self.state[1][2], self.state[2][2] ],
            [ self.state[0][0], self.state[1][1], self.state[2][2] ],
            [ self.state[2][0], self.state[1][1], self.state[0][2] ],
            ]
            
        if [player, player, player] in win_states:
            #print('HEY FOUND WINNER IN MINIMAX')
            #self.print_board()
            return True
        else:
            return False
        
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
    
    def empty_tiles(self):
        '''
        Find available tiles in self.state.
        '''
        tiles = []
        for i in range(3):
            for j in range(3):
                if self.state[i][j] is ' ':
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
        
    def minimax(self, state, depth, player):
        '''
        Function for running the minimax algorithm. 

        Parameters
        ----------
        state : The current board instantiation.
        depth : How many moves deep the algorithm is. 
        player : The 'X' or 'O' marker for the AI player

        Returns
        -------
        best
            Is a list of the form [position, score]. Position is the tile position,
            score is what is being used to evaluate a win, loss, or draw when someone 
            wins or the algorithm reaches a depth of 9. 

        '''
        if player == self.AI:
            best = [-1, -infinity]
        else:
            best = [-1, infinity]
            
        #Here is where we start recursing back up
        if depth == 0 or self.game_over(self.state):
            score = self.evaluate(state)
            return [-1, score]
        
        for tile in self.empty_tiles():
            position = tile
            self.state[int((position-1)/3)][(position-1)%3] = player
            score = self.minimax(state, depth - 1, -player)
            self.state[int((position-1)/3)][(position-1)%3] = ' ' #This resets back to empty so instance of board doesn't fill up
            score[0] = position
            
            if player == self.AI:
                if score[1] > best[1]:
                    best = score #max value
            else:
                if score[1] < best[1]:
                    best = score #min value
                    
        return best
    
    #Not sure why tile_choice is a needed parameter
    def make_move(self, tile_choice):
        '''
        Function for making moves on the internal board that comes along with 
        a minimax player object.

        Parameters
        ----------
        tile_choice : 
            The 'X' or 'O' tile that the AI is using.

        Returns
        -------
        aiMove[0]
            minimax returns a list, with the first position a move number and the 
            second position a score used to evaluate moves. So aiMove[0] grabs
            the number (the recommended move) and returns that.

        '''
        depth = len(self.empty_tiles())
        if depth == 0 or self.game_over(self.state):
            return
        
        if depth == 9:
            aiMove = [5, 2] #center tile if board is empty
        else:
            aiMove = self.minimax(self.state, depth, self.AI)
            
        return aiMove[0] #The first index of aiMove is the actual position
    
    def run_algorithm(self, boardState, tile_choice):
        '''
        Function that should be called by game engine. Starts off the cascade
        of function calls to implement algorithm and pass move back up to game
        engine

        Parameters
        ----------
        boardState : 
            The current state of the board on the iteration in game engine.
        tile_choice : 
            The 'X' or 'O' for the AI
        Returns
        -------
        moveChoice : 
            The number corresponding to the tile that the AI determines is best.

        '''
        AI_tile = tile_choice
        if AI_tile == 'X':
            User_tile = 'O'
        else:
            User_tile = 'X'
            
        self.state = boardState
        self.parseBoard(AI_tile, User_tile)
        
        
        #print(' '.join(map(str, self.state)))
        moveChoice = self.make_move(AI_tile)
        return moveChoice
    
    def print_board(self):
        '''
        Internal debug method for checking what the algorithm is seeing

        Returns
        -------
        None.

        '''
        print(str(self.state[0][0]) + ' | ' + str(self.state[0][1]) + ' | ' + str(self.state[0][2]))
        print('---------')
        print(str(self.state[1][0]) + ' | ' + str(self.state[1][1]) + ' | ' + str(self.state[1][2]))
        print('---------')
        print(str(self.state[2][0]) + ' | ' + str(self.state[2][1]) + ' | ' + str(self.state[2][2]))
        
    
    
    
            
        
        
        
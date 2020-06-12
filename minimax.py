# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:40:31 2020

@author: Mathias
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
        if self.wins(self.state, self.AI):
            score = 1
        elif self.wins(self.state, self.USER):
            score = -1
        else:
            score = 0
            
        return score
         
    def wins(self, state, player):
        
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
            print('HEY FOUND WINNER IN MINIMAX')
            self.print_board()
            return True
        else:
            return False
        
    def game_over(self, state):
        return self.wins(state, 'X') or self.wins(state, 'O')
    
    def empty_tiles(self):
        tiles = []
        for i in range(3):
            for j in range(3):
                if self.state[i][j] is ' ':
                    tiles.append(i*3+(j+1))
        return tiles
    
    def valid_move(self, position):
        if position in self.empty_tiles():
            return True
        else:
            return False
    
    '''
    #I'm gonna be honest I don't think this is necessary
    def set_tile(position, player):
        if valid_move(position):
            board([int((position-1)/3)][(position-1)%3]) = player
            return True
        else:
            return False
        '''
        
    def minimax(self, state, depth, player):
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
            self.state[int((position-1)/3)][(position-1)%3] = ' ' #I have a hunch this resets back to empty so instance of board doesn't fill up
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
        depth = len(self.empty_tiles())
        if depth == 0 or self.game_over(self.state):
            return
        
        if depth == 9:
            aiMove = [5, 2] #center tile if board is empty
        else:
            aiMove = self.minimax(self.state, depth, self.AI)
            
        return aiMove[0] #The first index of aiMove is the actual position
    
    def run_algorithm(self, boardState, tile_choice):
        AI_tile = tile_choice
        self.state = boardState
        #print(' '.join(map(str, self.state)))
        moveChoice = self.make_move(AI_tile)
        return moveChoice
    
    def print_board(self):
            print(str(self.state[0][0]) + ' | ' + str(self.state[0][1]) + ' | ' + str(self.state[0][2]))
            print('---------')
            print(str(self.state[1][0]) + ' | ' + str(self.state[1][1]) + ' | ' + str(self.state[1][2]))
            print('---------')
            print(str(self.state[2][0]) + ' | ' + str(self.state[2][1]) + ' | ' + str(self.state[2][2]))
        
    
    
    
            
        
        
        
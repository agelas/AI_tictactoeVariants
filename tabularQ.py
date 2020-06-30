# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 22:40:11 2020

@author: Mathias

TODO: Make a function for updating movesDictionary after the first training cycle
TODO: Increase discount factor the farther you are from end
"""
import random


class tabularQ_player:
    
    
    def hashBoard(self, state):
        
        hashmediary = ['n']
        
        for i in range(3):
            for j in range(3):
                if (state[i][j] == ' '):
                    hashmediary.append('n')
                elif (state[i][j] == 'X'):
                    hashmediary.append('X')
                elif (state[i][j] == 'O'):
                    hashmediary.append('O')
        hashsequence = ''.join(hashmediary)
        hashsequence = hashsequence.__hash__()
        return hashsequence
    
    def trainingCycle(self, training_cycles, player):
        
        state = [[' ',' ',' '],
                  [' ',' ',' '],
                  [' ',' ',' ']]
        
        Qtable = dict() #where the values are getting put.
        
        i = 0
        while(i < training_cycles):
            print('Training cycle ' + str(i))
            if player == 'X':
                tiles = ['X', 'O']
            else:
                tiles = ['O', 'X']
                
            states_list = []
            moves_list = []
            win = 0 #this is for creating the moves dictionary
        
            game_state = "In Progress"
            
            while(game_state == "In Progress"):
            
                hashed_board = self.hashBoard(state)
                
                available_moves = self.empty_tiles(state)
                length = len(available_moves)
                rand = random.randint(1, length)
                randMove = available_moves[rand - 1]
                
                if not self.game_over(state):
                    state[int((randMove-1)/3)][(randMove-1)%3] = 'X'
                    
                winner = self.check_winner(state, 'X')
                if winner is not None:
                    print(str(winner) + "won")
                    game_state = "Done"
                    self.print_board(state)
                    if winner[0] is None:
                        win = 0
                    else:
                        win = -1
                    break #So we can't hit the second winner check if X wins
                    
                available_moves = self.empty_tiles(state)
                length = len(available_moves)
                rand = random.randint(1, length)
                randMove = available_moves[rand - 1]
                
                if not self.game_over(state):
                    state[int((randMove-1)/3)][(randMove-1)%3] = 'O'
                    
                #If AI is X, add to states_list and moves_list
                if player == 'O':
                    states_list.append(hashed_board)
                    moves_list.append(randMove)
                
                winner = self.check_winner(state, 'O')   
                if winner is not None:
                    print(str(winner) + "won")
                    game_state = "Done"
                    self.print_board(state)
                    if winner[0] is None:
                        win = 0
                    else:
                        win = 1
                    
            
                
                #Calculate quality starting with last state and move
            
            if i == 0:
                Qtable = self.makeMoveDictionary(states_list, moves_list, win)
            else:
                newQtable = self.makeMoveDictionary(states_list, moves_list, win)
                print('MASTER:')
                print(Qtable)
                print('NEW TO MERGE:')
                print(newQtable)
                self.mergeQtables(Qtable, newQtable)
                print("BIG TABLE:")
                print(Qtable)
                
            i+=1
            state = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' ']] #Hard reset lol
            #print(states_list)
            #print(moves_list)
            
                
        
        return 5 #Not sure this function even returns, just fills in hash map
    
    def makeMoveDictionary(self, hashList, moveList, lastScore):
        
        moveDictionary = dict()
        moveDictionaryIntermediate = [] #Of form [{move: Qscore},{move: Qscore}]
        
        for i in (moveList):
            if i == moveList[-1]:
                #moveDictionary[i] = lastScore
                dictEntry = {i: lastScore}
            else:
                #moveDictionary[i] = 1
                dictEntry = {i: 1}
            moveDictionaryIntermediate.append(dictEntry)
                
        #print(moveDictionaryIntermediate)
        hashMoveDictionary = dict(zip(hashList, moveDictionaryIntermediate)) #moveDictionary.items() seems to make it a tuple
        #print("INITIAL:")
        #print(hashMoveDictionary)
        self.updateQvalues(hashMoveDictionary, moveList, hashList)
        
        return hashMoveDictionary
        
    def updateQvalues(self, hashMoveDictionary, moveList, hashList):
        alpha = 0.9 #learning rate
        gamma = 0.95 #discount rate
        
        for i in range(len(hashList)):
            if i == 0:
                print('skip')
            else:
                key1 = hashList[-(i+1)]
                key2 = moveList[-(i+1)]
                #print(hashMoveDictionary[key1][key2])
                nextStateDictIndex = hashList[-i] #Index of nested dictionary (move: Q score) of next state
                print(hashMoveDictionary[nextStateDictIndex])
                nextStateDict = hashMoveDictionary[nextStateDictIndex] #Getting {move:Qscore, move:Qscore}
                #print(type(nextStateDict))
                
                maxNQKey = max(nextStateDict, key = nextStateDict.get) #This'll get you key with max value
                maxNQ = nextStateDict[maxNQKey] #Gets the actual value of highest Q score in next state
                
                #print("maxNQ is: " + str(maxNQ))
                #print("Applied to: " + str(hashMoveDictionary[key1][key2]))
                
                updatedQ = (1-alpha)*hashMoveDictionary[key1][key2]+(alpha*gamma*maxNQ)
                hashMoveDictionary[key1][key2] = updatedQ
                
                #print("UPDATED:")
                #print(hashMoveDictionary)
                
    def mergeQtables(self, masterQ, mergingQ):
        
        for state, Qdict in mergingQ.items():
            if state in masterQ: #Checking if board state is in master table, 
                                #if it is, need to check if there are overlapping {move: Qscore} 
                                #nested dictionaries
                for key in Qdict: #Checking the nested dictionaries
                    if key in masterQ[state]: #If there is an overlapping {move: QScore}, key = move
                        masterQ[state][key] = max(masterQ[state][key], mergingQ[state][key]) #AI is optimistic, will go for larger Qscore
                    else:
                        masterQ[state][key] = mergingQ[state][key] #If that move isn't there, just add to master table
            else:
                stateToAdd = mergingQ[state]
                masterQ[state] = stateToAdd #Add board state to master
        
        return masterQ
                    
           
    
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
            return player, "Done"
        
        draw_flag = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
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
        return self.check_winner(state, 'X') or self.check_winner(state, 'O')
    
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
        if state[int((move_num-1)/3)][(move_num-1)%3] == ' ': 
            state[int((move_num-1)/3)][(move_num-1)%3] = player
            
    def empty_tiles(self, state):
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
        
    def print_board(self, state):
            '''
            Prints the board
            '''
            print(str(state[0][0]) + ' | ' + str(state[0][1]) + ' | ' + str(state[0][2]))
            print('---------')
            print(str(state[1][0]) + ' | ' + str(state[1][1]) + ' | ' + str(state[1][2]))
            print('---------')
            print(str(state[2][0]) + ' | ' + str(state[2][1]) + ' | ' + str(state[2][2]))
            print()
    
    
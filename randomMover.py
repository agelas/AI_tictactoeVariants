# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:01:29 2020

@author: Mathias
"""
import random

#random player

class random_player:
    
    def get_move(availables):
        #Need how many in list
        length = len(availables)
        #Random index from list
        randIndex = random.randint(1, length)
        return availables[randIndex - 1]
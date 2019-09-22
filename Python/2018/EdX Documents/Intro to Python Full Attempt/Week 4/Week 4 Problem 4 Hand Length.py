# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 20:17:22 2018

@author: joshc
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    handlength=[]
    for i in hand:
        handlength.append(hand[i])
    return sum(handlength)
        
    
    
hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
print(calculateHandlen(hand))
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 11:27:46 2018

@author: joshc
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals)

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    length = 0
    for i in aDict:
        length+=len(aDict[i])
    return length

print (how_many(animals))
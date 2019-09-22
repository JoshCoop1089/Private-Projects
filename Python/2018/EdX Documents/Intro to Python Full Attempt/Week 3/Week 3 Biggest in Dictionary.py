# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 11:33:51 2018

@author: joshc
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['e'] = ['emu']
animals['e'].append('elephant')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    value = 0
    key=[]
    for i in aDict:
        if len(aDict[i])>=value:
            value=len(aDict[i])
            key=i
    return key
        
print(biggest(animals))

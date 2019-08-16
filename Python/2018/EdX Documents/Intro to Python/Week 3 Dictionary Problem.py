# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:39:47 2017

@author: Josh
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    a=0
    for x in aDict.keys():
        a+=len(aDict[x])
    return a


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    big=0
    for x in aDict.keys():
       if len(aDict[x])>big:
           big=len(aDict[x]) 
    return x
       
    
print(biggest(animals))
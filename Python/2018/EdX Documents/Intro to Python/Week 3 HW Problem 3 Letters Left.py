# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:22:43 2017

@author: Josh
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    lettersleft=list(string.ascii_lowercase)
    for x in lettersGuessed:
        lettersleft.remove(x)
    return ''.join(lettersleft)



lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
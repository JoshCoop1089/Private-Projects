# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:09:28 2017

@author: Josh
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    CurrentGuess=''
    for x in secretWord:
        if x in lettersGuessed:
            CurrentGuess+=x
        else:
            CurrentGuess+='_ '
    return CurrentGuess
    
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))

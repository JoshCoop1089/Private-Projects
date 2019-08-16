# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:41:49 2017

@author: Josh
"""
secretWord = 'pineapple' 
lettersGuessed = ['z', 'x', 'q', 'p', 'i', 'n', 'e', 'a', 'p', 'p', 'l', 'e']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    secretwordList=sorted(list(secretWord))
    lettersGuessed=sorted(lettersGuessed)
    check=[]
    for x in lettersGuessed:
        if x in secretwordList:
            check.append(x)
            if check==secretwordList:
                return True
        lettersGuessed=lettersGuessed[1:]
    if lettersGuessed == []:
          return False
#            secretwordList-=secretwordList.index(x)
#            print (secretwordList)
            
            
print(isWordGuessed(secretWord, lettersGuessed))

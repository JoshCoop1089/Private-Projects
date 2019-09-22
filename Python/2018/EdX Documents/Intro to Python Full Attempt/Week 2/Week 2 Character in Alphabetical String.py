# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 00:19:39 2018

@author: joshc
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr)== 0 or (len(aStr)==1 and char != aStr):
        return False
    elif len(aStr)==1 and char==aStr:
        return True
    else:
        if char < aStr[len(aStr)//2]:
            return isIn(char,aStr[0:(len(aStr)//2)])
        else:
            return isIn(char,aStr[(len(aStr)//2):])


print(isIn('q','abcdefg'))

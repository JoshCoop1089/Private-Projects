# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 15:49:55 2018

@author: joshc
"""

def isPalindrome(aString):
    '''
    aString: a string
    '''
    if len(aString) == 0:
        return True
    for num in range(len(aString)):
        if aString[num] != aString[len(aString)-(num+1)]:
            return False
        else:
            return True
        
words = ["abba", "", "sakjfdlkasfjlk", "ere i saw elba able was i ere"]
for string in words:
    if (isPalindrome(string)):
        print("True")   
    else:
        print("False")
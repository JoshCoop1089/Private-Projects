# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:04:47 2017

@author: Josh
"""

#def isIn(char, aStr):
#    '''
#    char: a single character
#    aStr: an alphabetized string
#    
#    returns: True if char is in aStr; False otherwise
#    '''
#    i=(len(aStr)-1)//2
#    print('now testing: ' +str(aStr))
#    if char==aStr[i]:
#        print(True)
#    else:
#        print('test failed, finding proper half')
#        if char>aStr[i]:
#            aStr=aStr[i+1:]
#            print('Searching second half of string: ' +str(aStr))
#            isIn(char,aStr)
#        else:
#            aStr=aStr[0:i]
#            print('Searching first half of string: ' +str(aStr))
#            isIn(char,aStr)
#            
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    i=(len(aStr))//2
    print('now testing: '+str(aStr)+' at index '+str(i)+ 
          ' which is letter '+str(aStr[i])+
          ' versus char which is ' +str(char))
    if aStr=='':
        return False
    elif char==aStr[i] or char==aStr[len(aStr)-1] or char==aStr[0]:
        print('Found ya!')
        return True
    else:
        print('test failed, finding proper half')
        if char>aStr[i]:
            print('Searching second half of string: ' +str(aStr[i+1:]))
            return isIn(char,aStr[i+1:])
        elif char<aStr[i]:
            print('Searching first half of string: ' +str(aStr[:i]))
            return isIn(char,aStr[:i])         
isIn('w', 'abcdefghijklmnnnnnnnopqqqqqrrrrtuuuuvvvvvwxyyyzzz')
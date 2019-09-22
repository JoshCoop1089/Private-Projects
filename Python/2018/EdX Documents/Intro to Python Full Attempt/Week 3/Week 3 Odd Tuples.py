# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:52:37 2018

@author: joshc
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    outtup=()
    for i in range (len(aTup)):
        print (i)
        if i%2 ==0:
            outtup = outtup +(aTup[i],)
    return print(outtup)

oddTuples ((9, 18, 16, 8, 2))
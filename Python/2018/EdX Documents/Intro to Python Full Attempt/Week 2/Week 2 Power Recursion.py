# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 22:50:21 2018

@author: joshc
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base*recurPower(base,exp-1)

print (recurPower(4,0))
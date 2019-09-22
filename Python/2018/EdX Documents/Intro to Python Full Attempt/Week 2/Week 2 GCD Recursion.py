# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:08:58 2018

@author: joshc
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b,a%b)
    
print (gcdRecur(0,3))
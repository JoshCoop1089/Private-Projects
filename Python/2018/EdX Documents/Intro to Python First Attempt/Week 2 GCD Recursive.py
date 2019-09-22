# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 22:39:19 2017

@author: Josh
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b==0:
        return a
    else:
       return gcdRecur(b,a%b)
   
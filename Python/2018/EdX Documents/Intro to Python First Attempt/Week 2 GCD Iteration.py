# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 17:01:28 2017

@author: Josh
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    c=''
    if a>b:
        c=b
    elif a<b:
        c=a
    while c>0:
        if a%c==0 and b%c==0:
            return c
        else:
            c-=1
            
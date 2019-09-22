# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:08:40 2018

@author: joshc
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    i=''
    if a>b:
        i=b
    elif b>a:
        i=a
    elif a==b:
        return a
    while i>1:
        if b%i==0 and a%i==0:
            return i
        else:
            i-=1
    if i==1:
        return 1

print(gcdIter(5,0))
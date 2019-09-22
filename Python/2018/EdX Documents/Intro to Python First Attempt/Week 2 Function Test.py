# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 15:01:58 2017

@author: Josh
"""
#
#def is_even(i):
#    """
#    Input: i is non negative integer
#    Return: Is i even or odd?
#    """
#    return i%2==0
#
#for i in range(4):
#    if is_even(i)==True:
#        print('Even')
#    else:
#        print('Odd')
#        
        
def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)
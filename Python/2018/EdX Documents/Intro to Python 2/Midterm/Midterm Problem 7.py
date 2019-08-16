# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 11:21:18 2018

@author: joshc
"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    Lclone=L[:]
    for i in Lclone:
        x=g(f(i))
        if not x:
            print(i)
            L.remove(i)
            print('L is:',L)
    print('___________________________')
    if L==[]:
        return -1
    return max(L)
    
    
    
    
def f(i):
    return i + 2
def g(i):
    return i > 5
L = [0, -10, 5, 6, -4,9,-3,1,8,-6]
print(applyF_filterG(L, f, g))
print(L)

E=[0]
print(applyF_filterG(E, f, g))
print(E)


#Should print:
#
#9
#[5, 6, 9, 8]
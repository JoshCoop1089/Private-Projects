# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 19:40:23 2018

@author: joshc
"""


def solve(a0,a1,a2,b0,b1,b2):
    alice=0
    bob=0
    A=[a0,a1,a2]
    B=[b0,b1,b2]
    for i in range(len(A)):
        if A[i]>B[i]:
            alice+=1
        elif B[i]>A[i]:
            bob+=1
#    out=str(A)
    return str(alice)+' '+str(bob)

print(solve(5,6,7,3,6,10))
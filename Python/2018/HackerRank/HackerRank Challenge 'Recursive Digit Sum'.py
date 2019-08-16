# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 23:45:58 2018

@author: joshc
"""

def digitSum(n, k):
    P=int(str(n)*k)
    while P>10:
        P=super_digit(P)
    return P
def super_digit(P):
    print(P)
    listP=[int(x) for x in str(P)]
    P=sum(listP)
    print('P is now:',P)
    while P>10:
        P=super_digit(P)
    return P


n=19235613235
k=17

print(digitSum(n,k))

#Code has problems in HackerRank coder on ridiculously large inputs,
# how to get around max recursion depth and runtime erors?
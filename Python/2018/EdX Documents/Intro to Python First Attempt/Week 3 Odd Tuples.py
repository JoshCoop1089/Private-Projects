# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 13:38:02 2017

@author: Josh
"""

def oddTuples(aTup):
    tup=()
    j=0
    while j<len(aTup):
        print(j)
        print(tup)
        if j%2 == 0:
            tup+=(aTup[j],)
        j+=1
    return tup
aTup=( 15, 14, 10, 2, 17, 16) 
oddTuples(aTup)  
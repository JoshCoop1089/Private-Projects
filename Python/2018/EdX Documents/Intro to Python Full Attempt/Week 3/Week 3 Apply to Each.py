# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 12:40:35 2018

@author: joshc
"""
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
def add(a):
    return a+1
        
testList = [1, -4, 8, -9]
applyToEach(testList,add)
print(testList)
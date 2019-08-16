# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 21:01:37 2018

@author: joshc
"""

def diagonalDifference(a):
    maindiag=[]
    backdiag=[]
    for i in range(len(a)):
        j=n-1-i
        maindiag.append(a[i][i])
        backdiag.append(a[i][j])
    return abs(sum(maindiag)-sum(backdiag))
        
        
        
        
a=[[11, 2, 4],
   [4, 5, 6],
   [10, 8, -12]]
n=3
print(diagonalDifference(a))
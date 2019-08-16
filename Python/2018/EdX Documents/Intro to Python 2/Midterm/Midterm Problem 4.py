# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 11:01:47 2018

@author: joshc
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    dot=[]
    i=0
    while i <len(listA):
        dot.append(listA[i]*listB[i])
        i+=1
    return sum(dot)
        
    

listA = [1, 2, 3]
listB = [4, 5, 6]
print(dotProduct(listA,listB))

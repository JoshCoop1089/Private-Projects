# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 16:12:31 2018

@author: joshc
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    
    intersect = []
    difference = []
    interDict = {}
    diffDict = {}
    output = (interDict, diffDict)

    for key in d1:
        if key in d2:
            intersect.append(key)
        else:
            difference.append(key)
    for key in d2:
        if key not in d1:
            difference.append(key)
            
    for i in intersect:
        interDict[i] = f(d1[i],d2[i])
    for j in difference:
        if j in d1:
            diffDict[j] = d1[j]
        elif j in d2:
            diffDict[j] = d2[j]
            
    return output

def f(a,b):
    return a + b

def g(a,b):
    return a > b
            
            
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

output = dict_interdiff(d1,d2)
print(output)
print("---------------------------")

d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}

output = dict_interdiff(d1,d2)
print(output)
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 11:20:58 2018

@author: joshc
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    keys=[]
    uniquevals=[]
    repeat=[]
    for i in aDict:
        if aDict[i] not in uniquevals:
            uniquevals.append(aDict[i])
        elif aDict[i] in uniquevals:
            repeat.append(aDict[i])
#    for i in aDict:
#        if aDict[i] not in repeat:
#            keys.append(i)
    return sorted(repeat)
aDict={0: 3, 1: 2, 2: 3, 3: 1, 4: 0, 6: 0, 7: 4, 8: 2, 9: 7, 10: 0}
print(uniqueValues(aDict))


# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 15:57:46 2018

@author: joshc
"""

def largest_odd_times(L):
    """ 
    Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number 
    of times in L. If no such element exists, returns None 
    """
#    build frequency dict
#    find keys with odd values
#    find largest key
    freq = {}  
    bestKey = -1     
    for i in L:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] = 1
    for key in freq:
        if ((freq[key]%2 != 0) and (key > bestKey)):
            bestKey = key
    if bestKey == -1:
        return None
    else:
        return bestKey

nums = [[2, 2],[2,2,4,4],[3, 2],[3, 3, 2, 0],[3, 0, 5, 3, 5, 3],
        [3,9,5,3,5,3],[6, 8, 6, 8, 6, 8, 6, 8, 6, 8],[2, 4, 5, 4, 5, 4, 2, 2]]
for item in nums:
    best = largest_odd_times(item)
    print(best)
print("Output should be:\nNone\nNone\n3\n2\n3\n9\n8\n4")
        
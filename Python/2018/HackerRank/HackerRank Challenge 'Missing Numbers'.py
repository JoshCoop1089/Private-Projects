# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 23:12:47 2018

@author: joshc
"""

def missingNumbers(arr, brr,aFreq={},bFreq={},key=[]):
    arr.sort()
    brr.sort()
    for num in arr:
        if num not in aFreq:
            aFreq[num]=1
        else:
            aFreq[num]+=1
    for num in brr:
        if num not in bFreq:
            bFreq[num]=1
        else:
            bFreq[num]+=1
    for aKey in aFreq:
        if aKey not in bFreq or aFreq[aKey]!=bFreq[aKey]:
            key.append(aKey)
    for bKey in bFreq:
        if bKey not in aFreq:
            key.append(bKey)
    key.sort()
    return key       



arr=[203, 204, 205, 206, 207, 208, 203, 204, 205, 206, 202]
brr=[203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204, 201]

result=missingNumbers(arr, brr,aFreq={},bFreq={})
print(result)

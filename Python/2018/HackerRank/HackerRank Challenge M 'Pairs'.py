# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 23:42:15 2018

@author: joshc
"""

def solveMeFirst(x,y):
    return abs(x-y)
    
def pairs(k, arr,count=0):
    arrclone=arr[:]
    arrclone.sort()
    j=len(arrclone)-1
    while j >0:
        for i in arr:
            count +=1
    return count

k=2
arr=[1, 5, 3, 4, 2]
j=1
brr=[363374326, 364147530, 61825163, 1073065718,
     1281246024, 1399469912, 428047635, 491595254,
     879792181, 1069262793]
print('a',pairs(k,arr),' -->should be 3')
print('b',pairs(j,brr),' -->should be 0')
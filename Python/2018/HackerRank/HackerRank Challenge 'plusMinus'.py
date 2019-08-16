# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 21:37:32 2018

@author: joshc
"""

def plusMinus(arr):
    n=arr[0][0]
    plus=0
    minus=0
    zero=0
    for i in arr[1]:
        if i>0:
            plus+=1
        elif i<0:
            minus+=1
        else:
            zero+=1
    plus='{0:.6f}'.format(plus/n)
    minus='{:.6f}'.format(minus/n)
    zero='{0:.6f}'.format(zero/n)
    return plus+'\n'+minus+'\n'+zero
arr=[[6],[-4,3,-9,0,4,1]]

print(plusMinus(arr))

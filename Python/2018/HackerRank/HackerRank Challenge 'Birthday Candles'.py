# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 22:50:45 2018

@author: joshc
"""

def birthdayCakeCandles(n, ar):
    count=0
    for i in ar:
        if i == max(ar):
            count+=1
    return count
            
def birthdayCakeCandles(n, ar):
    return ar.count(max(ar))
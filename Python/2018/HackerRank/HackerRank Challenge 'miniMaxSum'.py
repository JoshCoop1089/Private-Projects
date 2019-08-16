# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 22:39:05 2018

@author: joshc
"""

def miniMaxSum(arr):
    arr.sort()
    arrmin=sum(arr[:-1])
    arrmax=sum(arr[1:])
    print(arrmin,arrmax)
    
arr=[1, 2, 3, 4, 5]
miniMaxSum(arr)
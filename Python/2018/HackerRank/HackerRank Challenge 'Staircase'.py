# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 22:35:36 2018

@author: joshc
"""

def staircase(n):
    for i in range(1,n+1):
        j=n-i
        print(' '*j+'#'*i)

n=6
staircase(n)
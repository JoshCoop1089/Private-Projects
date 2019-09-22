# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 00:29:35 2017

@author: Josh
"""

s='obob'
bob=0
i=0

while i<len(s)-2:
    x=s[i:i+3]
    i+=1
    print(x)
    if x == 'bob':
        bob +=1
        i+=1
    else:
        i+=1
        break
print(bob)

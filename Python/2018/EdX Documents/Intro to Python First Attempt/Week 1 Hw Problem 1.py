# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 22:40:04 2017

@author: Josh
"""

s='aeooo90sx'
z=0
for x in s:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        z=z+1
print ('Number of vowels: ' + str(z))

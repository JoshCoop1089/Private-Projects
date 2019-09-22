# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:39:32 2018

@author: joshc
"""

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step
        
#       When guess hits 4.9999999998, squares into the proper 
#        epsilon range but code has no option for guessing 
#        correctly inside while loop

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
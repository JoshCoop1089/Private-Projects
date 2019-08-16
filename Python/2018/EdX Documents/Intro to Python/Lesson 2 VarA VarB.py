# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 11:10:21 2017

@author: Josh
"""

varA = 1
varB = 2
str_A = 'varA'
str_B = 'varB'
if type(varA)== type (str_A) or type(varB) ==type(str_B):
    print ('string involved')
elif varA > varB:
    print ('bigger')
elif varB > varA:
    print('smaller')
else:
    print('equal')
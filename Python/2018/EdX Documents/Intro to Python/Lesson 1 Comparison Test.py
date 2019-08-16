# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:27:19 2017

@author: Josh
"""

x=float(input('Enter value for x: '))
y=float(input('Enter value for y: '))
if x==y:
    print ('x and y are equal')
    if y!=0:
        print("therefore x/y is", x/y)
elif x<y:
    print("x is smaller")
else:
    print("y is smaller")
print("thanks!")
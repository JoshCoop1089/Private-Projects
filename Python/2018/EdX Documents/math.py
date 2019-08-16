# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 17:44:16 2018

@author: joshc
"""

import math
x=math.sin(45)/(2*math.sin(72))
y=math.sin(63)/(2*math.sin(72))
a=1
b=(1/2)*(5**0.5)-x
c=(2**0.5)-y
s=(a+b+c)/2
Area=(s*(s-a)*(s-b)*(s-c))**0.5
percent=Area
print (percent)
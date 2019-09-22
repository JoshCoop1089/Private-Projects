# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 01:01:10 2018

@author: joshc
"""

def polysum(n,s):
    '''
    n is number of sides
    s is side length
    returns the sum of the area of polygon and square of the perimeter
    '''
    import math
    return round(((n*(s**2))/(4*math.tan(math.pi/n)) + (n*s)**2),4)
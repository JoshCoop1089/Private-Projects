# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 12:29:27 2017

@author: Josh
"""

from math import *
def polysum(n,s):
    '''
    Inputs: 
        n is the number of sides of the regular polygon
        s is the side length
    Outputs:
        The area of the n-sided polygon plus the square of the perimeter
    '''
    area=n*(s**2)/(4*tan(pi/n))
    perimeter=n*s
    return round(area+(perimeter**2),4)
    
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 15:30:20 2018

@author: joshc
"""

class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8
w1 = Weird(X, Y)
w2 = Wild(X, Y)
w3 = Wild(17, 18)
w4 = Wild(X, 18)
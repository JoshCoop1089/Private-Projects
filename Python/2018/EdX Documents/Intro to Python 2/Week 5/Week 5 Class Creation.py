# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 14:13:06 2018

@author: joshc
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def distance(self,other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
    def __sub__(self,other):
        return Coordinate(self.x-other.x,self.y-other.y)
    def norm(self): #method that defines a 
#                    3rd and 4th attribute to an instance
        self.n1 = abs(self.x) + abs(self.x)  
        self.n2 = ((self.x)**2 + (self.x)**2)**0.5
        return None # the new attributes self.n1 and 
#                     self.n2 are now ready to be used 
c=Coordinate(3,4)
origin= Coordinate(0,0)
c.norm()
#Initializes the two extra attributes for Coordinate class that\
#arent defined in initial init statement
print(c.distance(origin))
#-> 5.0
print(c)
#<3,4>
print(c.__sub__(origin))
print(c-origin)
#<3,4>
print(c.n1)
#-> 6    (3+3 from self.x being 3)

#class Foo():
#    pass
#
#f = Foo()
#f.X = 'Whatever'
#print(f.X)
#print(f)
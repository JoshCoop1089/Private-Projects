# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 16:43:51 2018

@author: joshc
"""

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
    
class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        if e in self.vals:
            self.vals[e] -=1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        count = 0;
        for i in self.vals:
            if i == e:
                count =self.vals[e]
        return count
        
        
d1 = Bag()
d1.insert(4)
d1.insert(4)
print(d1)
d1.remove(2)
print(d1)

print("Output should be:\n4:2\n4:2")
print("-----------------------")

d1 = Bag()
d1.insert(4)
d1.insert(4)
d1.insert(4)
print(d1.count(2))
print(d1.count(4))

print("Output should be:\n0\n3")
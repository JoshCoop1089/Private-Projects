# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:40:13 2018

@author: joshc
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self,other):
        """Returns new list of elements in both self and other"""
        intSetIntersect=intSet()
        for e in self.vals:
            if e in other.vals:
                intSetIntersect.insert(e)
        return intSetIntersect
    
    def __len__(self):
        length=0
        for e in self.vals:
            length+=1
        return length
            
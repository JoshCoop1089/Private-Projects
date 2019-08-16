# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 11:21:09 2018

@author: joshc
"""

def max_val(t,check=0): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    for item in t:
        if type(item)!=int:
            check=max_val(item,check)
        elif item>check:
                check=item
    return check
  

print('First return is:',max_val([5,4,3,2,1]))
print('should return 5')

print('----------------------------')
print('Second return is:',max_val(((1,6,2),7, [[0],[4]])))
print('should return 7')

print('----------------------------')
print('Third return is:',max_val((5, ((7,1),8), [[1],[9]])))
print('should return 9')

print('----------------------------')
print('Fourth return is:',max_val((5, (1,2), [[1,10],[9]])))
print('should return 10')

print('----------------------------')
print('Fifth return is:',max_val(([[1,([(1,3,11),13]),3],[9]],11)))
print('should return 13')

print('----------------------------')
print('Sixth return is:',max_val(([1,[9,10]],11,(1,2,12))))
print('should return 12')

#check the element
#    if not an int:
#        rerun the function on that element until it breaks 
#        itself down to a list of ints
#    if int:
#        store the value to compare against other ints
#        if it is bigger, store
#        if smaller, move onto next element:
#return the permanent big number
#        
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 22:45:15 2018

@author: joshc
"""

def get_stats(class_list):
    new_stats=[]
    for elt in class_list:
        new_stats.append([elt[0],elt[1],avg(elt[1])])
        if avg(elt[1])== 0:
            print('please insert grades for:',elt[0])
    return new_stats
def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        return 0.0

test_grades=[[['peter','parker'],[10,9,8]]\
             ,[['bruce','wayne'],[10,8,6]]\
             ,[['fuck','up'],[]]]




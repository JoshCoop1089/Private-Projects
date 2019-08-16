# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 00:23:56 2018

@author: joshc
"""

def gradingStudents(grades):
    out=[]
    for grade in grades:
        if grade < 38 or 0<=grade%5<3:
            out.append(grade)
        elif grade%5>=3:
            out.append(grade+5-(grade%5))
    return out
            
    
    
grades=[73, 67, 38, 33]

result=gradingStudents(grades)
print(result)
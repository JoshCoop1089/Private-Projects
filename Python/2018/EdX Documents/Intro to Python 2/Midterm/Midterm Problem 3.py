# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:37:49 2018

@author: joshc
"""
count=0
def count7(N):
    '''
    N: a non-negative integer
    '''
    print (N)
    if N==0:
        return 0
    elif N%10==7:
        count=1
        return count+count7(N//10)
    else:
        return count7(N//10)
    
print(count7(7174567))
#Gives 3 as output
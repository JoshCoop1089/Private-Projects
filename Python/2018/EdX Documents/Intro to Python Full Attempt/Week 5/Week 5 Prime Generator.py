# -*- coding: utf-8 -*-
"""
Created on Sun May 20 20:30:55 2018

@author: joshc
"""

def genPrime():
    primeList=[]
    prime = 1
    while True:
        prime+=1
        if all(prime%number !=0 for number in primeList):
            primeList.append(prime)
            yield primeList[-1]


prime= genPrime()
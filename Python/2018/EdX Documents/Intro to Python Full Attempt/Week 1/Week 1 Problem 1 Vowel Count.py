# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:51:50 2018

@author: joshc
"""
s='abcdefghijjklem'
vowelcount=0
for letter in s:
    if letter == 'a':
        vowelcount +=1
    elif letter =='e':
        vowelcount+=1
    elif letter == 'i':
        vowelcount+=1
    elif letter == 'o':
        vowelcount +=1
    elif letter == 'u':
        vowelcount +=1
print('Number of vowels: '+str(vowelcount))    

        
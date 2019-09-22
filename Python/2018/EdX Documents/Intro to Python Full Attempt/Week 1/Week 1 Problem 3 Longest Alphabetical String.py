# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 14:43:12 2018

@author: joshc
"""

s='sadklj;lkfaj;lkdgj'
mainstring=''
holdstring=''
for letter in s:
    if letter >= mainstring[-1:]:
        mainstring+=letter
        print(letter)
        print('mainstring: ' +str(mainstring))
        print('holdstring: ' +str(holdstring))
    else:
        print(letter)
        if len(holdstring)<len(mainstring):
            holdstring=mainstring
        mainstring=letter
        print('mainstring: ' +str(mainstring))
        print('holdstring: ' +str(holdstring))
if len(holdstring)>=len(mainstring):
    mainstring=holdstring
print('Longest substring in alphabetical order is: '+str(mainstring))
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 10:05:52 2017

@author: Josh
"""
alphabetleft='abcdefghijklmnopqrstuvwxyz'
Alphabetleft=list(alphabetleft)
secretword='zabnur'
#char=input('Enter a letter: ')
#
#
##printing out the remaining letters after a correct choice
#if char in secretword:
#    Alphabetleft.remove(char)
#    alphabetleft=''.join(Alphabetleft)
#print(alphabetleft)
#
#
#
#currentguess='_ _ _'
#lcg=currentguess.split(' ')
#print(lcg)

CurrentGuess=''
secretlist=list(secretword)
print(secretlist)
for i in range(len(secretword)):
    CurrentGuess+=' _ '
print('Your Current Word is: '+str(CurrentGuess))
lCG1=list(CurrentGuess)
for x in map(min,secretlist,lCG1):
    if True:
        lCG1[x]=secretlist[x]
        
        
CG=CurrentGuess.split(' ')
print(CG)
lCG=''.join(CG)
print(lCG)
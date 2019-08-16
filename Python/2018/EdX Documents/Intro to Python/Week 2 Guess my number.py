# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:36:06 2017

@author: Josh
"""

print('Please think of a number between 0 and 100!')
secret=int(input('Enter your secret number here: '))
if secret<0 or secret >= 100:
    print('Please input a number more than 0 but less than 100')
    secret=int(input('Enter your secret number here: '))
low=0
high=100
guess=0
while guess!=secret:
    guess=(low+high)//2
    print('Is your secret number ' +str(guess) + '?')
    check=str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if check == 'h':
        high=guess
    elif check == 'l':
        low=guess
    elif check == 'c':
        print('Game over. Your secret number was: '+str(secret))
        break
    else:
        print ('Sorry, I did not understand your input.')
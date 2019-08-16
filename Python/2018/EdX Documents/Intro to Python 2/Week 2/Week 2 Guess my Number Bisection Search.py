# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 22:07:08 2018

@author: joshc
"""

print('Please think of a number between 0 and 100!')
high=100
low=0
guess=(high+low)//2
check=''
while check !='c':
    if check != 'h' and check != 'l' and check != 'c' and check !='':
        print("Sorry, I didn't understand your input")
    print('Is your secret number ',guess)
    check=str(input("Enter 'h' to indicate the guess is too high. Enter 'l'to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if check=='h':
        high=guess
        guess=(high+low)//2
    elif check == 'l':
        low=guess
        guess=(high+low)//2
print('Game over. Your secret number was: ',guess)
    
    